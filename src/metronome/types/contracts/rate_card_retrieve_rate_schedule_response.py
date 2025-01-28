# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.rate import Rate
from ..shared.tier import Tier

__all__ = ["RateCardRetrieveRateScheduleResponse", "Data", "DataCommitRate"]


class DataCommitRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    price: Optional[float] = None
    """Commit rate price. For FLAT rate_type, this must be >=0."""

    tiers: Optional[List[Tier]] = None
    """Only set for TIERED rate_type."""


class Data(BaseModel):
    entitled: bool

    product_custom_fields: Dict[str, str]

    product_id: str

    product_name: str

    product_tags: List[str]

    rate: Rate

    starting_at: datetime

    commit_rate: Optional[DataCommitRate] = None
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or
    commit.
    """

    ending_before: Optional[datetime] = None

    pricing_group_values: Optional[Dict[str, str]] = None


class RateCardRetrieveRateScheduleResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
