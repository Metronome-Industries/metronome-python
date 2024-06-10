# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.credit_type import CreditType

__all__ = ["PlanListChargesResponse", "Data", "DataPrice", "DataUnitConversion"]


class DataPrice(BaseModel):
    tier: float
    """Used in pricing tiers. Indicates at what metric value the price applies."""

    value: float

    collection_interval: Optional[float] = None

    collection_schedule: Optional[str] = None

    quantity: Optional[float] = None


class DataUnitConversion(BaseModel):
    division_factor: float
    """The conversion factor"""

    rounding_behavior: Optional[Literal["floor", "ceiling"]] = None
    """Whether usage should be rounded down or up to the nearest whole number.

    If null, quantity will be rounded to 20 decimal places.
    """


class Data(BaseModel):
    id: str

    charge_type: Literal["usage", "fixed", "composite", "minimum", "seat"]

    credit_type: CreditType

    custom_fields: Dict[str, str]

    name: str

    prices: List[DataPrice]

    product_id: str

    product_name: str

    quantity: Optional[float] = None

    start_period: Optional[float] = None
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    unit_conversion: Optional[DataUnitConversion] = None
    """Specifies how quantities for usage based charges will be converted."""


class PlanListChargesResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
