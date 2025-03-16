# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["AlertResetParams"]

class AlertResetParams(TypedDict, total=False):
    alert_id: Required[str]
    """The Metronome ID of the alert"""

    customer_id: Required[str]
    """The Metronome ID of the customer"""