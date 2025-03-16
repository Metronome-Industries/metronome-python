# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ProductOrderSetParams"]

class ProductOrderSetParams(TypedDict, total=False):
    product_order: Required[List[str]]

    rate_card_id: Required[str]
    """ID of the rate card to update"""