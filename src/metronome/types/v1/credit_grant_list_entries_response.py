# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from .credit_ledger_entry import CreditLedgerEntry
from ..shared.credit_type_data import CreditTypeData

__all__ = ["CreditGrantListEntriesResponse", "Ledger", "LedgerEndingBalance", "LedgerStartingBalance"]


class LedgerEndingBalance(BaseModel):
    """the effective balances at the end of the specified time window"""

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


class LedgerStartingBalance(BaseModel):
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


class Ledger(BaseModel):
    credit_type: CreditTypeData

    ending_balance: LedgerEndingBalance
    """the effective balances at the end of the specified time window"""

    entries: List[CreditLedgerEntry]

    pending_entries: List[CreditLedgerEntry]

    starting_balance: LedgerStartingBalance


class CreditGrantListEntriesResponse(BaseModel):
    customer_id: str

    ledgers: List[Ledger]
