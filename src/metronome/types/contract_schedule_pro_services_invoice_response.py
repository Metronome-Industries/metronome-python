# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from .customers.invoice import Invoice

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ContractScheduleProServicesInvoiceResponse"]

class ContractScheduleProServicesInvoiceResponse(BaseModel):
    data: List[Invoice]