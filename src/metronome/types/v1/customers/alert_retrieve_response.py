# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .customer_alert import CustomerAlert

__all__ = ["AlertRetrieveResponse"]


class AlertRetrieveResponse(BaseModel):
    data: CustomerAlert
