# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["NamedScheduleRetrieveParams"]

class NamedScheduleRetrieveParams(TypedDict, total=False):
    customer_id: Required[str]
    """ID of the customer whose named schedule is to be retrieved"""

    schedule_name: Required[str]
    """The identifier for the schedule to be retrieved"""

    covering_date: Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]
    """
    If provided, at most one schedule segment will be returned (the one that covers
    this date). If not provided, all segments will be returned.
    """