# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["PropertyFilter"]


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
