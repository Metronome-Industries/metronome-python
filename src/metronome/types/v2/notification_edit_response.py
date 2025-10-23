# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .lifecycle_event_offset_notification_config import LifecycleEventOffsetNotificationConfig
from .lifecycle_event_system_notification_config import LifecycleEventSystemNotificationConfig

__all__ = ["NotificationEditResponse", "Data"]

Data: TypeAlias = Union[LifecycleEventSystemNotificationConfig, LifecycleEventOffsetNotificationConfig]


class NotificationEditResponse(BaseModel):
    data: Data
