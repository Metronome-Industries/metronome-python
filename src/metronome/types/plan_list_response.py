# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["PlanListResponse", "Data"]


class Data(BaseModel):
    id: str

    description: str

    name: str

    custom_fields: Optional[Dict[str, str]] = None


class PlanListResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
