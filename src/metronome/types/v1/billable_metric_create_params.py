# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillableMetricCreateParams", "EventTypeFilter", "PropertyFilter"]


class BillableMetricCreateParams(TypedDict, total=False):
    name: Required[str]
    """The display name of the billable metric."""

    aggregation_key: str
    """Specifies the type of aggregation performed on matching events.

    Required if `sql` is not provided.
    """

    aggregation_type: Literal["COUNT", "LATEST", "MAX", "SUM", "UNIQUE"]
    """Specifies the type of aggregation performed on matching events."""

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

    sql: str
    """The SQL query associated with the billable metric.

    This field is mutually exclusive with aggregation_type, event_type_filter,
    property_filters, aggregation_key, and group_keys. If provided, these other
    fields must be omitted.
    """


class EventTypeFilter(TypedDict, total=False):
    in_values: List[str]
    """A list of event types that are explicitly included in the billable metric.

    If specified, only events of these types will match the billable metric. Must be
    non-empty if present.
    """

    not_in_values: List[str]
    """A list of event types that are explicitly excluded from the billable metric.

    If specified, events of these types will not match the billable metric. Must be
    non-empty if present.
    """


class PropertyFilter(TypedDict, total=False):
    name: Required[str]
    """The name of the event property."""

    exists: bool
    """Determines whether the property must exist in the event.

    If true, only events with this property will pass the filter. If false, only
    events without this property will pass the filter. If null or omitted, the
    existence of the property is optional.
    """

    in_values: List[str]
    """Specifies the allowed values for the property to match an event.

    An event will pass the filter only if its property value is included in this
    list. If undefined, all property values will pass the filter. Must be non-empty
    if present.
    """

    not_in_values: List[str]
    """Specifies the values that prevent an event from matching the filter.

    An event will not pass the filter if its property value is included in this
    list. If null or empty, all property values will pass the filter. Must be
    non-empty if present.
    """
