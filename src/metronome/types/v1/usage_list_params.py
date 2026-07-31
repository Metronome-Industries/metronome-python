# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UsageListParams", "BillableMetric", "BillableMetricGroupBy"]


class UsageListParams(TypedDict, total=False):
    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    starting_on: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    window_size: Required[Literal["HOUR", "DAY", "NONE"]]
    """
    A window_size of "day" or "hour" will return the usage for the specified period
    segmented into daily or hourly aggregates. A window_size of "none" will return a
    single usage aggregate for the entirety of the specified period.
    """

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    billable_metrics: Iterable[BillableMetric]
    """A list of billable metrics to fetch usage for.

    If absent, all billable metrics will be returned.
    """

    customer_ids: SequenceNotStr[str]
    """A list of Metronome customer IDs to fetch usage for.

    If absent, usage for all customers will be returned.
    """


class BillableMetricGroupBy(TypedDict, total=False):
    key: Required[str]
    """The name of the group_by key to use"""

    values: SequenceNotStr[str]
    """Values of the group_by key to return in the query.

    If this field is omitted, all available values will be returned, up to a maximum
    of 200.
    """


class BillableMetric(TypedDict, total=False):
    id: Required[str]

    group_by: BillableMetricGroupBy
