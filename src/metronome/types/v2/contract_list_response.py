# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.contract_v2 import ContractV2

__all__ = ["ContractListResponse"]


class ContractListResponse(BaseModel):
    data: List[ContractV2]
