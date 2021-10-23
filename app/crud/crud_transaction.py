from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate


class CRUDTransaction(CRUDBase[Transaction, TransactionCreate, TransactionUpdate]):
    def create_with_user(
        self,
        db: Session,
        *,
        obj_in: TransactionCreate,
        user_id: int
    ) -> Transaction:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, user_id=user_id)

        return super().create(db, obj_in=db_obj)

    def get_multi_by_user(
        self,
        db: Session,
        *,
        user_id: int,
        skip: int,
        limit: int
    ) -> List[Transaction]:
        return (db
                .query(self.model)
                .filter(Transaction.user_id == user_id)
                .order_by(Transaction.id.desc())
                .offset(skip)
                .limit(limit)
                .all())


transaction = CRUDTransaction(Transaction)
