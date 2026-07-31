# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BillingProviderCreateParams"]


class BillingProviderCreateParams(TypedDict, total=False):
    billing_provider: Required[Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace"]]
    """The billing provider set for this configuration."""

    configuration: Required[Dict[str, object]]
    """Account-level configuration for the billing provider.

    The structure of this object is specific to the billing provider and delivery
    provider combination. See examples below.
    """

    delivery_method: Required[Literal["direct_to_billing_provider", "aws_sqs", "aws_sns"]]
    """The method to use for delivering invoices for this configuration."""
