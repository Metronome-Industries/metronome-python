# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

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