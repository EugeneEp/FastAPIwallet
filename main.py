from routers import auth
from routers import wallet
from app import app

app.include_router(auth.router)

app.include_router(
    wallet.router,
    prefix="/wallet",
    tags=["Wallet"]
)