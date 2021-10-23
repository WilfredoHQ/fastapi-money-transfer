from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Subsidiary(Base):
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String, nullable=False)
