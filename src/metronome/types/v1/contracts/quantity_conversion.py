# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["QuantityConversion"]


class QuantityConversion(BaseModel):
    conversion_factor: float
    """The factor to multiply or divide the quantity by."""

    operation: Literal["MULTIPLY", "DIVIDE"]
    """The operation to perform on the quantity"""

    name: Optional[str] = None
    """Optional name for this conversion."""
