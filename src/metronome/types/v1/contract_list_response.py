# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from ..shared.contract import Contract

__all__ = ["ContractListResponse"]

class ContractListResponse(BaseModel):
    data: List[Contract]