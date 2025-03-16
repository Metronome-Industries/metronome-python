# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["QuantityRounding"]

class QuantityRounding(BaseModel):
    decimal_places: float

    rounding_method: Literal["ROUND_UP", "ROUND_DOWN", "ROUND_HALF_UP"]