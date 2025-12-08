# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PaymentGateConfigV2", "PrecalculatedTaxConfig", "StripeConfig"]


class PrecalculatedTaxConfig(BaseModel):
    """Only applicable if using PRECALCULATED as your tax type."""

    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class StripeConfig(BaseModel):
    """Only applicable if using STRIPE as your payment gateway type."""

    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class PaymentGateConfigV2(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[PrecalculatedTaxConfig] = None
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[StripeConfig] = None
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "AVALARA", "PRECALCULATED"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """
