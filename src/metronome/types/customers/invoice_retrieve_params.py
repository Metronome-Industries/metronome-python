# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InvoiceRetrieveParams"]


class InvoiceRetrieveParams(TypedDict, total=False):
    customer_id: Required[str]

    invoice_id: Required[str]

    skip_zero_qty_line_items: bool
    """If set, all zero quantity line items will be filtered out of the response"""
