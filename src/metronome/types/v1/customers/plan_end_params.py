# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PlanEndParams"]


class PlanEndParams(TypedDict, total=False):
    customer_id: Required[str]

    customer_plan_id: Required[str]

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp for when the plan ends (exclusive) for this customer.

    Must be at 0:00 UTC (midnight). If not provided, the plan end date will be
    cleared.
    """

    void_invoices: bool
    """If true, plan end date can be before the last finalized invoice date.

    Any invoices generated after the plan end date will be voided.
    """

    void_stripe_invoices: bool
    """Only applicable when void_invoices is set to true.

    If true, for every invoice that is voided we will also attempt to void/delete
    the stripe invoice (if any). Stripe invoices will be voided if finalized or
    deleted if still in draft state.
    """
