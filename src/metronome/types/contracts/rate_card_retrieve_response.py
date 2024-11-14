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

    price: Optional[float] = None
    """Commit rate price. For FLAT rate_type, this must be >=0."""

    tiers: Optional[List[Tier]] = None
    """Only set for TIERED rate_type."""


class DataRateCardEntriesUpdate(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    entitled: bool

    product_id: str

    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]

    starting_at: datetime

    commit_rate: Optional[DataRateCardEntriesUpdateCommitRate] = None
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or
    commit. This feature requires opt-in before it can be used. Please contact
    Metronome support to enable this feature.
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
