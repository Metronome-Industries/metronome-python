# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .commit_specifier import CommitSpecifier
from .schedule_duration import ScheduleDuration
from .schedule_point_in_time import SchedulePointInTime
from .commit_hierarchy_configuration import CommitHierarchyConfiguration

__all__ = [
    "Commit",
    "Product",
    "Contract",
    "InvoiceContract",
    "Ledger",
    "LedgerPrepaidCommitSegmentStartLedgerEntry",
    "LedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry",
    "LedgerPrepaidCommitRolloverLedgerEntry",
    "LedgerPrepaidCommitExpirationLedgerEntry",
    "LedgerPrepaidCommitCanceledLedgerEntry",
    "LedgerPrepaidCommitCreditedLedgerEntry",
    "LedgerPrepaidCommitSeatBasedAdjustmentLedgerEntry",
    "LedgerPostpaidCommitInitialBalanceLedgerEntry",
    "LedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry",
    "LedgerPostpaidCommitRolloverLedgerEntry",
    "LedgerPostpaidCommitTrueupLedgerEntry",
    "LedgerPrepaidCommitManualLedgerEntry",
    "LedgerPostpaidCommitManualLedgerEntry",
    "LedgerPostpaidCommitExpirationLedgerEntry",
    "RolledOverFrom",
]


class Product(BaseModel):
    id: str

    name: str


class Contract(BaseModel):
    id: str


class InvoiceContract(BaseModel):
    """The contract that this commit will be billed on."""

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

    contract_id: Optional[str] = None


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

    contract_id: Optional[str] = None


class LedgerPrepaidCommitCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]

    contract_id: Optional[str] = None


class LedgerPrepaidCommitSeatBasedAdjustmentLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT"]


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

    contract_id: Optional[str] = None


class LedgerPostpaidCommitRolloverLedgerEntry(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class LedgerPostpaidCommitTrueupLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]

    contract_id: Optional[str] = None


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


Ledger: TypeAlias = Union[
    LedgerPrepaidCommitSegmentStartLedgerEntry,
    LedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry,
    LedgerPrepaidCommitRolloverLedgerEntry,
    LedgerPrepaidCommitExpirationLedgerEntry,
    LedgerPrepaidCommitCanceledLedgerEntry,
    LedgerPrepaidCommitCreditedLedgerEntry,
    LedgerPrepaidCommitSeatBasedAdjustmentLedgerEntry,
    LedgerPostpaidCommitInitialBalanceLedgerEntry,
    LedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry,
    LedgerPostpaidCommitRolloverLedgerEntry,
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

    created_at: datetime
    """Timestamp of when the commit was created.

    - Recurring commits: latter of commit service period date and parent commit
      start date
    - Rollover commits: when the new contract started
    """

    product: Product

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[ScheduleDuration] = None
    """
    The schedule that the customer will gain access to the credits purposed with
    this commit.
    """

    amount: Optional[float] = None
    """(DEPRECATED) Use access_schedule + invoice_schedule instead."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    archived_at: Optional[datetime] = None
    """RFC 3339 timestamp indicating when the commit was archived.

    If not provided, the commit is not archived.
    """

    balance: Optional[float] = None
    """The current balance of the credit or commit.

    This balance reflects the amount of credit or commit that the customer has
    access to use at this moment - thus, expired and upcoming credit or commit
    segments contribute 0 to the balance. The balance will match the sum of all
    ledger entries with the exception of the case where the sum of negative manual
    ledger entries exceeds the positive amount remaining on the credit or commit -
    in that case, the balance will be 0. All manual ledger entries associated with
    active credit or commit segments are included in the balance, including
    future-dated manual ledger entries.
    """

    contract: Optional[Contract] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

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

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    rolled_over_from: Optional[RolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a commit or credit is made with a uniqueness key that was
    previously used to create a commit or credit, a new record will not be created
    and the request will fail with a 409 error.
    """
