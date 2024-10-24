# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .customer import Customer

__all__ = ["CustomerSetNameResponse"]


class CustomerSetNameResponse(BaseModel):
    data: Customer
