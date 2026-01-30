from datetime import date

from pydantic import BaseModel, Field, condecimal


class TransactionBase(BaseModel):
    account_id: int
    amount: condecimal(max_digits=12, decimal_places=2)
    description: str | None = Field(default=None, max_length=255)
    transaction_date: date


class TransactionCreate(TransactionBase):
    pass


class TransactionRead(TransactionBase):
    id: int

    class Config:
        orm_mode = True
