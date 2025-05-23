# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "CreditGrantListResponse",
    "Balance",
    "Deduction",
    "GrantAmount",
    "GrantAmountCreditType",
    "PaidAmount",
    "PaidAmountCreditType",
    "PendingDeduction",
    "Product",
]


class Balance(BaseModel):
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


class Deduction(BaseModel):
    amount: float
    """an amount representing the change to the customer's credit balance"""

    created_by: str

    credit_grant_id: str
    """the credit grant this entry is related to"""

    effective_at: datetime

    reason: str

    running_balance: float
    """
    the running balance for this credit type at the time of the ledger entry,
    including all preceding charges
    """

    invoice_id: Optional[str] = None
    """
    if this entry is a deduction, the Metronome ID of the invoice where the credit
    deduction was consumed; if this entry is a grant, the Metronome ID of the
    invoice where the grant's paid_amount was charged
    """


class GrantAmountCreditType(BaseModel):
    id: str

    name: str


class GrantAmount(BaseModel):
    amount: float

    credit_type: GrantAmountCreditType
    """the credit type for the amount granted"""


class PaidAmountCreditType(BaseModel):
    id: str

    name: str


class PaidAmount(BaseModel):
    amount: float

    credit_type: PaidAmountCreditType
    """the credit type for the amount paid"""


class PendingDeduction(BaseModel):
    amount: float
    """an amount representing the change to the customer's credit balance"""

    created_by: str

    credit_grant_id: str
    """the credit grant this entry is related to"""

    effective_at: datetime

    reason: str

    running_balance: float
    """
    the running balance for this credit type at the time of the ledger entry,
    including all preceding charges
    """

    invoice_id: Optional[str] = None
    """
    if this entry is a deduction, the Metronome ID of the invoice where the credit
    deduction was consumed; if this entry is a grant, the Metronome ID of the
    invoice where the grant's paid_amount was charged
    """


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

    customer_id: str
    """the Metronome ID of the customer"""

    deductions: List[Deduction]

    effective_at: datetime

    expires_at: datetime

    grant_amount: GrantAmount
    """the amount of credits initially granted"""

    name: str

    paid_amount: PaidAmount
    """the amount paid for this credit grant"""

    pending_deductions: List[PendingDeduction]

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
