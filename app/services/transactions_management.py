import datetime

from app.api.finance.finance_schemas import NewSingleTransactionRequestSchema
from app.common.enums import TransactionCategory


def add_single_transaction(value: int, category: TransactionCategory, date: datetime.datetime):
    return NewSingleTransactionRequestSchema(success=True)