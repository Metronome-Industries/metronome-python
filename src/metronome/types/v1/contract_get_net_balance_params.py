# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.balance_filter import BalanceFilter

__all__ = ["ContractGetNetBalanceParams"]


class ContractGetNetBalanceParams(TypedDict, total=False):
    customer_id: Required[str]
    """The ID of the customer."""

    credit_type_id: str
    """
    The ID of the credit type (can be fiat or a custom pricing unit) to get the
    balance for. Defaults to USD (cents) if not specified.
    """

    filters: Iterable[BalanceFilter]
    """
    Balance filters are OR'd together, so if a given commit or credit matches any of
    the filters, it will be included in the net balance.
    """

    invoice_inclusion_mode: Literal["FINALIZED", "FINALIZED_AND_DRAFT"]
    """Controls which invoices are considered when calculating the remaining balance.

    `FINALIZED` considers only deductions from finalized invoices.
    `FINALIZED_AND_DRAFT` also includes deductions from pending draft invoices.
    """
