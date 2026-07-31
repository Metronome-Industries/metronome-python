# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CreditGrantListEntriesParams"]


class CreditGrantListEntriesParams(TypedDict, total=False):
    next_page: str
    """Cursor that indicates where the next page of results should start."""

    sort: Literal["asc", "desc"]
    """Ledgers sort order by date, asc or desc. Defaults to asc."""

    credit_type_ids: SequenceNotStr[str]
    """A list of Metronome credit type IDs to fetch ledger entries for.

    If absent, ledger entries for all credit types will be returned.
    """

    customer_ids: SequenceNotStr[str]
    """A list of Metronome customer IDs to fetch ledger entries for.

    If absent, ledger entries for all customers will be returned.
    """

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If supplied, ledger entries will only be returned with an effective_at before
    this time. This timestamp must not be in the future. If no timestamp is
    supplied, all entries up to the start of the customer's next billing period will
    be returned.
    """

    starting_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If supplied, only ledger entries effective at or after this time will be
    returned.
    """
