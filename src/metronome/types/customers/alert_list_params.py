# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List

from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["AlertListParams"]

class AlertListParams(TypedDict, total=False):
    customer_id: Required[str]
    """The Metronome ID of the customer"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    alert_statuses: List[Literal["ENABLED", "DISABLED", "ARCHIVED"]]
    """Optionally filter by alert status.

    If absent, only enabled alerts will be returned.
    """