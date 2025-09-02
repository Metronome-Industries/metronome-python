# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["RateListParams", "Selector"]


class RateListParams(TypedDict, total=False):
    at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """inclusive starting point for the rates schedule"""

    rate_card_id: Required[str]
    """ID of the rate card to get the schedule for"""

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    selectors: Iterable[Selector]
    """
    List of rate selectors, rates matching ANY of the selector will be included in
    the response Passing no selectors will result in all rates being returned.
    """


class Selector(TypedDict, total=False):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]
    """
    Subscription rates matching the billing frequency will be included in the
    response.
    """

    partial_pricing_group_values: Dict[str, str]
    """
    List of pricing group key value pairs, rates containing the matching key / value
    pairs will be included in the response.
    """

    pricing_group_values: Dict[str, str]
    """
    List of pricing group key value pairs, rates matching all of the key / value
    pairs will be included in the response.
    """

    product_id: str
    """Rates matching the product id will be included in the response."""

    product_tags: SequenceNotStr[str]
    """
    List of product tags, rates matching any of the tags will be included in the
    response.
    """
