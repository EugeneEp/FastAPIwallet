from app import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, BigInteger
from sqlalchemy.orm import relationship, backref
from datetime import datetime
import re
import hashlib
import glob
import os
import time as timec
import random
import requests
import json

# Функция на замену пробелов на "-", в случае если придется генерировать урл с названием чего либо
def slugify(s):
	pattern = r'[^\w+]'
	return re.sub(pattern, '-', s)

# функция на замену значений типа транзакций, полученным по апи
def movementTranslate(m):
	arr = {'charge':'Пополнение','withdraw':'Вывод','payment':'Перевод'}
	return arr[m]

# Функция шифрования пароля в мд5
def hashpass(password):
	salt = '69hdaw@e21e2'
	new_pass = password + salt
	h = hashlib.md5(new_pass.encode())
	return h.hexdigest()

# Функция шифрования ссылки на csv файл транзакций
def hashcsv(user_id):
	salt = 'j12090d)()(@'
	link = str(user_id) + salt
	h = hashlib.md5(link.encode())
	return 'static/upload/csv/' + h.hexdigest() + '.csv'

# Функция шифрования файла фото профиля
def hashprofile(user_id):
	salt = 'pp12oj321jp)('
	link = str(user_id) + salt
	h = hashlib.md5(link.encode())
	return h.hexdigest()

# Функция на слияние двух списков в нужный мне формат (не используется)
def mergeTwoListsAsDict(list1, list2):
	dict1 = {k: {'name': v} for k, v in enumerate(list1)}
	dict2 = {k: {'id': v} for k, v in enumerate(list2)}
	return {k: {**v, **dict2[k]} for k, v in dict1.items()}

# Функция конвертации таймстампа в дату
def timeToDate(time):
	timestamp = datetime.fromtimestamp(time)
	return timestamp.strftime('%Y-%m-%d %H:%M:%S')

# Функция ковертации даты в таймстамп
def dateToTime(time):
	return timec.mktime(datetime.strptime(time, "%Y-%m-%d").timetuple())

# Конвертация объекта пагинатора в словарь
def paginatorParse(obj, page):
	arr = {
		'pages':obj.pages,
		'page':page,
		'has_prev':obj.has_previous,
		'prev_num':obj.previous_page,
		'has_next':obj.has_next,
		'next_num':obj.next_page
	}
	return arr

# Конвертация объекта транзакций в словарь
def transParse(obj):
	arr = {}
	for v in obj:
		v.time = timeToDate(v.time)
		v.movement_type = movementTranslate(v.movement_type)
		arr[v.id] = {
			'time': v.time,
			'movement_type': v.movement_type,
			'amount': v.amount,
			'status': v.status 
		}
	return arr

# Класс для работы с апи
class API():
	url = 'https://apis-dev.maxwallet.ru/' # Урл апи
	api_key = '????????' # Апи ключ
	headers = {"Content-Type" : "application/json", "X-API-KEY" : api_key} # Заголовки

	# Конструктор, в который передаю название метода для исполнения
	def __init__(self, method, body):
		self.method = method
		self.url = self.url + self.method
		self.body = body


	# Метод для гет запроса
	def get(self):
		response = requests.get(self.url, headers=self.headers, params=self.body)
		return response.json()

	# Метод для пост запроса
	def post(self):
		response = requests.post(self.url, headers=self.headers, json=self.body)
		return response.json()

# Класс пользователей
class Users(Base):

	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	email = Column(String(255), nullable=True)
	phone = Column(BigInteger, nullable=True)
	password = Column(String(255))
	identity = Column(Text, nullable=True)
	confirmation = Column(String(255), default = 0)
	roots = Column(Integer, default = 1)
	secret_id = Column(Text, nullable=True)
	secret_key = Column(Text, nullable=True)
	self_employed_approve = Column(Integer, nullable=True)
	rate = Column(String(255), nullable=True)
	balance = 0

	# Связь 1 ко многим, для получение кошельков юзера
	wallets = relationship("Wallets", backref=backref('user'), lazy='dynamic')

	# Связь 1 ко многим, для получение транзакций юзера
	transactions = relationship("Transactions", backref=backref('user'), lazy='dynamic')

	def __init__(self, *args, **kwargs):
		super(Users, self).__init__(*args, **kwargs)
		self.generate_hash()

	# Зашифровать пароль
	def generate_hash(self):
		self.password = hashpass(self.password)

	# Добавить юзера по апи в банк
	def add_user(self):
		body = {
			'phone' : self.phone
		}
		method = 'customMethods/users'
		response = API(method=method, body=body).post()
		if response['ok'] == True :
			self.secret_id = response['data']['id']
		return response

	# Передать параметры идентификации юзера по апи в банк
	def add_identity(self, data):
		body = {k: v for k, v in data.items() if v != ''}
		method = 'customMethods/users/' + self.secret_id + '/identity'
		response = API(method=method, body=body).post()
		return response

	# Получить информацию о прохождении идентификации юзера
	def get_identity(self):
		method = 'customMethods/users/' + self.secret_id + '/identity'
		response = API(method=method, body={}).get()
		return response


# Класс кошельков юзера
class Wallets(Base):

	__tablename__ = 'wallets'

	id = Column(Integer, primary_key=True)
	wallet_id = Column(String(255), nullable=True)
	amount = Column(String(255), default=0)
	status = Column(Integer)
	user_id = Column(Integer, ForeignKey('users.id'))
	comment = Column(String(192), nullable=True)
	secret_id = Column(String(255), nullable=True)
	deleted = Column(Integer)

	def __init__(self, *args, **kwargs):
		super(Wallets, self).__init__(*args, **kwargs)

# Класс транзакций юзера
class Transactions(Base):

	__tablename__ = 'transactions'

	id = Column(Integer, primary_key=True)
	wallet_sender_id = Column(Integer, nullable=True)
	wallet_reciever_id = Column(Integer, nullable=True)
	user_id = Column(Integer, ForeignKey('users.id'))
	movement_type = Column(String(255))
	amount = Column(String(255))
	commission = Column(String(255))
	time = Column(Integer, default=timec.time())
	secret_t = Column(String(255), nullable=True)
	status = Column(Integer, default=1)
	card = Column(String(255), nullable=True)
	email = Column(String(255), nullable=True)
	link = Column(Integer, nullable=True)

	def __init__(self, *args, **kwargs):
		super(Transactions, self).__init__(*args, **kwargs)

# Класс для работы с смс
class Sms_approve(Base):

	__tablename__ = 'sms_approve'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, nullable=True)
	code = Column(Integer)
	action = Column(String(255))
	time = Column(Integer, default=timec.time())
	status = Column(Integer, default=0)
	phone = Column(String(255))
	api_url = 'https://api.smsgold.ru' # Урл апи смс сервиса
	method_getToken = '????????????' # Токен
	method_send = '/sms/v1/message/sendOne' # Метод для отправки смс

	def __init__(self, *args, **kwargs):
		super(Sms_approve, self).__init__(*args, **kwargs)
		self.generate_code()

	# Сгенерировать код
	def generate_code(self):
		self.code = 1111
		#self.code = random.randint(1000,9999)

	# Обновить время отправления смс, при повторной отправке
	def update_time(self):
		self.time = timec.time()

	# Метод для отправки смс
	def send_sms(self):
		headers = {"Content-Type" : "application/json", "charset" : "utf-8", "X-SDK" : "python | 0.0.1"}
		url = self.api_url + self.method_getToken
		response = requests.get(url, headers=headers)
		response = response.json()
		accessToken = response['accessToken']
		
		body = {
			'channel' : 'sms',
			'sms_text' : self.code,
			'viber_text' : '',
			'sms_sender' : 'SmsGold',
			'viber_sender' : '',
			'phone' : self.phone
		}

		headers['Authorization'] = 'Bearer ' + accessToken
		url = self.api_url + self.method_send

		response = requests.post(url, headers=headers, json=body)
		response = response.json()
		return response