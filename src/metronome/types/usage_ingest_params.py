# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["UsageIngestParams", "Usage"]


class UsageIngestParams(TypedDict, total=False):
    usage: Iterable[Usage]


class Usage(TypedDict, total=False):
    customer_id: Required[str]

    event_type: Required[str]

    timestamp: Required[str]
    """RFC 3339 formatted"""

    transaction_id: Required[str]

    properties: Dict[str, object]
