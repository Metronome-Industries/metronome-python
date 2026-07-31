# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RateCardCreateParams", "Alias", "CreditTypeConversion"]


class RateCardCreateParams(TypedDict, total=False):
    name: Required[str]
    """Used only in UI/API. It is not exposed to end customers."""

    aliases: Iterable[Alias]
    """Reference this alias when creating a contract.

    If the same alias is assigned to multiple rate cards, it will reference the rate
    card to which it was most recently assigned. It is not exposed to end customers.
    """

    credit_type_conversions: Iterable[CreditTypeConversion]
    """Required when using custom pricing units in rates."""

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str

    fiat_credit_type_id: str
    """
    The Metronome ID of the credit type to associate with the rate card, defaults to
    USD (cents) if not passed.
    """


class Alias(TypedDict, total=False):
    name: Required[str]

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class CreditTypeConversion(TypedDict, total=False):
    custom_credit_type_id: Required[str]

    fiat_per_custom_credit: Required[float]
