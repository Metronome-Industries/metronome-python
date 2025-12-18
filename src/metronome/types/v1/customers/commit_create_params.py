# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...shared_params.commit_specifier_input import CommitSpecifierInput

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
    """ID of the fixed product associated with the commit.

    This is required because products are used to invoice the commit amount.
    """

    type: Required[Literal["PREPAID", "POSTPAID"]]

    applicable_contract_ids: SequenceNotStr[str]
    """Which contract the commit applies to.

    If not provided, the commit applies to all contracts.
    """

    applicable_product_ids: SequenceNotStr[str]
    """Which products the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: SequenceNotStr[str]
    """Which tags the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str
    """Used only in UI/API. It is not exposed to end customers."""

    invoice_contract_id: str
    """The contract that this commit will be billed on.

    This is required for "POSTPAID" commits and for "PREPAID" commits unless there
    is no invoice schedule above (i.e., the commit is 'free'), or if do_not_invoice
    is set to true.
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

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]

    salesforce_opportunity_id: str
    """This field's availability is dependent on your client's configuration."""

    specifiers: Iterable[CommitSpecifierInput]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """

    uniqueness_key: str
    """Prevents the creation of duplicates.

    If a request to create a commit or credit is made with a uniqueness key that was
    previously used to create a commit or credit, a new record will not be created
    and the request will fail with a 409 error.
    """


class AccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class AccessSchedule(TypedDict, total=False):
    """Schedule for distributing the commit to the customer.

    For "POSTPAID" commits only one schedule item is allowed and amount must match invoice_schedule total.
    """

    schedule_items: Required[Iterable[AccessScheduleScheduleItem]]

    credit_type_id: str
    """Defaults to USD (cents) if not passed"""


class InvoiceScheduleRecurringSchedule(TypedDict, total=False):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

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
    """
    Required for "POSTPAID" commits: the true up invoice will be generated at this time and only one schedule item is allowed; the total must match accesss_schedule amount. Optional for "PREPAID" commits: if not provided, this will be a "complimentary" commit with no invoice.
    """

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: bool
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    recurring_schedule: InvoiceScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[InvoiceScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""
