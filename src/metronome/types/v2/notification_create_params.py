# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .lifecycle_event_offset_policy_param import LifecycleEventOffsetPolicyParam

__all__ = ["NotificationCreateParams"]


class NotificationCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name for this offset notification configuration."""

    policy: Required[LifecycleEventOffsetPolicyParam]
    """
    The offset lifecycle event policy that defines when and how this notification
    should be triggered. The lifecycle event type is inferred from the policy.type
    field.
    """

    uniqueness_key: str
    """Optional uniqueness key to prevent duplicate notification configurations."""
