from app.crud.base import CRUDBase
from app.models.subsidiary import Subsidiary
from app.schemas.subsidiary import SubsidiaryCreate, SubsidiaryUpdate


class CRUDSubsidiary(CRUDBase[Subsidiary, SubsidiaryCreate, SubsidiaryUpdate]):
    pass


subsidiary = CRUDSubsidiary(Subsidiary)
