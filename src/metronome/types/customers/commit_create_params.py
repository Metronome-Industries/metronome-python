# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CommitCreateParams",
    "AccessSchedule",
    "AccessScheduleScheduleItem",
    "InvoiceSchedule",
    "InvoiceScheduleRecurringSchedule",
    "InvoiceScheduleScheduleItem",
]


class CommitCreateParams(TypedDict, total=False):
    access_schedule: Required[AccessSchedule]
    """Schedule for distributing the commit to the customer.

    For "POSTPAID" commits only one schedule item is allowed and amount must match
    invoice_schedule total.
    """

    customer_id: Required[str]

    priority: Required[float]
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    product_id: Required[str]

    type: Required[Literal["PREPAID", "POSTPAID"]]

    applicable_contract_ids: List[str]
    """Which contract the commit applies to.

    If not provided, the commit applies to all contracts.
    """

    applicable_product_ids: List[str]
    """Which products the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: List[str]
    """Which tags the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    custom_fields: Dict[str, str]

    description: str
    """Used only in UI/API. It is not exposed to end customers."""

    invoice_contract_id: str
    """The contract that this commit will be billed on.

    This is required for "POSTPAID" commits and for "PREPAID" commits unless there
    is no invoice schedule above (i.e., the commit is 'free').
    """

    invoice_schedule: InvoiceSchedule
    """
    Required for "POSTPAID" commits: the true up invoice will be generated at this
    time and only one schedule item is allowed; the total must match
    accesss_schedule amount. Optional for "PREPAID" commits: if not provided, this
    will be a "complimentary" commit with no invoice.
    """

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: str
    """This field's availability is dependent on your client's configuration."""


class AccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class AccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[AccessScheduleScheduleItem]]

    credit_type_id: str


class InvoiceScheduleRecurringSchedule(TypedDict, total=False):
    amount_distribution: Required[Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)."""

    frequency: Required[Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL"]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)."""

    amount: float
    """Amount for the charge.

    Can be provided instead of unit_price and quantity. If amount is sent, the
    unit_price is assumed to be the amount and quantity is inferred to be 1.
    """

    quantity: float
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount and must be specified
    with unit_price. If specified amount cannot be provided.
    """

    unit_price: float
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified
    with quantity. If specified amount cannot be provided.
    """


class InvoiceScheduleScheduleItem(TypedDict, total=False):
    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """timestamp of the scheduled event"""

    amount: float
    """Amount for the charge.

    Can be provided instead of unit_price and quantity. If amount is sent, the
    unit_price is assumed to be the amount and quantity is inferred to be 1.
    """

    quantity: float
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount and must be specified
    with unit_price. If specified amount cannot be provided.
    """

    unit_price: float
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified
    with quantity. If specified amount cannot be provided.
    """


class InvoiceSchedule(TypedDict, total=False):
    credit_type_id: str
    """Defaults to USD if not passed. Only USD is supported at this time."""

    recurring_schedule: InvoiceScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[InvoiceScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""
