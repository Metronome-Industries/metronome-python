# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["EventTypeFilter"]


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
