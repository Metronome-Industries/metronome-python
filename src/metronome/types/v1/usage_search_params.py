# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UsageSearchParams"]


class UsageSearchParams(TypedDict, total=False):
    transaction_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="transactionIds")]]
    """The transaction IDs of the events to retrieve"""
