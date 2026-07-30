# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .invoice import Invoice

from datetime import datetime

__all__ = ["InvoiceListBreakdownsResponse"]

class InvoiceListBreakdownsResponse(Invoice):
    breakdown_end_timestamp: datetime

    breakdown_start_timestamp: datetime