from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Transaction])
def read_transactions(
    skip: int = 0,
    limit: int = 50,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Read transactions.
    """
    transactions = crud.transaction.get_multi_by_user(db, user_id=current_user.id, skip=skip, limit=limit)

    return transactions


@router.post("/", response_model=schemas.Transaction)
def create_transaction(
    transaction_in: schemas.TransactionCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Create transaction.
    """
    transaction = crud.transaction.create_with_user(db, obj_in=transaction_in, user_id=current_user.id)

    return transaction


@router.get("/{transaction_id}", response_model=schemas.Transaction)
def read_transaction(
    transaction_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Read transaction by id.
    """
    transaction = crud.transaction.get(db, id=transaction_id)

    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La transacción no existe")

    return transaction


@router.delete("/{transaction_id}", response_model=schemas.Transaction)
def delete_transaction(
    transaction_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete transaction.
    """
    transaction = crud.transaction.get(db, id=transaction_id)

    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La transacción no existe")

    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Necesita autorización")

    transaction = crud.transaction.remove(db, id=transaction_id)

    return transaction


@router.patch("/{transaction_id}", response_model=schemas.Transaction)
def update_transaction(
    transaction_id: int,
    transaction_in: schemas.TransactionUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Update transaction.
    """
    transaction = crud.transaction.get(db, id=transaction_id)

    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La transacción no existe")

    if transaction.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Necesita autorización")

    transaction = crud.transaction.update(db, db_obj=transaction, obj_in=transaction_in)

    return transaction
