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

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a commit or credit is made with a uniqueness key that was
    previously used to create a commit or credit, a new record will not be created
    and the request will fail with a 409 error.
    """
