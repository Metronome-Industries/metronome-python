# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ContractSetUsageFilterParams"]


class ContractSetUsageFilterParams(TypedDict, total=False):
    contract_id: Required[str]

    customer_id: Required[str]

    group_key: Required[str]

    group_values: Required[SequenceNotStr[str]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
