# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContractGetSubscriptionSeatsScheduleHistoryParams"]


class ContractGetSubscriptionSeatsScheduleHistoryParams(TypedDict, total=False):
    contract_id: Required[str]

    customer_id: Required[str]

    subscription_id: Required[str]

    covering_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Get the seats history segment for the covering date.

    Cannot be used with `starting_at` or `ending_before`.
    """

    cursor: Optional[str]
    """Cursor for pagination.

    Use the value from the `next_page` field of the previous response to retrieve
    the next page of results.
    """

    ending_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include seats history segments that are active at or before this timestamp.

    Use with `starting_at` to get a specific time range. If not set, there's no
    upper bound.
    """

    limit: Optional[int]
    """Maximum number of seat schedule entries to return. Defaults to 10."""

    starting_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Include seats history segments that are active at or after this timestamp.

    Use with `ending_before` to get a specific time range. If not set, there's no
    lower bound.
    """
