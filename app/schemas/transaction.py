from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


# Shared properties
class TransactionBase(BaseModel):
    code: Optional[str] = None
    transmitter: Optional[str] = None
    receiver: Optional[str] = None
    from_subsidiary_id: Optional[int] = None
    to_subsidiary_id: Optional[int] = None
    quantity: Optional[Decimal] = None
    commission: Optional[Decimal] = None
    is_delivered: Optional[bool] = False


# Properties to receive via API on creation
class TransactionCreate(TransactionBase):
    code: str
    transmitter: str
    receiver: str
    from_subsidiary_id: int
    to_subsidiary_id: int
    quantity: Decimal
    commission: Decimal


# Properties to receive via API on update
class TransactionUpdate(TransactionBase):
    pass


# Properties shared by models stored in DB
class TransactionInDBBase(TransactionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Transaction(TransactionInDBBase):
    pass


# Properties properties stored in DB
class TransactionInDB(TransactionInDBBase):
    pass
