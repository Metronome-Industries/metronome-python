# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["BalanceFilter"]


class BalanceFilter(TypedDict, total=False):
    balance_types: List[Literal["PREPAID_COMMIT", "POSTPAID_COMMIT", "CREDIT"]]
    """The balance type to filter by."""

    custom_fields: Dict[str, str]
    """Custom fields to compute balance across. Must match all custom fields"""

    ids: SequenceNotStr[str]
    """Specific IDs to compute balance across."""
