from fastapi import APIRouter
from app import get_db
from fastapi import Depends, Query, Path, Body, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional, List
from models import Users, Sms_approve, hashpass
import schemas
import time

router = APIRouter()

@router.post('/registration', response_model=schemas.regUserOut, tags=['Auth'])
async def reg_user(user: schemas.regUser, db: Session = Depends(get_db)):

	"""
    Регистрация пользователя

    - **phone**: Телефон
    - **password**: Пароль
    - **confirm**: Папроль повторно

    """

	user_exist = db.query(Users).filter(Users.phone==int(user.phone)).first()
	sms = db.query(Sms_approve).filter(Sms_approve.phone==user.phone, Sms_approve.action=='reg').first()
	if sms:
		if sms.status == 0:
			return JSONResponse(status_code=400, content={'message':'Вы не подтвердили смс'})
		if user_exist and sms.status == 1:
			return JSONResponse(status_code=400, content={'message':'Такой пользователь уже зарегистрирован'})
	else:
		return JSONResponse(status_code=400, content={'message':'Вы не отправили смс'})

	if user.confirm != user.password:
		return JSONResponse(status_code=400, content={'message':'Пароли не совпадают'})

	new_user = Users(phone=int(user.phone), password=user.password)
	db.add(new_user)
	db.commit()
	db.refresh(new_user)

	return schemas.regUserOut(id=new_user.id, phone=new_user.phone)

# Получить токен (логин)
@router.post('/login', tags=['Auth'], response_model=schemas.logUserOut)
async def log_user(user: schemas.logUser, db: Session = Depends(get_db)):

	"""
    Получить токен / вход

    - **phone**: Телефон
    - **password**: Пароль

    """

	current_user = db.query(Users).filter(Users.phone==int(user.phone), Users.password==hashpass(user.password)).first()
	if current_user:
		if current_user.roots == 0:
			return JSONResponse(status_code=400, content={'message':'Вы не прошли подтверждение'})
		return schemas.logUserOut(id=current_user.id, phone=current_user.phone)
	else:
		return JSONResponse(status_code=404, content={'message':'Телефон и пароль не совпадают'})

# Отправить код по смс
@router.post('/sms', tags=['SMS'], response_model=schemas.SmsOut)
async def send_sms(sms: schemas.Sms, db: Session = Depends(get_db)):

	"""
    Отправить код по смс

    - **phone**: Телефон
    - **sms_type**: reg

    """

	timelimit = int(time.time())
	# Было ли отправлено смс по этому номеру, на конкретное действие
	re_sms = db.query(Sms_approve).filter(Sms_approve.phone==sms.phone, Sms_approve.action==sms.sms_type).first()

	if re_sms:
		if (timelimit - re_sms.time) < 60:
			return JSONResponse(status_code=400, content={'message':'Повторное смс будет доступно через минуту'})
		elif re_sms.action == 'reg' and re_sms.status == 1:
			return JSONResponse(status_code=400, content={'message':'Пользователь уже прошел проверку'})
		else:
			re_sms.generate_code()
			re_sms.update_time()
			re_sms.status = 0
			# Отправить повторное смс по апи
			#send = re_sms.send_sms()
			db.commit()
	else:
		new_sms = Sms_approve(action=sms.sms_type, phone=sms.phone)

		# Отправить смс по апи
		#send = sms.send_sms()
		db.add(new_sms)
		db.commit()

	return schemas.SmsOut()

# Проверка кода смс
@router.post('/sms_check', response_model=schemas.SmsOut, tags=['SMS'])
async def sms_check(sms: schemas.SmsCheck, db: Session = Depends(get_db)):

	"""
    Проверка кода смс

    - **phone**: Телефон
    - **sms_type**: reg
    - **code**: Код смс

    """

	timelimit = int(time.time())

	re_sms = db.query(Sms_approve).filter(Sms_approve.status==0, Sms_approve.phone==sms.phone, Sms_approve.action==sms.sms_type, Sms_approve.code==sms.code).first()

	if re_sms:
		if (timelimit - re_sms.time) > (60 * 60):
			return JSONResponse(status_code=400, content={'message':'Проверочный код истек, повторите отправку'})
		re_sms.status = 1
		db.commit()
	else:
		return JSONResponse(status_code=400, content={'message':'Код смс введен не верно'})

	return schemas.SmsOut()