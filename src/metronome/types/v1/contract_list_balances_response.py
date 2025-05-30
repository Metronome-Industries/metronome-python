# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ContractListBalancesResponse",
    "Data",
    "DataUnionMember0",
    "DataUnionMember0Product",
    "DataUnionMember0AccessSchedule",
    "DataUnionMember0AccessScheduleScheduleItem",
    "DataUnionMember0AccessScheduleCreditType",
    "DataUnionMember0Contract",
    "DataUnionMember0InvoiceContract",
    "DataUnionMember0InvoiceSchedule",
    "DataUnionMember0InvoiceScheduleCreditType",
    "DataUnionMember0InvoiceScheduleScheduleItem",
    "DataUnionMember0Ledger",
    "DataUnionMember0LedgerUnionMember0",
    "DataUnionMember0LedgerUnionMember1",
    "DataUnionMember0LedgerUnionMember2",
    "DataUnionMember0LedgerUnionMember3",
    "DataUnionMember0LedgerUnionMember4",
    "DataUnionMember0LedgerUnionMember5",
    "DataUnionMember0LedgerUnionMember6",
    "DataUnionMember0LedgerUnionMember7",
    "DataUnionMember0LedgerUnionMember8",
    "DataUnionMember0LedgerUnionMember9",
    "DataUnionMember0LedgerUnionMember10",
    "DataUnionMember0LedgerUnionMember11",
    "DataUnionMember0LedgerUnionMember12",
    "DataUnionMember0RolledOverFrom",
    "DataUnionMember0Specifier",
    "DataUnionMember1",
    "DataUnionMember1Product",
    "DataUnionMember1AccessSchedule",
    "DataUnionMember1AccessScheduleScheduleItem",
    "DataUnionMember1AccessScheduleCreditType",
    "DataUnionMember1Contract",
    "DataUnionMember1Ledger",
    "DataUnionMember1LedgerUnionMember0",
    "DataUnionMember1LedgerUnionMember1",
    "DataUnionMember1LedgerUnionMember2",
    "DataUnionMember1LedgerUnionMember3",
    "DataUnionMember1LedgerUnionMember4",
    "DataUnionMember1LedgerUnionMember5",
    "DataUnionMember1Specifier",
]


class DataUnionMember0Product(BaseModel):
    id: str

    name: str


class DataUnionMember0AccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataUnionMember0AccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataUnionMember0AccessSchedule(BaseModel):
    schedule_items: List[DataUnionMember0AccessScheduleScheduleItem]

    credit_type: Optional[DataUnionMember0AccessScheduleCreditType] = None


class DataUnionMember0Contract(BaseModel):
    id: str


class DataUnionMember0InvoiceContract(BaseModel):
    id: str


class DataUnionMember0InvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class DataUnionMember0InvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataUnionMember0InvoiceSchedule(BaseModel):
    credit_type: Optional[DataUnionMember0InvoiceScheduleCreditType] = None

    schedule_items: Optional[List[DataUnionMember0InvoiceScheduleScheduleItem]] = None


class DataUnionMember0LedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class DataUnionMember0LedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataUnionMember0LedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class DataUnionMember0LedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class DataUnionMember0LedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]


class DataUnionMember0LedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]


class DataUnionMember0LedgerUnionMember6(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class DataUnionMember0LedgerUnionMember7(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataUnionMember0LedgerUnionMember8(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class DataUnionMember0LedgerUnionMember9(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]


class DataUnionMember0LedgerUnionMember10(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class DataUnionMember0LedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class DataUnionMember0LedgerUnionMember12(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


DataUnionMember0Ledger: TypeAlias = Union[
    DataUnionMember0LedgerUnionMember0,
    DataUnionMember0LedgerUnionMember1,
    DataUnionMember0LedgerUnionMember2,
    DataUnionMember0LedgerUnionMember3,
    DataUnionMember0LedgerUnionMember4,
    DataUnionMember0LedgerUnionMember5,
    DataUnionMember0LedgerUnionMember6,
    DataUnionMember0LedgerUnionMember7,
    DataUnionMember0LedgerUnionMember8,
    DataUnionMember0LedgerUnionMember9,
    DataUnionMember0LedgerUnionMember10,
    DataUnionMember0LedgerUnionMember11,
    DataUnionMember0LedgerUnionMember12,
]


class DataUnionMember0RolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class DataUnionMember0Specifier(BaseModel):
    presentation_group_values: Optional[Dict[str, str]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None
    """
    If provided, the specifier will only apply to the product with the specified ID.
    """

    product_tags: Optional[List[str]] = None
    """
    If provided, the specifier will only apply to products with all the specified
    tags.
    """


class DataUnionMember0(BaseModel):
    id: str

    product: DataUnionMember0Product

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[DataUnionMember0AccessSchedule] = None
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

    contract: Optional[DataUnionMember0Contract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    invoice_contract: Optional[DataUnionMember0InvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[DataUnionMember0InvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[DataUnionMember0Ledger]] = None
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

    rolled_over_from: Optional[DataUnionMember0RolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[DataUnionMember0Specifier]] = None
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


class DataUnionMember1Product(BaseModel):
    id: str

    name: str


class DataUnionMember1AccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataUnionMember1AccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataUnionMember1AccessSchedule(BaseModel):
    schedule_items: List[DataUnionMember1AccessScheduleScheduleItem]

    credit_type: Optional[DataUnionMember1AccessScheduleCreditType] = None


class DataUnionMember1Contract(BaseModel):
    id: str


class DataUnionMember1LedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataUnionMember1LedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataUnionMember1LedgerUnionMember2(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataUnionMember1LedgerUnionMember3(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class DataUnionMember1LedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class DataUnionMember1LedgerUnionMember5(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


DataUnionMember1Ledger: TypeAlias = Union[
    DataUnionMember1LedgerUnionMember0,
    DataUnionMember1LedgerUnionMember1,
    DataUnionMember1LedgerUnionMember2,
    DataUnionMember1LedgerUnionMember3,
    DataUnionMember1LedgerUnionMember4,
    DataUnionMember1LedgerUnionMember5,
]


class DataUnionMember1Specifier(BaseModel):
    presentation_group_values: Optional[Dict[str, str]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None
    """
    If provided, the specifier will only apply to the product with the specified ID.
    """

    product_tags: Optional[List[str]] = None
    """
    If provided, the specifier will only apply to products with all the specified
    tags.
    """


class DataUnionMember1(BaseModel):
    id: str

    product: DataUnionMember1Product

    type: Literal["CREDIT"]

    access_schedule: Optional[DataUnionMember1AccessSchedule] = None
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

    contract: Optional[DataUnionMember1Contract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[DataUnionMember1Ledger]] = None
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

    specifiers: Optional[List[DataUnionMember1Specifier]] = None
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


Data: TypeAlias = Union[DataUnionMember0, DataUnionMember1]


class ContractListBalancesResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
