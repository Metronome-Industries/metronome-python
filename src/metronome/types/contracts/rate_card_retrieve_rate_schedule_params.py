# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RateCardRetrieveRateScheduleParams", "Selector"]


class RateCardRetrieveRateScheduleParams(TypedDict, total=False):
    rate_card_id: Required[str]
    """ID of the rate card to get the schedule for"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """inclusive starting point for the rates schedule"""

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """optional exclusive end date for the rates schedule.

    When not specified rates will show all future schedule segments.
    """

    selectors: Iterable[Selector]
    """
    List of rate selectors, rates matching ANY of the selector will be included in
    the response Passing no selectors will result in all rates being returned.
    """


class Selector(TypedDict, total=False):
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
