# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional, List

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PlanListPriceAdjustmentsResponse", "Price"]

class Price(BaseModel):
    adjustment_type: Literal["fixed", "quantity", "percentage", "override"]
    """Determines how the value will be applied."""

    tier: Optional[float] = None
    """Used in pricing tiers. Indicates at what metric value the price applies."""

    value: Optional[float] = None

class PlanListPriceAdjustmentsResponse(BaseModel):
    charge_id: str

    charge_type: Literal["usage", "fixed", "composite", "minimum", "seat"]

    prices: List[Price]

    start_period: float

    quantity: Optional[float] = None