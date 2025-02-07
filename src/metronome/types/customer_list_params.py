# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["CustomerListParams"]


class CustomerListParams(TypedDict, total=False):
    customer_ids: List[str]
    """Filter the customer list by customer_id. Up to 100 ids can be provided."""

    ingest_alias: str
    """Filter the customer list by ingest_alias"""

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    only_archived: bool
    """Filter the customer list to only return archived customers.

    By default, only active customers are returned.
    """

    salesforce_account_ids: List[str]
    """Filter the customer list by salesforce_account_id.

    Up to 100 ids can be provided.
    """
