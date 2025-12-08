# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["QuantityRounding"]


class QuantityRounding(BaseModel):
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be rounded using the provided rounding method and decimal places. For example, if the method is "round up" and the decimal places is 0, then the quantity will be rounded up to the nearest integer.
    """

    decimal_places: float

    rounding_method: Literal["ROUND_UP", "ROUND_DOWN", "ROUND_HALF_UP"]
