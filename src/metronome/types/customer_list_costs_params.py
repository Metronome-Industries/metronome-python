# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union

from datetime import datetime

from .._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["CustomerListCostsParams"]

class CustomerListCostsParams(TypedDict, total=False):
    customer_id: Required[str]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_on: Required[Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]]
    """RFC 3339 timestamp (inclusive)"""

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""