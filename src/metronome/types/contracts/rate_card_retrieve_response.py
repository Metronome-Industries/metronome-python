# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.tier import Tier
from ..shared.credit_type_data import CreditTypeData

__all__ = [
    "RateCardRetrieveResponse",
    "Data",
    "DataRateCardEntries",
    "DataRateCardEntriesCurrent",
    "DataRateCardEntriesUpdate",
    "DataRateCardEntriesUpdateCommitRate",
    "DataAlias",
    "DataCreditTypeConversion",
]


class DataRateCardEntriesCurrent(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    credit_type: Optional[CreditTypeData] = None

    custom_rate: Optional[Dict[str, object]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    price: Optional[float] = None

    product_id: Optional[str] = None

    rate_type: Optional[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]] = None

    starting_at: Optional[datetime] = None

    tiers: Optional[List[Tier]] = None


class DataRateCardEntriesUpdateCommitRate(BaseModel):
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


class DataRateCardEntriesUpdate(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    entitled: bool

    product_id: str

    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]

    starting_at: datetime

    commit_rate: Optional[DataRateCardEntriesUpdateCommitRate] = None
    """The rate that will be used to rate a product when it is paid for by a commit.

    This feature requires opt-in before it can be used. Please contact Metronome
    support to enable this feature.
    """

    credit_type: Optional[CreditTypeData] = None

    custom_rate: Optional[Dict[str, object]] = None

    ending_before: Optional[datetime] = None

    is_prorated: Optional[bool] = None

    price: Optional[float] = None

    quantity: Optional[float] = None

    tiers: Optional[List[Tier]] = None


class DataRateCardEntries(BaseModel):
    current: Optional[DataRateCardEntriesCurrent] = None

    updates: Optional[List[DataRateCardEntriesUpdate]] = None


class DataAlias(BaseModel):
    name: str

    ending_before: Optional[datetime] = None

    starting_at: Optional[datetime] = None


class DataCreditTypeConversion(BaseModel):
    custom_credit_type: CreditTypeData

    fiat_per_custom_credit: str


class Data(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    name: str

    rate_card_entries: Dict[str, DataRateCardEntries]

    aliases: Optional[List[DataAlias]] = None

    credit_type_conversions: Optional[List[DataCreditTypeConversion]] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    fiat_credit_type: Optional[CreditTypeData] = None


class RateCardRetrieveResponse(BaseModel):
    data: Data
