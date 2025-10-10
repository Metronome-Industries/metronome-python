# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .payment import Payment
from ..._models import BaseModel

__all__ = ["PaymentCancelResponse"]


class PaymentCancelResponse(BaseModel):
    data: Payment
