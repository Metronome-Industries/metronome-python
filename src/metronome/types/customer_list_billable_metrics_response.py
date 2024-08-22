# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomerListBillableMetricsResponse", "EventTypeFilter", "PropertyFilter"]


class EventTypeFilter(BaseModel):
    in_values: Optional[List[str]] = None
    """A list of event types that are explicitly included in the billable metric.

    If specified, only events of these types will match the billable metric. Must be
    non-empty if present.
    """

    not_in_values: Optional[List[str]] = None
    """A list of event types that are explicitly excluded from the billable metric.

    If specified, events of these types will not match the billable metric. Must be
    non-empty if present.
    """


class PropertyFilter(BaseModel):
    name: str
    """The name of the event property."""

    exists: Optional[bool] = None
    """Determines whether the property must exist in the event.

    If true, only events with this property will pass the filter. If false, only
    events without this property will pass the filter. If null or omitted, the
    existence of the property is optional.
    """

    in_values: Optional[List[str]] = None
    """Specifies the allowed values for the property to match an event.

    An event will pass the filter only if its property value is included in this
    list. If undefined, all property values will pass the filter. Must be non-empty
    if present.
    """

    not_in_values: Optional[List[str]] = None
    """Specifies the values that prevent an event from matching the filter.

    An event will not pass the filter if its property value is included in this
    list. If null or empty, all property values will pass the filter. Must be
    non-empty if present.
    """


class CustomerListBillableMetricsResponse(BaseModel):
    id: str

    name: str

    aggregate: Optional[str] = None
    """(DEPRECATED) use aggregation_type instead"""

    aggregate_keys: Optional[List[str]] = None
    """(DEPRECATED) use aggregation_key instead"""

    aggregation_key: Optional[str] = None
    """A key that specifies which property of the event is used to aggregate data.

    This key must be one of the property filter names and is not applicable when the
    aggregation type is 'count'.
    """

    aggregation_type: Optional[Literal["COUNT", "LATEST", "MAX", "SUM", "UNIQUE"]] = None
    """Specifies the type of aggregation performed on matching events."""

    custom_fields: Optional[Dict[str, str]] = None

    event_type_filter: Optional[EventTypeFilter] = None
    """An optional filtering rule to match the 'event_type' property of an event."""

    filter: Optional[Dict[str, object]] = None
    """(DEPRECATED) use property_filters & event_type_filter instead"""

    group_by: Optional[List[str]] = None
    """(DEPRECATED) use group_keys instead"""

    group_keys: Optional[List[List[str]]] = None
    """Property names that are used to group usage costs on an invoice.

    Each entry represents a set of properties used to slice events into distinct
    buckets.
    """

    property_filters: Optional[List[PropertyFilter]] = None
    """A list of filters to match events to this billable metric.

    Each filter defines a rule on an event property. All rules must pass for the
    event to match the billable metric.
    """

    sql: Optional[str] = None
    """The SQL query associated with the billable metric"""
