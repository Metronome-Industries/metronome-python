# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["ProductOrderSetParams"]


class ProductOrderSetParams(TypedDict, total=False):
    product_order: Required[List[str]]

    rate_card_id: Required[str]
    """ID of the rate card to update"""
