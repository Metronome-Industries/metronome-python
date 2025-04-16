# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CreditLedgerEntry"]


class CreditLedgerEntry(BaseModel):
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
