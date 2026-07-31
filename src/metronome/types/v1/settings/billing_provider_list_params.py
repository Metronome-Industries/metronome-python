# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["BillingProviderListParams"]


class BillingProviderListParams(TypedDict, total=False):
    next_page: Optional[str]
    """The cursor to the next page of results"""
