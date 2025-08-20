# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .invoice import Invoice
from ...._models import BaseModel

__all__ = ["InvoiceRetrieveResponse"]


class InvoiceRetrieveResponse(BaseModel):
    data: Invoice
