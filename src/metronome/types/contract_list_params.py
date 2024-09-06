# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContractListParams"]


class ContractListParams(TypedDict, total=False):
    customer_id: Required[str]

    covering_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional RFC 3339 timestamp.

    If provided, the response will include only contracts effective on the provided
    date. This cannot be provided if the starting_at filter is provided.
    """

    include_archived: bool
    """Include archived contracts in the response"""

    include_ledgers: bool
    """Include commit ledgers in the response.

    Setting this flag may cause the query to be slower.
    """

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional RFC 3339 timestamp.

    If provided, the response will include only contracts where effective_at is on
    or after the provided date. This cannot be provided if the covering_date filter
    is provided.
    """
