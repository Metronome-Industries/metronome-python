# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "CommitListResponse",
    "Data",
    "DataProduct",
    "DataAccessSchedule",
    "DataAccessScheduleScheduleItem",
    "DataAccessScheduleCreditType",
    "DataContract",
    "DataInvoiceContract",
    "DataInvoiceSchedule",
    "DataInvoiceScheduleCreditType",
    "DataInvoiceScheduleScheduleItem",
    "DataLedger",
    "DataLedgerUnionMember0",
    "DataLedgerUnionMember1",
    "DataLedgerUnionMember2",
    "DataLedgerUnionMember3",
    "DataLedgerUnionMember4",
    "DataLedgerUnionMember5",
    "DataLedgerUnionMember6",
    "DataLedgerUnionMember7",
    "DataLedgerUnionMember8",
    "DataLedgerUnionMember9",
    "DataLedgerUnionMember10",
    "DataLedgerUnionMember11",
    "DataLedgerUnionMember12",
    "DataRolledOverFrom",
    "DataSpecifier",
]


class DataProduct(BaseModel):
    id: str

    name: str


class DataAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataAccessSchedule(BaseModel):
    schedule_items: List[DataAccessScheduleScheduleItem]

    credit_type: Optional[DataAccessScheduleCreditType] = None


class DataContract(BaseModel):
    id: str


class DataInvoiceContract(BaseModel):
    id: str


class DataInvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class DataInvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataInvoiceSchedule(BaseModel):
    credit_type: Optional[DataInvoiceScheduleCreditType] = None

    schedule_items: Optional[List[DataInvoiceScheduleScheduleItem]] = None


class DataLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class DataLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataLedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class DataLedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class DataLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]


class DataLedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]


class DataLedgerUnionMember6(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class DataLedgerUnionMember7(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataLedgerUnionMember8(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class DataLedgerUnionMember9(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]


class DataLedgerUnionMember10(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class DataLedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class DataLedgerUnionMember12(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


DataLedger: TypeAlias = Union[
    DataLedgerUnionMember0,
    DataLedgerUnionMember1,
    DataLedgerUnionMember2,
    DataLedgerUnionMember3,
    DataLedgerUnionMember4,
    DataLedgerUnionMember5,
    DataLedgerUnionMember6,
    DataLedgerUnionMember7,
    DataLedgerUnionMember8,
    DataLedgerUnionMember9,
    DataLedgerUnionMember10,
    DataLedgerUnionMember11,
    DataLedgerUnionMember12,
]


class DataRolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class DataSpecifier(BaseModel):
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


class Data(BaseModel):
    id: str

    product: DataProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[DataAccessSchedule] = None
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

    contract: Optional[DataContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    invoice_contract: Optional[DataInvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[DataInvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[DataLedger]] = None
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

    rolled_over_from: Optional[DataRolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[DataSpecifier]] = None
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


class CommitListResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
