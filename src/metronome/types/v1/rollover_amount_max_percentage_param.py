# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RolloverAmountMaxPercentageParam"]


class RolloverAmountMaxPercentageParam(TypedDict, total=False):
    type: Required[Literal["MAX_PERCENTAGE"]]
    """Rollover up to a percentage of the original credit grant amount."""

    value: Required[float]
    """The maximum percentage (0-1) of the original credit grant to rollover."""
