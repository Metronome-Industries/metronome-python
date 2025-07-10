# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageSearchParams"]


class UsageSearchParams(TypedDict, total=False):
    transaction_ids: Required[Annotated[List[str], PropertyInfo(alias="transactionIds")]]
    """The transaction IDs of the events to retrieve"""
