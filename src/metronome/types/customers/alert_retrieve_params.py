# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AlertRetrieveParams"]


class AlertRetrieveParams(TypedDict, total=False):
    alert_id: Required[str]
    """The Metronome ID of the alert"""

    customer_id: Required[str]
    """The Metronome ID of the customer"""
