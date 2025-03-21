# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContractGetEditHistoryParams"]


class ContractGetEditHistoryParams(TypedDict, total=False):
    contract_id: Required[str]

    customer_id: Required[str]
