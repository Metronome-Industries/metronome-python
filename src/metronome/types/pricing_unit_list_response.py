# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PricingUnitListResponse"]

class PricingUnitListResponse(BaseModel):
    id: Optional[str] = None

    is_currency: Optional[bool] = None

    name: Optional[str] = None