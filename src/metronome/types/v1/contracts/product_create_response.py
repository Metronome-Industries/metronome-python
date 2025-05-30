# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ProductCreateResponse", "Data"]


class Data(BaseModel):
    id: str


class ProductCreateResponse(BaseModel):
    data: Data
