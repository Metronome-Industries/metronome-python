# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["QuantityConversionParam"]


class QuantityConversionParam(TypedDict, total=False):
    conversion_factor: Required[float]
    """The factor to multiply or divide the quantity by."""

    operation: Required[Literal["MULTIPLY", "DIVIDE"]]
    """The operation to perform on the quantity"""

    name: str
    """Optional name for this conversion."""
