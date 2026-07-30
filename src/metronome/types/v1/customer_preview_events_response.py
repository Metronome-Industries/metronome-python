# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from .customers.invoice import Invoice

__all__ = ["CustomerPreviewEventsResponse"]

class CustomerPreviewEventsResponse(BaseModel):
    data: List[Invoice]