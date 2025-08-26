# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CreditUpdateEndDateResponse", "Data"]


class Data(BaseModel):
    id: str


class CreditUpdateEndDateResponse(BaseModel):
    data: Data
