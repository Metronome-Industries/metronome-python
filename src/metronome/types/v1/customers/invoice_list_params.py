# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InvoiceListParams"]


class InvoiceListParams(TypedDict, total=False):
    customer_id: Required[str]

    credit_type_id: str
    """Only return invoices for the specified credit type"""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp (exclusive).

    Invoices will only be returned for billing periods that end before this time.
    """

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    skip_zero_qty_line_items: bool
    """If set, all zero quantity line items will be filtered out of the response"""

    sort: Literal["date_asc", "date_desc"]
    """Invoice sort order by issued_at, e.g.

    date_asc or date_desc. Defaults to date_asc.
    """

    starting_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp (inclusive).

    Invoices will only be returned for billing periods that start at or after this
    time.
    """

    status: str
    """Invoice status, e.g. DRAFT, FINALIZED, or VOID"""
