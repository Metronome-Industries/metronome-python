# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentCancelParams"]


class PaymentCancelParams(TypedDict, total=False):
    customer_id: Required[str]

    invoice_id: Required[str]
