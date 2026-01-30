from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    account_type = Column(String(50), nullable=False, default="checking")
