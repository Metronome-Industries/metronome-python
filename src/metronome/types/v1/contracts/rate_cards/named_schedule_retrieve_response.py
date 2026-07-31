# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["NamedScheduleRetrieveResponse", "Data"]


class Data(BaseModel):
    starting_at: datetime

    value: object

    ending_before: Optional[datetime] = None


class NamedScheduleRetrieveResponse(BaseModel):
    data: List[Data]
