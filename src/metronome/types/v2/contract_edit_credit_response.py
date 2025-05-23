# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContractEditCreditResponse", "Data"]


class Data(BaseModel):
    id: str


class ContractEditCreditResponse(BaseModel):
    data: Data
