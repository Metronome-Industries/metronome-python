# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .commit import Commit
from .discount import Discount
from .override import Override
from ..._models import BaseModel
from .credit_type import CreditType
from .scheduled_charge import ScheduledCharge

__all__ = [
    "ContractWithoutAmendments",
    "Transition",
    "UsageStatementSchedule",
    "Credit",
    "CreditProduct",
    "CreditAccessSchedule",
    "CreditAccessScheduleScheduleItem",
    "CreditContract",
    "CreditLedger",
    "CreditLedgerCreditSegmentStartLedgerEntry",
    "CreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry",
    "CreditLedgerCreditExpirationLedgerEntry",
    "CreditLedgerCreditCanceledLedgerEntry",
    "CreditLedgerCreditCreditedLedgerEntry",
    "CreditLedgerCreditManualLedgerEntry",
    "ProfessionalService",
    "ResellerRoyalty",
    "UsageFilter",
    "UsageFilterCurrent",
    "UsageFilterInitial",
    "UsageFilterUpdate",
]


class Transition(BaseModel):
    from_contract_id: str

    to_contract_id: str

    type: Literal["SUPERSEDE", "RENEWAL"]


class UsageStatementSchedule(BaseModel):
    frequency: Literal["MONTHLY", "monthly", "QUARTERLY", "quarterly"]


class CreditProduct(BaseModel):
    id: str

    name: str


class CreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class CreditAccessSchedule(BaseModel):
    schedule_items: List[CreditAccessScheduleScheduleItem]

    credit_type: Optional[CreditType] = None


class CreditContract(BaseModel):
    id: str


class CreditLedgerCreditSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class CreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class CreditLedgerCreditExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class CreditLedgerCreditCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class CreditLedgerCreditCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class CreditLedgerCreditManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


CreditLedger = Union[
    CreditLedgerCreditSegmentStartLedgerEntry,
    CreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry,
    CreditLedgerCreditExpirationLedgerEntry,
    CreditLedgerCreditCanceledLedgerEntry,
    CreditLedgerCreditCreditedLedgerEntry,
    CreditLedgerCreditManualLedgerEntry,
]


class Credit(BaseModel):
    id: str

    product: CreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[CreditAccessSchedule] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    contract: Optional[CreditContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[CreditLedger]] = None
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


class ProfessionalService(BaseModel):
    id: str

    max_amount: float
    """Maximum amount for the term."""

    product_id: str

    quantity: float
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount.
    """

    unit_price: float
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified.
    """

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class ResellerRoyalty(BaseModel):
    fraction: float

    netsuite_reseller_id: str

    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

    starting_at: datetime

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    aws_account_number: Optional[str] = None

    aws_offer_id: Optional[str] = None

    aws_payer_reference_id: Optional[str] = None

    ending_before: Optional[datetime] = None

    gcp_account_id: Optional[str] = None

    gcp_offer_id: Optional[str] = None

    reseller_contract_value: Optional[float] = None


class UsageFilterCurrent(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: Optional[datetime] = None


class UsageFilterInitial(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: Optional[datetime] = None


class UsageFilterUpdate(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: datetime


class UsageFilter(BaseModel):
    current: Optional[UsageFilterCurrent] = None

    initial: UsageFilterInitial

    updates: List[UsageFilterUpdate]


class ContractWithoutAmendments(BaseModel):
    commits: List[Commit]

    created_at: datetime

    created_by: str

    overrides: List[Override]

    scheduled_charges: List[ScheduledCharge]

    starting_at: datetime

    transitions: List[Transition]

    usage_statement_schedule: UsageStatementSchedule

    credits: Optional[List[Credit]] = None

    discounts: Optional[List[Discount]] = None
    """This field's availability is dependent on your client's configuration."""

    ending_before: Optional[datetime] = None

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    professional_services: Optional[List[ProfessionalService]] = None
    """This field's availability is dependent on your client's configuration."""

    rate_card_id: Optional[str] = None

    reseller_royalties: Optional[List[ResellerRoyalty]] = None
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    total_contract_value: Optional[float] = None
    """This field's availability is dependent on your client's configuration."""

    usage_filter: Optional[UsageFilter] = None
