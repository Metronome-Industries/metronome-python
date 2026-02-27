# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PackageListParams"]


class PackageListParams(TypedDict, total=False):
    limit: int
    """The maximum number of packages to return. Defaults to 10."""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"]
    """Filter packages by archived status. Defaults to NOT_ARCHIVED."""
