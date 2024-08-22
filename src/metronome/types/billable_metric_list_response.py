# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.property_filter import PropertyFilter
from .shared.event_type_filter import EventTypeFilter

__all__ = ["BillableMetricListResponse"]


class BillableMetricListResponse(BaseModel):
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
