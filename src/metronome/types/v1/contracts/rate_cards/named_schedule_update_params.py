# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["NamedScheduleUpdateParams"]


class NamedScheduleUpdateParams(TypedDict, total=False):
    contract_id: Required[str]
    """ID of the contract whose named schedule is to be updated"""

    customer_id: Required[str]
    """ID of the customer whose named schedule is to be updated"""

    schedule_name: Required[str]
    """The identifier for the schedule to be updated"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    value: Required[object]
    """The value to set for the named schedule.

    The structure of this object is specific to the named schedule.
    """

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
