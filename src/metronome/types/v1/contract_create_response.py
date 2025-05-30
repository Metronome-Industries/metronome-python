# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContractCreateResponse", "Data"]


class Data(BaseModel):
    id: str


class ContractCreateResponse(BaseModel):
    data: Data
