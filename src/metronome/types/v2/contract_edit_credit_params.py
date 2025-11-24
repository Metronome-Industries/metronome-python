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
    "ContractEditCreditParams",
    "AccessSchedule",
    "AccessScheduleAddScheduleItem",
    "AccessScheduleRemoveScheduleItem",
    "AccessScheduleUpdateScheduleItem",
]


class ContractEditCreditParams(TypedDict, total=False):
    credit_id: Required[str]
    """ID of the credit to edit"""

    customer_id: Required[str]
    """ID of the customer whose credit is being edited"""

    access_schedule: AccessSchedule

    applicable_product_ids: Optional[SequenceNotStr[str]]
    """Which products the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    applicable_product_tags: Optional[SequenceNotStr[str]]
    """Which tags the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    description: str
    """Updated description for the credit"""

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for credit hierarchy access control"""

    name: str
    """Updated name for the credit"""

    priority: Optional[float]
    """
    If multiple commits are applicable, the one with the lower priority will apply
    first.
    """

    product_id: str

    rate_type: Literal["LIST_RATE", "COMMIT_RATE"]
    """
    If provided, updates the credit to use the specified rate type for current and
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
