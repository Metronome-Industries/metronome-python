# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotificationCreateParams", "Policy"]


class NotificationCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name for this offset notification configuration."""

    policy: Required[Policy]
    """
    The offset lifecycle event policy that defines when and how this notification
    should be triggered. The lifecycle event type is inferred from the policy.type
    field.
    """

    uniqueness_key: str
    """Optional uniqueness key to prevent duplicate notification configurations."""


class Policy(TypedDict, total=False):
    offset: Required[str]
    """
    ISO-8601 duration string indicating how much time before or after the base event
    this notification should be sent. Positive values indicate notifications after
    the event, negative values indicate notifications before the event. Examples:
    "P1D" (1 day after), "-PT2H" (2 hours before)
    """

    type: Required[str]
    """The type of lifecycle event that this offset is based on."""
