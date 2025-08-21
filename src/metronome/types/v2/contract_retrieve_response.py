# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..shared.contract_v2 import ContractV2

__all__ = ["ContractRetrieveResponse"]


class ContractRetrieveResponse(BaseModel):
    data: ContractV2
