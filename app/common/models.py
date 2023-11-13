"""
File for storing all Pydantic models and @dataclasses
"""
import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from app.common.enums import TransactionCategory





class ErrorResponse(BaseModel):
    StatusCode: int
    ErrorMessage: str
