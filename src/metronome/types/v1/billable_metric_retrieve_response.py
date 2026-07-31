# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.property_filter import PropertyFilter
from ..shared.event_type_filter import EventTypeFilter

__all__ = ["BillableMetricRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str
    """ID of the billable metric"""

    name: str
    """The display name of the billable metric."""

    aggregation_key: Optional[str] = None
    """A key that specifies which property of the event is used to aggregate data.

    This key must be one of the property filter names and is not applicable when the
    aggregation type is 'count'.
    """

    aggregation_type: Optional[Literal["COUNT", "LATEST", "MAX", "SUM", "UNIQUE"]] = None
    """Specifies the type of aggregation performed on matching events."""

    archived_at: Optional[datetime] = None
    """RFC 3339 timestamp indicating when the billable metric was archived.

    If not provided, the billable metric is not archived.
    """

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    event_type_filter: Optional[EventTypeFilter] = None
    """An optional filtering rule to match the 'event_type' property of an event."""

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


class BillableMetricRetrieveResponse(BaseModel):
    data: Data
