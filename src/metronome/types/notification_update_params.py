# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["NotificationUpdateParams", "Policy", "PolicyLifecycleEventOffsetPolicy", "PolicyLifecycleEventSystemPolicy"]


class NotificationUpdateParams(TypedDict, total=False):
    policy: Required[Policy]
    """Updated policy configuration.

    The policy.type must match the existing lifecycle event type.
    """

    id: str
    """The ID of the notification configuration to edit.

    Not provided when updating the configuration for system events
    """

    is_enabled: bool
    """
    Set to true to enable webhook messages for the notification indicated in the
    policy, false to disable. Only supported by system lifecycle events.
    """


class PolicyLifecycleEventOffsetPolicy(TypedDict, total=False):
    offset: Required[str]
    """
    ISO-8601 duration string indicating how much time before or after the base event
    this notification should be sent. Positive values indicate notifications after
    the event, negative values indicate notifications before the event. Examples:
    "P1D" (1 day after), "-PT2H" (2 hours before)
    """

    type: Required[str]
    """The type of lifecycle event that this offset is based on."""


class PolicyLifecycleEventSystemPolicy(TypedDict, total=False):
    type: Required[str]
    """The type of lifecycle event (e.g., "contract.create", "contract.start")"""


Policy: TypeAlias = Union[PolicyLifecycleEventOffsetPolicy, PolicyLifecycleEventSystemPolicy]
