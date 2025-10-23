# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomerPreviewEventsParams", "Event"]


class CustomerPreviewEventsParams(TypedDict, total=False):
    customer_id: Required[str]

    events: Required[Iterable[Event]]
    """Array of usage events to include in the preview calculation.

    Must contain at least one event in `merge` mode.
    """

    mode: Literal["replace", "merge"]
    """Controls how the provided events are combined with existing usage data.

    Use `replace` to calculate the preview as if these are the only events for the
    customer, ignoring all historical usage. Use `merge` to combine these events
    with the customer's existing usage. Defaults to `replace`.
    """

    skip_zero_qty_line_items: bool
    """When `true`, line items with zero quantity are excluded from the response."""


class Event(TypedDict, total=False):
    event_type: Required[str]

    properties: Dict[str, object]

    timestamp: str
    """RFC 3339 formatted. If not provided, the current time will be used."""

    transaction_id: str
    """Optional unique identifier for event deduplication.

    When provided, preview events are automatically deduplicated against historical
    events from the past 34 days. Duplicate transaction IDs within the same request
    will return an error.
    """
