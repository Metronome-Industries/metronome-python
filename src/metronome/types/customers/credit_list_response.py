# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from ..shared.credit import Credit

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["CreditListResponse"]

class CreditListResponse(BaseModel):
    data: List[Credit]

    next_page: Optional[str] = None