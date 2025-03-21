# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InvoiceListBreakdownsParams"]


class InvoiceListBreakdownsParams(TypedDict, total=False):
    customer_id: Required[str]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp.

    Breakdowns will only be returned for time windows that end on or before this
    time.
    """

    starting_on: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp.

    Breakdowns will only be returned for time windows that start on or after this
    time.
    """

    credit_type_id: str
    """Only return invoices for the specified credit type"""

    limit: int
    """Max number of results that should be returned.

    For daily breakdowns, the response can return up to 35 days worth of breakdowns.
    For hourly breakdowns, the response can return up to 24 hours. If there are more
    results, a cursor to the next page is returned.
    """

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    skip_zero_qty_line_items: bool
    """If set, all zero quantity line items will be filtered out of the response"""

    sort: Literal["date_asc", "date_desc"]
    """Invoice sort order by issued_at, e.g.

    date_asc or date_desc. Defaults to date_asc.
    """

    status: str
    """Invoice status, e.g. DRAFT or FINALIZED"""

    window_size: Literal["HOUR", "DAY"]
    """The granularity of the breakdowns to return. Defaults to day."""
