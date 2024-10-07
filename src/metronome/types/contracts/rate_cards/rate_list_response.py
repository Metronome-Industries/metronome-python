# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...shared.rate import Rate
from ...shared.tier import Tier
from ...shared.credit_type_data import CreditTypeData

__all__ = ["RateListResponse", "CommitRate"]


class CommitRate(BaseModel):
    rate_type: Literal[
        "FLAT",
        "flat",
        "PERCENTAGE",
        "percentage",
        "SUBSCRIPTION",
        "subscription",
        "TIERED",
        "tiered",
        "CUSTOM",
        "custom",
    ]

    credit_type: Optional[CreditTypeData] = None

    is_prorated: Optional[bool] = None
    """Commit rate proration configuration. Only valid for SUBSCRIPTION rate_type."""

    price: Optional[float] = None
    """Commit rate price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    quantity: Optional[float] = None
    """Commit rate quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Optional[List[Tier]] = None
    """Only set for TIERED rate_type."""

    use_list_prices: Optional[bool] = None
    """Only set for PERCENTAGE rate_type.

    Defaults to false. If true, rate is computed using list prices rather than the
    standard rates for this product on the contract.
    """


class RateListResponse(BaseModel):
    entitled: bool

    product_id: str

    product_name: str

    product_tags: List[str]

    rate: Rate

    starting_at: datetime

    commit_rate: Optional[CommitRate] = None
    """The rate that will be used to rate a product when it is paid for by a commit.

    This feature requires opt-in before it can be used. Please contact Metronome
    support to enable this feature.
    """

    ending_before: Optional[datetime] = None

    pricing_group_values: Optional[Dict[str, str]] = None
