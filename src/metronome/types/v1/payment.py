# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .payment_status import PaymentStatus
from ..shared.credit_type_data import CreditTypeData

__all__ = ["Payment", "PaymentGateway", "PaymentGatewayStripe", "PaymentGatewayStripeError", "RevenueSystemPayment"]


class PaymentGatewayStripeError(BaseModel):
    code: Optional[str] = None

    decline_code: Optional[str] = None

    type: Optional[str] = None


class PaymentGatewayStripe(BaseModel):
    payment_intent_id: str

    error: Optional[PaymentGatewayStripeError] = None

    payment_method_id: Optional[str] = None


class PaymentGateway(BaseModel):
    stripe: PaymentGatewayStripe

    type: Literal["stripe"]


class RevenueSystemPayment(BaseModel):
    revenue_system_provider: str

    sync_status: str

    error_message: Optional[str] = None
    """The error message from the revenue system, if available."""

    revenue_system_external_payment_id: Optional[str] = None


class Payment(BaseModel):
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

    revenue_system_payments: Optional[List[RevenueSystemPayment]] = None

    status: Optional[PaymentStatus] = None

    updated_at: Optional[datetime] = None
