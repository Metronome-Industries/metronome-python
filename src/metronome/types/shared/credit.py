# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .schedule_duration import ScheduleDuration

__all__ = [
    "Credit",
    "Product",
    "Contract",
    "Ledger",
    "LedgerCreditSegmentStartLedgerEntry",
    "LedgerCreditAutomatedInvoiceDeductionLedgerEntry",
    "LedgerCreditExpirationLedgerEntry",
    "LedgerCreditCanceledLedgerEntry",
    "LedgerCreditCreditedLedgerEntry",
    "LedgerCreditManualLedgerEntry",
]


class Product(BaseModel):
    id: str

    name: str


class Contract(BaseModel):
    id: str


class LedgerCreditSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class LedgerCreditAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class LedgerCreditExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class LedgerCreditCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class LedgerCreditCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class LedgerCreditManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


Ledger: TypeAlias = Union[
    LedgerCreditSegmentStartLedgerEntry,
    LedgerCreditAutomatedInvoiceDeductionLedgerEntry,
    LedgerCreditExpirationLedgerEntry,
    LedgerCreditCanceledLedgerEntry,
    LedgerCreditCreditedLedgerEntry,
    LedgerCreditManualLedgerEntry,
]


class Credit(BaseModel):
    id: str

    product: Product

    type: Literal["CREDIT"]

    access_schedule: Optional[ScheduleDuration] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    contract: Optional[Contract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[Ledger]] = None
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
