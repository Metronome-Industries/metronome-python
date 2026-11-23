# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CustomerCreateParams",
    "BillingConfig",
    "CustomerBillingProviderConfiguration",
    "CustomerBillingProviderConfigurationConfiguration",
    "CustomerBillingProviderConfigurationUnbillableInvoicesConfiguration",
    "CustomerRevenueSystemConfiguration",
]


class CustomerCreateParams(TypedDict, total=False):
    name: Required[str]
    """This will be truncated to 160 characters if the provided name is longer."""

    billing_config: BillingConfig

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    customer_billing_provider_configurations: Iterable[CustomerBillingProviderConfiguration]

    customer_revenue_system_configurations: Iterable[CustomerRevenueSystemConfiguration]

    external_id: str
    """
    (deprecated, use ingest_aliases instead) an alias that can be used to refer to
    this customer in usage events
    """

    ingest_aliases: SequenceNotStr[str]
    """Aliases that can be used to refer to this customer in usage events"""


class BillingConfig(TypedDict, total=False):
    billing_provider_customer_id: Required[str]

    billing_provider_type: Required[
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

    aws_customer_account_id: str
    """Deprecated and ignored by the server.

    The customer ID comes from `billing_provider_customer_id`.
    """

    aws_customer_id: str
    """Deprecated and ignored by the server.

    The customer ID comes from `billing_provider_customer_id`.
    """

    aws_is_subscription_product: bool
    """True if the aws_product_code is a SAAS subscription product, false otherwise."""

    aws_product_code: str

    aws_region: Literal[
        "af-south-1",
        "ap-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-northeast-3",
        "ap-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "eu-central-1",
        "eu-north-1",
        "eu-south-1",
        "eu-west-1",
        "eu-west-2",
        "eu-west-3",
        "me-south-1",
        "sa-east-1",
        "us-east-1",
        "us-east-2",
        "us-gov-east-1",
        "us-gov-west-1",
        "us-west-1",
        "us-west-2",
    ]

    stripe_collection_method: Literal["charge_automatically", "send_invoice"]
    """The collection method for the customer's invoices."""


class CustomerBillingProviderConfigurationConfiguration(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider and delivery provider combination. Defaults to an empty object, however, for most billing provider + delivery method combinations, it will not be a valid configuration.
    """

    aws_customer_account_id: str
    """AWS Marketplace only.

    The buyer's 12 digit AWS account ID. Must be sent together with
    `aws_license_arn`.
    """

    aws_license_arn: str
    """AWS Marketplace only.

    The ARN of the buyer's AWS License Manager license for this purchase. Must be
    sent together with `aws_customer_account_id`.
    """


class CustomerBillingProviderConfigurationUnbillableInvoicesConfiguration(TypedDict, total=False):
    """
    An individual rule that, when evaluated to true, indicates that any invoices for this billing provider will not be sent to its associated destination for the associated contract. Rules only apply to the specified `invoice_type` (or all invoices if omitted) and `fiat_credit_type_id` (or all invoices if omitted). Rule precedence is evaluated from more specific to less specific. This method will fail with a 400 if multiple rules with the same specificity are included.
    """

    invoice_type: Required[Literal["USAGE", "SCHEDULED"]]
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


class CustomerBillingProviderConfiguration(TypedDict, total=False):
    billing_provider: Required[Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]]
    """The billing provider set for this configuration."""

    configuration: CustomerBillingProviderConfigurationConfiguration
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider and delivery
    provider combination. Defaults to an empty object, however, for most billing
    provider + delivery method combinations, it will not be a valid configuration.
    """

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "aws_sns"]
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
    configurations.
    """

    unbillable_invoices_configuration: Iterable[CustomerBillingProviderConfigurationUnbillableInvoicesConfiguration]
    """Rules that stop matching invoices from being sent to the billing provider.

    Supported for Stripe and NetSuite billing provider configurations. When omitted,
    every invoice is sent to the billing provider. Stripe invoices can be force-sent
    after a rule suppresses them.
    """


class CustomerRevenueSystemConfiguration(TypedDict, total=False):
    provider: Required[Literal["netsuite"]]
    """The revenue system provider set for this configuration."""

    configuration: Dict[str, object]
    """Configuration for the revenue system provider.

    The structure of this object is specific to the revenue system provider. For
    NetSuite, this should contain `netsuite_customer_id`.
    """

    delivery_method: Literal["direct_to_billing_provider"]
    """The method to use for delivering invoices to this customer.

    If not provided, the `delivery_method_id` must be provided.
    """

    delivery_method_id: str
    """ID of the delivery method to use for this customer.

    If not provided, the `delivery_method` must be provided.
    """
