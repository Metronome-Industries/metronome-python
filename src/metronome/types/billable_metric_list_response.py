# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["BillableMetricListResponse"]


class BillableMetricListResponse(BaseModel):
    id: str

    name: str

    group_by: Optional[List[str]] = None
