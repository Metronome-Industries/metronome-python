# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from .invoice import Invoice

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["InvoiceRetrieveResponse"]

class InvoiceRetrieveResponse(BaseModel):
    data: Invoice