# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BalanceFilter"]


class BalanceFilter(BaseModel):
    balance_types: Optional[List[Literal["PREPAID_COMMIT", "POSTPAID_COMMIT", "CREDIT"]]] = None
    """The balance type to filter by."""

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to compute balance across. Must match all custom fields"""

    ids: Optional[List[str]] = None
    """Specific IDs to compute balance across."""
