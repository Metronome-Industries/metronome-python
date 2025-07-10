# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomerPreviewEventsParams", "Event"]


class CustomerPreviewEventsParams(TypedDict, total=False):
    customer_id: Required[str]

    events: Required[Iterable[Event]]

    mode: Literal["replace", "merge"]
    """
    If set to "replace", the preview will be generated as if those were the only
    events for the specified customer. If set to "merge", the events will be merged
    with any existing events for the specified customer. Defaults to "replace".
    """

    skip_zero_qty_line_items: bool
    """If set, all zero quantity line items will be filtered out of the response."""


class Event(TypedDict, total=False):
    event_type: Required[str]

    customer_id: str
    """
    This has no effect for preview events, but may be set for consistency with Event
    objects. They will be processed even if they do not match the customer's ID or
    ingest aliases.
    """

    properties: Dict[str, object]

    timestamp: str
    """RFC 3339 formatted. If not provided, the current time will be used."""

    transaction_id: str
    """
    This has no effect for preview events, but may be set for consistency with Event
    objects. Duplicate transaction_ids are NOT filtered out, even within the same
    request.
    """
