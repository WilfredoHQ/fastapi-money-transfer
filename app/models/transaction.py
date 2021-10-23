from sqlalchemy import Boolean, Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Transaction(Base):
    id = Column(Integer, index=True, primary_key=True)
    code = Column(String, index=True, nullable=False, unique=True)
    transmitter = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    from_subsidiary_id = Column(Integer, ForeignKey("subsidiary.id"))
    to_subsidiary_id = Column(Integer, ForeignKey("subsidiary.id"))
    quantity = Column(Numeric, nullable=False)
    commission = Column(Numeric, nullable=False)
    is_delivered = Column(Boolean, index=True, default=False)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="transactions")
