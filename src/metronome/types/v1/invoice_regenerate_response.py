# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

__all__ = ["InvoiceRegenerateResponse", "Data"]

class Data(BaseModel):
    id: str
    """The new invoice id"""

class InvoiceRegenerateResponse(BaseModel):
    data: Optional[Data] = None