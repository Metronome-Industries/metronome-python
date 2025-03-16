# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .customer import Customer

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CustomerCreateResponse"]

class CustomerCreateResponse(BaseModel):
    data: Customer