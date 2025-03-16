# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from typing import Optional

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["QuantityConversion"]

class QuantityConversion(BaseModel):
    conversion_factor: float
    """The factor to multiply or divide the quantity by."""

    operation: Literal["MULTIPLY", "DIVIDE"]
    """The operation to perform on the quantity"""

    name: Optional[str] = None
    """Optional name for this conversion."""