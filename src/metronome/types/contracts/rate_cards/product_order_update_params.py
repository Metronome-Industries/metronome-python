# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable

from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ProductOrderUpdateParams", "ProductMove"]

class ProductOrderUpdateParams(TypedDict, total=False):
    product_moves: Required[Iterable[ProductMove]]

    rate_card_id: Required[str]
    """ID of the rate card to update"""

class ProductMove(TypedDict, total=False):
    position: Required[float]
    """0-based index of the new position of the product"""

    product_id: Required[str]
    """ID of the product to move"""