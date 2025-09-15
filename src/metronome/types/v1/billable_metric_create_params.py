# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr
from ..shared_params.property_filter import PropertyFilter
from ..shared_params.event_type_filter import EventTypeFilter

__all__ = ["BillableMetricCreateParams"]


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

    group_keys: Iterable[SequenceNotStr[str]]
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
