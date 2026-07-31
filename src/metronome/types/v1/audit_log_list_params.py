# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AuditLogListParams"]


class AuditLogListParams(TypedDict, total=False):
    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp (exclusive). Cannot be used with 'next_page'."""

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    resource_id: str
    """Optional parameter that can be used to filter which audit logs are returned.

    If you specify resource_id, you must also specify resource_type.
    """

    resource_type: str
    """Optional parameter that can be used to filter which audit logs are returned.

    If you specify resource_type, you must also specify resource_id.
    """

    sort: Literal["date_asc", "date_desc"]
    """Sort order by timestamp, e.g. date_asc or date_desc. Defaults to date_asc."""

    starting_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp of the earliest audit log to return.

    Cannot be used with 'next_page'.
    """
