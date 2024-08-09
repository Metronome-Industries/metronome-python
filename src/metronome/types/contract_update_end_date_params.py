# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ContractUpdateEndDateParams"]


class ContractUpdateEndDateParams(TypedDict, total=False):
    contract_id: Required[str]
    """ID of the contract to update"""

    customer_id: Required[str]
    """ID of the customer whose contract is to be updated"""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp indicating when the contract will end (exclusive).

    If not provided, the contract will be updated to be open-ended.
    """
