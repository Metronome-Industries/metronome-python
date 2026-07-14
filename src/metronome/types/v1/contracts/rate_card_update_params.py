# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RateCardUpdateParams", "AddCreditTypeConversion", "Alias"]


class RateCardUpdateParams(TypedDict, total=False):
    rate_card_id: Required[str]
    """ID of the rate card to update"""

    add_credit_type_conversions: Iterable[AddCreditTypeConversion]
    """Add credit type conversions for using custom pricing units in rates.

    Existing conversions cannot be modified.
    """

    aliases: Iterable[Alias]
    """Reference this alias when creating a contract.

    If the same alias is assigned to multiple rate cards, it will reference the rate
    card to which it was most recently assigned. It is not exposed to end customers.
    """

    description: str

    name: str
    """Used only in UI/API. It is not exposed to end customers."""


class AddCreditTypeConversion(TypedDict, total=False):
    custom_credit_type_id: Required[str]

    fiat_per_custom_credit: Required[float]


class Alias(TypedDict, total=False):
    name: Required[str]

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
