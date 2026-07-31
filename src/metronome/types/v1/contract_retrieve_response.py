# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..shared.contract import Contract

__all__ = ["ContractRetrieveResponse"]


class ContractRetrieveResponse(BaseModel):
    data: Contract
