# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["CommitListParams"]

class CommitListParams(TypedDict, total=False):
    customer_id: Required[str]

    commit_id: str

    covering_date: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Include only commits that have access schedules that "cover" the provided date"""

    effective_before: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Include only commits that have any access before the provided date (exclusive)"""

    include_archived: bool
    """Include commits from archived contracts."""

    include_balance: bool
    """Include the balance in the response.

    Setting this flag may cause the query to be slower.
    """

    include_contract_commits: bool
    """Include commits on the contract level."""

    include_ledgers: bool
    """Include commit ledgers in the response.

    Setting this flag may cause the query to be slower.
    """

    next_page: str
    """The next page token from a previous response."""

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """Include only commits that have any access on or after the provided date"""