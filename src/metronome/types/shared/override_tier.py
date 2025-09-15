# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OverrideTier"]


class OverrideTier(BaseModel):
    multiplier: float

    size: Optional[float] = None
