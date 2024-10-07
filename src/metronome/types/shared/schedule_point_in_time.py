# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .credit_type_data import CreditTypeData

__all__ = ["SchedulePointInTime", "ScheduleItem"]


class ScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class SchedulePointInTime(BaseModel):
    credit_type: Optional[CreditTypeData] = None

    schedule_items: Optional[List[ScheduleItem]] = None
