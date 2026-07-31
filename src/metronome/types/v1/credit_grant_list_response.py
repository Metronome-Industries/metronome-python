# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from .credit_ledger_entry import CreditLedgerEntry
from ..shared.credit_type_data import CreditTypeData

__all__ = ["CreditGrantListResponse", "Balance", "GrantAmount", "PaidAmount", "Product"]


class Balance(BaseModel):
    """
    The effective balance of the grant as of the end of the customer's current billing period. Expiration deductions will be included only if the grant expires before the end of the current billing period.
    """

    effective_at: datetime
    """The end_date of the customer's current billing period."""

    excluding_pending: float
    """The grant's current balance including all posted deductions.

    If the grant has expired, this amount will be 0.
    """

    including_pending: float
    """The grant's current balance including all posted and pending deductions.

    If the grant expires before the end of the customer's current billing period,
    this amount will be 0.
    """


class GrantAmount(BaseModel):
    """the amount of credits initially granted"""

    amount: float

    credit_type: CreditTypeData
    """the credit type for the amount granted"""


class PaidAmount(BaseModel):
    """the amount paid for this credit grant"""

    amount: float

    credit_type: CreditTypeData
    """the credit type for the amount paid"""


class Product(BaseModel):
    id: str

    name: str


class CreditGrantListResponse(BaseModel):
    id: str
    """the Metronome ID of the credit grant"""

    balance: Balance
    """
    The effective balance of the grant as of the end of the customer's current
    billing period. Expiration deductions will be included only if the grant expires
    before the end of the current billing period.
    """

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    customer_id: str
    """the Metronome ID of the customer"""

    deductions: List[CreditLedgerEntry]

    effective_at: datetime

    expires_at: datetime

    grant_amount: GrantAmount
    """the amount of credits initially granted"""

    name: str

    paid_amount: PaidAmount
    """the amount paid for this credit grant"""

    pending_deductions: List[CreditLedgerEntry]

    priority: float

    credit_grant_type: Optional[str] = None

    invoice_id: Optional[str] = None
    """
    the Metronome ID of the invoice with the purchase charge for this credit grant,
    if applicable
    """

    products: Optional[List[Product]] = None
    """The products which these credits will be applied to.

    (If unspecified, the credits will be applied to charges for all products.)
    """

    reason: Optional[str] = None

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """
