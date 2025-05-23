# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = [
    "CreditGrantListEntriesResponse",
    "Data",
    "DataLedger",
    "DataLedgerCreditType",
    "DataLedgerEndingBalance",
    "DataLedgerEntry",
    "DataLedgerPendingEntry",
    "DataLedgerStartingBalance",
]


class DataLedgerCreditType(BaseModel):
    id: str

    name: str


class DataLedgerEndingBalance(BaseModel):
    effective_at: datetime
    """
    the ending_before request parameter (if supplied) or the current billing
    period's end date
    """

    excluding_pending: float
    """
    the ending balance, including the balance of all grants that have not expired
    before the effective_at date and deductions that happened before the
    effective_at date
    """

    including_pending: float
    """
    the excluding_pending balance plus any pending invoice deductions and
    expirations that will happen by the effective_at date
    """


class DataLedgerEntry(BaseModel):
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


class DataLedgerPendingEntry(BaseModel):
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


class DataLedgerStartingBalance(BaseModel):
    effective_at: datetime
    """
    the starting_on request parameter (if supplied) or the first credit grant's
    effective_at date
    """

    excluding_pending: float
    """
    the starting balance, including all posted grants, deductions, and expirations
    that happened at or before the effective_at timestamp
    """

    including_pending: float
    """
    the excluding_pending balance plus any pending activity that has not been posted
    at the time of the query
    """


class DataLedger(BaseModel):
    credit_type: DataLedgerCreditType

    ending_balance: DataLedgerEndingBalance
    """the effective balances at the end of the specified time window"""

    entries: List[DataLedgerEntry]

    pending_entries: List[DataLedgerPendingEntry]

    starting_balance: DataLedgerStartingBalance


class Data(BaseModel):
    customer_id: str

    ledgers: List[DataLedger]


class CreditGrantListEntriesResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
