# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreditListParams"]


class CreditListParams(TypedDict, total=False):
    customer_id: Required[str]

    covering_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return only credits that have access schedules that "cover" the provided date"""

    credit_id: str

    effective_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Include only credits that have any access before the provided date (exclusive)"""

    include_archived: bool
    """Include credits from archived contracts."""

    include_balance: bool
    """Include the balance in the response.

    Setting this flag may cause the query to be slower.
    """

    include_contract_credits: bool
    """Include credits on the contract level."""

    include_ledgers: bool
    """Include credit ledgers in the response.

    Setting this flag may cause the query to be slower.
    """

    next_page: str
    """The next page token from a previous response."""

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Include only credits that have any access on or after the provided date"""
