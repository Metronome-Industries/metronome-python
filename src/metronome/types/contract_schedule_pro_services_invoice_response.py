# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .customers.invoice import Invoice

__all__ = ["ContractScheduleProServicesInvoiceResponse"]


class ContractScheduleProServicesInvoiceResponse(BaseModel):
    data: List[Invoice]
