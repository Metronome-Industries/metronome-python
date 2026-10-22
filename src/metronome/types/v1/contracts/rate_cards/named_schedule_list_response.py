# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["NamedScheduleListResponse", "Segment"]


class Segment(BaseModel):
    starting_at: datetime

    value: object

    ending_before: Optional[datetime] = None


class NamedScheduleListResponse(BaseModel):
    contract_id: str
    """ID of the contract this named schedule belongs to."""

    schedule_name: str
    """Name of the schedule."""

    segments: List[Segment]

    properties: Optional[Dict[str, str]] = None
    """Properties on this named schedule."""
