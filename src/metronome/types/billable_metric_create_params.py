# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .shared_params.property_filter import PropertyFilter
from .shared_params.event_type_filter import EventTypeFilter

__all__ = ["BillableMetricCreateParams"]


class BillableMetricCreateParams(TypedDict, total=False):
    aggregation_type: Required[Literal["COUNT", "LATEST", "MAX", "SUM", "UNIQUE"]]
    """Specifies the type of aggregation performed on matching events."""

    name: Required[str]
    """The display name of the billable metric."""

    aggregation_key: str
    """A key that specifies which property of the event is used to aggregate data.

    This key must be one of the property filter names and is not applicable when the
    aggregation type is 'count'.
    """

    custom_fields: Dict[str, str]
    """Custom fields to attach to the billable metric."""

    event_type_filter: EventTypeFilter
    """An optional filtering rule to match the 'event_type' property of an event."""

    group_keys: Iterable[List[str]]
    """Property names that are used to group usage costs on an invoice.

    Each entry represents a set of properties used to slice events into distinct
    buckets.
    """

    property_filters: Iterable[PropertyFilter]
    """A list of filters to match events to this billable metric.

    Each filter defines a rule on an event property. All rules must pass for the
    event to match the billable metric.
    """
