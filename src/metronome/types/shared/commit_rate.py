# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .tier import Tier
from ..._models import BaseModel

__all__ = ["CommitRate"]


class CommitRate(BaseModel):
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or commit.
    """

    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    price: Optional[float] = None
    """Commit rate price. For FLAT rate_type, this must be >=0."""

    tiers: Optional[List[Tier]] = None
    """Only set for TIERED rate_type."""
