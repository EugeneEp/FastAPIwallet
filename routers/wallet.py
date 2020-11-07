from fastapi import APIRouter, File, UploadFile
from app import get_db, get_current_user
from config import settings
from fastapi import Depends, Query, Path, Body, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional, List
import schemas
import shutil
from sqlalchemy import and_
from sqlalchemy_pagination import paginate
from models import Users, Transactions, hashpass, hashcsv, mergeTwoListsAsDict, timeToDate, dateToTime, movementTranslate, paginatorParse, transParse
from datetime import datetime
import time as timec
import glob
import os
import re
import csv

router = APIRouter()

# Получить данные профиля
@router.get('/profile')
async def profile(current_user: Users = Depends(get_current_user)):
	identity = {'fullname': '', 'passport': '', 'passportIssuedAt': ''}
	if current_user.identity:
		identity.update(current_user.identity)
	return {'success':True,'msg':'', 'identity':identity}

# Изменить данные профиля
@router.put('/profile', response_model=schemas.userIdentityOut)
async def profile(ident: schemas.userIdentity,
			current_user: Users = Depends(get_current_user),
			db: Session = Depends(get_db)):
	print(current_user.identity)
	current_user.identity = ident.identity
	db.add(current_user)
	db.commit()
	return schemas.userIdentityOut()

# Загрузить аватарку
@router.post('/profile_picture')
async def profile_picture(image: UploadFile = File(...),
					current_user: Users = Depends(get_current_user)):
	for x in glob.glob('static/upload/profile/' + str(current_user.id) + '.png'):
		os.unlink(x)

	filename = str(current_user.id) + '.png'
	with open('static/upload/profile/'+filename, "wb") as buffer:
		shutil.copyfileobj(image.file, buffer)

	return {'success':True,'message':'Фотография обновлена'}

# Транзакции пользователя
@router.post('/transactions')
async def get_transactions(date_from: Optional[datetime] = None,
				date_end: Optional[datetime] = None, 
				page: Optional[int] = Query(1, gt=0, description='Страница'),
				current_user: Users = Depends(get_current_user),
				db: Session = Depends(get_db)):
	filters = []

	filters.append(Transactions.user_id == current_user.id)

	if date_from and date_from != "":
		filters.append(Transactions.time > dateToTime(date_from))
	if date_end and date_end != "":
		filters.append(Transactions.time < dateToTime(date_end))

	transactions = paginate(db.query(Transactions).filter(and_(*filters)).order_by(Transactions.id.desc()), page, 8)

	t = transParse(transactions.items)
	p = paginatorParse(transactions, page)

	return {'success':True,'msg':'','trans':t,'paginator':p}

# Получить список транзакций в CSV формате
@router.post('/csv')
async def get_csv(date_from: Optional[datetime] = None,
			date_end: Optional[datetime] = None,
			current_user: Users = Depends(get_current_user),
			db: Session = Depends(get_db)):
	try:
		mylist = [['Дата', 'Тип транзакции', 'Статус', 'Сумма']]

		filters = []

		filters.append(Transactions.user_id == current_user.id)

		if date_from and date_from != "":
			filters.append(Transactions.time > dateToTime(date_from))
		if date_end and date_end != "":
			filters.append(Transactions.time < dateToTime(date_end))
			
		transactions = db.query(Transactions).filter(and_(*filters)).order_by(Transactions.id.desc()).all()
		for t in transactions:
			t.time = timeToDate(t.time)
			t.movement_type = movementTranslate(t.movement_type)
			mylist.append([t.time, t.movement_type, t.status, t.amount])
			
		link = hashcsv(current_user.id)

		with open(link, 'w', newline='', encoding='cp1251') as myfile:
			wr = csv.writer(myfile, delimiter=";")
			for x in mylist:
				wr.writerow(x)

		return {'success':True, 'msg':'', 'link': settings.HOST_NAME + '/' + link + '?t=' + str(timec.time())}
	except:
		return JSONResponse(status_code=500, content={'message':'Что-то пошло не так'})


# Пополнить кошелек
@router.post('/charge')
async def charge(current_user: {} = Depends(get_current_user)):
	return JSONResponse(status_code=403, content={'message':'Метод еще не готов'})

# Перевод на кошелек
@router.post('/transfer')
async def transfer(current_user: Users = Depends(get_current_user)):
	return JSONResponse(status_code=403, content={'message':'Метод еще не готов'})

# Создать ссылку для сбора средств на кошелек
@router.post('/moneybank')
async def moneybank(current_user: Users = Depends(get_current_user)):
	return JSONResponse(status_code=403, content={'message':'Метод еще не готов'})

# Создать ссылку на пожертвования
@router.post('/donate')
async def donate(current_user: Users = Depends(get_current_user)):
	return JSONResponse(status_code=403, content={'message':'Метод еще не готов'})