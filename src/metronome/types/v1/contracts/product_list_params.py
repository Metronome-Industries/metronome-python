# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ProductListParams"]


class ProductListParams(TypedDict, total=False):
    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"]
    """Filter options for the product list. If not provided, defaults to not archived."""
