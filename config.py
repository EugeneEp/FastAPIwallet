from pydantic import BaseSettings
class Settings(BaseSettings):
	app_name: str = "FastAPI Wallet"
	SQLALCHEMY_DATABASE_URL: str = 'postgresql://postgres:11111111@localhost:5432/acckasdq_1'
	SECRET_KEY: str = 'JIO982je1ij189JIW)DWj='
	HOST_NAME: str = 'http://127.0.0.1:8000'

settings = Settings()