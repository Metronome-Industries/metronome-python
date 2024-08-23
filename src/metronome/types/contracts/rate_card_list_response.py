# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.tier import Tier
from ..shared.credit_type import CreditType

__all__ = [
    "RateCardListResponse",
    "RateCardEntries",
    "RateCardEntriesCurrent",
    "RateCardEntriesUpdate",
    "Alias",
    "CreditTypeConversion",
]


class RateCardEntriesCurrent(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    credit_type: Optional[CreditType] = None

    custom_rate: Optional[Dict[str, object]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    price: Optional[float] = None

    product_id: Optional[str] = None

    rate_type: Optional[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]] = None

    starting_at: Optional[datetime] = None

    tiers: Optional[List[Tier]] = None


class RateCardEntriesUpdate(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    entitled: bool

    product_id: str

    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "CUSTOM", "TIERED"]

    starting_at: datetime

    credit_type: Optional[CreditType] = None

    custom_rate: Optional[Dict[str, object]] = None

    ending_before: Optional[datetime] = None

    is_prorated: Optional[bool] = None

    price: Optional[float] = None

    quantity: Optional[float] = None

    tiers: Optional[List[Tier]] = None


class RateCardEntries(BaseModel):
    current: Optional[RateCardEntriesCurrent] = None

    updates: Optional[List[RateCardEntriesUpdate]] = None


class Alias(BaseModel):
    name: str

    ending_before: Optional[datetime] = None

    starting_at: Optional[datetime] = None


class CreditTypeConversion(BaseModel):
    custom_credit_type: CreditType

    fiat_per_custom_credit: str


class RateCardListResponse(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    name: str

    rate_card_entries: Dict[str, RateCardEntries]

    aliases: Optional[List[Alias]] = None

    credit_type_conversions: Optional[List[CreditTypeConversion]] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    fiat_credit_type: Optional[CreditType] = None
