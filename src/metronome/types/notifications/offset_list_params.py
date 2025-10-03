# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["OffsetListParams"]


class OffsetListParams(TypedDict, total=False):
    archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"]
    """Filter options for the notification configurations.

    If not provided, defaults to NOT_ARCHIVED.
    """

    cursor: str

    limit: float
