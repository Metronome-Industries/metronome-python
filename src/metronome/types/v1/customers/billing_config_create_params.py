# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingConfigCreateParams"]


class BillingConfigCreateParams(TypedDict, total=False):
    customer_id: Required[str]

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

    billing_provider_customer_id: Required[str]
    """The customer ID in the billing provider's system.

    For Azure, this is the subscription ID.
    """

    aws_customer_account_id: str

    aws_customer_id: str

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
