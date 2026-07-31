# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ....._types import SequenceNotStr

__all__ = ["ProductOrderSetParams"]


class ProductOrderSetParams(TypedDict, total=False):
    product_order: Required[SequenceNotStr[str]]

    rate_card_id: Required[str]
    """ID of the rate card to update"""
