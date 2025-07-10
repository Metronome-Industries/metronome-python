# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .customer_alert import CustomerAlert

__all__ = ["AlertListResponse"]


class AlertListResponse(BaseModel):
    data: List[CustomerAlert]

    next_page: Optional[str] = None
