# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.commit import Commit
from .shared.credit_type import CreditType

__all__ = [
    "ContractListBalancesResponse",
    "Data",
    "DataCredit",
    "DataCreditProduct",
    "DataCreditAccessSchedule",
    "DataCreditAccessScheduleScheduleItem",
    "DataCreditContract",
    "DataCreditLedger",
    "DataCreditLedgerCreditSegmentStartLedgerEntry",
    "DataCreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry",
    "DataCreditLedgerCreditExpirationLedgerEntry",
    "DataCreditLedgerCreditCanceledLedgerEntry",
    "DataCreditLedgerCreditCreditedLedgerEntry",
    "DataCreditLedgerCreditManualLedgerEntry",
]


class DataCreditProduct(BaseModel):
    id: str

    name: str


class DataCreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataCreditAccessSchedule(BaseModel):
    schedule_items: List[DataCreditAccessScheduleScheduleItem]

    credit_type: Optional[CreditType] = None


class DataCreditContract(BaseModel):
    id: str


class DataCreditLedgerCreditSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataCreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataCreditLedgerCreditExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataCreditLedgerCreditCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class DataCreditLedgerCreditCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class DataCreditLedgerCreditManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


DataCreditLedger: TypeAlias = Union[
    DataCreditLedgerCreditSegmentStartLedgerEntry,
    DataCreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry,
    DataCreditLedgerCreditExpirationLedgerEntry,
    DataCreditLedgerCreditCanceledLedgerEntry,
    DataCreditLedgerCreditCreditedLedgerEntry,
    DataCreditLedgerCreditManualLedgerEntry,
]


class DataCredit(BaseModel):
    id: str

    product: DataCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[DataCreditAccessSchedule] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    contract: Optional[DataCreditContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[DataCreditLedger]] = None
    """A list of ordered events that impact the balance of a credit.

    For example, an invoice deduction or an expiration.
    """

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    priority: Optional[float] = None
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


Data: TypeAlias = Union[Commit, DataCredit]


class ContractListBalancesResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
