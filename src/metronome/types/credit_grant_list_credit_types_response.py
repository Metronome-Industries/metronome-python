# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CreditGrantListCreditTypesResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None

    is_currency: Optional[bool] = None

    name: Optional[str] = None


class CreditGrantListCreditTypesResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
