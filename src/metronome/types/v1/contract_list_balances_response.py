# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ContractListBalancesResponse",
    "UnionMember0",
    "UnionMember0Product",
    "UnionMember0AccessSchedule",
    "UnionMember0AccessScheduleScheduleItem",
    "UnionMember0AccessScheduleCreditType",
    "UnionMember0Contract",
    "UnionMember0HierarchyConfiguration",
    "UnionMember0HierarchyConfigurationChildAccess",
    "UnionMember0HierarchyConfigurationChildAccessType",
    "UnionMember0HierarchyConfigurationChildAccessUnionMember2",
    "UnionMember0InvoiceContract",
    "UnionMember0InvoiceSchedule",
    "UnionMember0InvoiceScheduleCreditType",
    "UnionMember0InvoiceScheduleScheduleItem",
    "UnionMember0Ledger",
    "UnionMember0LedgerUnionMember0",
    "UnionMember0LedgerUnionMember1",
    "UnionMember0LedgerUnionMember2",
    "UnionMember0LedgerUnionMember3",
    "UnionMember0LedgerUnionMember4",
    "UnionMember0LedgerUnionMember5",
    "UnionMember0LedgerUnionMember6",
    "UnionMember0LedgerUnionMember7",
    "UnionMember0LedgerUnionMember8",
    "UnionMember0LedgerUnionMember9",
    "UnionMember0LedgerUnionMember10",
    "UnionMember0LedgerUnionMember11",
    "UnionMember0LedgerUnionMember12",
    "UnionMember0LedgerUnionMember13",
    "UnionMember0RolledOverFrom",
    "UnionMember0Specifier",
    "UnionMember1",
    "UnionMember1Product",
    "UnionMember1AccessSchedule",
    "UnionMember1AccessScheduleScheduleItem",
    "UnionMember1AccessScheduleCreditType",
    "UnionMember1Contract",
    "UnionMember1HierarchyConfiguration",
    "UnionMember1HierarchyConfigurationChildAccess",
    "UnionMember1HierarchyConfigurationChildAccessType",
    "UnionMember1HierarchyConfigurationChildAccessUnionMember2",
    "UnionMember1Ledger",
    "UnionMember1LedgerUnionMember0",
    "UnionMember1LedgerUnionMember1",
    "UnionMember1LedgerUnionMember2",
    "UnionMember1LedgerUnionMember3",
    "UnionMember1LedgerUnionMember4",
    "UnionMember1LedgerUnionMember5",
    "UnionMember1LedgerUnionMember6",
    "UnionMember1Specifier",
]


class UnionMember0Product(BaseModel):
    id: str

    name: str


class UnionMember0AccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class UnionMember0AccessScheduleCreditType(BaseModel):
    id: str

    name: str


class UnionMember0AccessSchedule(BaseModel):
    schedule_items: List[UnionMember0AccessScheduleScheduleItem]

    credit_type: Optional[UnionMember0AccessScheduleCreditType] = None


class UnionMember0Contract(BaseModel):
    id: str


class UnionMember0HierarchyConfigurationChildAccessType(BaseModel):
    type: Literal["ALL"]


class UnionMember0HierarchyConfigurationChildAccessUnionMember2(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


UnionMember0HierarchyConfigurationChildAccess: TypeAlias = Union[
    UnionMember0HierarchyConfigurationChildAccessType,
    UnionMember0HierarchyConfigurationChildAccessType,
    UnionMember0HierarchyConfigurationChildAccessUnionMember2,
]


class UnionMember0HierarchyConfiguration(BaseModel):
    child_access: UnionMember0HierarchyConfigurationChildAccess


class UnionMember0InvoiceContract(BaseModel):
    id: str


class UnionMember0InvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class UnionMember0InvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    quantity: float

    timestamp: datetime

    unit_price: float

    invoice_id: Optional[str] = None


class UnionMember0InvoiceSchedule(BaseModel):
    credit_type: Optional[UnionMember0InvoiceScheduleCreditType] = None

    do_not_invoice: Optional[bool] = None
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    schedule_items: Optional[List[UnionMember0InvoiceScheduleScheduleItem]] = None


class UnionMember0LedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class UnionMember0LedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class UnionMember0LedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class UnionMember0LedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class UnionMember0LedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]

    contract_id: Optional[str] = None


class UnionMember0LedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]

    contract_id: Optional[str] = None


class UnionMember0LedgerUnionMember6(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT"]


class UnionMember0LedgerUnionMember7(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class UnionMember0LedgerUnionMember8(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class UnionMember0LedgerUnionMember9(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class UnionMember0LedgerUnionMember10(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]

    contract_id: Optional[str] = None


class UnionMember0LedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class UnionMember0LedgerUnionMember12(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class UnionMember0LedgerUnionMember13(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


UnionMember0Ledger: TypeAlias = Union[
    UnionMember0LedgerUnionMember0,
    UnionMember0LedgerUnionMember1,
    UnionMember0LedgerUnionMember2,
    UnionMember0LedgerUnionMember3,
    UnionMember0LedgerUnionMember4,
    UnionMember0LedgerUnionMember5,
    UnionMember0LedgerUnionMember6,
    UnionMember0LedgerUnionMember7,
    UnionMember0LedgerUnionMember8,
    UnionMember0LedgerUnionMember9,
    UnionMember0LedgerUnionMember10,
    UnionMember0LedgerUnionMember11,
    UnionMember0LedgerUnionMember12,
    UnionMember0LedgerUnionMember13,
]


class UnionMember0RolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class UnionMember0Specifier(BaseModel):
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


class UnionMember0(BaseModel):
    id: str

    product: UnionMember0Product

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[UnionMember0AccessSchedule] = None
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

    contract: Optional[UnionMember0Contract] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    hierarchy_configuration: Optional[UnionMember0HierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

    invoice_contract: Optional[UnionMember0InvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[UnionMember0InvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[UnionMember0Ledger]] = None
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

    rolled_over_from: Optional[UnionMember0RolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[UnionMember0Specifier]] = None
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


class UnionMember1Product(BaseModel):
    id: str

    name: str


class UnionMember1AccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class UnionMember1AccessScheduleCreditType(BaseModel):
    id: str

    name: str


class UnionMember1AccessSchedule(BaseModel):
    schedule_items: List[UnionMember1AccessScheduleScheduleItem]

    credit_type: Optional[UnionMember1AccessScheduleCreditType] = None


class UnionMember1Contract(BaseModel):
    id: str


class UnionMember1HierarchyConfigurationChildAccessType(BaseModel):
    type: Literal["ALL"]


class UnionMember1HierarchyConfigurationChildAccessUnionMember2(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


UnionMember1HierarchyConfigurationChildAccess: TypeAlias = Union[
    UnionMember1HierarchyConfigurationChildAccessType,
    UnionMember1HierarchyConfigurationChildAccessType,
    UnionMember1HierarchyConfigurationChildAccessUnionMember2,
]


class UnionMember1HierarchyConfiguration(BaseModel):
    child_access: UnionMember1HierarchyConfigurationChildAccess


class UnionMember1LedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class UnionMember1LedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class UnionMember1LedgerUnionMember2(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class UnionMember1LedgerUnionMember3(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]

    contract_id: Optional[str] = None


class UnionMember1LedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]

    contract_id: Optional[str] = None


class UnionMember1LedgerUnionMember5(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


class UnionMember1LedgerUnionMember6(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEAT_BASED_ADJUSTMENT"]


UnionMember1Ledger: TypeAlias = Union[
    UnionMember1LedgerUnionMember0,
    UnionMember1LedgerUnionMember1,
    UnionMember1LedgerUnionMember2,
    UnionMember1LedgerUnionMember3,
    UnionMember1LedgerUnionMember4,
    UnionMember1LedgerUnionMember5,
    UnionMember1LedgerUnionMember6,
]


class UnionMember1Specifier(BaseModel):
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


class UnionMember1(BaseModel):
    id: str

    product: UnionMember1Product

    type: Literal["CREDIT"]

    access_schedule: Optional[UnionMember1AccessSchedule] = None
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

    contract: Optional[UnionMember1Contract] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    hierarchy_configuration: Optional[UnionMember1HierarchyConfiguration] = None
    """Optional configuration for credit hierarchy access control"""

    ledger: Optional[List[UnionMember1Ledger]] = None
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

    specifiers: Optional[List[UnionMember1Specifier]] = None
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


ContractListBalancesResponse: TypeAlias = Union[UnionMember0, UnionMember1]
