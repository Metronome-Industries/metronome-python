# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CreditGrantEditParams"]


class CreditGrantEditParams(TypedDict, total=False):
    id: Required[str]
    """the ID of the credit grant"""

    credit_grant_type: str
    """the updated credit grant type"""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """the updated expiration date for the credit grant"""

    name: str
    """the updated name for the credit grant"""
