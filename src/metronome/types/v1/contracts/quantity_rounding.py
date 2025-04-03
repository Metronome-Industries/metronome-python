# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["QuantityRounding"]


class QuantityRounding(BaseModel):
    decimal_places: float

    rounding_method: Literal["ROUND_UP", "ROUND_DOWN", "ROUND_HALF_UP"]
