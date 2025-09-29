# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.credit_type_data import CreditTypeData

__all__ = ["PaymentListResponse", "PaymentGateway", "PaymentGatewayStripe", "PaymentGatewayStripeError"]


class PaymentGatewayStripeError(BaseModel):
    code: Optional[str] = None

    decline_code: Optional[str] = None

    type: Optional[str] = None


class PaymentGatewayStripe(BaseModel):
    payment_intent_id: str

    error: Optional[PaymentGatewayStripeError] = None


class PaymentGateway(BaseModel):
    stripe: PaymentGatewayStripe

    type: Literal["stripe"]


class PaymentListResponse(BaseModel):
    id: str

    amount: Optional[float] = None

    amount_paid: Optional[float] = None

    contract_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    error_message: Optional[str] = None

    fiat_credit_type: Optional[CreditTypeData] = None

    invoice_id: Optional[str] = None

    payment_gateway: Optional[PaymentGateway] = None

    status: Optional[Literal["pending", "requires_intervention", "paid", "canceled"]] = None

    updated_at: Optional[datetime] = None
