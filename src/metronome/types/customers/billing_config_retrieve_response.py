# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BillingConfigRetrieveResponse", "Data"]


class Data(BaseModel):
    aws_expiration_date: Optional[datetime] = None
    """Contract expiration date for the customer.

    The expected format is RFC 3339 and can be retrieved from AWS's GetEntitlements
    API. (See
    https://docs.aws.amazon.com/marketplaceentitlement/latest/APIReference/API_GetEntitlements.html.)
    """

    aws_product_code: Optional[str] = None

    aws_region: Optional[
        Literal[
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
    ] = None

    azure_expiration_date: Optional[datetime] = None
    """Subscription term start/end date for the customer.

    The expected format is RFC 3339 and can be retrieved from Azure's Get
    Subscription API. (See
    https://learn.microsoft.com/en-us/partner-center/marketplace/partner-center-portal/pc-saas-fulfillment-subscription-api#get-subscription.)
    """

    azure_plan_id: Optional[str] = None

    azure_start_date: Optional[datetime] = None
    """Subscription term start/end date for the customer.

    The expected format is RFC 3339 and can be retrieved from Azure's Get
    Subscription API. (See
    https://learn.microsoft.com/en-us/partner-center/marketplace/partner-center-portal/pc-saas-fulfillment-subscription-api#get-subscription.)
    """

    azure_subscription_status: Optional[
        Literal["Subscribed", "Unsubscribed", "Suspended", "PendingFulfillmentStart"]
    ] = None

    billing_provider_customer_id: Optional[str] = None

    stripe_collection_method: Optional[Literal["charge_automatically", "send_invoice"]] = None


class BillingConfigRetrieveResponse(BaseModel):
    data: Data
