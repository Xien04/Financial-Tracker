from pydantic import BaseModel, Field, condecimal


class BudgetBase(BaseModel):
    name: str = Field(..., max_length=100)
    amount: condecimal(max_digits=12, decimal_places=2)
    period: str = Field(default="monthly", max_length=20)


class BudgetCreate(BudgetBase):
    pass


class BudgetRead(BudgetBase):
    id: int

    class Config:
        orm_mode = True
