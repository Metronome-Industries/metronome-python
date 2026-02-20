# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["UsageListWithGroupsParams", "GroupBy"]


class UsageListWithGroupsParams(TypedDict, total=False):
    billable_metric_id: Required[str]

    customer_id: Required[str]

    window_size: Required[Literal["HOUR", "DAY", "NONE"]]
    """
    A window_size of "day" or "hour" will return the usage for the specified period
    segmented into daily or hourly aggregates. A window_size of "none" will return a
    single usage aggregate for the entirety of the specified period.
    """

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    current_period: bool
    """If true, will return the usage for the current billing period.

    Will return an error if the customer is currently uncontracted or starting_on
    and ending_before are specified when this is true.
    """

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    group_by: GroupBy
    """Use group_key and group_filters instead.

    Use a single group key to group by. Compound group keys are not supported.
    """

    group_filters: Dict[str, SequenceNotStr[str]]
    """Object mapping group keys to arrays of values to filter on.

    Only usage matching these filter values will be returned. Keys must be present
    in group_key. Omit a key or use an empty array to include all values for that
    dimension.
    """

    group_key: SequenceNotStr[str]
    """Group key to group usage by.

    Supports both simple (single key) and compound (multiple keys) group keys.

    For simple group keys, provide a single key e.g. `["region"]`. For compound
    group keys, provide multiple keys e.g. `["region", "team"]`.

    For streaming metrics, the keys must be defined as a simple or compound group
    key on the billable metric. For compound group keys, all keys must match an
    exact compound group key definition — partial matches are not allowed.

    Cannot be used together with `group_by`.
    """

    starting_on: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class GroupBy(TypedDict, total=False):
    """Use group_key and group_filters instead.

    Use a single group key to group by. Compound group keys are not supported.
    """

    key: Required[str]
    """The name of the group_by key to use"""

    values: SequenceNotStr[str]
    """Values of the group_by key to return in the query.

    Omit this if you'd like all values for the key returned.
    """
