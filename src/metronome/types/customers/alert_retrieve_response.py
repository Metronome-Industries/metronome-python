# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from .customer_alert import CustomerAlert

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AlertRetrieveResponse"]

class AlertRetrieveResponse(BaseModel):
    data: CustomerAlert