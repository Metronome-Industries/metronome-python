# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.commit import Commit

__all__ = ["CommitListResponse"]


class CommitListResponse(BaseModel):
    data: List[Commit]

    next_page: Optional[str] = None
