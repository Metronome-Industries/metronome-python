# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PlanListPriceAdjustmentsParams"]


class PlanListPriceAdjustmentsParams(TypedDict, total=False):
    customer_id: Required[str]

    customer_plan_id: Required[str]

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""
