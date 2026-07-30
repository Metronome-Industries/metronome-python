# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["OffsetRetrieveParams"]

class OffsetRetrieveParams(TypedDict, total=False):
    id: Required[str]
    """The ID of the notification configuration to retrieve"""