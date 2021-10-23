from fastapi import APIRouter

from app.api.api_v1.endpoints import login, subsidiaries, transactions, users

api_router = APIRouter()
api_router.include_router(login.router, prefix="/login", tags=["Login"])
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(subsidiaries.router, prefix="/subsidiaries", tags=["Subsidiaries"])
api_router.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
