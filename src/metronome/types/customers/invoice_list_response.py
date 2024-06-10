# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .invoice import Invoice
from ..._models import BaseModel

__all__ = ["InvoiceListResponse"]


class InvoiceListResponse(BaseModel):
    data: List[Invoice]

    next_page: Optional[str] = None
