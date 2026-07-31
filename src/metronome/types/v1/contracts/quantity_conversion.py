# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["QuantityConversion"]


class QuantityConversion(BaseModel):
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be converted using the provided conversion factor and operation. For example, if the operation is "multiply" and the conversion factor is 100, then the quantity will be multiplied by 100. This can be used in cases where data is sent in one unit and priced in another.  For example, data could be sent in MB and priced in GB. In this case, the conversion factor would be 1024 and the operation would be "divide".
    """

    conversion_factor: float
    """The factor to multiply or divide the quantity by."""

    operation: Literal["MULTIPLY", "DIVIDE"]
    """The operation to perform on the quantity"""

    name: Optional[str] = None
    """Optional name for this conversion."""
