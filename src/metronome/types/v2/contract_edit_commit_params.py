# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.commit_specifier_input import CommitSpecifierInput
from ..shared_params.commit_hierarchy_configuration import CommitHierarchyConfiguration

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

    applicable_product_ids: Optional[SequenceNotStr[str]]
    """Which products the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: Optional[SequenceNotStr[str]]
    """Which tags the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    description: str
    """Updated description for the commit"""

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for commit hierarchy access control"""

    invoice_contract_id: str
    """ID of contract to use for invoicing"""

    invoice_schedule: InvoiceSchedule

    name: str
    """Updated name for the commit"""

    priority: Optional[float]
    """
    If multiple commits are applicable, the one with the lower priority will apply
    first.
    """

    product_id: str

    rate_type: Literal["LIST_RATE", "COMMIT_RATE"]
    """
    If provided, updates the commit to use the specified rate type for current and
    future invoices. Previously finalized invoices will need to be voided and
    regenerated to reflect the rate type change.
    """

    specifiers: Optional[Iterable[CommitSpecifierInput]]
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
