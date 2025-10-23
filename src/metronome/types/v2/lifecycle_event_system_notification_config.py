# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .lifecycle_event_system_policy import LifecycleEventSystemPolicy

__all__ = ["LifecycleEventSystemNotificationConfig"]


class LifecycleEventSystemNotificationConfig(BaseModel):
    policy: LifecycleEventSystemPolicy

    type: Literal["SYSTEM_LIFECYCLE_EVENT"]
    """Indicates this is a system lifecycle event notification"""

    is_enabled: Optional[bool] = None
    """Whether or not webhook publishing for this lifecycle event is enabled"""
