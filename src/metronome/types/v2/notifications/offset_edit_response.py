# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from ..lifecycle_event_system_notification_config import LifecycleEventSystemNotificationConfig

from ..lifecycle_event_offset_notification_config import LifecycleEventOffsetNotificationConfig

from typing_extensions import TypeAliasType, TypeAlias

from ...._models import BaseModel

__all__ = ["OffsetEditResponse", "Data"]

Data: TypeAlias = Union[LifecycleEventSystemNotificationConfig, LifecycleEventOffsetNotificationConfig]

class OffsetEditResponse(BaseModel):
    data: Data