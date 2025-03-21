# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CreditUpdateEndDateParams"]


class CreditUpdateEndDateParams(TypedDict, total=False):
    access_ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    RFC 3339 timestamp indicating when access to the credit will end and it will no
    longer be possible to draw it down (exclusive).
    """

    credit_id: Required[str]
    """ID of the commit to update"""

    customer_id: Required[str]
    """ID of the customer whose credit is to be updated"""
