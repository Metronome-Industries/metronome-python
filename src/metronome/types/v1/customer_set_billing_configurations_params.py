# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomerSetBillingConfigurationsParams", "Data", "DataUnbillableInvoicesConfiguration"]


class CustomerSetBillingConfigurationsParams(TypedDict, total=False):
    data: Required[Iterable[Data]]


class DataUnbillableInvoicesConfiguration(TypedDict, total=False):
    """
    An individual rule that, when evaluated to true, indicates that any invoices for this billing provider will not be sent to its associated destination for the associated contract. Rules only apply to the specified `invoice_type` (or all invoices if omitted) and `fiat_credit_type_id` (or all invoices if omitted). Rule precedence is evaluated from more specific to less specific. This method will fail with a 400 if multiple rules with the same specificity are included.
    """

    invoice_type: Required[Literal["usage", "scheduled"]]
    """The type of invoice this rule applies to."""

    fiat_credit_type_id: str
    """Restricts the rule to invoices in this fiat currency.

    Omit for a catch-all rule that applies to every currency of the `invoice_type`.
    Required when `max_amount` is set.
    """

    max_amount: float
    """A positive decimal, in the units of `fiat_credit_type_id`.

    Only invoices whose total is at or below this amount are suppressed; a higher
    total is still sent to the billing provider. When omitted, every matching
    invoice is suppressed regardless of amount.
    """


class Data(TypedDict, total=False):
    billing_provider: Required[
        Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
            "metronome",
        ]
    ]
    """The billing provider set for this configuration."""

    customer_id: Required[str]

    configuration: Dict[str, object]
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider and delivery
    method combination. Defaults to an empty object, however, for most billing
    provider + delivery method combinations, it will not be a valid configuration.
    For AWS marketplace configurations, the aws_is_subscription_product flag can be
    used to indicate a product with usage-based pricing. More information can be
    found
    [here](https://docs.metronome.com/invoice-customers/solutions/marketplaces/invoice-aws/#provision-aws-marketplace-customers-in-metronome).
    """

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]
    """The method to use for delivering invoices to this customer.

    If not provided, the `delivery_method_id` must be provided.
    """

    delivery_method_id: str
    """ID of the delivery method to use for this customer.

    If not provided, the `delivery_method` must be provided.
    """

    tax_provider: Literal["anrok", "avalara", "stripe"]
    """
    Specifies which tax provider Metronome should use for tax calculation when
    billing through Stripe. This is only supported for Stripe billing provider
    configurations with auto_charge_payment_intent or manual_charge_payment_intent
    collection methods.
    """

    unbillable_invoices_configuration: Iterable[DataUnbillableInvoicesConfiguration]
    """Rules that stop matching invoices from being sent to the billing provider.

    Only supported for Stripe billing provider configurations. When omitted, every
    invoice is sent to the billing provider.
    """
