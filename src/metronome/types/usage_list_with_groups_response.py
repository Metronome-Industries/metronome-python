# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["UsageListWithGroupsResponse", "Data"]


class Data(BaseModel):
    ending_before: datetime

    group_key: Optional[str] = None

    group_value: Optional[str] = None

    starting_on: datetime

    value: Optional[float] = None


class UsageListWithGroupsResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
