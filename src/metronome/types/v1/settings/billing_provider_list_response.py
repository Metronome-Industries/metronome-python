# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["BillingProviderListResponse", "Data"]


class Data(BaseModel):
    billing_provider: Literal[
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
    """The billing provider set for this configuration."""

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]
    """The method to use for delivering invoices to this customer."""

    delivery_method_configuration: Dict[str, object]
    """Configuration for the delivery method.

    The structure of this object is specific to the delivery method. Some
    configuration may be omitted for security reasons.
    """

    delivery_method_id: str
    """ID of the delivery method to use for this customer."""


class BillingProviderListResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
