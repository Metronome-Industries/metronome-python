# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomerSetBillingConfigurationsResponse", "Data"]


class Data(BaseModel):
    id: Optional[str] = None
    """ID of the created configuration"""

    billing_provider: Optional[
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
    ] = None
    """The billing provider set for this configuration."""

    configuration: Optional[Dict[str, object]] = None
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider and delivery
    method combination.
    """

    customer_id: Optional[str] = None
    """ID of the customer this configuration is associated with."""

    delivery_method_id: Optional[str] = None
    """ID of the delivery method used for this customer configuration."""

    tax_provider: Optional[Literal["anrok", "avalara", "stripe"]] = None
    """The tax provider set for this configuration."""


class CustomerSetBillingConfigurationsResponse(BaseModel):
    data: List[Data]
