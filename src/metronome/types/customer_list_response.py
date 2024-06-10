# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .customer_detail import CustomerDetail

__all__ = ["CustomerListResponse"]


class CustomerListResponse(BaseModel):
    data: List[CustomerDetail]

    next_page: Optional[str] = None
