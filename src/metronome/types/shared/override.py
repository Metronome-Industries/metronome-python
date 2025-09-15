# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .tier import Tier
from ..._models import BaseModel
from .override_tier import OverrideTier
from .overwrite_rate import OverwriteRate
from .credit_type_data import CreditTypeData

__all__ = ["Override", "OverrideSpecifier", "Product"]


class OverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None

    recurring_credit_ids: Optional[List[str]] = None


class Product(BaseModel):
    id: str

    name: str


class Override(BaseModel):
    id: str

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    credit_type: Optional[CreditTypeData] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[OverrideSpecifier]] = None

    override_tiers: Optional[List[OverrideTier]] = None

    overwrite_rate: Optional[OverwriteRate] = None

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    priority: Optional[float] = None

    product: Optional[Product] = None

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    rate_type: Optional[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    tiers: Optional[List[Tier]] = None
    """Only set for TIERED rate_type."""

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None

    value: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """
