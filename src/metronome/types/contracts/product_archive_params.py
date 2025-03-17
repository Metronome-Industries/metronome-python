# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProductArchiveParams"]


class ProductArchiveParams(TypedDict, total=False):
    product_id: Required[str]
    """ID of the product to be archived"""
