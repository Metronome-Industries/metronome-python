# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "NotificationUpdateResponse",
    "Data",
    "DataLifecycleEventSystemNotificationConfig",
    "DataLifecycleEventSystemNotificationConfigPolicy",
    "DataLifecycleEventOffsetNotificationConfig",
    "DataLifecycleEventOffsetNotificationConfigPolicy",
]


class DataLifecycleEventSystemNotificationConfigPolicy(BaseModel):
    type: str
    """The type of lifecycle event (e.g., "contract.create", "contract.start")"""


class DataLifecycleEventSystemNotificationConfig(BaseModel):
    policy: DataLifecycleEventSystemNotificationConfigPolicy

    type: str
    """Indicates this is a system lifecycle event notification"""

    is_enabled: Optional[bool] = None
    """Whether or not webhook publishing for this lifecycle event is enabled"""


class DataLifecycleEventOffsetNotificationConfigPolicy(BaseModel):
    offset: str
    """
    ISO-8601 duration string indicating how much time before or after the base event
    this notification should be sent. Positive values indicate notifications after
    the event, negative values indicate notifications before the event. Examples:
    "P1D" (1 day after), "-PT2H" (2 hours before)
    """

    type: str
    """The type of lifecycle event that this offset is based on."""


class DataLifecycleEventOffsetNotificationConfig(BaseModel):
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

    policy: DataLifecycleEventOffsetNotificationConfigPolicy

    type: str
    """Indicates this is an offset lifecycle event notification"""


Data: TypeAlias = Union[DataLifecycleEventSystemNotificationConfig, DataLifecycleEventOffsetNotificationConfig]


class NotificationUpdateResponse(BaseModel):
    data: Data
