# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Override", "OverrideSpecifier", "OverwriteRate", "OverwriteRateTier", "Product"]


class OverrideSpecifier(BaseModel):
    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None


class OverwriteRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class OverwriteRate(BaseModel):
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

    custom_rate: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    is_prorated: Optional[bool] = None
    """Default proration configuration. Only valid for SUBSCRIPTION rate_type."""

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Optional[List[OverwriteRateTier]] = None
    """Only set for TIERED rate_type."""


class Product(BaseModel):
    id: str

    name: str


class Override(BaseModel):
    id: str

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[OverrideSpecifier]] = None

    overwrite_rate: Optional[OverwriteRate] = None

    product: Optional[Product] = None

    type: Optional[Literal["OVERWRITE", "MULTIPLIER"]] = None
