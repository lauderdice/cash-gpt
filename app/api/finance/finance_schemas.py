import datetime

from pydantic import BaseModel

from app.common.enums import TransactionCategory


class NewSingleTransactionResponseSchema(BaseModel):
    success: bool


class NewSingleTransactionRequestSchema(BaseModel):
    value: int
    category: TransactionCategory
    date: datetime.datetime