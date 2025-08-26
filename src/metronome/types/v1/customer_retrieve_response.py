# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .customer_detail import CustomerDetail

__all__ = ["CustomerRetrieveResponse"]


class CustomerRetrieveResponse(BaseModel):
    data: CustomerDetail
