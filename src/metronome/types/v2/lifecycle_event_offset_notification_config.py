# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .lifecycle_event_offset_policy import LifecycleEventOffsetPolicy

__all__ = ["LifecycleEventOffsetNotificationConfig"]


class LifecycleEventOffsetNotificationConfig(BaseModel):
    id: str
    """ID for this offset notification configuration"""

    archived_at: Optional[datetime] = None
    """When this notification configuration was archived"""

    created_at: datetime
    """RFC 3339 timestamp when this notification configuration was created."""

    created_by: str
    """Who created this notification configuration"""

    environment_type: str
    """The environment type where this notification configuration was created."""

    name: str
    """The name for this offset notification configuration."""

    policy: LifecycleEventOffsetPolicy

    type: Literal["OFFSET_LIFECYCLE_EVENT"]
    """Indicates this is an offset lifecycle event notification"""
