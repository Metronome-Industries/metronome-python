# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertListParams"]


class AlertListParams(TypedDict, total=False):
    customer_id: Required[str]
    """The Metronome ID of the customer"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    alert_statuses: List[
        Literal["enabled", "disabled", "archived", "ENABLED", "DISABLED", "ARCHIVED", "Enabled", "Disabled", "Archived"]
    ]
    """Optionally filter by alert status.

    If absent, only enabled alerts will be returned.
    """
