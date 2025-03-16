# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, List, Optional

from .shared.commit import Commit

from .shared.credit import Credit

from typing_extensions import TypeAliasType, TypeAlias

from .._models import BaseModel

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ContractListBalancesResponse", "Data"]

Data: TypeAlias = Union[Commit, Credit]

class ContractListBalancesResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None