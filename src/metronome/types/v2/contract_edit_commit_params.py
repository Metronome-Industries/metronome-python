# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
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
    "Specifier",
]


class ContractEditCommitParams(TypedDict, total=False):
    commit_id: Required[str]
    """ID of the commit to edit"""

    customer_id: Required[str]
    """ID of the customer whose commit is being edited"""

    access_schedule: AccessSchedule

    applicable_product_ids: Optional[List[str]]
    """Which products the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]]
    """Which tags the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    invoice_contract_id: str
    """ID of contract to use for invoicing"""

    invoice_schedule: InvoiceSchedule

    priority: Optional[float]
    """
    If multiple commits are applicable, the one with the lower priority will apply
    first.
    """

    product_id: str

    specifiers: Optional[Iterable[Specifier]]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


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


class Specifier(TypedDict, total=False):
    presentation_group_values: Dict[str, str]

    pricing_group_values: Dict[str, str]

    product_id: str
    """
    If provided, the specifier will only apply to the product with the specified ID.
    """

    product_tags: List[str]
    """
    If provided, the specifier will only apply to products with all the specified
    tags.
    """
