from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api import deps
from app.core import security
from app.core.config import settings
from app.core.security import get_password_hash
from app.utils import (generate_password_reset_token,
                       send_reset_password_email, verify_password_reset_token)

router = APIRouter()


@router.post("/access-token", response_model=schemas.Token)
def login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests.
    """
    user = crud.user.authenticate(db, email=form_data.username, password=form_data.password)

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="El email o contraseña son incorrectos")
    elif not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario inactivo")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return {
        "access_token": security.create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "bearer",
    }


@router.post("/reset-password")
def reset_password(
    data_in: schemas.ResetPassword,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Reset password.
    """
    email = verify_password_reset_token(token=data_in.token)

    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El email no existe")
    elif not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Usuario inactivo")

    hashed_password = get_password_hash(password=data_in.new_password)
    user.hashed_password = hashed_password
    db.add(user)
    db.commit()

    return {"detail": "Contraseña actualizada con éxito"}


@router.post("/reset-password/{email}")
def reset_password_token(
    email: str,
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Get a token for reset password.
    """
    user = crud.user.get_by_email(db, email=email)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El email no existe")

    password_reset_token = generate_password_reset_token(email=email)
    send_reset_password_email(email_to=user.email, full_name=user.full_name, token=password_reset_token)

    return {"detail": "Email de recuperación enviado"}
