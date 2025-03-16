# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .customer_detail import CustomerDetail

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CustomerRetrieveResponse"]

class CustomerRetrieveResponse(BaseModel):
    data: CustomerDetail