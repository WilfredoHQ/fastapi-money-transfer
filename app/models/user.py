from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    id = Column(Integer, index=True, primary_key=True)
    dni = Column(String, index=True, nullable=False, unique=True)
    full_name = Column(String, nullable=False)
    email = Column(String, index=True, nullable=False, unique=True)
    hashed_password = Column(String, index=True, nullable=False)
    is_active = Column(Boolean, default=True)
    transactions = relationship("Transaction", back_populates="user")
