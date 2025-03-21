# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PricingUnitListResponse"]


class PricingUnitListResponse(BaseModel):
    id: Optional[str] = None

    is_currency: Optional[bool] = None

    name: Optional[str] = None
