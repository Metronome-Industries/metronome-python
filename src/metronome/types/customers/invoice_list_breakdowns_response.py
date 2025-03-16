# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .invoice import Invoice

from datetime import datetime

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["InvoiceListBreakdownsResponse"]

class InvoiceListBreakdownsResponse(Invoice):
    breakdown_end_timestamp: datetime

    breakdown_start_timestamp: datetime