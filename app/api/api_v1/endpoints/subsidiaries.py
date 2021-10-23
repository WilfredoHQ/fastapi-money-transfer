from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Subsidiary])
def read_subsidiaries(
    skip: int = 0,
    limit: int = 50,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Read subsidiaries.
    """
    subsidiaries = crud.subsidiary.get_multi(db, skip=skip, limit=limit)

    return subsidiaries


@router.post("/", response_model=schemas.Subsidiary)
def create_subsidiary(
    subsidiary_in: schemas.SubsidiaryCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Create subsidiary.
    """
    subsidiary = crud.subsidiary.create(db, obj_in=subsidiary_in)

    return subsidiary


@router.get("/{subsidiary_id}", response_model=schemas.Subsidiary)
def read_subsidiary(
    subsidiary_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Read subsidiary by id.
    """
    subsidiary = crud.subsidiary.get(db, id=subsidiary_id)

    if not subsidiary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La sucursal no existe")

    return subsidiary


@router.delete("/{subsidiary_id}", response_model=schemas.Subsidiary)
def delete_subsidiary(
    subsidiary_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Delete subsidiary.
    """
    subsidiary = crud.subsidiary.get(db, id=subsidiary_id)

    if not subsidiary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La sucursal no existe")

    subsidiary = crud.subsidiary.remove(db, id=subsidiary_id)

    return subsidiary


@router.patch("/{subsidiary_id}", response_model=schemas.Subsidiary)
def update_subsidiary(
    subsidiary_id: int,
    subsidiary_in: schemas.SubsidiaryUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db)
) -> Any:
    """
    Update subsidiary.
    """
    subsidiary = crud.subsidiary.get(db, id=subsidiary_id)

    if not subsidiary:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="La sucursal no existe")

    subsidiary = crud.subsidiary.update(db, db_obj=subsidiary, obj_in=subsidiary_in)

    return subsidiary
