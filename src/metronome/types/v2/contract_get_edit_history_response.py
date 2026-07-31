# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.tier import Tier
from ..shared.discount import Discount
from ..shared.pro_service import ProService
from ..shared.override_tier import OverrideTier
from ..shared.commit_specifier import CommitSpecifier
from ..shared.credit_type_data import CreditTypeData
from ..shared.schedule_duration import ScheduleDuration
from ..shared.commit_specifier_input import CommitSpecifierInput
from ..shared.payment_gate_config_v2 import PaymentGateConfigV2
from ..shared.schedule_point_in_time import SchedulePointInTime
from ..shared.update_base_threshold_commit import UpdateBaseThresholdCommit
from ..shared.commit_hierarchy_configuration import CommitHierarchyConfiguration
from ..shared.spend_threshold_configuration_v2 import SpendThresholdConfigurationV2
from ..shared.recurring_commit_subscription_config import RecurringCommitSubscriptionConfig
from ..shared.prepaid_balance_threshold_configuration_v2 import PrepaidBalanceThresholdConfigurationV2

__all__ = [
    "ContractGetEditHistoryResponse",
    "Data",
    "DataAddCommit",
    "DataAddCommitProduct",
    "DataAddCommitInvoiceSchedule",
    "DataAddCommitInvoiceScheduleScheduleItem",
    "DataAddCredit",
    "DataAddCreditProduct",
    "DataAddOverride",
    "DataAddOverrideOverrideSpecifier",
    "DataAddOverrideOverwriteRate",
    "DataAddOverrideProduct",
    "DataAddRecurringCommit",
    "DataAddRecurringCommitAccessAmount",
    "DataAddRecurringCommitCommitDuration",
    "DataAddRecurringCommitProduct",
    "DataAddRecurringCommitContract",
    "DataAddRecurringCommitInvoiceAmount",
    "DataAddRecurringCommitProrationRounding",
    "DataAddRecurringCommitProrationRoundingAccess",
    "DataAddRecurringCommitProrationRoundingInvoice",
    "DataAddRecurringCredit",
    "DataAddRecurringCreditAccessAmount",
    "DataAddRecurringCreditCommitDuration",
    "DataAddRecurringCreditProduct",
    "DataAddRecurringCreditContract",
    "DataAddRecurringCreditProrationRounding",
    "DataAddRecurringCreditProrationRoundingAccess",
    "DataAddResellerRoyalty",
    "DataAddScheduledCharge",
    "DataAddScheduledChargeProduct",
    "DataAddSubscription",
    "DataAddSubscriptionBillingPeriods",
    "DataAddSubscriptionBillingPeriodsCurrent",
    "DataAddSubscriptionBillingPeriodsNext",
    "DataAddSubscriptionBillingPeriodsPrevious",
    "DataAddSubscriptionProration",
    "DataAddSubscriptionProrationRounding",
    "DataAddSubscriptionQuantitySchedule",
    "DataAddSubscriptionSubscriptionRate",
    "DataAddSubscriptionSubscriptionRateProduct",
    "DataAddSubscriptionBillingCycleConfig",
    "DataAddSubscriptionSeatConfig",
    "DataAddUsageFilter",
    "DataArchiveCommit",
    "DataArchiveCredit",
    "DataArchiveScheduledCharge",
    "DataRemoveOverride",
    "DataUpdateCommit",
    "DataUpdateCommitAccessSchedule",
    "DataUpdateCommitAccessScheduleAddScheduleItem",
    "DataUpdateCommitAccessScheduleRemoveScheduleItem",
    "DataUpdateCommitAccessScheduleUpdateScheduleItem",
    "DataUpdateCommitInvoiceSchedule",
    "DataUpdateCommitInvoiceScheduleAddScheduleItem",
    "DataUpdateCommitInvoiceScheduleRemoveScheduleItem",
    "DataUpdateCommitInvoiceScheduleUpdateScheduleItem",
    "DataUpdateCredit",
    "DataUpdateCreditAccessSchedule",
    "DataUpdateCreditAccessScheduleAddScheduleItem",
    "DataUpdateCreditAccessScheduleRemoveScheduleItem",
    "DataUpdateCreditAccessScheduleUpdateScheduleItem",
    "DataUpdateDiscount",
    "DataUpdateDiscountSchedule",
    "DataUpdateDiscountScheduleRecurringSchedule",
    "DataUpdateDiscountScheduleScheduleItem",
    "DataUpdatePrepaidBalanceThresholdConfiguration",
    "DataUpdatePrepaidBalanceThresholdConfigurationCommit",
    "DataUpdatePrepaidBalanceThresholdConfigurationDiscountConfiguration",
    "DataUpdatePrepaidBalanceThresholdConfigurationDiscountConfigurationCap",
    "DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifier",
    "DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExclude",
    "DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExcludeCustomFieldFilter",
    "DataUpdateRecurringCommit",
    "DataUpdateRecurringCommitAccessAmount",
    "DataUpdateRecurringCommitInvoiceAmount",
    "DataUpdateRecurringCommitProrationRounding",
    "DataUpdateRecurringCommitProrationRoundingAccess",
    "DataUpdateRecurringCommitProrationRoundingInvoice",
    "DataUpdateRecurringCredit",
    "DataUpdateRecurringCreditAccessAmount",
    "DataUpdateRecurringCreditProrationRounding",
    "DataUpdateRecurringCreditProrationRoundingAccess",
    "DataUpdateRefundInvoice",
    "DataUpdateScheduledCharge",
    "DataUpdateScheduledChargeInvoiceSchedule",
    "DataUpdateScheduledChargeInvoiceScheduleAddScheduleItem",
    "DataUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem",
    "DataUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem",
    "DataUpdateSpendThresholdConfiguration",
    "DataUpdateSpendThresholdConfigurationDiscountConfiguration",
    "DataUpdateSpendThresholdConfigurationDiscountConfigurationCap",
    "DataUpdateSubscription",
    "DataUpdateSubscriptionQuantityUpdate",
    "DataUpdateSubscriptionSeatUpdates",
    "DataUpdateSubscriptionSeatUpdatesAddSeatID",
    "DataUpdateSubscriptionSeatUpdatesAddUnassignedSeat",
    "DataUpdateSubscriptionSeatUpdatesRemoveSeatID",
    "DataUpdateSubscriptionSeatUpdatesRemoveUnassignedSeat",
]


class DataAddCommitProduct(BaseModel):
    id: str

    name: str


class DataAddCommitInvoiceScheduleScheduleItem(BaseModel):
    id: str

    timestamp: datetime

    amount: Optional[float] = None

    invoice_id: Optional[str] = None

    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataAddCommitInvoiceSchedule(BaseModel):
    """The schedule that the customer will be invoiced for this commit."""

    credit_type: Optional[CreditTypeData] = None

    do_not_invoice: Optional[bool] = None
    """If true, this schedule will not generate an invoice."""

    schedule_items: Optional[List[DataAddCommitInvoiceScheduleScheduleItem]] = None


class DataAddCommit(BaseModel):
    id: str

    product: DataAddCommitProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[ScheduleDuration] = None
    """
    The schedule that the customer will gain access to the credits purposed with
    this commit.
    """

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    description: Optional[str] = None

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

    invoice_schedule: Optional[DataAddCommitInvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    priority: Optional[float] = None
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[CommitSpecifierInput]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataAddCreditProduct(BaseModel):
    id: str

    name: str


class DataAddCredit(BaseModel):
    id: str

    product: DataAddCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[ScheduleDuration] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    description: Optional[str] = None

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for recurring credit hierarchy access control"""

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    priority: Optional[float] = None
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[CommitSpecifierInput]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataAddOverrideOverrideSpecifier(BaseModel):
    any_commit_or_credit_ids: Optional[List[str]] = None

    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None


class DataAddOverrideOverwriteRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "TIERED_PERCENTAGE", "CUSTOM"]

    credit_type: Optional[CreditTypeData] = None

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

    tiers: Optional[List[Tier]] = None
    """Only set for TIERED rate_type."""


class DataAddOverrideProduct(BaseModel):
    id: str

    name: str


class DataAddOverride(BaseModel):
    id: str

    created_at: datetime

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[DataAddOverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[OverrideTier]] = None

    overwrite_rate: Optional[DataAddOverrideOverwriteRate] = None

    priority: Optional[float] = None

    product: Optional[DataAddOverrideProduct] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None


class DataAddRecurringCommitAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataAddRecurringCommitCommitDuration(BaseModel):
    """The amount of time the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataAddRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataAddRecurringCommitContract(BaseModel):
    id: str


class DataAddRecurringCommitInvoiceAmount(BaseModel):
    """The amount the customer should be billed for the commit. Not required."""

    credit_type_id: str

    quantity: float

    unit_price: float


class DataAddRecurringCommitProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataAddRecurringCommitProrationRoundingInvoice(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataAddRecurringCommitProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring commit amounts."""

    access: Optional[DataAddRecurringCommitProrationRoundingAccess] = None

    invoice: Optional[DataAddRecurringCommitProrationRoundingInvoice] = None


class DataAddRecurringCommit(BaseModel):
    id: str

    access_amount: DataAddRecurringCommitAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataAddRecurringCommitCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataAddRecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataAddRecurringCommitContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for recurring credit hierarchy access control"""

    invoice_amount: Optional[DataAddRecurringCommitInvoiceAmount] = None
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

    proration_rounding: Optional[DataAddRecurringCommitProrationRounding] = None
    """Rounding configuration for prorated recurring commit amounts."""

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY", "DAILY"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates. - Daily recurring commits have
    a limit of one per contract, and are unable to be created with seat-based
    subscriptions
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[RecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataAddRecurringCreditAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataAddRecurringCreditCommitDuration(BaseModel):
    """The amount of time the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataAddRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataAddRecurringCreditContract(BaseModel):
    id: str


class DataAddRecurringCreditProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataAddRecurringCreditProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring credit amounts."""

    access: Optional[DataAddRecurringCreditProrationRoundingAccess] = None


class DataAddRecurringCredit(BaseModel):
    id: str

    access_amount: DataAddRecurringCreditAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataAddRecurringCreditCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataAddRecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataAddRecurringCreditContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
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

    proration_rounding: Optional[DataAddRecurringCreditProrationRounding] = None
    """Rounding configuration for prorated recurring credit amounts."""

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY", "DAILY"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates. - Daily recurring commits have
    a limit of one per contract, and are unable to be created with seat-based
    subscriptions
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[RecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataAddResellerRoyalty(BaseModel):
    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

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


class DataAddScheduledChargeProduct(BaseModel):
    id: str

    name: str


class DataAddScheduledCharge(BaseModel):
    id: str

    product: DataAddScheduledChargeProduct

    schedule: SchedulePointInTime

    name: Optional[str] = None
    """displayed on invoices"""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataAddSubscriptionBillingPeriodsCurrent(BaseModel):
    ending_before: datetime

    starting_at: datetime


class DataAddSubscriptionBillingPeriodsNext(BaseModel):
    ending_before: datetime

    starting_at: datetime


class DataAddSubscriptionBillingPeriodsPrevious(BaseModel):
    ending_before: datetime

    starting_at: datetime


class DataAddSubscriptionBillingPeriods(BaseModel):
    """Previous, current, and next billing periods for the subscription."""

    current: Optional[DataAddSubscriptionBillingPeriodsCurrent] = None

    next: Optional[DataAddSubscriptionBillingPeriodsNext] = None

    previous: Optional[DataAddSubscriptionBillingPeriodsPrevious] = None


class DataAddSubscriptionProrationRounding(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataAddSubscriptionProration(BaseModel):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]

    is_prorated: bool

    rounding: Optional[DataAddSubscriptionProrationRounding] = None


class DataAddSubscriptionQuantitySchedule(BaseModel):
    quantity: float

    starting_at: datetime

    ending_before: Optional[datetime] = None


class DataAddSubscriptionSubscriptionRateProduct(BaseModel):
    id: str

    name: str


class DataAddSubscriptionSubscriptionRate(BaseModel):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    product: DataAddSubscriptionSubscriptionRateProduct


class DataAddSubscriptionBillingCycleConfig(BaseModel):
    anchor_date: datetime
    """The date this subscription's billing cycle is anchored to."""

    invoice_placement: Literal["ON_SCHEDULED_INVOICE", "ON_USAGE_INVOICE"]
    """
    Controls whether this subscription consolidates onto usage invoices or gets its
    own scheduled invoice.
    """


class DataAddSubscriptionSeatConfig(BaseModel):
    seat_group_key: str
    """
    The property name, sent on usage events, that identifies the seat ID associated
    with the usage event. For example, the property name might be seat_id or
    user_id. The property must be set as a group key on billable metrics and a
    presentation/pricing group key on contract products. This allows linked
    recurring credits with an allocation per seat to be consumed by only one seat's
    usage.
    """


class DataAddSubscription(BaseModel):
    billing_periods: DataAddSubscriptionBillingPeriods
    """Previous, current, and next billing periods for the subscription."""

    collection_schedule: Literal["ADVANCE", "ARREARS"]

    proration: DataAddSubscriptionProration

    quantity_management_mode: Literal["SEAT_BASED", "QUANTITY_ONLY"]
    """Determines how the subscription's quantity is controlled.

    Defaults to QUANTITY_ONLY. **QUANTITY_ONLY**: The subscription quantity is
    specified directly on the subscription. `initial_quantity` must be provided with
    this option. Compatible with recurring commits/credits that use POOLED
    allocation. **SEAT_BASED**: Use when you want to pass specific seat identifiers
    (e.g. add user_123) to increment and decrement a subscription quantity, rather
    than directly providing the quantity. You must use a **SEAT_BASED** subscription
    to use a linked recurring credit with an allocation per seat. `seat_config` must
    be provided with this option.
    """

    quantity_schedule: List[DataAddSubscriptionQuantitySchedule]
    """List of quantity schedule items for the subscription.

    Only includes the current quantity and future quantity changes.
    """

    starting_at: datetime

    subscription_rate: DataAddSubscriptionSubscriptionRate

    id: Optional[str] = None

    billing_cycle_config: Optional[DataAddSubscriptionBillingCycleConfig] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    ending_before: Optional[datetime] = None

    fiat_credit_type_id: Optional[str] = None

    name: Optional[str] = None

    seat_config: Optional[DataAddSubscriptionSeatConfig] = None


class DataAddUsageFilter(BaseModel):
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


class DataArchiveCommit(BaseModel):
    id: str


class DataArchiveCredit(BaseModel):
    id: str


class DataArchiveScheduledCharge(BaseModel):
    id: str


class DataRemoveOverride(BaseModel):
    id: str


class DataUpdateCommitAccessScheduleAddScheduleItem(BaseModel):
    amount: float

    ending_before: datetime
    """RFC 3339 timestamp (exclusive)"""

    starting_at: datetime
    """RFC 3339 timestamp (inclusive)"""


class DataUpdateCommitAccessScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataUpdateCommitAccessScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    ending_before: Optional[datetime] = None
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Optional[datetime] = None
    """RFC 3339 timestamp (inclusive)"""


class DataUpdateCommitAccessSchedule(BaseModel):
    add_schedule_items: Optional[List[DataUpdateCommitAccessScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataUpdateCommitAccessScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataUpdateCommitAccessScheduleUpdateScheduleItem]] = None


class DataUpdateCommitInvoiceScheduleAddScheduleItem(BaseModel):
    timestamp: datetime

    amount: Optional[float] = None

    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateCommitInvoiceScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataUpdateCommitInvoiceScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    quantity: Optional[float] = None

    timestamp: Optional[datetime] = None

    unit_price: Optional[float] = None


class DataUpdateCommitInvoiceSchedule(BaseModel):
    add_schedule_items: Optional[List[DataUpdateCommitInvoiceScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataUpdateCommitInvoiceScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataUpdateCommitInvoiceScheduleUpdateScheduleItem]] = None


class DataUpdateCommit(BaseModel):
    id: str

    access_schedule: Optional[DataUpdateCommitAccessSchedule] = None

    applicable_product_ids: Optional[List[str]] = None
    """Which products the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    description: Optional[str] = None

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

    invoice_schedule: Optional[DataUpdateCommitInvoiceSchedule] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    priority: Optional[float] = None
    """
    If multiple commits are applicable, the one with the lower priority will apply
    first.
    """

    product_id: Optional[str] = None

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None
    """If set, the commit's rate type was updated to the specified value."""

    rollover_fraction: Optional[float] = None

    specifiers: Optional[List[CommitSpecifierInput]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataUpdateCreditAccessScheduleAddScheduleItem(BaseModel):
    amount: float

    ending_before: datetime
    """RFC 3339 timestamp (exclusive)"""

    starting_at: datetime
    """RFC 3339 timestamp (inclusive)"""


class DataUpdateCreditAccessScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataUpdateCreditAccessScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    ending_before: Optional[datetime] = None
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Optional[datetime] = None
    """RFC 3339 timestamp (inclusive)"""


class DataUpdateCreditAccessSchedule(BaseModel):
    add_schedule_items: Optional[List[DataUpdateCreditAccessScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataUpdateCreditAccessScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataUpdateCreditAccessScheduleUpdateScheduleItem]] = None


class DataUpdateCredit(BaseModel):
    id: str

    access_schedule: Optional[DataUpdateCreditAccessSchedule] = None

    applicable_product_ids: Optional[List[str]] = None
    """Which products the credit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the credit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the credit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the credit applies to all products.
    """

    description: Optional[str] = None

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for credit hierarchy access control"""

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    priority: Optional[float] = None
    """
    If multiple credits are applicable, the one with the lower priority will apply
    first.
    """

    product_id: Optional[str] = None

    rate_type: Optional[Literal["LIST_RATE", "COMMIT_RATE"]] = None
    """If set, the credit's rate type was updated to the specified value."""

    rollover_fraction: Optional[float] = None

    specifiers: Optional[List[CommitSpecifierInput]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataUpdateDiscountScheduleRecurringSchedule(BaseModel):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

    amount_distribution: Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]

    ending_before: datetime
    """RFC 3339 timestamp (exclusive)."""

    frequency: Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL", "WEEKLY"]

    starting_at: datetime
    """RFC 3339 timestamp (inclusive)."""

    amount: Optional[float] = None
    """Amount for the charge.

    Can be provided instead of unit_price and quantity. If amount is sent, the
    unit_price is assumed to be the amount and quantity is inferred to be 1.
    """

    quantity: Optional[float] = None
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount and must be specified
    with unit_price. If specified amount cannot be provided.
    """

    unit_price: Optional[float] = None
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified
    with quantity. If specified amount cannot be provided.
    """


class DataUpdateDiscountScheduleScheduleItem(BaseModel):
    timestamp: datetime
    """timestamp of the scheduled event"""

    amount: Optional[float] = None
    """Amount for the charge.

    Can be provided instead of unit_price and quantity. If amount is sent, the
    unit_price is assumed to be the amount and quantity is inferred to be 1.
    """

    quantity: Optional[float] = None
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount and must be specified
    with unit_price. If specified amount cannot be provided.
    """

    unit_price: Optional[float] = None
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified
    with quantity. If specified amount cannot be provided.
    """


class DataUpdateDiscountSchedule(BaseModel):
    """Must provide either schedule_items or recurring_schedule."""

    credit_type_id: Optional[str] = None
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: Optional[bool] = None
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    recurring_schedule: Optional[DataUpdateDiscountScheduleRecurringSchedule] = None
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Optional[List[DataUpdateDiscountScheduleScheduleItem]] = None
    """Either provide amount or provide both unit_price and quantity."""


class DataUpdateDiscount(BaseModel):
    id: str

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    schedule: Optional[DataUpdateDiscountSchedule] = None
    """Must provide either schedule_items or recurring_schedule."""


class DataUpdatePrepaidBalanceThresholdConfigurationCommit(UpdateBaseThresholdCommit):
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

    specifiers: Optional[List[CommitSpecifierInput]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataUpdatePrepaidBalanceThresholdConfigurationDiscountConfigurationCap(BaseModel):
    """Update the discount cap. Set to null to remove an existing cap."""

    amount: float
    """Accumulated spend ceiling above which the discount stops applying."""

    spend_tracker_alias: str
    """Alias of the spend tracker this cap is measured against."""


class DataUpdatePrepaidBalanceThresholdConfigurationDiscountConfiguration(BaseModel):
    cap: Optional[DataUpdatePrepaidBalanceThresholdConfigurationDiscountConfigurationCap] = None
    """Update the discount cap. Set to null to remove an existing cap."""

    payment_fraction: Optional[float] = None
    """
    The fraction of the original amount that the customer pays after applying the
    discount. Set to null to remove the discount fraction. For example, 0.85 means
    the customer pays 85% of the original amount (a 15% discount).
    """


class DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExcludeCustomFieldFilter(BaseModel):
    entity: Literal["Commit", "ContractCredit", "ContractCreditOrCommit"]

    key: str

    value: str


class DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExclude(BaseModel):
    custom_field_filters: List[
        DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExcludeCustomFieldFilter
    ]


class DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifier(BaseModel):
    exclude: List[DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExclude]


class DataUpdatePrepaidBalanceThresholdConfiguration(BaseModel):
    commit: Optional[DataUpdatePrepaidBalanceThresholdConfigurationCommit] = None

    custom_credit_type_id: Optional[str] = None
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """

    discount_configuration: Optional[DataUpdatePrepaidBalanceThresholdConfigurationDiscountConfiguration] = None

    is_enabled: Optional[bool] = None
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: Optional[PaymentGateConfigV2] = None

    recharge_to_amount: Optional[float] = None
    """Specify the amount the balance should be recharged to."""

    threshold_amount: Optional[float] = None
    """Specify the threshold amount for the contract.

    Each time the contract's balance lowers to this amount, a threshold charge will
    be initiated.
    """

    threshold_balance_specifiers: Optional[
        List[DataUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifier]
    ] = None
    """
    Determines which balances are excluded from remaining balance calculation for
    threshold billing.
    """


class DataUpdateRecurringCommitAccessAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateRecurringCommitInvoiceAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateRecurringCommitProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataUpdateRecurringCommitProrationRoundingInvoice(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataUpdateRecurringCommitProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring commit amounts."""

    access: Optional[DataUpdateRecurringCommitProrationRoundingAccess] = None

    invoice: Optional[DataUpdateRecurringCommitProrationRoundingInvoice] = None


class DataUpdateRecurringCommit(BaseModel):
    id: str

    access_amount: Optional[DataUpdateRecurringCommitAccessAmount] = None

    ending_before: Optional[datetime] = None

    invoice_amount: Optional[DataUpdateRecurringCommitInvoiceAmount] = None

    proration_rounding: Optional[DataUpdateRecurringCommitProrationRounding] = None
    """Rounding configuration for prorated recurring commit amounts."""

    rate_type: Optional[Literal["LIST_RATE", "COMMIT_RATE"]] = None


class DataUpdateRecurringCreditAccessAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateRecurringCreditProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataUpdateRecurringCreditProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring credit amounts."""

    access: Optional[DataUpdateRecurringCreditProrationRoundingAccess] = None


class DataUpdateRecurringCredit(BaseModel):
    id: str

    access_amount: Optional[DataUpdateRecurringCreditAccessAmount] = None

    ending_before: Optional[datetime] = None

    proration_rounding: Optional[DataUpdateRecurringCreditProrationRounding] = None
    """Rounding configuration for prorated recurring credit amounts."""

    rate_type: Optional[Literal["LIST_RATE", "COMMIT_RATE"]] = None


class DataUpdateRefundInvoice(BaseModel):
    date: datetime

    invoice_id: str


class DataUpdateScheduledChargeInvoiceScheduleAddScheduleItem(BaseModel):
    timestamp: datetime

    amount: Optional[float] = None

    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    quantity: Optional[float] = None

    timestamp: Optional[datetime] = None

    unit_price: Optional[float] = None


class DataUpdateScheduledChargeInvoiceSchedule(BaseModel):
    add_schedule_items: Optional[List[DataUpdateScheduledChargeInvoiceScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem]] = None


class DataUpdateScheduledCharge(BaseModel):
    id: str

    invoice_schedule: Optional[DataUpdateScheduledChargeInvoiceSchedule] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None


class DataUpdateSpendThresholdConfigurationDiscountConfigurationCap(BaseModel):
    """Update the discount cap. Set to null to remove an existing cap."""

    amount: float
    """Accumulated spend ceiling above which the discount stops applying."""

    spend_tracker_alias: str
    """Alias of the spend tracker this cap is measured against."""


class DataUpdateSpendThresholdConfigurationDiscountConfiguration(BaseModel):
    cap: Optional[DataUpdateSpendThresholdConfigurationDiscountConfigurationCap] = None
    """Update the discount cap. Set to null to remove an existing cap."""

    payment_fraction: Optional[float] = None
    """
    The fraction of the original amount that the customer pays after applying the
    discount. Set to null to remove the discount fraction. For example, 0.85 means
    the customer pays 85% of the original amount (a 15% discount).
    """


class DataUpdateSpendThresholdConfiguration(BaseModel):
    commit: Optional[UpdateBaseThresholdCommit] = None

    discount_configuration: Optional[DataUpdateSpendThresholdConfigurationDiscountConfiguration] = None

    is_enabled: Optional[bool] = None
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: Optional[PaymentGateConfigV2] = None

    threshold_amount: Optional[float] = None
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class DataUpdateSubscriptionQuantityUpdate(BaseModel):
    starting_at: datetime

    quantity: Optional[float] = None

    quantity_delta: Optional[float] = None


class DataUpdateSubscriptionSeatUpdatesAddSeatID(BaseModel):
    seat_ids: List[str]

    starting_at: datetime
    """Assigned seats will be added/removed starting at this date."""


class DataUpdateSubscriptionSeatUpdatesAddUnassignedSeat(BaseModel):
    quantity: float
    """
    The number of unassigned seats on the subscription will increase/decrease by
    this delta. Must be greater than 0.
    """

    starting_at: datetime
    """Unassigned seats will be updated starting at this date."""


class DataUpdateSubscriptionSeatUpdatesRemoveSeatID(BaseModel):
    seat_ids: List[str]

    starting_at: datetime
    """Assigned seats will be added/removed starting at this date."""


class DataUpdateSubscriptionSeatUpdatesRemoveUnassignedSeat(BaseModel):
    quantity: float
    """
    The number of unassigned seats on the subscription will increase/decrease by
    this delta. Must be greater than 0.
    """

    starting_at: datetime
    """Unassigned seats will be updated starting at this date."""


class DataUpdateSubscriptionSeatUpdates(BaseModel):
    """Manage subscription seats for subscriptions in SEAT_BASED mode."""

    add_seat_ids: Optional[List[DataUpdateSubscriptionSeatUpdatesAddSeatID]] = None
    """Adds seat IDs to the subscription.

    If there are unassigned seats, the new seat IDs will fill these unassigned seats
    and not increase the total subscription quantity. Otherwise, if there are more
    new seat IDs than unassigned seats, the total subscription quantity will
    increase.
    """

    add_unassigned_seats: Optional[List[DataUpdateSubscriptionSeatUpdatesAddUnassignedSeat]] = None
    """Adds unassigned seats to the subscription.

    This will increase the total subscription quantity.
    """

    remove_seat_ids: Optional[List[DataUpdateSubscriptionSeatUpdatesRemoveSeatID]] = None
    """Removes seat IDs from the subscription, if possible.

    If a seat ID is removed, the total subscription quantity will decrease.
    Otherwise, if the seat ID is not found on the subscription, this is a no-op.
    """

    remove_unassigned_seats: Optional[List[DataUpdateSubscriptionSeatUpdatesRemoveUnassignedSeat]] = None
    """Removes unassigned seats from the subscription.

    This will decrease the total subscription quantity if there are are unassigned
    seats.
    """


class DataUpdateSubscription(BaseModel):
    id: str

    ending_before: Optional[datetime] = None

    quantity_updates: Optional[List[DataUpdateSubscriptionQuantityUpdate]] = None

    seat_updates: Optional[DataUpdateSubscriptionSeatUpdates] = None
    """Manage subscription seats for subscriptions in SEAT_BASED mode."""


class Data(BaseModel):
    id: str

    add_commits: Optional[List[DataAddCommit]] = None

    add_credits: Optional[List[DataAddCredit]] = None

    add_discounts: Optional[List[Discount]] = None

    add_overrides: Optional[List[DataAddOverride]] = None

    add_prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfigurationV2] = None

    add_pro_services: Optional[List[ProService]] = None

    add_recurring_commits: Optional[List[DataAddRecurringCommit]] = None

    add_recurring_credits: Optional[List[DataAddRecurringCredit]] = None

    add_reseller_royalties: Optional[List[DataAddResellerRoyalty]] = None

    add_scheduled_charges: Optional[List[DataAddScheduledCharge]] = None

    add_spend_threshold_configuration: Optional[SpendThresholdConfigurationV2] = None

    add_subscriptions: Optional[List[DataAddSubscription]] = None
    """List of subscriptions on the contract."""

    add_usage_filters: Optional[List[DataAddUsageFilter]] = None

    archive_commits: Optional[List[DataArchiveCommit]] = None

    archive_credits: Optional[List[DataArchiveCredit]] = None

    archive_scheduled_charges: Optional[List[DataArchiveScheduledCharge]] = None

    remove_overrides: Optional[List[DataRemoveOverride]] = None

    timestamp: Optional[datetime] = None

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """

    update_commits: Optional[List[DataUpdateCommit]] = None

    update_contract_end_date: Optional[datetime] = None

    update_contract_name: Optional[str] = None
    """Value to update the contract name to.

    If not provided, the contract name will remain unchanged.
    """

    update_credits: Optional[List[DataUpdateCredit]] = None

    update_discounts: Optional[List[DataUpdateDiscount]] = None

    update_prepaid_balance_threshold_configuration: Optional[DataUpdatePrepaidBalanceThresholdConfiguration] = None

    update_recurring_commits: Optional[List[DataUpdateRecurringCommit]] = None

    update_recurring_credits: Optional[List[DataUpdateRecurringCredit]] = None

    update_refund_invoices: Optional[List[DataUpdateRefundInvoice]] = None

    update_scheduled_charges: Optional[List[DataUpdateScheduledCharge]] = None

    update_spend_threshold_configuration: Optional[DataUpdateSpendThresholdConfiguration] = None

    update_subscriptions: Optional[List[DataUpdateSubscription]] = None
    """Optional list of subscriptions to update."""


class ContractGetEditHistoryResponse(BaseModel):
    data: List[Data]
