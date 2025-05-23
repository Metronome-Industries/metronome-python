# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CreditGrantCreateParams",
    "GrantAmount",
    "PaidAmount",
    "RolloverSettings",
    "RolloverSettingsRolloverAmount",
    "RolloverSettingsRolloverAmountUnionMember0",
    "RolloverSettingsRolloverAmountUnionMember1",
]


class CreditGrantCreateParams(TypedDict, total=False):
    customer_id: Required[str]
    """the Metronome ID of the customer"""

    expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """
    The credit grant will only apply to usage or charges dated before this timestamp
    """

    grant_amount: Required[GrantAmount]
    """the amount of credits granted"""

    name: Required[str]
    """the name of the credit grant as it will appear on invoices"""

    paid_amount: Required[PaidAmount]
    """the amount paid for this credit grant"""

    priority: Required[float]

    credit_grant_type: str

    custom_fields: Dict[str, str]
    """Custom fields to attach to the credit grant."""

    effective_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    The credit grant will only apply to usage or charges dated on or after this
    timestamp
    """

    invoice_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date to issue an invoice for the paid_amount."""

    product_ids: List[str]
    """The product(s) which these credits will be applied to.

    (If unspecified, the credits will be applied to charges for all products.). The
    array ordering specified here will be used to determine the order in which
    credits will be applied to invoice line items
    """

    reason: str

    rollover_settings: RolloverSettings
    """
    Configure a rollover for this credit grant so if it expires it rolls over a
    configured amount to a new credit grant. This feature is currently opt-in only.
    Contact Metronome to be added to the beta.
    """

    uniqueness_key: str
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class GrantAmount(TypedDict, total=False):
    amount: Required[float]

    credit_type_id: Required[str]
    """the ID of the pricing unit to be used. Defaults to USD (cents) if not passed."""


class PaidAmount(TypedDict, total=False):
    amount: Required[float]

    credit_type_id: Required[str]
    """the ID of the pricing unit to be used. Defaults to USD (cents) if not passed."""


class RolloverSettingsRolloverAmountUnionMember0(TypedDict, total=False):
    type: Required[Literal["MAX_PERCENTAGE"]]
    """Rollover up to a percentage of the original credit grant amount."""

    value: Required[float]
    """The maximum percentage (0-1) of the original credit grant to rollover."""


class RolloverSettingsRolloverAmountUnionMember1(TypedDict, total=False):
    type: Required[Literal["MAX_AMOUNT"]]
    """Rollover up to a fixed amount of the original credit grant amount."""

    value: Required[float]
    """The maximum amount to rollover."""


RolloverSettingsRolloverAmount: TypeAlias = Union[
    RolloverSettingsRolloverAmountUnionMember0, RolloverSettingsRolloverAmountUnionMember1
]


class RolloverSettings(TypedDict, total=False):
    expires_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """The date to expire the rollover credits."""

    priority: Required[float]
    """
    The priority to give the rollover credit grant that gets created when a rollover
    happens.
    """

    rollover_amount: Required[RolloverSettingsRolloverAmount]
    """Specify how much to rollover to the rollover credit grant"""
