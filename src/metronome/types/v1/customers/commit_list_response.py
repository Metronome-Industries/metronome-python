# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "CommitListResponse",
    "Product",
    "AccessSchedule",
    "AccessScheduleScheduleItem",
    "AccessScheduleCreditType",
    "Contract",
    "HierarchyConfiguration",
    "HierarchyConfigurationChildAccess",
    "HierarchyConfigurationChildAccessType",
    "HierarchyConfigurationChildAccessUnionMember2",
    "InvoiceContract",
    "InvoiceSchedule",
    "InvoiceScheduleCreditType",
    "InvoiceScheduleScheduleItem",
    "Ledger",
    "LedgerUnionMember0",
    "LedgerUnionMember1",
    "LedgerUnionMember2",
    "LedgerUnionMember3",
    "LedgerUnionMember4",
    "LedgerUnionMember5",
    "LedgerUnionMember6",
    "LedgerUnionMember7",
    "LedgerUnionMember8",
    "LedgerUnionMember9",
    "LedgerUnionMember10",
    "LedgerUnionMember11",
    "LedgerUnionMember12",
    "LedgerUnionMember13",
    "RolledOverFrom",
    "Specifier",
]


class Product(BaseModel):
    id: str

    name: str


class AccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class AccessScheduleCreditType(BaseModel):
    id: str

    name: str


class AccessSchedule(BaseModel):
    schedule_items: List[AccessScheduleScheduleItem]

    credit_type: Optional[AccessScheduleCreditType] = None


class Contract(BaseModel):
    id: str


class HierarchyConfigurationChildAccessType(BaseModel):
    type: Literal["ALL"]


class HierarchyConfigurationChildAccessUnionMember2(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


HierarchyConfigurationChildAccess: TypeAlias = Union[
    HierarchyConfigurationChildAccessType,
    HierarchyConfigurationChildAccessType,
    HierarchyConfigurationChildAccessUnionMember2,
]


class HierarchyConfiguration(BaseModel):
    child_access: HierarchyConfigurationChildAccess


class InvoiceContract(BaseModel):
    id: str


class InvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class InvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    quantity: float

    timestamp: datetime

    unit_price: float

    invoice_id: Optional[str] = None


class InvoiceSchedule(BaseModel):
    credit_type: Optional[InvoiceScheduleCreditType] = None

    do_not_invoice: Optional[bool] = None
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    schedule_items: Optional[List[InvoiceScheduleScheduleItem]] = None


class LedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class LedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class LedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class LedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class LedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]

    contract_id: Optional[str] = None


class LedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]

    contract_id: Optional[str] = None


class LedgerUnionMember6(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT"]


class LedgerUnionMember7(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class LedgerUnionMember8(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class LedgerUnionMember9(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class LedgerUnionMember10(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]

    contract_id: Optional[str] = None


class LedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class LedgerUnionMember12(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class LedgerUnionMember13(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


Ledger: TypeAlias = Union[
    LedgerUnionMember0,
    LedgerUnionMember1,
    LedgerUnionMember2,
    LedgerUnionMember3,
    LedgerUnionMember4,
    LedgerUnionMember5,
    LedgerUnionMember6,
    LedgerUnionMember7,
    LedgerUnionMember8,
    LedgerUnionMember9,
    LedgerUnionMember10,
    LedgerUnionMember11,
    LedgerUnionMember12,
    LedgerUnionMember13,
]


class RolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class Specifier(BaseModel):
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


class CommitListResponse(BaseModel):
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

    hierarchy_configuration: Optional[HierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

    invoice_contract: Optional[InvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[InvoiceSchedule] = None
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

    specifiers: Optional[List[Specifier]] = None
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
