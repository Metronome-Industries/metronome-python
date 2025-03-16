# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["PlanListParams"]

class PlanListParams(TypedDict, total=False):
    customer_id: Required[str]

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""