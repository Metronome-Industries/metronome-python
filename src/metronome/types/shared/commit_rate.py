# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .tier import Tier
from ..._models import BaseModel

__all__ = ["CommitRate", "MinimumConfig"]


class MinimumConfig(BaseModel):
    """Only set for TIERED_PERCENTAGE or PERCENTAGE rate_type."""

    minimum: float


class CommitRate(BaseModel):
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or commit.
    """

    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "TIERED_PERCENTAGE", "CUSTOM"]

    minimum_config: Optional[MinimumConfig] = None
    """Only set for TIERED_PERCENTAGE or PERCENTAGE rate_type."""

    price: Optional[float] = None
    """Commit rate price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    tiers: Optional[List[Tier]] = None
    """Only set for TIERED rate_type."""
