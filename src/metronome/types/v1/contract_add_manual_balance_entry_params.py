# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContractAddManualBalanceEntryParams"]


class ContractAddManualBalanceEntryParams(TypedDict, total=False):
    id: Required[str]
    """ID of the balance (commit or credit) to update."""

    amount: Required[float]
    """Amount to add to the segment.

    A negative number will draw down from the balance.
    """

    customer_id: Required[str]
    """ID of the customer whose balance is to be updated."""

    reason: Required[str]
    """Reason for the manual adjustment. This will be displayed in the ledger."""

    segment_id: Required[str]
    """ID of the segment to update."""

    contract_id: str
    """ID of the contract to update. Leave blank to update a customer level balance."""

    per_group_amounts: Dict[str, float]
    """
    If using individually configured commits/credits attached to seat managed
    subscriptions, the amount to add for each seat. Must sum to total amount.
    """

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp indicating when the manual adjustment takes place.

    If not provided, it will default to the start of the segment.
    """
