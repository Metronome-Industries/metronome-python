# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    customer_id: Required[str]

    invoice_id: Required[str]

    limit: int
    """The maximum number of payments to return. Defaults to 25."""

    next_page: str
    """The next page token from a previous response."""

    statuses: List[Literal["pending", "requires_intervention", "paid", "canceled"]]
