# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["LifecycleEventSystemNotificationConfig", "Policy"]

class Policy(BaseModel):
    type: str
    """The type of lifecycle event (e.g., "contract.create", "contract.start")"""

class LifecycleEventSystemNotificationConfig(BaseModel):
    policy: Policy

    type: str
    """Indicates this is a system lifecycle event notification"""

    is_enabled: Optional[bool] = None
    """Whether or not webhook publishing for this lifecycle event is enabled"""