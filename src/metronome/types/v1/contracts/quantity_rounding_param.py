# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["QuantityRoundingParam"]


class QuantityRoundingParam(TypedDict, total=False):
    decimal_places: Required[float]

    rounding_method: Required[Literal["ROUND_UP", "ROUND_DOWN", "ROUND_HALF_UP"]]
