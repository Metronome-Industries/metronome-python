# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from ..shared.commit import Commit

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CommitListResponse"]

class CommitListResponse(BaseModel):
    data: List[Commit]

    next_page: Optional[str] = None