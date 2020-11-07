from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from config import settings
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import jwt

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.mount("/static", StaticFiles(directory="static"), name="static")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login')

engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from models import Users

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
	try:
		data = jwt.decode(token, settings.SECRET_KEY)
		user = db.query(Users).filter(Users.phone==int(data['sub'])).first()
		if not user:
			return JSONResponse(status_code=401, content={'message':'Пользователь не найден'})
		return user
	except jwt.ExpiredSignatureError:
		return JSONResponse(status_code=401, content={'message':'Истек срок действия токена'})
	except (jwt.InvalidTokenError, Exception) as e:
		print('test')
		print(e)
		return JSONResponse(status_code=401, content={'message':'Некорректный токен'})
	return user