# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .lifecycle_event_system_notification_config import LifecycleEventSystemNotificationConfig

__all__ = ["NotificationListSystemResponse"]


class NotificationListSystemResponse(BaseModel):
    data: List[LifecycleEventSystemNotificationConfig]

    cursor: Optional[str] = None
