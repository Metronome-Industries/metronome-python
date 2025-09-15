# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.contract import Contract

__all__ = ["ContractListResponse"]


class ContractListResponse(BaseModel):
    data: List[Contract]
