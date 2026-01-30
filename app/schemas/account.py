from pydantic import BaseModel, Field


class AccountBase(BaseModel):
    name: str = Field(..., max_length=100)
    account_type: str = Field(default="checking", max_length=50)


class AccountCreate(AccountBase):
    pass


class AccountRead(AccountBase):
    id: int

    class Config:
        orm_mode = True
