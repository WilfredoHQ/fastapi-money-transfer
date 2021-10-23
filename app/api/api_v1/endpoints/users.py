from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.core.config import settings
from app.utils import send_new_account_email

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 50,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Read users.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)

    return users


@router.post("/", response_model=schemas.User)
def create_user(
    user_in: schemas.UserCreate,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Create user.
    """
    user = crud.user.get_by_dni(db, dni=user_in.dni)

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El DNI ya existe")

    user = crud.user.get_by_email(db, email=user_in.email)

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya existe")

    user = crud.user.create(db, obj_in=user_in)

    if settings.EMAILS_ENABLED and user_in.email:
        send_new_account_email(email_to=user_in.email, full_name=user_in.full_name)

    return user


@router.get("/me", response_model=schemas.User)
def read_user_me(
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Read current user.
    """
    return current_user


@router.patch("/me", response_model=schemas.User)
def update_user_me(
    user_in: schemas.UserUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Update current user.
    """
    user = crud.user.get_by_email(db, email=user_in.email)

    if user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="El email ya existe")

    user = crud.user.update(db, db_obj=current_user, obj_in=user_in)

    return user


@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Read user by id.
    """
    user = crud.user.get(db, id=user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El usuario no existe")

    return user
