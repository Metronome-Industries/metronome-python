# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomerCreateParams", "BillingConfig"]


class CustomerCreateParams(TypedDict, total=False):
    name: Required[str]
    """This will be truncated to 160 characters if the provided name is longer."""

    billing_config: BillingConfig

    custom_fields: Dict[str, str]

    external_id: str
    """
    (deprecated, use ingest_aliases instead) the first ID (Metronome ID or ingest
    alias) that can be used in usage events
    """

    ingest_aliases: List[str]
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
        ]
    ]

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
