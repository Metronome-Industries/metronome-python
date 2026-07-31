# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .credit_type_data import CreditTypeData

__all__ = ["SchedulePointInTime", "ScheduleItem"]


class ScheduleItem(BaseModel):
    id: str

    amount: float

    quantity: float

    timestamp: datetime

    unit_price: float

    invoice_id: Optional[str] = None


class SchedulePointInTime(BaseModel):
    credit_type: Optional[CreditTypeData] = None

    do_not_invoice: Optional[bool] = None
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    schedule_items: Optional[List[ScheduleItem]] = None
