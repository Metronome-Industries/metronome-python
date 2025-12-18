# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .tier import Tier

__all__ = ["CommitRate"]


class CommitRate(TypedDict, total=False):
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or commit.
    """

    rate_type: Required[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]]

    price: float
    """Commit rate price. For FLAT rate_type, this must be >=0."""

    tiers: Iterable[Tier]
    """Only set for TIERED rate_type."""
