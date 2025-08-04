# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .customer import Customer
from ..._models import BaseModel

__all__ = ["CustomerCreateResponse"]


class CustomerCreateResponse(BaseModel):
    data: Customer
