# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditGrantVoidParams"]


class CreditGrantVoidParams(TypedDict, total=False):
    id: Required[str]

    release_uniqueness_key: bool
    """If true, resets the uniqueness key on this grant so it can be re-used"""

    void_credit_purchase_invoice: bool
    """If true, void the purchase invoice associated with the grant"""
