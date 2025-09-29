# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["OffsetListParams"]


class OffsetListParams(TypedDict, total=False):
    cursor: str

    limit: float
