# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["EventTypeFilter"]


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
