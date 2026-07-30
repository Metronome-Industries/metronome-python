# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["Tier"]

class Tier(BaseModel):
    price: float

    size: Optional[float] = None