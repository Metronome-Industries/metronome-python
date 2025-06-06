# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["RateAddResponse", "Data", "DataCommitRate", "DataCommitRateTier", "DataCreditType", "DataTier"]


class DataCommitRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataCommitRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    price: Optional[float] = None
    """Commit rate price. For FLAT rate_type, this must be >=0."""

    tiers: Optional[List[DataCommitRateTier]] = None
    """Only set for TIERED rate_type."""


class DataCreditType(BaseModel):
    id: str

    name: str


class DataTier(BaseModel):
    price: float

    size: Optional[float] = None


class Data(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]

    commit_rate: Optional[DataCommitRate] = None
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or
    commit.
    """

    credit_type: Optional[DataCreditType] = None

    custom_rate: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    pricing_group_values: Optional[Dict[str, str]] = None
    """
    if pricing groups are used, this will contain the values used to calculate the
    price
    """

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Optional[List[DataTier]] = None
    """Only set for TIERED rate_type."""

    use_list_prices: Optional[bool] = None
    """Only set for PERCENTAGE rate_type.

    Defaults to false. If true, rate is computed using list prices rather than the
    standard rates for this product on the contract.
    """


class RateAddResponse(BaseModel):
    data: Data
