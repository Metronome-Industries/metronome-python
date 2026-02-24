# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .tier import Tier

__all__ = ["CommitRate", "MinimumConfig"]


class MinimumConfig(TypedDict, total=False):
    """Only set for TIERED_PERCENTAGE or PERCENTAGE rate_type."""

    minimum: Required[float]


class CommitRate(TypedDict, total=False):
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or commit.
    """

    rate_type: Required[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "TIERED_PERCENTAGE", "CUSTOM"]]

    minimum_config: MinimumConfig
    """Only set for TIERED_PERCENTAGE or PERCENTAGE rate_type."""

    price: float
    """Commit rate price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    tiers: Iterable[Tier]
    """Only set for TIERED rate_type."""
