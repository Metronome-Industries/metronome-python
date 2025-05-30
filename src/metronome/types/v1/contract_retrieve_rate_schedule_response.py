# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ContractRetrieveRateScheduleResponse",
    "Data",
    "DataListRate",
    "DataListRateCreditType",
    "DataListRateTier",
    "DataCommitRate",
    "DataCommitRateTier",
    "DataOverrideRate",
    "DataOverrideRateCreditType",
    "DataOverrideRateTier",
]


class DataListRateCreditType(BaseModel):
    id: str

    name: str


class DataListRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataListRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]

    credit_type: Optional[DataListRateCreditType] = None

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

    tiers: Optional[List[DataListRateTier]] = None
    """Only set for TIERED rate_type."""

    use_list_prices: Optional[bool] = None
    """Only set for PERCENTAGE rate_type.

    Defaults to false. If true, rate is computed using list prices rather than the
    standard rates for this product on the contract.
    """


class DataCommitRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataCommitRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    price: Optional[float] = None
    """Commit rate price. For FLAT rate_type, this must be >=0."""

    tiers: Optional[List[DataCommitRateTier]] = None
    """Only set for TIERED rate_type."""


class DataOverrideRateCreditType(BaseModel):
    id: str

    name: str


class DataOverrideRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataOverrideRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]

    credit_type: Optional[DataOverrideRateCreditType] = None

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

    tiers: Optional[List[DataOverrideRateTier]] = None
    """Only set for TIERED rate_type."""

    use_list_prices: Optional[bool] = None
    """Only set for PERCENTAGE rate_type.

    Defaults to false. If true, rate is computed using list prices rather than the
    standard rates for this product on the contract.
    """


class Data(BaseModel):
    entitled: bool

    list_rate: DataListRate

    product_custom_fields: Dict[str, str]

    product_id: str

    product_name: str

    product_tags: List[str]

    rate_card_id: str

    starting_at: datetime

    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_rate: Optional[DataCommitRate] = None
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or
    commit.
    """

    ending_before: Optional[datetime] = None

    override_rate: Optional[DataOverrideRate] = None

    pricing_group_values: Optional[Dict[str, str]] = None


class ContractRetrieveRateScheduleResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
