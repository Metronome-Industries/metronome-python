# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InvoiceVoidResponse", "Data"]


class Data(BaseModel):
    id: str


class InvoiceVoidResponse(BaseModel):
    data: Optional[Data] = None
