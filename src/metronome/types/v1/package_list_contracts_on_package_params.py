# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["PackageListContractsOnPackageParams"]


class PackageListContractsOnPackageParams(TypedDict, total=False):
    package_id: Required[str]

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    covering_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional RFC 3339 timestamp.

    Only include contracts active on the provided date. This cannot be provided if
    starting_at filter is provided.
    """

    include_archived: bool
    """Default false. Determines whether to include archived contracts in the results"""

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional RFC 3339 timestamp.

    Only include contracts that started on or after this date. This cannot be
    provided if covering_date filter is provided.
    """
