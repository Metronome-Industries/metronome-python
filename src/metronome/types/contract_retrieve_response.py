# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.commit import Commit
from .shared.discount import Discount
from .shared.override import Override
from .shared.credit_type import CreditType
from .shared.scheduled_charge import ScheduledCharge
from .shared.contract_without_amendments import ContractWithoutAmendments

__all__ = [
    "ContractRetrieveResponse",
    "Data",
    "DataAmendment",
    "DataAmendmentCredit",
    "DataAmendmentCreditProduct",
    "DataAmendmentCreditAccessSchedule",
    "DataAmendmentCreditAccessScheduleScheduleItem",
    "DataAmendmentCreditContract",
    "DataAmendmentCreditLedger",
    "DataAmendmentCreditLedgerCreditSegmentStartLedgerEntry",
    "DataAmendmentCreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry",
    "DataAmendmentCreditLedgerCreditExpirationLedgerEntry",
    "DataAmendmentCreditLedgerCreditCanceledLedgerEntry",
    "DataAmendmentCreditLedgerCreditCreditedLedgerEntry",
    "DataAmendmentCreditLedgerCreditManualLedgerEntry",
    "DataAmendmentProfessionalService",
    "DataAmendmentResellerRoyalty",
    "DataCustomerBillingProviderConfiguration",
]


class DataAmendmentCreditProduct(BaseModel):
    id: str

    name: str


class DataAmendmentCreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataAmendmentCreditAccessSchedule(BaseModel):
    schedule_items: List[DataAmendmentCreditAccessScheduleScheduleItem]

    credit_type: Optional[CreditType] = None


class DataAmendmentCreditContract(BaseModel):
    id: str


class DataAmendmentCreditLedgerCreditSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataAmendmentCreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataAmendmentCreditLedgerCreditExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataAmendmentCreditLedgerCreditCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class DataAmendmentCreditLedgerCreditCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class DataAmendmentCreditLedgerCreditManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


DataAmendmentCreditLedger: TypeAlias = Union[
    DataAmendmentCreditLedgerCreditSegmentStartLedgerEntry,
    DataAmendmentCreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry,
    DataAmendmentCreditLedgerCreditExpirationLedgerEntry,
    DataAmendmentCreditLedgerCreditCanceledLedgerEntry,
    DataAmendmentCreditLedgerCreditCreditedLedgerEntry,
    DataAmendmentCreditLedgerCreditManualLedgerEntry,
]


class DataAmendmentCredit(BaseModel):
    id: str

    product: DataAmendmentCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[DataAmendmentCreditAccessSchedule] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    contract: Optional[DataAmendmentCreditContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[DataAmendmentCreditLedger]] = None
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


class DataAmendmentProfessionalService(BaseModel):
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


class DataAmendmentResellerRoyalty(BaseModel):
    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

    aws_account_number: Optional[str] = None

    aws_offer_id: Optional[str] = None

    aws_payer_reference_id: Optional[str] = None

    ending_before: Optional[datetime] = None

    fraction: Optional[float] = None

    gcp_account_id: Optional[str] = None

    gcp_offer_id: Optional[str] = None

    netsuite_reseller_id: Optional[str] = None

    reseller_contract_value: Optional[float] = None

    starting_at: Optional[datetime] = None


class DataAmendment(BaseModel):
    id: str

    commits: List[Commit]

    created_at: datetime

    created_by: str

    overrides: List[Override]

    scheduled_charges: List[ScheduledCharge]

    starting_at: datetime

    credits: Optional[List[DataAmendmentCredit]] = None

    discounts: Optional[List[Discount]] = None
    """This field's availability is dependent on your client's configuration."""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    professional_services: Optional[List[DataAmendmentProfessionalService]] = None
    """This field's availability is dependent on your client's configuration."""

    reseller_royalties: Optional[List[DataAmendmentResellerRoyalty]] = None
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataCustomerBillingProviderConfiguration(BaseModel):
    billing_provider: Literal[
        "aws_marketplace",
        "stripe",
        "netsuite",
        "custom",
        "azure_marketplace",
        "quickbooks_online",
        "workday",
        "gcp_marketplace",
    ]

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]


class Data(BaseModel):
    id: str

    amendments: List[DataAmendment]

    current: ContractWithoutAmendments

    customer_id: str

    initial: ContractWithoutAmendments

    custom_fields: Optional[Dict[str, str]] = None

    customer_billing_provider_configuration: Optional[DataCustomerBillingProviderConfiguration] = None
    """This field's availability is dependent on your client's configuration."""

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class ContractRetrieveResponse(BaseModel):
    data: Data
