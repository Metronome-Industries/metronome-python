# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .credit_type_data import CreditTypeData

__all__ = ["ScheduleDuration", "ScheduleItem"]


class ScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class ScheduleDuration(BaseModel):
    schedule_items: List[ScheduleItem]

    access_type: Optional[Literal["SPEND", "QUANTITY"]] = None
    """Indicates how the balance is drawn down.

    `SPEND` deducts the dollar cost of usage. `QUANTITY` deducts the number of units
    used.
    """

    credit_type: Optional[CreditTypeData] = None
