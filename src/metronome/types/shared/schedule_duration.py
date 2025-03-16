# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import List, Optional

from .credit_type_data import CreditTypeData

from typing_extensions import Literal

from pydantic import Field as FieldInfo

__all__ = ["ScheduleDuration", "ScheduleItem"]

class ScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime

class ScheduleDuration(BaseModel):
    schedule_items: List[ScheduleItem]

    credit_type: Optional[CreditTypeData] = None