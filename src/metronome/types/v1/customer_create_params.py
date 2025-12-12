# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "CustomerCreateParams",
    "BillingConfig",
    "CustomerBillingProviderConfiguration",
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

    aws_customer_id: str

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

    stripe_collection_method: Literal[
        "charge_automatically", "send_invoice", "auto_charge_payment_intent", "manually_charge_payment_intent"
    ]
    """
    The collection method for the customer's invoices. NOTE:
    `auto_charge_payment_intent` and `manually_charge_payment_intent` are in beta.
    """


class CustomerBillingProviderConfiguration(TypedDict, total=False):
    billing_provider: Required[Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]]
    """The billing provider set for this configuration."""

    configuration: Dict[str, object]
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider and delivery
    provider combination. Defaults to an empty object, however, for most billing
    provider + delivery method combinations, it will not be a valid configuration.
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
