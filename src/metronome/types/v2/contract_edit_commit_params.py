# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ContractEditCommitParams",
    "AccessSchedule",
    "AccessScheduleAddScheduleItem",
    "AccessScheduleRemoveScheduleItem",
    "AccessScheduleUpdateScheduleItem",
    "InvoiceSchedule",
    "InvoiceScheduleAddScheduleItem",
    "InvoiceScheduleRemoveScheduleItem",
    "InvoiceScheduleUpdateScheduleItem",
]


class ContractEditCommitParams(TypedDict, total=False):
    commit_id: Required[str]
    """ID of the commit to edit"""

    customer_id: Required[str]
    """ID of the customer whose commit is being edited"""

    access_schedule: AccessSchedule

    applicable_product_ids: Optional[List[str]]
    """Which products the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]]
    """Which tags the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    invoice_contract_id: str
    """ID of contract to use for invoicing"""

    invoice_schedule: InvoiceSchedule

    product_id: str


class AccessScheduleAddScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


class AccessScheduleRemoveScheduleItem(TypedDict, total=False):
    id: Required[str]


class AccessScheduleUpdateScheduleItem(TypedDict, total=False):
    id: Required[str]

    amount: float

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class AccessSchedule(TypedDict, total=False):
    add_schedule_items: Iterable[AccessScheduleAddScheduleItem]

    remove_schedule_items: Iterable[AccessScheduleRemoveScheduleItem]

    update_schedule_items: Iterable[AccessScheduleUpdateScheduleItem]


class InvoiceScheduleAddScheduleItem(TypedDict, total=False):
    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    amount: float

    quantity: float

    unit_price: float


class InvoiceScheduleRemoveScheduleItem(TypedDict, total=False):
    id: Required[str]


class InvoiceScheduleUpdateScheduleItem(TypedDict, total=False):
    id: Required[str]

    amount: float

    quantity: float

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    unit_price: float


class InvoiceSchedule(TypedDict, total=False):
    add_schedule_items: Iterable[InvoiceScheduleAddScheduleItem]

    remove_schedule_items: Iterable[InvoiceScheduleRemoveScheduleItem]

    update_schedule_items: Iterable[InvoiceScheduleUpdateScheduleItem]
