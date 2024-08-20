# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RolloverAmountMaxAmountParam"]


class RolloverAmountMaxAmountParam(TypedDict, total=False):
    type: Required[Literal["MAX_AMOUNT"]]
    """Rollover up to a fixed amount of the original credit grant amount."""

    value: Required[float]
    """The maximum amount to rollover."""
