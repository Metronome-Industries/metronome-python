# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.credit_type import CreditType
from .credit_ledger_entry import CreditLedgerEntry

__all__ = ["CreditGrantListResponse", "Data", "DataBalance", "DataGrantAmount", "DataPaidAmount", "DataProduct"]


class DataBalance(BaseModel):
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


class DataGrantAmount(BaseModel):
    amount: float

    credit_type: CreditType
    """the credit type for the amount granted"""


class DataPaidAmount(BaseModel):
    amount: float

    credit_type: CreditType
    """the credit type for the amount paid"""


class DataProduct(BaseModel):
    id: str

    name: str


class Data(BaseModel):
    id: str
    """the Metronome ID of the credit grant"""

    balance: DataBalance
    """
    The effective balance of the grant as of the end of the customer's current
    billing period. Expiration deductions will be included only if the grant expires
    before the end of the current billing period.
    """

    custom_fields: Dict[str, str]

    customer_id: str
    """the Metronome ID of the customer"""

    deductions: List[CreditLedgerEntry]

    effective_at: datetime

    expires_at: datetime

    grant_amount: DataGrantAmount
    """the amount of credits initially granted"""

    name: str

    paid_amount: DataPaidAmount
    """the amount paid for this credit grant"""

    pending_deductions: List[CreditLedgerEntry]

    priority: float

    credit_grant_type: Optional[str] = None

    invoice_id: Optional[str] = None
    """
    the Metronome ID of the invoice with the purchase charge for this credit grant,
    if applicable
    """

    products: Optional[List[DataProduct]] = None
    """The products which these credits will be applied to.

    (If unspecified, the credits will be applied to charges for all products.)
    """

    reason: Optional[str] = None

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class CreditGrantListResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
