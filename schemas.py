from pydantic import BaseModel, Field
from typing import Optional, Set, List
import jwt
from datetime import datetime, timedelta
import re
from fastapi.responses import JSONResponse
from config import settings



# Registration schemas

class regUser(BaseModel):
	phone: str = Field(..., example='79999999999', min_length=11)
	password: str = Field(..., example='********')
	confirm: str = Field(..., example='********')

	def __init__(self, *args, **kwargs):
		super(regUser, self).__init__(*args, **kwargs)
		self.phone = re.sub("\D", "", self.phone)

class regUserOut(BaseModel):
	id: int = Field(...)
	token: str = None
	phone: str = Field(...)
	success: bool = True
	message: str = 'Успех'

	def __init__(self, *args, **kwargs):
		super(regUserOut, self).__init__(*args, **kwargs)
		self.token = jwt.encode({
			'sub': self.phone,
			'iat':datetime.utcnow(),
			'exp': datetime.utcnow() + timedelta(days=3)},
			settings.SECRET_KEY)

# Login schemas

class logUser(BaseModel):
	phone: str = Field(..., example='79999999999')
	password: str = Field(..., example='********')

	def __init__(self, *args, **kwargs):
		super(logUser, self).__init__(*args, **kwargs)
		self.phone = re.sub("\D", "", self.phone)

class logUserOut(BaseModel):
	id: int = Field(...)
	token: str = None
	phone: str = Field(...)
	success: bool = True
	message: str = 'Успех'

	def __init__(self, *args, **kwargs):
		super(logUserOut, self).__init__(*args, **kwargs)
		self.token = jwt.encode({
			'sub': self.phone,
			'iat':datetime.utcnow(),
			'exp': datetime.utcnow() + timedelta(days=3)},
			settings.SECRET_KEY)

# Sms schemas

class Sms(BaseModel):
	phone: str = Field(..., min_length=11, example='79999999999')
	sms_type: str = Field(..., example='reg')

	def __init__(self, *args, **kwargs):
		super(Sms, self).__init__(*args, **kwargs)
		self.phone = re.sub("\D", "", self.phone)

class SmsOut(BaseModel):
	success: bool = True
	message: str = 'Успех'

class SmsCheck(BaseModel):
	phone: str = Field(..., example='79999999999')
	sms_type: str = Field(..., example='reg')
	code: int = Field(..., ge=4, example='1111')

	def __init__(self, *args, **kwargs):
		super(SmsCheck, self).__init__(*args, **kwargs)
		self.phone = re.sub("\D", "", self.phone)

# Identity user scheme

class userIdentity(BaseModel):
	fullname: str = Field(..., example='test test test')
	passport: str = Field(..., example='1111 111111')
	passportIssuedAt: str = Field(..., example='2008-09-15')
	fullnameArr: dict = None
	identity: dict = None

	def __init__(self, *args, **kwargs):
		super(userIdentity, self).__init__(*args, **kwargs)
		self.fill_identity()

	def fill_identity(self):
		self.fullnameArr = self.fullname.split()
		self.passport = self.passport.replace(' ', '')

		if len(self.fullnameArr) < 3:
			return JSONResponse(status_code=400, content={'message':'ФИО введены не корректно'})
		self.identity = {
			'fullname': self.fullname,
			'lastName': self.fullnameArr[0],
			'firstName': self.fullnameArr[1],
			'secondName': self.fullnameArr[2],
			'passport': self.passport,
			'passportIssuedAt': self.passportIssuedAt
		}

class userIdentityOut(BaseModel):
	success: bool = True
	message: str = 'Данные успешно отправлены'	