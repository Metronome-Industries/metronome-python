# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContractRetrieveParams"]


class ContractRetrieveParams(TypedDict, total=False):
    contract_id: Required[str]

    customer_id: Required[str]

    include_balance: bool
    """Include the balance of credits and commits in the response.

    Setting this flag may cause the query to be slower.
    """

    include_ledgers: bool
    """Include commit ledgers in the response.

    Setting this flag may cause the query to be slower.
    """
