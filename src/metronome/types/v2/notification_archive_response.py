# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .lifecycle_event_offset_notification_config import LifecycleEventOffsetNotificationConfig

__all__ = ["NotificationArchiveResponse"]


class NotificationArchiveResponse(BaseModel):
    data: LifecycleEventOffsetNotificationConfig
