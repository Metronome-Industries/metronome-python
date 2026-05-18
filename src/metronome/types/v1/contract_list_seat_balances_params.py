# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ContractListSeatBalancesParams"]


class ContractListSeatBalancesParams(TypedDict, total=False):
    contract_id: Required[str]
    """The contract ID to retrieve seat balances for"""

    customer_id: Required[str]
    """The customer ID to retrieve seat balances for"""

    covering_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Include only commits or credits with access that cover this specific date
    (cannot be used with starting_at or ending_before).
    """

    cursor: str
    """Page token from a previous response to retrieve the next page"""

    effective_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Include only commits or credits with access effective on or before this date
    (cannot be used with covering_date).
    """

    include_credits_and_commits: bool
    """Include credits and commits in the response"""

    include_ledgers: bool
    """Include ledger entries for each commit and commit.

    `include_credits_and_commits` must be set to `true` for `include_ledgers=true`
    to apply.
    """

    limit: int
    """Maximum number of seats to return.

    Range: 1-100. Default: 25. When `include_credits_and_commits = true`, if the
    total commits/credits across all seats exceeds 100, a limit of 100 applies to
    the total credits and commits. Seats are included greedily to maximize the
    number of seats returned. Example: if seat 1 has 98 commits and seat 2 has 10
    commits, both seats will be returned (total: 108 commits). Each returned seat
    includes all of its associated credits and commits.
    """

    seat_ids: SequenceNotStr[str]
    """Optional filter to only include specific seats."""

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    Include only commits or credits with access effective on or after this date
    (cannot be used with covering_date).
    """

    subscription_ids: SequenceNotStr[str]
    """Optional filter to only include seats from specific subscriptions.

    If subscriptions ids are not mapped to SEAT_BASED subscriptions, error will be
    returned.
    """
