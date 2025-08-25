# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomerRetrieveCustomerBillingConfigurationsResponse", "Data"]


class Data(BaseModel):
    id: str
    """
    ID of this configuration; can be provided as the
    billing_provider_configuration_id when creating a contract.
    """

    billing_provider: Literal[
        "aws_marketplace",
        "stripe",
        "netsuite",
        "custom",
        "azure_marketplace",
        "quickbooks_online",
        "workday",
        "gcp_marketplace",
    ]
    """The billing provider set for this configuration."""

    configuration: Dict[str, object]
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider.
    """

    customer_id: str

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]
    """The method to use for delivering invoices to this customer."""

    delivery_method_configuration: Dict[str, object]
    """Configuration for the delivery method.

    The structure of this object is specific to the delivery method.
    """

    delivery_method_id: str
    """ID of the delivery method to use for this customer."""


class CustomerRetrieveCustomerBillingConfigurationsResponse(BaseModel):
    data: List[Data]
