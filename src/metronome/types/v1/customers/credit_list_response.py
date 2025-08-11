# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.credit import Credit

__all__ = ["CreditListResponse"]


class CreditListResponse(BaseModel):
    data: List[Credit]

    next_page: Optional[str] = None
