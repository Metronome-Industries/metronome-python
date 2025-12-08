# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentGateConfig", "PrecalculatedTaxConfig", "StripeConfig"]


class PrecalculatedTaxConfig(TypedDict, total=False):
    """Only applicable if using PRECALCULATED as your tax type."""

    tax_amount: Required[float]
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: str
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class StripeConfig(TypedDict, total=False):
    """Only applicable if using STRIPE as your payment gate type."""

    payment_type: Required[Literal["INVOICE", "PAYMENT_INTENT"]]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Dict[str, str]
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class PaymentGateConfig(TypedDict, total=False):
    payment_gate_type: Required[Literal["NONE", "STRIPE", "EXTERNAL"]]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: PrecalculatedTaxConfig
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: StripeConfig
    """Only applicable if using STRIPE as your payment gate type."""

    tax_type: Literal["NONE", "STRIPE", "ANROK", "AVALARA", "PRECALCULATED"]
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """
