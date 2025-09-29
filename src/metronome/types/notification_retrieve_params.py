# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotificationRetrieveParams"]


class NotificationRetrieveParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the notification configuration to retrieve"""
