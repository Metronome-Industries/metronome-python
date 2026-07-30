# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Dict, List

__all__ = ["CommitSpecifier"]

class CommitSpecifier(BaseModel):
    presentation_group_values: Optional[Dict[str, str]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None
    """
    If provided, the specifier will only apply to the product with the specified ID.
    """

    product_tags: Optional[List[str]] = None
    """
    If provided, the specifier will only apply to products with all the specified
    tags.
    """