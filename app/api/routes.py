from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.account import Account
from app.models.budget import Budget
from app.models.transaction import Transaction
from app.schemas.account import AccountCreate, AccountRead
from app.schemas.budget import BudgetCreate, BudgetRead
from app.schemas.transaction import TransactionCreate, TransactionRead

api_router = APIRouter()


@api_router.get("/health", tags=["health"])
def health_check() -> dict:
    return {"status": "ok"}


@api_router.post("/accounts", response_model=AccountRead, status_code=status.HTTP_201_CREATED)
def create_account(payload: AccountCreate, db: Session = Depends(get_db)) -> Account:
    existing = db.query(Account).filter(Account.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Account name already exists.")
    account = Account(name=payload.name, account_type=payload.account_type)
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


@api_router.get("/accounts", response_model=list[AccountRead])
def list_accounts(db: Session = Depends(get_db)) -> list[Account]:
    return db.query(Account).order_by(Account.name.asc()).all()


@api_router.post("/budgets", response_model=BudgetRead, status_code=status.HTTP_201_CREATED)
def create_budget(payload: BudgetCreate, db: Session = Depends(get_db)) -> Budget:
    existing = db.query(Budget).filter(Budget.name == payload.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Budget name already exists.")
    budget = Budget(name=payload.name, amount=payload.amount, period=payload.period)
    db.add(budget)
    db.commit()
    db.refresh(budget)
    return budget


@api_router.get("/budgets", response_model=list[BudgetRead])
def list_budgets(db: Session = Depends(get_db)) -> list[Budget]:
    return db.query(Budget).order_by(Budget.name.asc()).all()


@api_router.post(
    "/transactions", response_model=TransactionRead, status_code=status.HTTP_201_CREATED
)
def create_transaction(
    payload: TransactionCreate, db: Session = Depends(get_db)
) -> Transaction:
    account = db.query(Account).filter(Account.id == payload.account_id).first()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found.")
    transaction = Transaction(
        account_id=payload.account_id,
        amount=payload.amount,
        description=payload.description,
        transaction_date=payload.transaction_date,
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


@api_router.get("/transactions", response_model=list[TransactionRead])
def list_transactions(db: Session = Depends(get_db)) -> list[Transaction]:
    return db.query(Transaction).order_by(Transaction.transaction_date.desc()).all()
