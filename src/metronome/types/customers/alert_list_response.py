# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from .customer_alert import CustomerAlert

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AlertListResponse"]

class AlertListResponse(BaseModel):
    data: List[CustomerAlert]

    next_page: Optional[str] = None