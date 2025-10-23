# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["LifecycleEventSystemPolicy"]


class LifecycleEventSystemPolicy(BaseModel):
    type: str
    """The type of lifecycle event (e.g., "contract.create", "contract.start")"""
