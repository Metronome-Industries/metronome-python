# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PlanListChargesResponse", "CreditType", "Price", "UnitConversion"]


class CreditType(BaseModel):
    id: str

    name: str


class Price(BaseModel):
    tier: float
    """Used in pricing tiers. Indicates at what metric value the price applies."""

    value: float

    collection_interval: Optional[float] = None

    collection_schedule: Optional[str] = None

    quantity: Optional[float] = None


class UnitConversion(BaseModel):
    division_factor: float
    """The conversion factor"""

    rounding_behavior: Optional[Literal["floor", "ceiling"]] = None
    """Whether usage should be rounded down or up to the nearest whole number.

    If null, quantity will be rounded to 20 decimal places.
    """


class PlanListChargesResponse(BaseModel):
    id: str

    charge_type: Literal["usage", "fixed", "composite", "minimum", "seat"]

    credit_type: CreditType

    custom_fields: Dict[str, str]

    name: str

    prices: List[Price]

    product_id: str

    product_name: str

    quantity: Optional[float] = None

    start_period: Optional[float] = None
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    tier_reset_frequency: Optional[float] = None
    """Used in pricing tiers.

    Indicates how often the tier resets. Default is 1 - the tier count resets every
    billing period.
    """

    unit_conversion: Optional[UnitConversion] = None
    """Specifies how quantities for usage based charges will be converted."""
