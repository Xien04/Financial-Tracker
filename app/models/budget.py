from sqlalchemy import Column, Integer, Numeric, String

from app.db.base import Base


class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    amount = Column(Numeric(12, 2), nullable=False)
    period = Column(String(20), nullable=False, default="monthly")
