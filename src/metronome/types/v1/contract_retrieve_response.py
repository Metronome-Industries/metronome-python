# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ContractRetrieveResponse",
    "Data",
    "DataAmendment",
    "DataAmendmentCommit",
    "DataAmendmentCommitProduct",
    "DataAmendmentCommitAccessSchedule",
    "DataAmendmentCommitAccessScheduleScheduleItem",
    "DataAmendmentCommitAccessScheduleCreditType",
    "DataAmendmentCommitContract",
    "DataAmendmentCommitInvoiceContract",
    "DataAmendmentCommitInvoiceSchedule",
    "DataAmendmentCommitInvoiceScheduleCreditType",
    "DataAmendmentCommitInvoiceScheduleScheduleItem",
    "DataAmendmentCommitLedger",
    "DataAmendmentCommitLedgerUnionMember0",
    "DataAmendmentCommitLedgerUnionMember1",
    "DataAmendmentCommitLedgerUnionMember2",
    "DataAmendmentCommitLedgerUnionMember3",
    "DataAmendmentCommitLedgerUnionMember4",
    "DataAmendmentCommitLedgerUnionMember5",
    "DataAmendmentCommitLedgerUnionMember6",
    "DataAmendmentCommitLedgerUnionMember7",
    "DataAmendmentCommitLedgerUnionMember8",
    "DataAmendmentCommitLedgerUnionMember9",
    "DataAmendmentCommitLedgerUnionMember10",
    "DataAmendmentCommitLedgerUnionMember11",
    "DataAmendmentCommitLedgerUnionMember12",
    "DataAmendmentCommitRolledOverFrom",
    "DataAmendmentCommitSpecifier",
    "DataAmendmentOverride",
    "DataAmendmentOverrideCreditType",
    "DataAmendmentOverrideOverrideSpecifier",
    "DataAmendmentOverrideOverrideTier",
    "DataAmendmentOverrideOverwriteRate",
    "DataAmendmentOverrideOverwriteRateCreditType",
    "DataAmendmentOverrideOverwriteRateTier",
    "DataAmendmentOverrideProduct",
    "DataAmendmentOverrideTier",
    "DataAmendmentScheduledCharge",
    "DataAmendmentScheduledChargeProduct",
    "DataAmendmentScheduledChargeSchedule",
    "DataAmendmentScheduledChargeScheduleCreditType",
    "DataAmendmentScheduledChargeScheduleScheduleItem",
    "DataAmendmentCredit",
    "DataAmendmentCreditProduct",
    "DataAmendmentCreditAccessSchedule",
    "DataAmendmentCreditAccessScheduleScheduleItem",
    "DataAmendmentCreditAccessScheduleCreditType",
    "DataAmendmentCreditContract",
    "DataAmendmentCreditLedger",
    "DataAmendmentCreditLedgerUnionMember0",
    "DataAmendmentCreditLedgerUnionMember1",
    "DataAmendmentCreditLedgerUnionMember2",
    "DataAmendmentCreditLedgerUnionMember3",
    "DataAmendmentCreditLedgerUnionMember4",
    "DataAmendmentCreditLedgerUnionMember5",
    "DataAmendmentCreditSpecifier",
    "DataAmendmentDiscount",
    "DataAmendmentDiscountProduct",
    "DataAmendmentDiscountSchedule",
    "DataAmendmentDiscountScheduleCreditType",
    "DataAmendmentDiscountScheduleScheduleItem",
    "DataAmendmentProfessionalService",
    "DataAmendmentResellerRoyalty",
    "DataCurrent",
    "DataCurrentCommit",
    "DataCurrentCommitProduct",
    "DataCurrentCommitAccessSchedule",
    "DataCurrentCommitAccessScheduleScheduleItem",
    "DataCurrentCommitAccessScheduleCreditType",
    "DataCurrentCommitContract",
    "DataCurrentCommitInvoiceContract",
    "DataCurrentCommitInvoiceSchedule",
    "DataCurrentCommitInvoiceScheduleCreditType",
    "DataCurrentCommitInvoiceScheduleScheduleItem",
    "DataCurrentCommitLedger",
    "DataCurrentCommitLedgerUnionMember0",
    "DataCurrentCommitLedgerUnionMember1",
    "DataCurrentCommitLedgerUnionMember2",
    "DataCurrentCommitLedgerUnionMember3",
    "DataCurrentCommitLedgerUnionMember4",
    "DataCurrentCommitLedgerUnionMember5",
    "DataCurrentCommitLedgerUnionMember6",
    "DataCurrentCommitLedgerUnionMember7",
    "DataCurrentCommitLedgerUnionMember8",
    "DataCurrentCommitLedgerUnionMember9",
    "DataCurrentCommitLedgerUnionMember10",
    "DataCurrentCommitLedgerUnionMember11",
    "DataCurrentCommitLedgerUnionMember12",
    "DataCurrentCommitRolledOverFrom",
    "DataCurrentCommitSpecifier",
    "DataCurrentOverride",
    "DataCurrentOverrideCreditType",
    "DataCurrentOverrideOverrideSpecifier",
    "DataCurrentOverrideOverrideTier",
    "DataCurrentOverrideOverwriteRate",
    "DataCurrentOverrideOverwriteRateCreditType",
    "DataCurrentOverrideOverwriteRateTier",
    "DataCurrentOverrideProduct",
    "DataCurrentOverrideTier",
    "DataCurrentScheduledCharge",
    "DataCurrentScheduledChargeProduct",
    "DataCurrentScheduledChargeSchedule",
    "DataCurrentScheduledChargeScheduleCreditType",
    "DataCurrentScheduledChargeScheduleScheduleItem",
    "DataCurrentTransition",
    "DataCurrentUsageStatementSchedule",
    "DataCurrentCredit",
    "DataCurrentCreditProduct",
    "DataCurrentCreditAccessSchedule",
    "DataCurrentCreditAccessScheduleScheduleItem",
    "DataCurrentCreditAccessScheduleCreditType",
    "DataCurrentCreditContract",
    "DataCurrentCreditLedger",
    "DataCurrentCreditLedgerUnionMember0",
    "DataCurrentCreditLedgerUnionMember1",
    "DataCurrentCreditLedgerUnionMember2",
    "DataCurrentCreditLedgerUnionMember3",
    "DataCurrentCreditLedgerUnionMember4",
    "DataCurrentCreditLedgerUnionMember5",
    "DataCurrentCreditSpecifier",
    "DataCurrentDiscount",
    "DataCurrentDiscountProduct",
    "DataCurrentDiscountSchedule",
    "DataCurrentDiscountScheduleCreditType",
    "DataCurrentDiscountScheduleScheduleItem",
    "DataCurrentPrepaidBalanceThresholdConfiguration",
    "DataCurrentPrepaidBalanceThresholdConfigurationCommit",
    "DataCurrentPrepaidBalanceThresholdConfigurationCommitSpecifier",
    "DataCurrentPrepaidBalanceThresholdConfigurationPaymentGateConfig",
    "DataCurrentPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataCurrentProfessionalService",
    "DataCurrentRecurringCommit",
    "DataCurrentRecurringCommitAccessAmount",
    "DataCurrentRecurringCommitCommitDuration",
    "DataCurrentRecurringCommitProduct",
    "DataCurrentRecurringCommitContract",
    "DataCurrentRecurringCommitInvoiceAmount",
    "DataCurrentRecurringCommitSpecifier",
    "DataCurrentRecurringCredit",
    "DataCurrentRecurringCreditAccessAmount",
    "DataCurrentRecurringCreditCommitDuration",
    "DataCurrentRecurringCreditProduct",
    "DataCurrentRecurringCreditContract",
    "DataCurrentRecurringCreditSpecifier",
    "DataCurrentResellerRoyalty",
    "DataCurrentSpendThresholdConfiguration",
    "DataCurrentSpendThresholdConfigurationCommit",
    "DataCurrentSpendThresholdConfigurationPaymentGateConfig",
    "DataCurrentSpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataCurrentUsageFilter",
    "DataCurrentUsageFilterCurrent",
    "DataCurrentUsageFilterInitial",
    "DataCurrentUsageFilterUpdate",
    "DataInitial",
    "DataInitialCommit",
    "DataInitialCommitProduct",
    "DataInitialCommitAccessSchedule",
    "DataInitialCommitAccessScheduleScheduleItem",
    "DataInitialCommitAccessScheduleCreditType",
    "DataInitialCommitContract",
    "DataInitialCommitInvoiceContract",
    "DataInitialCommitInvoiceSchedule",
    "DataInitialCommitInvoiceScheduleCreditType",
    "DataInitialCommitInvoiceScheduleScheduleItem",
    "DataInitialCommitLedger",
    "DataInitialCommitLedgerUnionMember0",
    "DataInitialCommitLedgerUnionMember1",
    "DataInitialCommitLedgerUnionMember2",
    "DataInitialCommitLedgerUnionMember3",
    "DataInitialCommitLedgerUnionMember4",
    "DataInitialCommitLedgerUnionMember5",
    "DataInitialCommitLedgerUnionMember6",
    "DataInitialCommitLedgerUnionMember7",
    "DataInitialCommitLedgerUnionMember8",
    "DataInitialCommitLedgerUnionMember9",
    "DataInitialCommitLedgerUnionMember10",
    "DataInitialCommitLedgerUnionMember11",
    "DataInitialCommitLedgerUnionMember12",
    "DataInitialCommitRolledOverFrom",
    "DataInitialCommitSpecifier",
    "DataInitialOverride",
    "DataInitialOverrideCreditType",
    "DataInitialOverrideOverrideSpecifier",
    "DataInitialOverrideOverrideTier",
    "DataInitialOverrideOverwriteRate",
    "DataInitialOverrideOverwriteRateCreditType",
    "DataInitialOverrideOverwriteRateTier",
    "DataInitialOverrideProduct",
    "DataInitialOverrideTier",
    "DataInitialScheduledCharge",
    "DataInitialScheduledChargeProduct",
    "DataInitialScheduledChargeSchedule",
    "DataInitialScheduledChargeScheduleCreditType",
    "DataInitialScheduledChargeScheduleScheduleItem",
    "DataInitialTransition",
    "DataInitialUsageStatementSchedule",
    "DataInitialCredit",
    "DataInitialCreditProduct",
    "DataInitialCreditAccessSchedule",
    "DataInitialCreditAccessScheduleScheduleItem",
    "DataInitialCreditAccessScheduleCreditType",
    "DataInitialCreditContract",
    "DataInitialCreditLedger",
    "DataInitialCreditLedgerUnionMember0",
    "DataInitialCreditLedgerUnionMember1",
    "DataInitialCreditLedgerUnionMember2",
    "DataInitialCreditLedgerUnionMember3",
    "DataInitialCreditLedgerUnionMember4",
    "DataInitialCreditLedgerUnionMember5",
    "DataInitialCreditSpecifier",
    "DataInitialDiscount",
    "DataInitialDiscountProduct",
    "DataInitialDiscountSchedule",
    "DataInitialDiscountScheduleCreditType",
    "DataInitialDiscountScheduleScheduleItem",
    "DataInitialPrepaidBalanceThresholdConfiguration",
    "DataInitialPrepaidBalanceThresholdConfigurationCommit",
    "DataInitialPrepaidBalanceThresholdConfigurationCommitSpecifier",
    "DataInitialPrepaidBalanceThresholdConfigurationPaymentGateConfig",
    "DataInitialPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataInitialProfessionalService",
    "DataInitialRecurringCommit",
    "DataInitialRecurringCommitAccessAmount",
    "DataInitialRecurringCommitCommitDuration",
    "DataInitialRecurringCommitProduct",
    "DataInitialRecurringCommitContract",
    "DataInitialRecurringCommitInvoiceAmount",
    "DataInitialRecurringCommitSpecifier",
    "DataInitialRecurringCredit",
    "DataInitialRecurringCreditAccessAmount",
    "DataInitialRecurringCreditCommitDuration",
    "DataInitialRecurringCreditProduct",
    "DataInitialRecurringCreditContract",
    "DataInitialRecurringCreditSpecifier",
    "DataInitialResellerRoyalty",
    "DataInitialSpendThresholdConfiguration",
    "DataInitialSpendThresholdConfigurationCommit",
    "DataInitialSpendThresholdConfigurationPaymentGateConfig",
    "DataInitialSpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataInitialUsageFilter",
    "DataInitialUsageFilterCurrent",
    "DataInitialUsageFilterInitial",
    "DataInitialUsageFilterUpdate",
    "DataCustomerBillingProviderConfiguration",
    "DataPrepaidBalanceThresholdConfiguration",
    "DataPrepaidBalanceThresholdConfigurationCommit",
    "DataPrepaidBalanceThresholdConfigurationCommitSpecifier",
    "DataPrepaidBalanceThresholdConfigurationPaymentGateConfig",
    "DataPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataSpendThresholdConfiguration",
    "DataSpendThresholdConfigurationCommit",
    "DataSpendThresholdConfigurationPaymentGateConfig",
    "DataSpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataSubscription",
    "DataSubscriptionProration",
    "DataSubscriptionQuantitySchedule",
    "DataSubscriptionSubscriptionRate",
    "DataSubscriptionSubscriptionRateProduct",
]


class DataAmendmentCommitProduct(BaseModel):
    id: str

    name: str


class DataAmendmentCommitAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataAmendmentCommitAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataAmendmentCommitAccessSchedule(BaseModel):
    schedule_items: List[DataAmendmentCommitAccessScheduleScheduleItem]

    credit_type: Optional[DataAmendmentCommitAccessScheduleCreditType] = None


class DataAmendmentCommitContract(BaseModel):
    id: str


class DataAmendmentCommitInvoiceContract(BaseModel):
    id: str


class DataAmendmentCommitInvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class DataAmendmentCommitInvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataAmendmentCommitInvoiceSchedule(BaseModel):
    credit_type: Optional[DataAmendmentCommitInvoiceScheduleCreditType] = None

    schedule_items: Optional[List[DataAmendmentCommitInvoiceScheduleScheduleItem]] = None


class DataAmendmentCommitLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class DataAmendmentCommitLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataAmendmentCommitLedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class DataAmendmentCommitLedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class DataAmendmentCommitLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]


class DataAmendmentCommitLedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]


class DataAmendmentCommitLedgerUnionMember6(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class DataAmendmentCommitLedgerUnionMember7(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataAmendmentCommitLedgerUnionMember8(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class DataAmendmentCommitLedgerUnionMember9(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]


class DataAmendmentCommitLedgerUnionMember10(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class DataAmendmentCommitLedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class DataAmendmentCommitLedgerUnionMember12(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


DataAmendmentCommitLedger: TypeAlias = Union[
    DataAmendmentCommitLedgerUnionMember0,
    DataAmendmentCommitLedgerUnionMember1,
    DataAmendmentCommitLedgerUnionMember2,
    DataAmendmentCommitLedgerUnionMember3,
    DataAmendmentCommitLedgerUnionMember4,
    DataAmendmentCommitLedgerUnionMember5,
    DataAmendmentCommitLedgerUnionMember6,
    DataAmendmentCommitLedgerUnionMember7,
    DataAmendmentCommitLedgerUnionMember8,
    DataAmendmentCommitLedgerUnionMember9,
    DataAmendmentCommitLedgerUnionMember10,
    DataAmendmentCommitLedgerUnionMember11,
    DataAmendmentCommitLedgerUnionMember12,
]


class DataAmendmentCommitRolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class DataAmendmentCommitSpecifier(BaseModel):
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


class DataAmendmentCommit(BaseModel):
    id: str

    product: DataAmendmentCommitProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[DataAmendmentCommitAccessSchedule] = None
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

    contract: Optional[DataAmendmentCommitContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    invoice_contract: Optional[DataAmendmentCommitInvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[DataAmendmentCommitInvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[DataAmendmentCommitLedger]] = None
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

    rolled_over_from: Optional[DataAmendmentCommitRolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[DataAmendmentCommitSpecifier]] = None
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


class DataAmendmentOverrideCreditType(BaseModel):
    id: str

    name: str


class DataAmendmentOverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None

    recurring_credit_ids: Optional[List[str]] = None


class DataAmendmentOverrideOverrideTier(BaseModel):
    multiplier: float

    size: Optional[float] = None


class DataAmendmentOverrideOverwriteRateCreditType(BaseModel):
    id: str

    name: str


class DataAmendmentOverrideOverwriteRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataAmendmentOverrideOverwriteRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    credit_type: Optional[DataAmendmentOverrideOverwriteRateCreditType] = None

    custom_rate: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Optional[List[DataAmendmentOverrideOverwriteRateTier]] = None
    """Only set for TIERED rate_type."""


class DataAmendmentOverrideProduct(BaseModel):
    id: str

    name: str


class DataAmendmentOverrideTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataAmendmentOverride(BaseModel):
    id: str

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    credit_type: Optional[DataAmendmentOverrideCreditType] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[DataAmendmentOverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[DataAmendmentOverrideOverrideTier]] = None

    overwrite_rate: Optional[DataAmendmentOverrideOverwriteRate] = None

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    priority: Optional[float] = None

    product: Optional[DataAmendmentOverrideProduct] = None

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    rate_type: Optional[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    tiers: Optional[List[DataAmendmentOverrideTier]] = None
    """Only set for TIERED rate_type."""

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None

    value: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """


class DataAmendmentScheduledChargeProduct(BaseModel):
    id: str

    name: str


class DataAmendmentScheduledChargeScheduleCreditType(BaseModel):
    id: str

    name: str


class DataAmendmentScheduledChargeScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataAmendmentScheduledChargeSchedule(BaseModel):
    credit_type: Optional[DataAmendmentScheduledChargeScheduleCreditType] = None

    schedule_items: Optional[List[DataAmendmentScheduledChargeScheduleScheduleItem]] = None


class DataAmendmentScheduledCharge(BaseModel):
    id: str

    product: DataAmendmentScheduledChargeProduct

    schedule: DataAmendmentScheduledChargeSchedule

    archived_at: Optional[datetime] = None

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None
    """displayed on invoices"""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataAmendmentCreditProduct(BaseModel):
    id: str

    name: str


class DataAmendmentCreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataAmendmentCreditAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataAmendmentCreditAccessSchedule(BaseModel):
    schedule_items: List[DataAmendmentCreditAccessScheduleScheduleItem]

    credit_type: Optional[DataAmendmentCreditAccessScheduleCreditType] = None


class DataAmendmentCreditContract(BaseModel):
    id: str


class DataAmendmentCreditLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataAmendmentCreditLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataAmendmentCreditLedgerUnionMember2(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataAmendmentCreditLedgerUnionMember3(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class DataAmendmentCreditLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class DataAmendmentCreditLedgerUnionMember5(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


DataAmendmentCreditLedger: TypeAlias = Union[
    DataAmendmentCreditLedgerUnionMember0,
    DataAmendmentCreditLedgerUnionMember1,
    DataAmendmentCreditLedgerUnionMember2,
    DataAmendmentCreditLedgerUnionMember3,
    DataAmendmentCreditLedgerUnionMember4,
    DataAmendmentCreditLedgerUnionMember5,
]


class DataAmendmentCreditSpecifier(BaseModel):
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


class DataAmendmentCredit(BaseModel):
    id: str

    product: DataAmendmentCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[DataAmendmentCreditAccessSchedule] = None
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

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[DataAmendmentCreditSpecifier]] = None
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


class DataAmendmentDiscountProduct(BaseModel):
    id: str

    name: str


class DataAmendmentDiscountScheduleCreditType(BaseModel):
    id: str

    name: str


class DataAmendmentDiscountScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataAmendmentDiscountSchedule(BaseModel):
    credit_type: Optional[DataAmendmentDiscountScheduleCreditType] = None

    schedule_items: Optional[List[DataAmendmentDiscountScheduleScheduleItem]] = None


class DataAmendmentDiscount(BaseModel):
    id: str

    product: DataAmendmentDiscountProduct

    schedule: DataAmendmentDiscountSchedule

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
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

    commits: List[DataAmendmentCommit]

    created_at: datetime

    created_by: str

    overrides: List[DataAmendmentOverride]

    scheduled_charges: List[DataAmendmentScheduledCharge]

    starting_at: datetime

    credits: Optional[List[DataAmendmentCredit]] = None

    discounts: Optional[List[DataAmendmentDiscount]] = None
    """This field's availability is dependent on your client's configuration."""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    professional_services: Optional[List[DataAmendmentProfessionalService]] = None
    """This field's availability is dependent on your client's configuration."""

    reseller_royalties: Optional[List[DataAmendmentResellerRoyalty]] = None
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataCurrentCommitProduct(BaseModel):
    id: str

    name: str


class DataCurrentCommitAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataCurrentCommitAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCurrentCommitAccessSchedule(BaseModel):
    schedule_items: List[DataCurrentCommitAccessScheduleScheduleItem]

    credit_type: Optional[DataCurrentCommitAccessScheduleCreditType] = None


class DataCurrentCommitContract(BaseModel):
    id: str


class DataCurrentCommitInvoiceContract(BaseModel):
    id: str


class DataCurrentCommitInvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCurrentCommitInvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataCurrentCommitInvoiceSchedule(BaseModel):
    credit_type: Optional[DataCurrentCommitInvoiceScheduleCreditType] = None

    schedule_items: Optional[List[DataCurrentCommitInvoiceScheduleScheduleItem]] = None


class DataCurrentCommitLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class DataCurrentCommitLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataCurrentCommitLedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class DataCurrentCommitLedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class DataCurrentCommitLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]


class DataCurrentCommitLedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]


class DataCurrentCommitLedgerUnionMember6(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class DataCurrentCommitLedgerUnionMember7(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataCurrentCommitLedgerUnionMember8(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class DataCurrentCommitLedgerUnionMember9(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]


class DataCurrentCommitLedgerUnionMember10(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class DataCurrentCommitLedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class DataCurrentCommitLedgerUnionMember12(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


DataCurrentCommitLedger: TypeAlias = Union[
    DataCurrentCommitLedgerUnionMember0,
    DataCurrentCommitLedgerUnionMember1,
    DataCurrentCommitLedgerUnionMember2,
    DataCurrentCommitLedgerUnionMember3,
    DataCurrentCommitLedgerUnionMember4,
    DataCurrentCommitLedgerUnionMember5,
    DataCurrentCommitLedgerUnionMember6,
    DataCurrentCommitLedgerUnionMember7,
    DataCurrentCommitLedgerUnionMember8,
    DataCurrentCommitLedgerUnionMember9,
    DataCurrentCommitLedgerUnionMember10,
    DataCurrentCommitLedgerUnionMember11,
    DataCurrentCommitLedgerUnionMember12,
]


class DataCurrentCommitRolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class DataCurrentCommitSpecifier(BaseModel):
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


class DataCurrentCommit(BaseModel):
    id: str

    product: DataCurrentCommitProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[DataCurrentCommitAccessSchedule] = None
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

    contract: Optional[DataCurrentCommitContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    invoice_contract: Optional[DataCurrentCommitInvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[DataCurrentCommitInvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[DataCurrentCommitLedger]] = None
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

    rolled_over_from: Optional[DataCurrentCommitRolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[DataCurrentCommitSpecifier]] = None
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


class DataCurrentOverrideCreditType(BaseModel):
    id: str

    name: str


class DataCurrentOverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None

    recurring_credit_ids: Optional[List[str]] = None


class DataCurrentOverrideOverrideTier(BaseModel):
    multiplier: float

    size: Optional[float] = None


class DataCurrentOverrideOverwriteRateCreditType(BaseModel):
    id: str

    name: str


class DataCurrentOverrideOverwriteRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataCurrentOverrideOverwriteRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    credit_type: Optional[DataCurrentOverrideOverwriteRateCreditType] = None

    custom_rate: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Optional[List[DataCurrentOverrideOverwriteRateTier]] = None
    """Only set for TIERED rate_type."""


class DataCurrentOverrideProduct(BaseModel):
    id: str

    name: str


class DataCurrentOverrideTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataCurrentOverride(BaseModel):
    id: str

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    credit_type: Optional[DataCurrentOverrideCreditType] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[DataCurrentOverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[DataCurrentOverrideOverrideTier]] = None

    overwrite_rate: Optional[DataCurrentOverrideOverwriteRate] = None

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    priority: Optional[float] = None

    product: Optional[DataCurrentOverrideProduct] = None

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    rate_type: Optional[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    tiers: Optional[List[DataCurrentOverrideTier]] = None
    """Only set for TIERED rate_type."""

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None

    value: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """


class DataCurrentScheduledChargeProduct(BaseModel):
    id: str

    name: str


class DataCurrentScheduledChargeScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCurrentScheduledChargeScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataCurrentScheduledChargeSchedule(BaseModel):
    credit_type: Optional[DataCurrentScheduledChargeScheduleCreditType] = None

    schedule_items: Optional[List[DataCurrentScheduledChargeScheduleScheduleItem]] = None


class DataCurrentScheduledCharge(BaseModel):
    id: str

    product: DataCurrentScheduledChargeProduct

    schedule: DataCurrentScheduledChargeSchedule

    archived_at: Optional[datetime] = None

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None
    """displayed on invoices"""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataCurrentTransition(BaseModel):
    from_contract_id: str

    to_contract_id: str

    type: Literal["SUPERSEDE", "RENEWAL"]


class DataCurrentUsageStatementSchedule(BaseModel):
    billing_anchor_date: datetime
    """Contract usage statements follow a selected cadence based on this date."""

    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]


class DataCurrentCreditProduct(BaseModel):
    id: str

    name: str


class DataCurrentCreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataCurrentCreditAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCurrentCreditAccessSchedule(BaseModel):
    schedule_items: List[DataCurrentCreditAccessScheduleScheduleItem]

    credit_type: Optional[DataCurrentCreditAccessScheduleCreditType] = None


class DataCurrentCreditContract(BaseModel):
    id: str


class DataCurrentCreditLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataCurrentCreditLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataCurrentCreditLedgerUnionMember2(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataCurrentCreditLedgerUnionMember3(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class DataCurrentCreditLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class DataCurrentCreditLedgerUnionMember5(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


DataCurrentCreditLedger: TypeAlias = Union[
    DataCurrentCreditLedgerUnionMember0,
    DataCurrentCreditLedgerUnionMember1,
    DataCurrentCreditLedgerUnionMember2,
    DataCurrentCreditLedgerUnionMember3,
    DataCurrentCreditLedgerUnionMember4,
    DataCurrentCreditLedgerUnionMember5,
]


class DataCurrentCreditSpecifier(BaseModel):
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


class DataCurrentCredit(BaseModel):
    id: str

    product: DataCurrentCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[DataCurrentCreditAccessSchedule] = None
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

    contract: Optional[DataCurrentCreditContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[DataCurrentCreditLedger]] = None
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

    specifiers: Optional[List[DataCurrentCreditSpecifier]] = None
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


class DataCurrentDiscountProduct(BaseModel):
    id: str

    name: str


class DataCurrentDiscountScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCurrentDiscountScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataCurrentDiscountSchedule(BaseModel):
    credit_type: Optional[DataCurrentDiscountScheduleCreditType] = None

    schedule_items: Optional[List[DataCurrentDiscountScheduleScheduleItem]] = None


class DataCurrentDiscount(BaseModel):
    id: str

    product: DataCurrentDiscountProduct

    schedule: DataCurrentDiscountSchedule

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataCurrentPrepaidBalanceThresholdConfigurationCommitSpecifier(BaseModel):
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


class DataCurrentPrepaidBalanceThresholdConfigurationCommit(BaseModel):
    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """

    applicable_product_ids: Optional[List[str]] = None
    """Which products the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """

    specifiers: Optional[List[DataCurrentPrepaidBalanceThresholdConfigurationCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """


class DataCurrentPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""


class DataCurrentPrepaidBalanceThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    stripe_config: Optional[DataCurrentPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using Stripe as your payment gateway through Metronome."""

    tax_type: Optional[Literal["NONE", "STRIPE"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataCurrentPrepaidBalanceThresholdConfiguration(BaseModel):
    commit: DataCurrentPrepaidBalanceThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataCurrentPrepaidBalanceThresholdConfigurationPaymentGateConfig

    recharge_to_amount: float
    """Specify the amount the balance should be recharged to."""

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's prepaid balance lowers to this amount, a threshold
    charge will be initiated.
    """


class DataCurrentProfessionalService(BaseModel):
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


class DataCurrentRecurringCommitAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataCurrentRecurringCommitCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataCurrentRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataCurrentRecurringCommitContract(BaseModel):
    id: str


class DataCurrentRecurringCommitInvoiceAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataCurrentRecurringCommitSpecifier(BaseModel):
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


class DataCurrentRecurringCommit(BaseModel):
    id: str

    access_amount: DataCurrentRecurringCommitAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataCurrentRecurringCommitCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataCurrentRecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataCurrentRecurringCommitContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    invoice_amount: Optional[DataCurrentRecurringCommitInvoiceAmount] = None
    """The amount the customer should be billed for the commit. Not required."""

    name: Optional[str] = None
    """Displayed on invoices. Will be passed through to the individual commits"""

    netsuite_sales_order_id: Optional[str] = None
    """Will be passed down to the individual commits"""

    proration: Optional[Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]] = None
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates.
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Optional[List[DataCurrentRecurringCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataCurrentRecurringCreditAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataCurrentRecurringCreditCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataCurrentRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataCurrentRecurringCreditContract(BaseModel):
    id: str


class DataCurrentRecurringCreditSpecifier(BaseModel):
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


class DataCurrentRecurringCredit(BaseModel):
    id: str

    access_amount: DataCurrentRecurringCreditAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataCurrentRecurringCreditCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataCurrentRecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataCurrentRecurringCreditContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    name: Optional[str] = None
    """Displayed on invoices. Will be passed through to the individual commits"""

    netsuite_sales_order_id: Optional[str] = None
    """Will be passed down to the individual commits"""

    proration: Optional[Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]] = None
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates.
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Optional[List[DataCurrentRecurringCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataCurrentResellerRoyalty(BaseModel):
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


class DataCurrentSpendThresholdConfigurationCommit(BaseModel):
    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """

    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """


class DataCurrentSpendThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""


class DataCurrentSpendThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    stripe_config: Optional[DataCurrentSpendThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using Stripe as your payment gateway through Metronome."""

    tax_type: Optional[Literal["NONE", "STRIPE"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataCurrentSpendThresholdConfiguration(BaseModel):
    commit: DataCurrentSpendThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataCurrentSpendThresholdConfigurationPaymentGateConfig

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class DataCurrentUsageFilterCurrent(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: Optional[datetime] = None


class DataCurrentUsageFilterInitial(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: Optional[datetime] = None


class DataCurrentUsageFilterUpdate(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: datetime


class DataCurrentUsageFilter(BaseModel):
    current: Optional[DataCurrentUsageFilterCurrent] = None

    initial: DataCurrentUsageFilterInitial

    updates: List[DataCurrentUsageFilterUpdate]


class DataCurrent(BaseModel):
    commits: List[DataCurrentCommit]

    created_at: datetime

    created_by: str

    overrides: List[DataCurrentOverride]

    scheduled_charges: List[DataCurrentScheduledCharge]

    starting_at: datetime

    transitions: List[DataCurrentTransition]

    usage_statement_schedule: DataCurrentUsageStatementSchedule

    credits: Optional[List[DataCurrentCredit]] = None

    discounts: Optional[List[DataCurrentDiscount]] = None
    """This field's availability is dependent on your client's configuration."""

    ending_before: Optional[datetime] = None

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    prepaid_balance_threshold_configuration: Optional[DataCurrentPrepaidBalanceThresholdConfiguration] = None

    professional_services: Optional[List[DataCurrentProfessionalService]] = None
    """This field's availability is dependent on your client's configuration."""

    rate_card_id: Optional[str] = None

    recurring_commits: Optional[List[DataCurrentRecurringCommit]] = None

    recurring_credits: Optional[List[DataCurrentRecurringCredit]] = None

    reseller_royalties: Optional[List[DataCurrentResellerRoyalty]] = None
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    scheduled_charges_on_usage_invoices: Optional[Literal["ALL"]] = None
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    spend_threshold_configuration: Optional[DataCurrentSpendThresholdConfiguration] = None

    total_contract_value: Optional[float] = None
    """This field's availability is dependent on your client's configuration."""

    usage_filter: Optional[DataCurrentUsageFilter] = None


class DataInitialCommitProduct(BaseModel):
    id: str

    name: str


class DataInitialCommitAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataInitialCommitAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataInitialCommitAccessSchedule(BaseModel):
    schedule_items: List[DataInitialCommitAccessScheduleScheduleItem]

    credit_type: Optional[DataInitialCommitAccessScheduleCreditType] = None


class DataInitialCommitContract(BaseModel):
    id: str


class DataInitialCommitInvoiceContract(BaseModel):
    id: str


class DataInitialCommitInvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class DataInitialCommitInvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataInitialCommitInvoiceSchedule(BaseModel):
    credit_type: Optional[DataInitialCommitInvoiceScheduleCreditType] = None

    schedule_items: Optional[List[DataInitialCommitInvoiceScheduleScheduleItem]] = None


class DataInitialCommitLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class DataInitialCommitLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataInitialCommitLedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class DataInitialCommitLedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class DataInitialCommitLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]


class DataInitialCommitLedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]


class DataInitialCommitLedgerUnionMember6(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class DataInitialCommitLedgerUnionMember7(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataInitialCommitLedgerUnionMember8(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class DataInitialCommitLedgerUnionMember9(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]


class DataInitialCommitLedgerUnionMember10(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class DataInitialCommitLedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class DataInitialCommitLedgerUnionMember12(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


DataInitialCommitLedger: TypeAlias = Union[
    DataInitialCommitLedgerUnionMember0,
    DataInitialCommitLedgerUnionMember1,
    DataInitialCommitLedgerUnionMember2,
    DataInitialCommitLedgerUnionMember3,
    DataInitialCommitLedgerUnionMember4,
    DataInitialCommitLedgerUnionMember5,
    DataInitialCommitLedgerUnionMember6,
    DataInitialCommitLedgerUnionMember7,
    DataInitialCommitLedgerUnionMember8,
    DataInitialCommitLedgerUnionMember9,
    DataInitialCommitLedgerUnionMember10,
    DataInitialCommitLedgerUnionMember11,
    DataInitialCommitLedgerUnionMember12,
]


class DataInitialCommitRolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class DataInitialCommitSpecifier(BaseModel):
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


class DataInitialCommit(BaseModel):
    id: str

    product: DataInitialCommitProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[DataInitialCommitAccessSchedule] = None
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

    contract: Optional[DataInitialCommitContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    invoice_contract: Optional[DataInitialCommitInvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[DataInitialCommitInvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[DataInitialCommitLedger]] = None
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

    rolled_over_from: Optional[DataInitialCommitRolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[DataInitialCommitSpecifier]] = None
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


class DataInitialOverrideCreditType(BaseModel):
    id: str

    name: str


class DataInitialOverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None

    recurring_credit_ids: Optional[List[str]] = None


class DataInitialOverrideOverrideTier(BaseModel):
    multiplier: float

    size: Optional[float] = None


class DataInitialOverrideOverwriteRateCreditType(BaseModel):
    id: str

    name: str


class DataInitialOverrideOverwriteRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataInitialOverrideOverwriteRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    credit_type: Optional[DataInitialOverrideOverwriteRateCreditType] = None

    custom_rate: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Optional[List[DataInitialOverrideOverwriteRateTier]] = None
    """Only set for TIERED rate_type."""


class DataInitialOverrideProduct(BaseModel):
    id: str

    name: str


class DataInitialOverrideTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataInitialOverride(BaseModel):
    id: str

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    credit_type: Optional[DataInitialOverrideCreditType] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    is_prorated: Optional[bool] = None
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[DataInitialOverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[DataInitialOverrideOverrideTier]] = None

    overwrite_rate: Optional[DataInitialOverrideOverwriteRate] = None

    price: Optional[float] = None
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    priority: Optional[float] = None

    product: Optional[DataInitialOverrideProduct] = None

    quantity: Optional[float] = None
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    rate_type: Optional[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    tiers: Optional[List[DataInitialOverrideTier]] = None
    """Only set for TIERED rate_type."""

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None

    value: Optional[Dict[str, object]] = None
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """


class DataInitialScheduledChargeProduct(BaseModel):
    id: str

    name: str


class DataInitialScheduledChargeScheduleCreditType(BaseModel):
    id: str

    name: str


class DataInitialScheduledChargeScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataInitialScheduledChargeSchedule(BaseModel):
    credit_type: Optional[DataInitialScheduledChargeScheduleCreditType] = None

    schedule_items: Optional[List[DataInitialScheduledChargeScheduleScheduleItem]] = None


class DataInitialScheduledCharge(BaseModel):
    id: str

    product: DataInitialScheduledChargeProduct

    schedule: DataInitialScheduledChargeSchedule

    archived_at: Optional[datetime] = None

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None
    """displayed on invoices"""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataInitialTransition(BaseModel):
    from_contract_id: str

    to_contract_id: str

    type: Literal["SUPERSEDE", "RENEWAL"]


class DataInitialUsageStatementSchedule(BaseModel):
    billing_anchor_date: datetime
    """Contract usage statements follow a selected cadence based on this date."""

    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]


class DataInitialCreditProduct(BaseModel):
    id: str

    name: str


class DataInitialCreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataInitialCreditAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataInitialCreditAccessSchedule(BaseModel):
    schedule_items: List[DataInitialCreditAccessScheduleScheduleItem]

    credit_type: Optional[DataInitialCreditAccessScheduleCreditType] = None


class DataInitialCreditContract(BaseModel):
    id: str


class DataInitialCreditLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataInitialCreditLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]


class DataInitialCreditLedgerUnionMember2(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataInitialCreditLedgerUnionMember3(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]


class DataInitialCreditLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]


class DataInitialCreditLedgerUnionMember5(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


DataInitialCreditLedger: TypeAlias = Union[
    DataInitialCreditLedgerUnionMember0,
    DataInitialCreditLedgerUnionMember1,
    DataInitialCreditLedgerUnionMember2,
    DataInitialCreditLedgerUnionMember3,
    DataInitialCreditLedgerUnionMember4,
    DataInitialCreditLedgerUnionMember5,
]


class DataInitialCreditSpecifier(BaseModel):
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


class DataInitialCredit(BaseModel):
    id: str

    product: DataInitialCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[DataInitialCreditAccessSchedule] = None
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

    contract: Optional[DataInitialCreditContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ledger: Optional[List[DataInitialCreditLedger]] = None
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

    specifiers: Optional[List[DataInitialCreditSpecifier]] = None
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


class DataInitialDiscountProduct(BaseModel):
    id: str

    name: str


class DataInitialDiscountScheduleCreditType(BaseModel):
    id: str

    name: str


class DataInitialDiscountScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    invoice_id: str

    quantity: float

    timestamp: datetime

    unit_price: float


class DataInitialDiscountSchedule(BaseModel):
    credit_type: Optional[DataInitialDiscountScheduleCreditType] = None

    schedule_items: Optional[List[DataInitialDiscountScheduleScheduleItem]] = None


class DataInitialDiscount(BaseModel):
    id: str

    product: DataInitialDiscountProduct

    schedule: DataInitialDiscountSchedule

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataInitialPrepaidBalanceThresholdConfigurationCommitSpecifier(BaseModel):
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


class DataInitialPrepaidBalanceThresholdConfigurationCommit(BaseModel):
    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """

    applicable_product_ids: Optional[List[str]] = None
    """Which products the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """

    specifiers: Optional[List[DataInitialPrepaidBalanceThresholdConfigurationCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """


class DataInitialPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""


class DataInitialPrepaidBalanceThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    stripe_config: Optional[DataInitialPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using Stripe as your payment gateway through Metronome."""

    tax_type: Optional[Literal["NONE", "STRIPE"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataInitialPrepaidBalanceThresholdConfiguration(BaseModel):
    commit: DataInitialPrepaidBalanceThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataInitialPrepaidBalanceThresholdConfigurationPaymentGateConfig

    recharge_to_amount: float
    """Specify the amount the balance should be recharged to."""

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's prepaid balance lowers to this amount, a threshold
    charge will be initiated.
    """


class DataInitialProfessionalService(BaseModel):
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


class DataInitialRecurringCommitAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataInitialRecurringCommitCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataInitialRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataInitialRecurringCommitContract(BaseModel):
    id: str


class DataInitialRecurringCommitInvoiceAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataInitialRecurringCommitSpecifier(BaseModel):
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


class DataInitialRecurringCommit(BaseModel):
    id: str

    access_amount: DataInitialRecurringCommitAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataInitialRecurringCommitCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataInitialRecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataInitialRecurringCommitContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    invoice_amount: Optional[DataInitialRecurringCommitInvoiceAmount] = None
    """The amount the customer should be billed for the commit. Not required."""

    name: Optional[str] = None
    """Displayed on invoices. Will be passed through to the individual commits"""

    netsuite_sales_order_id: Optional[str] = None
    """Will be passed down to the individual commits"""

    proration: Optional[Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]] = None
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates.
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Optional[List[DataInitialRecurringCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataInitialRecurringCreditAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataInitialRecurringCreditCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataInitialRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataInitialRecurringCreditContract(BaseModel):
    id: str


class DataInitialRecurringCreditSpecifier(BaseModel):
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


class DataInitialRecurringCredit(BaseModel):
    id: str

    access_amount: DataInitialRecurringCreditAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataInitialRecurringCreditCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataInitialRecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataInitialRecurringCreditContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    name: Optional[str] = None
    """Displayed on invoices. Will be passed through to the individual commits"""

    netsuite_sales_order_id: Optional[str] = None
    """Will be passed down to the individual commits"""

    proration: Optional[Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]] = None
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates.
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Optional[List[DataInitialRecurringCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataInitialResellerRoyalty(BaseModel):
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


class DataInitialSpendThresholdConfigurationCommit(BaseModel):
    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """

    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """


class DataInitialSpendThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""


class DataInitialSpendThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    stripe_config: Optional[DataInitialSpendThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using Stripe as your payment gateway through Metronome."""

    tax_type: Optional[Literal["NONE", "STRIPE"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataInitialSpendThresholdConfiguration(BaseModel):
    commit: DataInitialSpendThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataInitialSpendThresholdConfigurationPaymentGateConfig

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class DataInitialUsageFilterCurrent(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: Optional[datetime] = None


class DataInitialUsageFilterInitial(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: Optional[datetime] = None


class DataInitialUsageFilterUpdate(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: datetime


class DataInitialUsageFilter(BaseModel):
    current: Optional[DataInitialUsageFilterCurrent] = None

    initial: DataInitialUsageFilterInitial

    updates: List[DataInitialUsageFilterUpdate]


class DataInitial(BaseModel):
    commits: List[DataInitialCommit]

    created_at: datetime

    created_by: str

    overrides: List[DataInitialOverride]

    scheduled_charges: List[DataInitialScheduledCharge]

    starting_at: datetime

    transitions: List[DataInitialTransition]

    usage_statement_schedule: DataInitialUsageStatementSchedule

    credits: Optional[List[DataInitialCredit]] = None

    discounts: Optional[List[DataInitialDiscount]] = None
    """This field's availability is dependent on your client's configuration."""

    ending_before: Optional[datetime] = None

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    prepaid_balance_threshold_configuration: Optional[DataInitialPrepaidBalanceThresholdConfiguration] = None

    professional_services: Optional[List[DataInitialProfessionalService]] = None
    """This field's availability is dependent on your client's configuration."""

    rate_card_id: Optional[str] = None

    recurring_commits: Optional[List[DataInitialRecurringCommit]] = None

    recurring_credits: Optional[List[DataInitialRecurringCredit]] = None

    reseller_royalties: Optional[List[DataInitialResellerRoyalty]] = None
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    scheduled_charges_on_usage_invoices: Optional[Literal["ALL"]] = None
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    spend_threshold_configuration: Optional[DataInitialSpendThresholdConfiguration] = None

    total_contract_value: Optional[float] = None
    """This field's availability is dependent on your client's configuration."""

    usage_filter: Optional[DataInitialUsageFilter] = None


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

    id: Optional[str] = None

    configuration: Optional[Dict[str, object]] = None
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider.
    """


class DataPrepaidBalanceThresholdConfigurationCommitSpecifier(BaseModel):
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


class DataPrepaidBalanceThresholdConfigurationCommit(BaseModel):
    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """

    applicable_product_ids: Optional[List[str]] = None
    """Which products the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """

    specifiers: Optional[List[DataPrepaidBalanceThresholdConfigurationCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """


class DataPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""


class DataPrepaidBalanceThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    stripe_config: Optional[DataPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using Stripe as your payment gateway through Metronome."""

    tax_type: Optional[Literal["NONE", "STRIPE"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataPrepaidBalanceThresholdConfiguration(BaseModel):
    commit: DataPrepaidBalanceThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataPrepaidBalanceThresholdConfigurationPaymentGateConfig

    recharge_to_amount: float
    """Specify the amount the balance should be recharged to."""

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's prepaid balance lowers to this amount, a threshold
    charge will be initiated.
    """


class DataSpendThresholdConfigurationCommit(BaseModel):
    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """

    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """


class DataSpendThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""


class DataSpendThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    stripe_config: Optional[DataSpendThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using Stripe as your payment gateway through Metronome."""

    tax_type: Optional[Literal["NONE", "STRIPE"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataSpendThresholdConfiguration(BaseModel):
    commit: DataSpendThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataSpendThresholdConfigurationPaymentGateConfig

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class DataSubscriptionProration(BaseModel):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]

    is_prorated: bool


class DataSubscriptionQuantitySchedule(BaseModel):
    quantity: float

    starting_at: datetime

    ending_before: Optional[datetime] = None


class DataSubscriptionSubscriptionRateProduct(BaseModel):
    id: str

    name: str


class DataSubscriptionSubscriptionRate(BaseModel):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    product: DataSubscriptionSubscriptionRateProduct


class DataSubscription(BaseModel):
    collection_schedule: Literal["ADVANCE", "ARREARS"]

    proration: DataSubscriptionProration

    quantity_schedule: List[DataSubscriptionQuantitySchedule]

    starting_at: datetime

    subscription_rate: DataSubscriptionSubscriptionRate

    id: Optional[str] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ending_before: Optional[datetime] = None

    fiat_credit_type_id: Optional[str] = None

    name: Optional[str] = None


class Data(BaseModel):
    id: str

    amendments: List[DataAmendment]

    current: DataCurrent

    customer_id: str

    initial: DataInitial

    archived_at: Optional[datetime] = None
    """RFC 3339 timestamp indicating when the contract was archived.

    If not returned, the contract is not archived.
    """

    custom_fields: Optional[Dict[str, str]] = None

    customer_billing_provider_configuration: Optional[DataCustomerBillingProviderConfiguration] = None
    """The billing provider configuration associated with a contract."""

    prepaid_balance_threshold_configuration: Optional[DataPrepaidBalanceThresholdConfiguration] = None

    scheduled_charges_on_usage_invoices: Optional[Literal["ALL"]] = None
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    spend_threshold_configuration: Optional[DataSpendThresholdConfiguration] = None

    subscriptions: Optional[List[DataSubscription]] = None
    """(beta) List of subscriptions on the contract."""

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class ContractRetrieveResponse(BaseModel):
    data: Data
