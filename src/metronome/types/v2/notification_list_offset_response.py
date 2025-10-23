# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .lifecycle_event_offset_notification_config import LifecycleEventOffsetNotificationConfig

__all__ = ["NotificationListOffsetResponse"]


class NotificationListOffsetResponse(BaseModel):
    data: List[LifecycleEventOffsetNotificationConfig]

    cursor: Optional[str] = None
