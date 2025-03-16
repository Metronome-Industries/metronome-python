# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Optional

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["CustomerUpdateConfigParams"]

class CustomerUpdateConfigParams(TypedDict, total=False):
    customer_id: Required[str]

    leave_stripe_invoices_in_draft: Optional[bool]
    """Leave in draft or set to auto-advance on invoices sent to Stripe.

    Falls back to the client-level config if unset, which defaults to true if unset.
    """

    salesforce_account_id: Optional[str]
    """The Salesforce account ID for the customer"""