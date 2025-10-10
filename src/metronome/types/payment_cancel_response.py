# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.credit_type_data import CreditTypeData

__all__ = [
    "PaymentCancelResponse",
    "Data",
    "DataPaymentGateway",
    "DataPaymentGatewayStripe",
    "DataPaymentGatewayStripeError",
]


class DataPaymentGatewayStripeError(BaseModel):
    code: Optional[str] = None

    decline_code: Optional[str] = None

    type: Optional[str] = None


class DataPaymentGatewayStripe(BaseModel):
    payment_intent_id: str

    error: Optional[DataPaymentGatewayStripeError] = None


class DataPaymentGateway(BaseModel):
    stripe: DataPaymentGatewayStripe

    type: Literal["stripe"]


class Data(BaseModel):
    id: str

    amount: Optional[float] = None

    amount_paid: Optional[float] = None

    contract_id: Optional[str] = None

    created_at: Optional[datetime] = None

    customer_id: Optional[str] = None

    error_message: Optional[str] = None

    fiat_credit_type: Optional[CreditTypeData] = None

    invoice_id: Optional[str] = None

    payment_gateway: Optional[DataPaymentGateway] = None

    status: Optional[Literal["pending", "requires_intervention", "paid", "canceled"]] = None

    updated_at: Optional[datetime] = None


class PaymentCancelResponse(BaseModel):
    data: Data
