# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .credit_type import CreditType
from .schedule_point_in_time import SchedulePointInTime

__all__ = [
    "Commit",
    "Product",
    "AccessSchedule",
    "AccessScheduleScheduleItem",
    "Contract",
    "InvoiceContract",
    "Ledger",
    "LedgerPrepaidCommitSegmentStartLedgerEntry",
    "LedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry",
    "LedgerPrepaidCommitRolloverLedgerEntry",
    "LedgerPrepaidCommitExpirationLedgerEntry",
    "LedgerPrepaidCommitCanceledLedgerEntry",
    "LedgerPrepaidCommitCreditedLedgerEntry",
    "LedgerPostpaidCommitInitialBalanceLedgerEntry",
    "LedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry",
    "LedgerPostpaidCommitRolloverLedgerEntry",
    "LedgerPostpaidCommitCanceledLedgerEntry",
    "LedgerPostpaidCommitCreditedLedgerEntry",
    "LedgerPostpaidCommitTrueupLedgerEntry",
    "LedgerPrepaidCommitManualLedgerEntry",
    "LedgerPostpaidCommitManualLedgerEntry",
    "LedgerPostpaidCommitExpirationLedgerEntry",
    "RolledOverFrom",
]


class Product(BaseModel):
    id: str

    name: str


class AccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class AccessSchedule(BaseModel):
    schedule_items: List[AccessScheduleScheduleItem]

    credit_type: Optional[CreditType] = None


class Contract(BaseModel):
    id: str


class InvoiceContract(BaseModel):
    id: str


class LedgerPrepaidCommitSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class LedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class LedgerPrepaidCommitRolloverLedgerEntry(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class LedgerPrepaidCommitExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class LedgerPrepaidCommitCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]


class LedgerPrepaidCommitCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]


class LedgerPostpaidCommitInitialBalanceLedgerEntry(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class LedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class LedgerPostpaidCommitRolloverLedgerEntry(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class LedgerPostpaidCommitCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_CANCELED"]


class LedgerPostpaidCommitCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_CREDITED"]


class LedgerPostpaidCommitTrueupLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]


class LedgerPrepaidCommitManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class LedgerPostpaidCommitManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class LedgerPostpaidCommitExpirationLedgerEntry(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


Ledger = Union[
    LedgerPrepaidCommitSegmentStartLedgerEntry,
    LedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry,
    LedgerPrepaidCommitRolloverLedgerEntry,
    LedgerPrepaidCommitExpirationLedgerEntry,
    LedgerPrepaidCommitCanceledLedgerEntry,
    LedgerPrepaidCommitCreditedLedgerEntry,
    LedgerPostpaidCommitInitialBalanceLedgerEntry,
    LedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry,
    LedgerPostpaidCommitRolloverLedgerEntry,
    LedgerPostpaidCommitCanceledLedgerEntry,
    LedgerPostpaidCommitCreditedLedgerEntry,
    LedgerPostpaidCommitTrueupLedgerEntry,
    LedgerPrepaidCommitManualLedgerEntry,
    LedgerPostpaidCommitManualLedgerEntry,
    LedgerPostpaidCommitExpirationLedgerEntry,
]


class RolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class Commit(BaseModel):
    id: str

    product: Product

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[AccessSchedule] = None
    """
    The schedule that the customer will gain access to the credits purposed with
    this commit.
    """

    amount: Optional[float] = None
    """(DEPRECATED) Use access_schedule + invoice_schedule instead."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    contract: Optional[Contract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    invoice_contract: Optional[InvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[SchedulePointInTime] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[Ledger]] = None
    """A list of ordered events that impact the balance of a commit.

    For example, an invoice deduction or a rollover.
    """

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    priority: Optional[float] = None
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    rolled_over_from: Optional[RolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""
