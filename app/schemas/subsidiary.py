from typing import Optional

from pydantic import BaseModel


# Shared properties
class SubsidiaryBase(BaseModel):
    name: Optional[str] = None


# Properties to receive via API on creation
class SubsidiaryCreate(SubsidiaryBase):
    name: str


# Properties to receive via API on update
class SubsidiaryUpdate(SubsidiaryBase):
    pass


# Properties shared by models stored in DB
class SubsidiaryInDBBase(SubsidiaryBase):
    id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Subsidiary(SubsidiaryInDBBase):
    pass


# Properties properties stored in DB
class SubsidiaryInDB(SubsidiaryInDBBase):
    pass
