# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["InvoiceAddChargeParams"]


class InvoiceAddChargeParams(TypedDict, total=False):
    customer_id: Required[str]

    charge_id: Required[str]
    """The Metronome ID of the charge to add to the invoice.

    Note that the charge must be on a product that is not on the current plan, and
    the product must have only fixed charges.
    """

    customer_plan_id: Required[str]
    """The Metronome ID of the customer plan to add the charge to."""

    description: Required[str]

    invoice_start_timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The start_timestamp of the invoice to add the charge to."""

    price: Required[float]
    """The price of the charge.

    This price will match the currency on the invoice, e.g. USD cents.
    """

    quantity: Required[float]
