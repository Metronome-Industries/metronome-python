# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BillableMetricListParams"]


class BillableMetricListParams(TypedDict, total=False):
    include_archived: bool
    """If true, the list of returned metrics will include archived metrics"""

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""
