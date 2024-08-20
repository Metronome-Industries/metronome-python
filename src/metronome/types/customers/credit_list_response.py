# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.credit_type import CreditType

__all__ = [
    "CreditListResponse",
    "Data",
    "DataProduct",
    "DataAccessSchedule",
    "DataAccessScheduleScheduleItem",
    "DataContract",
    "DataLedger",
    "DataLedgerCreditSegmentStartLedgerEntry",
    "DataLedgerCreditAutomatedInvoiceDeductionLedgerEntry",
    "DataLedgerCreditExpirationLedgerEntry",
    "DataLedgerCreditCanceledLedgerEntry",
    "DataLedgerCreditCreditedLedgerEntry",
    "DataLedgerCreditManualLedgerEntry",
]


class DataProduct(BaseModel):
    id: str

    name: str


class DataAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataAccessSchedule(BaseModel):
    schedule_items: List[DataAccessScheduleScheduleItem]

    credit_type: Optional[CreditType] = None


class DataContract(BaseModel):
    id: str


class DataLedgerCreditSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataLedgerCreditAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataLedgerCreditExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataLedgerCreditCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class DataLedgerCreditCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class DataLedgerCreditManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


DataLedger: TypeAlias = Union[
    DataLedgerCreditSegmentStartLedgerEntry,
    DataLedgerCreditAutomatedInvoiceDeductionLedgerEntry,
    DataLedgerCreditExpirationLedgerEntry,
    DataLedgerCreditCanceledLedgerEntry,
    DataLedgerCreditCreditedLedgerEntry,
    DataLedgerCreditManualLedgerEntry,
]


class Data(BaseModel):
    id: str

    product: DataProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[DataAccessSchedule] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    contract: Optional[DataContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[DataLedger]] = None
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


class CreditListResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
