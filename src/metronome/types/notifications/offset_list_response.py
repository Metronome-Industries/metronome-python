# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["OffsetListResponse", "Data", "DataPolicy"]


class DataPolicy(BaseModel):
    offset: str
    """
    ISO-8601 duration string indicating how much time before or after the base event
    this notification should be sent. Positive values indicate notifications after
    the event, negative values indicate notifications before the event. Examples:
    "P1D" (1 day after), "-PT2H" (2 hours before)
    """

    type: str
    """The type of lifecycle event that this offset is based on."""


class Data(BaseModel):
    id: str
    """ID for this offset notification configuration"""

    created_at: datetime
    """RFC 3339 timestamp when this notification configuration was created."""

    created_by: str
    """Who created this notification configuration"""

    environment_type: str
    """The environment type where this notification configuration was created."""

    name: str
    """The name for this offset notification configuration."""

    policy: DataPolicy

    type: str
    """Indicates this is an offset lifecycle event notification"""


class OffsetListResponse(BaseModel):
    data: List[Data]

    cursor: Optional[str] = None
