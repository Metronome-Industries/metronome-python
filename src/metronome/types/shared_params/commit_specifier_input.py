# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import TypedDict

__all__ = ["CommitSpecifierInput"]


class CommitSpecifierInput(TypedDict, total=False):
    presentation_group_values: Dict[str, str]

    pricing_group_values: Dict[str, str]

    product_id: str
    """
    If provided, the specifier will only apply to the product with the specified ID.
    """

    product_tags: List[str]
    """
    If provided, the specifier will only apply to products with all the specified
    tags.
    """
