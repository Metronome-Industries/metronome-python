# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..shared.commit import Commit
from ..shared.credit import Credit

__all__ = ["ContractListBalancesResponse", "Data"]

Data: TypeAlias = Union[Commit, Credit]


class ContractListBalancesResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
