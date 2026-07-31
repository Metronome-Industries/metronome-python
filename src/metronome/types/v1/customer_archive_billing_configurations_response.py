# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["CustomerArchiveBillingConfigurationsResponse", "Data"]


class Data(BaseModel):
    customer_billing_provider_configuration_ids: List[str]
    """Array of billing provider configuration IDs to archive"""

    customer_id: str
    """The customer ID the billing provider configurations belong to"""


class CustomerArchiveBillingConfigurationsResponse(BaseModel):
    data: Data
