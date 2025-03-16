# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import List, Union

from datetime import datetime

from .._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ContractSetUsageFilterParams"]

class ContractSetUsageFilterParams(TypedDict, total=False):
    contract_id: Required[str]

    customer_id: Required[str]

    group_key: Required[str]

    group_values: Required[List[str]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]]