# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ContractRetrieveParams"]


class ContractRetrieveParams(TypedDict, total=False):
    contract_id: Required[str]

    customer_id: Required[str]

    as_of_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Optional RFC 3339 timestamp.

    Return the contract as of this date. Cannot be used with include_ledgers
    parameter.
    """

    include_balance: bool
    """Include the balance of credits and commits in the response.

    Setting this flag may cause the query to be slower.
    """

    include_ledgers: bool
    """Include commit/credit ledgers in the response.

    Setting this flag may cause the query to be slower. Cannot be used with
    as_of_date parameter.
    """
