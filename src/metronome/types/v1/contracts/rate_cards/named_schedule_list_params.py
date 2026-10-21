# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["NamedScheduleListParams"]


class NamedScheduleListParams(TypedDict, total=False):
    customer_id: Required[str]
    """ID of the customer to list contract named schedules for"""

    contract_id: str
    """Optional ID of a contract to scope the results to a single contract"""

    covering_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, result contains at most one segment covering this date for each
    schedule.
    """

    limit: int
    """Maximum number of named schedules to return."""

    next_page: str
    """Cursor for pagination. Use the value from a previous response's next_page."""

    properties: Dict[str, str]
    """Optional key-value filters.

    A schedule matches when it contains at least this subset of properties.
    """

    schedule_name: str
    """Optional filter to scope the results to a single schedule name"""
