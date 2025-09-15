# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["CreditGrantListParams"]


class CreditGrantListParams(TypedDict, total=False):
    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    credit_grant_ids: SequenceNotStr[str]
    """An array of credit grant IDs.

    If this is specified, neither credit_type_ids nor customer_ids may be specified.
    """

    credit_type_ids: SequenceNotStr[str]
    """An array of credit type IDs.

    This must not be specified if credit_grant_ids is specified.
    """

    customer_ids: SequenceNotStr[str]
    """An array of Metronome customer IDs.

    This must not be specified if credit_grant_ids is specified.
    """

    effective_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return credit grants that are effective before this timestamp (exclusive)."""

    not_expiring_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only return credit grants that expire at or after this timestamp."""
