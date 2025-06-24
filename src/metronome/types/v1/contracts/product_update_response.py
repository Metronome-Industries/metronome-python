# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["ProductUpdateResponse", "Data"]


class Data(BaseModel):
    id: str


class ProductUpdateResponse(BaseModel):
    data: Data
