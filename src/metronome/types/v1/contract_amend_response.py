# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContractAmendResponse", "Data"]


class Data(BaseModel):
    id: str


class ContractAmendResponse(BaseModel):
    data: Data
