# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ContractListSeatBalancesResponse",
    "Data",
    "DataBalance",
    "DataCommit",
    "DataCommitLedgerEntry",
    "DataCredit",
    "DataCreditLedgerEntry",
    "Pagination",
]


class DataBalance(BaseModel):
    balance: float
    """
    The total balance across all commits and credits for this seat, of this credit
    type.
    """

    credit_type_id: str

    starting_balance: float
    """
    The total initial balances of all commits and credits for this seat, of this
    credit type.
    """


class DataCommitLedgerEntry(BaseModel):
    amount: float
    """Amount of the ledger entry"""

    timestamp: datetime
    """The datetime when the ledger is created"""

    type: Literal[
        "PREPAID_COMMIT_SEGMENT_START",
        "PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION",
        "PREPAID_COMMIT_ROLLOVER",
        "PREPAID_COMMIT_EXPIRATION",
        "PREPAID_COMMIT_CANCELED",
        "PREPAID_COMMIT_CREDITED",
        "PREPAID_COMMIT_MANUAL",
        "PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT",
    ]
    """Commit ledger type"""


class DataCommit(BaseModel):
    id: str
    """The commit or credit ID"""

    balance: float
    """The current balance for this commit for this specific seat"""

    start_date: datetime
    """The datetime when the commit becomes active"""

    end_date: Optional[datetime] = None
    """The datetime when the commit expires"""

    ledger_entries: Optional[List[DataCommitLedgerEntry]] = None
    """
    Transaction history for this commit for this seat (only included if
    include_ledgers=true)
    """


class DataCreditLedgerEntry(BaseModel):
    amount: float
    """Amount of the ledger entry"""

    timestamp: datetime
    """The datetime when the ledger is created"""

    type: Literal[
        "CREDIT_SEGMENT_START",
        "CREDIT_AUTOMATED_INVOICE_DEDUCTION",
        "CREDIT_EXPIRATION",
        "CREDIT_CANCELED",
        "CREDIT_CREDITED",
        "CREDIT_MANUAL",
        "CREDIT_SEAT_BASED_ADJUSTMENT",
        "CREDIT_ROLLOVER",
    ]
    """Credit ledger type"""


class DataCredit(BaseModel):
    id: str
    """The credit ID"""

    balance: float
    """The current balance for this credit for this specific seat"""

    start_date: datetime
    """The datetime when the credit becomes active"""

    end_date: Optional[datetime] = None
    """The datetime when the credit expires"""

    ledger_entries: Optional[List[DataCreditLedgerEntry]] = None
    """
    Transaction history for this credit for this seat (only included if
    include_ledgers=true)
    """


class Data(BaseModel):
    balances: List[DataBalance]

    seat_id: str
    """The unique identifier for the seat"""

    commits: Optional[List[DataCommit]] = None
    """Array of commits applicable to this seat with their balances"""

    credits: Optional[List[DataCredit]] = None
    """Array of credits applicable to this seat with their balances"""


class Pagination(BaseModel):
    seats_available_for_next_page: float
    """Number of seats available to fetch in the next page"""

    seats_included: float
    """Number of seats included in this response"""

    next_page: Optional[str] = None
    """Token to retrieve the next page of results. Null if no more pages available"""


class ContractListSeatBalancesResponse(BaseModel):
    data: List[Data]

    pagination: Pagination
