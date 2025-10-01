# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ContractGetSubscriptionSeatsScheduleHistoryResponse", "Data"]


class Data(BaseModel):
    assigned_seat_ids: List[str]
    """Array of seat IDs that are assigned in this period"""

    ending_before: Optional[datetime] = None
    """The end time of this seat schedule period (null if ongoing)"""

    starting_at: datetime
    """The start time of this seat schedule period"""

    total_quantity: int
    """Total number of assigned and unassigned seats in this period"""


class ContractGetSubscriptionSeatsScheduleHistoryResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
    """Cursor for the next page of results"""
