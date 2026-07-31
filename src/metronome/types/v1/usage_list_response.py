# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UsageListResponse"]


class UsageListResponse(BaseModel):
    billable_metric_id: str

    billable_metric_name: str

    customer_id: str

    end_timestamp: datetime

    start_timestamp: datetime

    value: Optional[float] = None

    groups: Optional[Dict[str, Optional[float]]] = None
    """Values will be either a number or null.

    Null indicates that there were no matches for the group_by value.
    """
