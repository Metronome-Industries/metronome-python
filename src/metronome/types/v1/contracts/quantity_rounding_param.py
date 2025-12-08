# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["QuantityRoundingParam"]


class QuantityRoundingParam(TypedDict, total=False):
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be rounded using the provided rounding method and decimal places. For example, if the method is "round up" and the decimal places is 0, then the quantity will be rounded up to the nearest integer.
    """

    decimal_places: Required[float]

    rounding_method: Required[Literal["ROUND_UP", "ROUND_DOWN", "ROUND_HALF_UP"]]
