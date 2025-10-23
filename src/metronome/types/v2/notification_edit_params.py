# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .lifecycle_event_offset_policy_param import LifecycleEventOffsetPolicyParam
from .lifecycle_event_system_policy_param import LifecycleEventSystemPolicyParam

__all__ = ["NotificationEditParams", "Variant0", "Variant1"]


class Variant0(TypedDict, total=False):
    policy: Required[LifecycleEventSystemPolicyParam]

    type: Required[Literal["SYSTEM_LIFECYCLE_EVENT"]]
    """Indicates this is a system lifecycle event notification"""

    is_enabled: bool
    """
    Set to true to enable webhook messages for the notification indicated in the
    policy, false to disable. Only supported by system lifecycle events.
    """


class Variant1(TypedDict, total=False):
    id: Required[str]
    """The ID of the notification configuration to edit."""

    policy: Required[LifecycleEventOffsetPolicyParam]

    type: Required[Literal["OFFSET_LIFECYCLE_EVENT"]]
    """Indicates this is an offset lifecycle event notification"""

    is_enabled: bool
    """
    Set to true to enable webhook messages for the notification indicated in the
    policy, false to disable. Only supported by system lifecycle events.
    """


NotificationEditParams: TypeAlias = Union[Variant0, Variant1]
