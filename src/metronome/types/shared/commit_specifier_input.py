# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = ["CommitSpecifierInput"]


class CommitSpecifierInput(BaseModel):
    presentation_group_values: Optional[Dict[str, str]] = None
    """
    If provided, the specifier will apply to product usage with these set of
    presentation group values.
    """

    pricing_group_values: Optional[Dict[str, str]] = None
    """
    If provided, the specifier will apply to product usage with these set of pricing
    group values.
    """

    product_id: Optional[str] = None
    """
    If provided, the specifier will only apply to the product with the specified ID.
    """

    product_tags: Optional[List[str]] = None
    """
    If provided, the specifier will only apply to products with all the specified
    tags.
    """
