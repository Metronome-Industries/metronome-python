# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BillableMetricListParams"]


class BillableMetricListParams(TypedDict, total=False):
    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    on_current_plan: bool
    """
    If true, the list of metrics will be filtered to just ones that are on the
    customer's current plan
    """
