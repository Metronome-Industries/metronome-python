# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContractScheduleProServicesInvoiceParams", "LineItem"]


class ContractScheduleProServicesInvoiceParams(TypedDict, total=False):
    contract_id: Required[str]

    customer_id: Required[str]

    issued_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date the invoice is issued"""

    line_items: Required[Iterable[LineItem]]
    """Each line requires an amount or both unit_price and quantity."""

    netsuite_invoice_header_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end date of the invoice header in Netsuite"""

    netsuite_invoice_header_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The start date of the invoice header in Netsuite"""


class LineItem(TypedDict, total=False):
    """Describes the line item for a professional service charge on an invoice."""

    professional_service_id: Required[str]

    amendment_id: str
    """If the professional_service_id was added on an amendment, this is required."""

    amount: float
    """Amount for the term on the new invoice."""

    metadata: str
    """For client use."""

    netsuite_invoice_billing_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end date for the billing period on the invoice."""

    netsuite_invoice_billing_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The start date for the billing period on the invoice."""

    quantity: float
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount.
    """

    unit_price: float
    """If specified, this overrides the unit price on the pro service term.

    Must also provide quantity (but not amount) if providing unit_price.
    """
