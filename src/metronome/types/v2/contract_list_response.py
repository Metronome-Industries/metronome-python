# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ContractListResponse",
    "Data",
    "DataCommit",
    "DataCommitProduct",
    "DataCommitAccessSchedule",
    "DataCommitAccessScheduleScheduleItem",
    "DataCommitAccessScheduleCreditType",
    "DataCommitContract",
    "DataCommitHierarchyConfiguration",
    "DataCommitHierarchyConfigurationChildAccess",
    "DataCommitHierarchyConfigurationChildAccessType",
    "DataCommitHierarchyConfigurationChildAccessUnionMember2",
    "DataCommitInvoiceContract",
    "DataCommitInvoiceSchedule",
    "DataCommitInvoiceScheduleCreditType",
    "DataCommitInvoiceScheduleScheduleItem",
    "DataCommitLedger",
    "DataCommitLedgerUnionMember0",
    "DataCommitLedgerUnionMember1",
    "DataCommitLedgerUnionMember2",
    "DataCommitLedgerUnionMember3",
    "DataCommitLedgerUnionMember4",
    "DataCommitLedgerUnionMember5",
    "DataCommitLedgerUnionMember6",
    "DataCommitLedgerUnionMember7",
    "DataCommitLedgerUnionMember8",
    "DataCommitLedgerUnionMember9",
    "DataCommitLedgerUnionMember10",
    "DataCommitLedgerUnionMember11",
    "DataCommitLedgerUnionMember12",
    "DataCommitLedgerUnionMember13",
    "DataCommitRolledOverFrom",
    "DataCommitSpecifier",
    "DataOverride",
    "DataOverrideOverrideSpecifier",
    "DataOverrideOverrideTier",
    "DataOverrideOverwriteRate",
    "DataOverrideOverwriteRateCreditType",
    "DataOverrideOverwriteRateTier",
    "DataOverrideProduct",
    "DataScheduledCharge",
    "DataScheduledChargeProduct",
    "DataScheduledChargeSchedule",
    "DataScheduledChargeScheduleCreditType",
    "DataScheduledChargeScheduleScheduleItem",
    "DataTransition",
    "DataUsageFilter",
    "DataUsageStatementSchedule",
    "DataCredit",
    "DataCreditProduct",
    "DataCreditAccessSchedule",
    "DataCreditAccessScheduleScheduleItem",
    "DataCreditAccessScheduleCreditType",
    "DataCreditContract",
    "DataCreditHierarchyConfiguration",
    "DataCreditHierarchyConfigurationChildAccess",
    "DataCreditHierarchyConfigurationChildAccessType",
    "DataCreditHierarchyConfigurationChildAccessUnionMember2",
    "DataCreditLedger",
    "DataCreditLedgerUnionMember0",
    "DataCreditLedgerUnionMember1",
    "DataCreditLedgerUnionMember2",
    "DataCreditLedgerUnionMember3",
    "DataCreditLedgerUnionMember4",
    "DataCreditLedgerUnionMember5",
    "DataCreditLedgerUnionMember6",
    "DataCreditSpecifier",
    "DataCustomerBillingProviderConfiguration",
    "DataDiscount",
    "DataDiscountProduct",
    "DataDiscountSchedule",
    "DataDiscountScheduleCreditType",
    "DataDiscountScheduleScheduleItem",
    "DataHasMore",
    "DataHierarchyConfiguration",
    "DataHierarchyConfigurationChildren",
    "DataHierarchyConfigurationChildrenChild",
    "DataHierarchyConfigurationParent",
    "DataHierarchyConfigurationParentParent",
    "DataPrepaidBalanceThresholdConfiguration",
    "DataPrepaidBalanceThresholdConfigurationCommit",
    "DataPrepaidBalanceThresholdConfigurationCommitSpecifier",
    "DataPrepaidBalanceThresholdConfigurationPaymentGateConfig",
    "DataPrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "DataPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataProfessionalService",
    "DataRecurringCommit",
    "DataRecurringCommitAccessAmount",
    "DataRecurringCommitCommitDuration",
    "DataRecurringCommitProduct",
    "DataRecurringCommitContract",
    "DataRecurringCommitHierarchyConfiguration",
    "DataRecurringCommitHierarchyConfigurationChildAccess",
    "DataRecurringCommitHierarchyConfigurationChildAccessType",
    "DataRecurringCommitHierarchyConfigurationChildAccessUnionMember2",
    "DataRecurringCommitInvoiceAmount",
    "DataRecurringCommitSpecifier",
    "DataRecurringCommitSubscriptionConfig",
    "DataRecurringCommitSubscriptionConfigApplySeatIncreaseConfig",
    "DataRecurringCredit",
    "DataRecurringCreditAccessAmount",
    "DataRecurringCreditCommitDuration",
    "DataRecurringCreditProduct",
    "DataRecurringCreditContract",
    "DataRecurringCreditHierarchyConfiguration",
    "DataRecurringCreditHierarchyConfigurationChildAccess",
    "DataRecurringCreditHierarchyConfigurationChildAccessType",
    "DataRecurringCreditHierarchyConfigurationChildAccessUnionMember2",
    "DataRecurringCreditSpecifier",
    "DataRecurringCreditSubscriptionConfig",
    "DataRecurringCreditSubscriptionConfigApplySeatIncreaseConfig",
    "DataResellerRoyalty",
    "DataResellerRoyaltySegment",
    "DataSpendThresholdConfiguration",
    "DataSpendThresholdConfigurationCommit",
    "DataSpendThresholdConfigurationPaymentGateConfig",
    "DataSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "DataSpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataSubscription",
    "DataSubscriptionProration",
    "DataSubscriptionQuantitySchedule",
    "DataSubscriptionSubscriptionRate",
    "DataSubscriptionSubscriptionRateProduct",
]


class DataCommitProduct(BaseModel):
    id: str

    name: str


class DataCommitAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataCommitAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCommitAccessSchedule(BaseModel):
    schedule_items: List[DataCommitAccessScheduleScheduleItem]

    credit_type: Optional[DataCommitAccessScheduleCreditType] = None


class DataCommitContract(BaseModel):
    id: str


class DataCommitHierarchyConfigurationChildAccessType(BaseModel):
    type: Literal["ALL"]


class DataCommitHierarchyConfigurationChildAccessUnionMember2(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataCommitHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataCommitHierarchyConfigurationChildAccessType,
    DataCommitHierarchyConfigurationChildAccessType,
    DataCommitHierarchyConfigurationChildAccessUnionMember2,
]


class DataCommitHierarchyConfiguration(BaseModel):
    child_access: DataCommitHierarchyConfigurationChildAccess


class DataCommitInvoiceContract(BaseModel):
    id: str


class DataCommitInvoiceScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCommitInvoiceScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    quantity: float

    timestamp: datetime

    unit_price: float

    invoice_id: Optional[str] = None


class DataCommitInvoiceSchedule(BaseModel):
    credit_type: Optional[DataCommitInvoiceScheduleCreditType] = None

    schedule_items: Optional[List[DataCommitInvoiceScheduleScheduleItem]] = None


class DataCommitLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class DataCommitLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class DataCommitLedgerUnionMember2(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class DataCommitLedgerUnionMember3(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class DataCommitLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]

    contract_id: Optional[str] = None


class DataCommitLedgerUnionMember5(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]

    contract_id: Optional[str] = None


class DataCommitLedgerUnionMember6(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT"]


class DataCommitLedgerUnionMember7(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class DataCommitLedgerUnionMember8(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class DataCommitLedgerUnionMember9(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class DataCommitLedgerUnionMember10(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]

    contract_id: Optional[str] = None


class DataCommitLedgerUnionMember11(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class DataCommitLedgerUnionMember12(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class DataCommitLedgerUnionMember13(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


DataCommitLedger: TypeAlias = Union[
    DataCommitLedgerUnionMember0,
    DataCommitLedgerUnionMember1,
    DataCommitLedgerUnionMember2,
    DataCommitLedgerUnionMember3,
    DataCommitLedgerUnionMember4,
    DataCommitLedgerUnionMember5,
    DataCommitLedgerUnionMember6,
    DataCommitLedgerUnionMember7,
    DataCommitLedgerUnionMember8,
    DataCommitLedgerUnionMember9,
    DataCommitLedgerUnionMember10,
    DataCommitLedgerUnionMember11,
    DataCommitLedgerUnionMember12,
    DataCommitLedgerUnionMember13,
]


class DataCommitRolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class DataCommitSpecifier(BaseModel):
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


class DataCommit(BaseModel):
    id: str

    product: DataCommitProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[DataCommitAccessSchedule] = None
    """
    The schedule that the customer will gain access to the credits purposed with
    this commit.
    """

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    archived_at: Optional[datetime] = None

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

    contract: Optional[DataCommitContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    hierarchy_configuration: Optional[DataCommitHierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

    invoice_contract: Optional[DataCommitInvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[DataCommitInvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[DataCommitLedger]] = None
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

    rolled_over_from: Optional[DataCommitRolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[DataCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataOverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None

    recurring_credit_ids: Optional[List[str]] = None


class DataOverrideOverrideTier(BaseModel):
    multiplier: float

    size: Optional[float] = None


class DataOverrideOverwriteRateCreditType(BaseModel):
    id: str

    name: str


class DataOverrideOverwriteRateTier(BaseModel):
    price: float

    size: Optional[float] = None


class DataOverrideOverwriteRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

    credit_type: Optional[DataOverrideOverwriteRateCreditType] = None

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

    tiers: Optional[List[DataOverrideOverwriteRateTier]] = None
    """Only set for TIERED rate_type."""


class DataOverrideProduct(BaseModel):
    id: str

    name: str


class DataOverride(BaseModel):
    id: str

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[DataOverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[DataOverrideOverrideTier]] = None

    overwrite_rate: Optional[DataOverrideOverwriteRate] = None

    priority: Optional[float] = None

    product: Optional[DataOverrideProduct] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None


class DataScheduledChargeProduct(BaseModel):
    id: str

    name: str


class DataScheduledChargeScheduleCreditType(BaseModel):
    id: str

    name: str


class DataScheduledChargeScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    quantity: float

    timestamp: datetime

    unit_price: float

    invoice_id: Optional[str] = None


class DataScheduledChargeSchedule(BaseModel):
    credit_type: Optional[DataScheduledChargeScheduleCreditType] = None

    schedule_items: Optional[List[DataScheduledChargeScheduleScheduleItem]] = None


class DataScheduledCharge(BaseModel):
    id: str

    product: DataScheduledChargeProduct

    schedule: DataScheduledChargeSchedule

    archived_at: Optional[datetime] = None

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None
    """displayed on invoices"""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataTransition(BaseModel):
    from_contract_id: str

    to_contract_id: str

    type: Literal["SUPERSEDE", "RENEWAL"]


class DataUsageFilter(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: datetime
    """
    This will match contract starting_at value if usage filter is active from the
    beginning of the contract.
    """

    ending_before: Optional[datetime] = None
    """
    This will match contract ending_before value if usage filter is active until the
    end of the contract. It will be undefined if the contract is open-ended.
    """


class DataUsageStatementSchedule(BaseModel):
    billing_anchor_date: datetime
    """Contract usage statements follow a selected cadence based on this date."""

    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]


class DataCreditProduct(BaseModel):
    id: str

    name: str


class DataCreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    ending_before: datetime

    starting_at: datetime


class DataCreditAccessScheduleCreditType(BaseModel):
    id: str

    name: str


class DataCreditAccessSchedule(BaseModel):
    schedule_items: List[DataCreditAccessScheduleScheduleItem]

    credit_type: Optional[DataCreditAccessScheduleCreditType] = None


class DataCreditContract(BaseModel):
    id: str


class DataCreditHierarchyConfigurationChildAccessType(BaseModel):
    type: Literal["ALL"]


class DataCreditHierarchyConfigurationChildAccessUnionMember2(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataCreditHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataCreditHierarchyConfigurationChildAccessType,
    DataCreditHierarchyConfigurationChildAccessType,
    DataCreditHierarchyConfigurationChildAccessUnionMember2,
]


class DataCreditHierarchyConfiguration(BaseModel):
    child_access: DataCreditHierarchyConfigurationChildAccess


class DataCreditLedgerUnionMember0(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class DataCreditLedgerUnionMember1(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class DataCreditLedgerUnionMember2(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class DataCreditLedgerUnionMember3(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]

    contract_id: Optional[str] = None


class DataCreditLedgerUnionMember4(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]

    contract_id: Optional[str] = None


class DataCreditLedgerUnionMember5(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


class DataCreditLedgerUnionMember6(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEAT_BASED_ADJUSTMENT"]


DataCreditLedger: TypeAlias = Union[
    DataCreditLedgerUnionMember0,
    DataCreditLedgerUnionMember1,
    DataCreditLedgerUnionMember2,
    DataCreditLedgerUnionMember3,
    DataCreditLedgerUnionMember4,
    DataCreditLedgerUnionMember5,
    DataCreditLedgerUnionMember6,
]


class DataCreditSpecifier(BaseModel):
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


class DataCredit(BaseModel):
    id: str

    product: DataCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[DataCreditAccessSchedule] = None
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

    contract: Optional[DataCreditContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    hierarchy_configuration: Optional[DataCreditHierarchyConfiguration] = None
    """Optional configuration for credit hierarchy access control"""

    ledger: Optional[List[DataCreditLedger]] = None
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

    specifiers: Optional[List[DataCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataCustomerBillingProviderConfiguration(BaseModel):
    id: str
    """ID of Customer's billing provider configuration."""

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


class DataDiscountProduct(BaseModel):
    id: str

    name: str


class DataDiscountScheduleCreditType(BaseModel):
    id: str

    name: str


class DataDiscountScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    quantity: float

    timestamp: datetime

    unit_price: float

    invoice_id: Optional[str] = None


class DataDiscountSchedule(BaseModel):
    credit_type: Optional[DataDiscountScheduleCreditType] = None

    schedule_items: Optional[List[DataDiscountScheduleScheduleItem]] = None


class DataDiscount(BaseModel):
    id: str

    product: DataDiscountProduct

    schedule: DataDiscountSchedule

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataHasMore(BaseModel):
    commits: bool
    """Whether there are more commits on this contract than the limit for this
    endpoint.

    Use the /contracts/customerCommits/list endpoint to get the full list of
    commits.
    """

    credits: bool
    """Whether there are more credits on this contract than the limit for this
    endpoint.

    Use the /contracts/customerCredits/list endpoint to get the full list of
    credits.
    """


class DataHierarchyConfigurationChildrenChild(BaseModel):
    contract_id: str

    customer_id: str


class DataHierarchyConfigurationChildren(BaseModel):
    children: List[DataHierarchyConfigurationChildrenChild]
    """List of contracts that belong to this parent."""


class DataHierarchyConfigurationParentParent(BaseModel):
    contract_id: str

    customer_id: str


class DataHierarchyConfigurationParent(BaseModel):
    parent: DataHierarchyConfigurationParentParent
    """The single parent contract/customer for this child."""


DataHierarchyConfiguration: TypeAlias = Union[DataHierarchyConfigurationChildren, DataHierarchyConfigurationParent]


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

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the threshold commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
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
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataPrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class DataPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class DataPrepaidBalanceThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[
        DataPrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig
    ] = None
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[DataPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
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

    Each time the contract's balance lowers to this amount, a threshold charge will
    be initiated.
    """

    custom_credit_type_id: Optional[str] = None
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """


class DataProfessionalService(BaseModel):
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


class DataRecurringCommitAccessAmount(BaseModel):
    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataRecurringCommitCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataRecurringCommitContract(BaseModel):
    id: str


class DataRecurringCommitHierarchyConfigurationChildAccessType(BaseModel):
    type: Literal["ALL"]


class DataRecurringCommitHierarchyConfigurationChildAccessUnionMember2(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataRecurringCommitHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataRecurringCommitHierarchyConfigurationChildAccessType,
    DataRecurringCommitHierarchyConfigurationChildAccessType,
    DataRecurringCommitHierarchyConfigurationChildAccessUnionMember2,
]


class DataRecurringCommitHierarchyConfiguration(BaseModel):
    child_access: DataRecurringCommitHierarchyConfigurationChildAccess


class DataRecurringCommitInvoiceAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataRecurringCommitSpecifier(BaseModel):
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


class DataRecurringCommitSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class DataRecurringCommitSubscriptionConfig(BaseModel):
    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: DataRecurringCommitSubscriptionConfigApplySeatIncreaseConfig

    subscription_id: str


class DataRecurringCommit(BaseModel):
    id: str

    access_amount: DataRecurringCommitAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataRecurringCommitCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataRecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataRecurringCommitContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[DataRecurringCommitHierarchyConfiguration] = None
    """Optional configuration for recurring credit hierarchy access control"""

    invoice_amount: Optional[DataRecurringCommitInvoiceAmount] = None
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

    specifiers: Optional[List[DataRecurringCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[DataRecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataRecurringCreditAccessAmount(BaseModel):
    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataRecurringCreditCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataRecurringCreditContract(BaseModel):
    id: str


class DataRecurringCreditHierarchyConfigurationChildAccessType(BaseModel):
    type: Literal["ALL"]


class DataRecurringCreditHierarchyConfigurationChildAccessUnionMember2(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataRecurringCreditHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataRecurringCreditHierarchyConfigurationChildAccessType,
    DataRecurringCreditHierarchyConfigurationChildAccessType,
    DataRecurringCreditHierarchyConfigurationChildAccessUnionMember2,
]


class DataRecurringCreditHierarchyConfiguration(BaseModel):
    child_access: DataRecurringCreditHierarchyConfigurationChildAccess


class DataRecurringCreditSpecifier(BaseModel):
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


class DataRecurringCreditSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class DataRecurringCreditSubscriptionConfig(BaseModel):
    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: DataRecurringCreditSubscriptionConfigApplySeatIncreaseConfig

    subscription_id: str


class DataRecurringCredit(BaseModel):
    id: str

    access_amount: DataRecurringCreditAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataRecurringCreditCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataRecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataRecurringCreditContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[DataRecurringCreditHierarchyConfiguration] = None
    """Optional configuration for recurring credit hierarchy access control"""

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

    specifiers: Optional[List[DataRecurringCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[DataRecurringCreditSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataResellerRoyaltySegment(BaseModel):
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


class DataResellerRoyalty(BaseModel):
    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

    segments: List[DataResellerRoyaltySegment]


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


class DataSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class DataSpendThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class DataSpendThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[DataSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig] = None
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[DataSpendThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
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
    """List of quantity schedule items for the subscription.

    Only includes the current quantity and future quantity changes.
    """

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

    commits: List[DataCommit]

    created_at: datetime

    created_by: str

    customer_id: str

    overrides: List[DataOverride]

    scheduled_charges: List[DataScheduledCharge]

    starting_at: datetime

    transitions: List[DataTransition]

    usage_filter: List[DataUsageFilter]

    usage_statement_schedule: DataUsageStatementSchedule

    archived_at: Optional[datetime] = None

    credits: Optional[List[DataCredit]] = None

    custom_fields: Optional[Dict[str, str]] = None

    customer_billing_provider_configuration: Optional[DataCustomerBillingProviderConfiguration] = None
    """This field's availability is dependent on your client's configuration."""

    discounts: Optional[List[DataDiscount]] = None
    """This field's availability is dependent on your client's configuration."""

    ending_before: Optional[datetime] = None

    has_more: Optional[DataHasMore] = None
    """Indicates whether there are more items than the limit for this endpoint.

    Use the respective list endpoints to get the full lists.
    """

    hierarchy_configuration: Optional[DataHierarchyConfiguration] = None
    """
    Either a **parent** configuration with a list of children or a **child**
    configuration with a single parent.
    """

    multiplier_override_prioritization: Optional[Literal["LOWEST_MULTIPLIER", "EXPLICIT"]] = None
    """
    Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
    prices automatically. EXPLICIT prioritization requires specifying priorities for
    each multiplier; the one with the lowest priority value will be prioritized
    first.
    """

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    prepaid_balance_threshold_configuration: Optional[DataPrepaidBalanceThresholdConfiguration] = None

    priority: Optional[float] = None
    """Priority of the contract."""

    professional_services: Optional[List[DataProfessionalService]] = None
    """This field's availability is dependent on your client's configuration."""

    rate_card_id: Optional[str] = None

    recurring_commits: Optional[List[DataRecurringCommit]] = None

    recurring_credits: Optional[List[DataRecurringCredit]] = None

    reseller_royalties: Optional[List[DataResellerRoyalty]] = None
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

    spend_threshold_configuration: Optional[DataSpendThresholdConfiguration] = None

    subscriptions: Optional[List[DataSubscription]] = None
    """List of subscriptions on the contract."""

    total_contract_value: Optional[float] = None

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class ContractListResponse(BaseModel):
    data: List[Data]
