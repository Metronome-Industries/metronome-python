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
    "ContractEditResponse",
    "Data",
    "DataEdit",
    "DataEditAddCommit",
    "DataEditAddCommitProduct",
    "DataEditAddCommitInvoiceSchedule",
    "DataEditAddCommitInvoiceScheduleScheduleItem",
    "DataEditAddCredit",
    "DataEditAddCreditProduct",
    "DataEditAddOverride",
    "DataEditAddOverrideOverrideSpecifier",
    "DataEditAddOverrideOverwriteRate",
    "DataEditAddOverrideProduct",
    "DataEditAddRecurringCommit",
    "DataEditAddRecurringCommitAccessAmount",
    "DataEditAddRecurringCommitCommitDuration",
    "DataEditAddRecurringCommitProduct",
    "DataEditAddRecurringCommitContract",
    "DataEditAddRecurringCommitInvoiceAmount",
    "DataEditAddRecurringCommitProrationRounding",
    "DataEditAddRecurringCommitProrationRoundingAccess",
    "DataEditAddRecurringCommitProrationRoundingInvoice",
    "DataEditAddRecurringCredit",
    "DataEditAddRecurringCreditAccessAmount",
    "DataEditAddRecurringCreditCommitDuration",
    "DataEditAddRecurringCreditProduct",
    "DataEditAddRecurringCreditContract",
    "DataEditAddRecurringCreditProrationRounding",
    "DataEditAddRecurringCreditProrationRoundingAccess",
    "DataEditAddResellerRoyalty",
    "DataEditAddScheduledCharge",
    "DataEditAddScheduledChargeProduct",
    "DataEditAddSubscription",
    "DataEditAddSubscriptionBillingPeriods",
    "DataEditAddSubscriptionBillingPeriodsCurrent",
    "DataEditAddSubscriptionBillingPeriodsNext",
    "DataEditAddSubscriptionBillingPeriodsPrevious",
    "DataEditAddSubscriptionProration",
    "DataEditAddSubscriptionProrationRounding",
    "DataEditAddSubscriptionQuantitySchedule",
    "DataEditAddSubscriptionSubscriptionRate",
    "DataEditAddSubscriptionSubscriptionRateProduct",
    "DataEditAddSubscriptionBillingCycleConfig",
    "DataEditAddSubscriptionSeatConfig",
    "DataEditAddUsageFilter",
    "DataEditArchiveCommit",
    "DataEditArchiveCredit",
    "DataEditArchiveScheduledCharge",
    "DataEditRemoveOverride",
    "DataEditUpdateCommit",
    "DataEditUpdateCommitAccessSchedule",
    "DataEditUpdateCommitAccessScheduleAddScheduleItem",
    "DataEditUpdateCommitAccessScheduleRemoveScheduleItem",
    "DataEditUpdateCommitAccessScheduleUpdateScheduleItem",
    "DataEditUpdateCommitInvoiceSchedule",
    "DataEditUpdateCommitInvoiceScheduleAddScheduleItem",
    "DataEditUpdateCommitInvoiceScheduleRemoveScheduleItem",
    "DataEditUpdateCommitInvoiceScheduleUpdateScheduleItem",
    "DataEditUpdateCredit",
    "DataEditUpdateCreditAccessSchedule",
    "DataEditUpdateCreditAccessScheduleAddScheduleItem",
    "DataEditUpdateCreditAccessScheduleRemoveScheduleItem",
    "DataEditUpdateCreditAccessScheduleUpdateScheduleItem",
    "DataEditUpdateDiscount",
    "DataEditUpdateDiscountSchedule",
    "DataEditUpdateDiscountScheduleRecurringSchedule",
    "DataEditUpdateDiscountScheduleScheduleItem",
    "DataEditUpdatePrepaidBalanceThresholdConfiguration",
    "DataEditUpdatePrepaidBalanceThresholdConfigurationCommit",
    "DataEditUpdatePrepaidBalanceThresholdConfigurationDiscountConfiguration",
    "DataEditUpdatePrepaidBalanceThresholdConfigurationDiscountConfigurationCap",
    "DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifier",
    "DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExclude",
    "DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExcludeCustomFieldFilter",
    "DataEditUpdateRecurringCommit",
    "DataEditUpdateRecurringCommitAccessAmount",
    "DataEditUpdateRecurringCommitInvoiceAmount",
    "DataEditUpdateRecurringCommitProrationRounding",
    "DataEditUpdateRecurringCommitProrationRoundingAccess",
    "DataEditUpdateRecurringCommitProrationRoundingInvoice",
    "DataEditUpdateRecurringCredit",
    "DataEditUpdateRecurringCreditAccessAmount",
    "DataEditUpdateRecurringCreditProrationRounding",
    "DataEditUpdateRecurringCreditProrationRoundingAccess",
    "DataEditUpdateRefundInvoice",
    "DataEditUpdateScheduledCharge",
    "DataEditUpdateScheduledChargeInvoiceSchedule",
    "DataEditUpdateScheduledChargeInvoiceScheduleAddScheduleItem",
    "DataEditUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem",
    "DataEditUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem",
    "DataEditUpdateSpendThresholdConfiguration",
    "DataEditUpdateSpendThresholdConfigurationDiscountConfiguration",
    "DataEditUpdateSpendThresholdConfigurationDiscountConfigurationCap",
    "DataEditUpdateSubscription",
    "DataEditUpdateSubscriptionQuantityUpdate",
    "DataEditUpdateSubscriptionSeatUpdates",
    "DataEditUpdateSubscriptionSeatUpdatesAddSeatID",
    "DataEditUpdateSubscriptionSeatUpdatesAddUnassignedSeat",
    "DataEditUpdateSubscriptionSeatUpdatesRemoveSeatID",
    "DataEditUpdateSubscriptionSeatUpdatesRemoveUnassignedSeat",
]


class DataEditAddCommitProduct(BaseModel):
    id: str

    name: str


class DataEditAddCommitInvoiceScheduleScheduleItem(BaseModel):
    id: str

    timestamp: datetime

    amount: Optional[float] = None

    invoice_id: Optional[str] = None

    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataEditAddCommitInvoiceSchedule(BaseModel):
    """The schedule that the customer will be invoiced for this commit."""

    credit_type: Optional[CreditTypeData] = None

    do_not_invoice: Optional[bool] = None
    """If true, this schedule will not generate an invoice."""

    schedule_items: Optional[List[DataEditAddCommitInvoiceScheduleScheduleItem]] = None


class DataEditAddCommit(BaseModel):
    id: str

    product: DataEditAddCommitProduct

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

    invoice_schedule: Optional[DataEditAddCommitInvoiceSchedule] = None
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


class DataEditAddCreditProduct(BaseModel):
    id: str

    name: str


class DataEditAddCredit(BaseModel):
    id: str

    product: DataEditAddCreditProduct

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


class DataEditAddOverrideOverrideSpecifier(BaseModel):
    any_commit_or_credit_ids: Optional[List[str]] = None

    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None


class DataEditAddOverrideOverwriteRate(BaseModel):
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


class DataEditAddOverrideProduct(BaseModel):
    id: str

    name: str


class DataEditAddOverride(BaseModel):
    id: str

    created_at: datetime

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[DataEditAddOverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[OverrideTier]] = None

    overwrite_rate: Optional[DataEditAddOverrideOverwriteRate] = None

    priority: Optional[float] = None

    product: Optional[DataEditAddOverrideProduct] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None


class DataEditAddRecurringCommitAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataEditAddRecurringCommitCommitDuration(BaseModel):
    """The amount of time the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataEditAddRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataEditAddRecurringCommitContract(BaseModel):
    id: str


class DataEditAddRecurringCommitInvoiceAmount(BaseModel):
    """The amount the customer should be billed for the commit. Not required."""

    credit_type_id: str

    quantity: float

    unit_price: float


class DataEditAddRecurringCommitProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataEditAddRecurringCommitProrationRoundingInvoice(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataEditAddRecurringCommitProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring commit amounts."""

    access: Optional[DataEditAddRecurringCommitProrationRoundingAccess] = None

    invoice: Optional[DataEditAddRecurringCommitProrationRoundingInvoice] = None


class DataEditAddRecurringCommit(BaseModel):
    id: str

    access_amount: DataEditAddRecurringCommitAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataEditAddRecurringCommitCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataEditAddRecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataEditAddRecurringCommitContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for recurring credit hierarchy access control"""

    invoice_amount: Optional[DataEditAddRecurringCommitInvoiceAmount] = None
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

    proration_rounding: Optional[DataEditAddRecurringCommitProrationRounding] = None
    """Rounding configuration for prorated recurring commit amounts."""

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY", "DAILY"]] = None
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

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[RecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataEditAddRecurringCreditAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataEditAddRecurringCreditCommitDuration(BaseModel):
    """The amount of time the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataEditAddRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataEditAddRecurringCreditContract(BaseModel):
    id: str


class DataEditAddRecurringCreditProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataEditAddRecurringCreditProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring credit amounts."""

    access: Optional[DataEditAddRecurringCreditProrationRoundingAccess] = None


class DataEditAddRecurringCredit(BaseModel):
    id: str

    access_amount: DataEditAddRecurringCreditAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataEditAddRecurringCreditCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataEditAddRecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataEditAddRecurringCreditContract] = None

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

    proration_rounding: Optional[DataEditAddRecurringCreditProrationRounding] = None
    """Rounding configuration for prorated recurring credit amounts."""

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY", "DAILY"]] = None
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

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[RecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataEditAddResellerRoyalty(BaseModel):
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


class DataEditAddScheduledChargeProduct(BaseModel):
    id: str

    name: str


class DataEditAddScheduledCharge(BaseModel):
    id: str

    product: DataEditAddScheduledChargeProduct

    schedule: SchedulePointInTime

    name: Optional[str] = None
    """displayed on invoices"""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class DataEditAddSubscriptionBillingPeriodsCurrent(BaseModel):
    ending_before: datetime

    starting_at: datetime


class DataEditAddSubscriptionBillingPeriodsNext(BaseModel):
    ending_before: datetime

    starting_at: datetime


class DataEditAddSubscriptionBillingPeriodsPrevious(BaseModel):
    ending_before: datetime

    starting_at: datetime


class DataEditAddSubscriptionBillingPeriods(BaseModel):
    """Previous, current, and next billing periods for the subscription."""

    current: Optional[DataEditAddSubscriptionBillingPeriodsCurrent] = None

    next: Optional[DataEditAddSubscriptionBillingPeriodsNext] = None

    previous: Optional[DataEditAddSubscriptionBillingPeriodsPrevious] = None


class DataEditAddSubscriptionProrationRounding(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataEditAddSubscriptionProration(BaseModel):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]

    is_prorated: bool

    rounding: Optional[DataEditAddSubscriptionProrationRounding] = None


class DataEditAddSubscriptionQuantitySchedule(BaseModel):
    quantity: float

    starting_at: datetime

    ending_before: Optional[datetime] = None


class DataEditAddSubscriptionSubscriptionRateProduct(BaseModel):
    id: str

    name: str


class DataEditAddSubscriptionSubscriptionRate(BaseModel):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    product: DataEditAddSubscriptionSubscriptionRateProduct


class DataEditAddSubscriptionBillingCycleConfig(BaseModel):
    anchor_date: datetime
    """The date this subscription's billing cycle is anchored to."""

    invoice_placement: Literal["ON_SCHEDULED_INVOICE", "ON_USAGE_INVOICE"]
    """
    Controls whether this subscription consolidates onto usage invoices or gets its
    own scheduled invoice.
    """


class DataEditAddSubscriptionSeatConfig(BaseModel):
    seat_group_key: str
    """
    The property name, sent on usage events, that identifies the seat ID associated
    with the usage event. For example, the property name might be seat_id or
    user_id. The property must be set as a group key on billable metrics and a
    presentation/pricing group key on contract products. This allows linked
    recurring credits with an allocation per seat to be consumed by only one seat's
    usage.
    """


class DataEditAddSubscription(BaseModel):
    billing_periods: DataEditAddSubscriptionBillingPeriods
    """Previous, current, and next billing periods for the subscription."""

    collection_schedule: Literal["ADVANCE", "ARREARS"]

    proration: DataEditAddSubscriptionProration

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

    quantity_schedule: List[DataEditAddSubscriptionQuantitySchedule]
    """List of quantity schedule items for the subscription.

    Only includes the current quantity and future quantity changes.
    """

    starting_at: datetime

    subscription_rate: DataEditAddSubscriptionSubscriptionRate

    id: Optional[str] = None

    billing_cycle_config: Optional[DataEditAddSubscriptionBillingCycleConfig] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    ending_before: Optional[datetime] = None

    fiat_credit_type_id: Optional[str] = None

    name: Optional[str] = None

    seat_config: Optional[DataEditAddSubscriptionSeatConfig] = None


class DataEditAddUsageFilter(BaseModel):
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


class DataEditArchiveCommit(BaseModel):
    id: str


class DataEditArchiveCredit(BaseModel):
    id: str


class DataEditArchiveScheduledCharge(BaseModel):
    id: str


class DataEditRemoveOverride(BaseModel):
    id: str


class DataEditUpdateCommitAccessScheduleAddScheduleItem(BaseModel):
    amount: float

    ending_before: datetime
    """RFC 3339 timestamp (exclusive)"""

    starting_at: datetime
    """RFC 3339 timestamp (inclusive)"""


class DataEditUpdateCommitAccessScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataEditUpdateCommitAccessScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    ending_before: Optional[datetime] = None
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Optional[datetime] = None
    """RFC 3339 timestamp (inclusive)"""


class DataEditUpdateCommitAccessSchedule(BaseModel):
    add_schedule_items: Optional[List[DataEditUpdateCommitAccessScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataEditUpdateCommitAccessScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataEditUpdateCommitAccessScheduleUpdateScheduleItem]] = None


class DataEditUpdateCommitInvoiceScheduleAddScheduleItem(BaseModel):
    timestamp: datetime

    amount: Optional[float] = None

    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataEditUpdateCommitInvoiceScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataEditUpdateCommitInvoiceScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    quantity: Optional[float] = None

    timestamp: Optional[datetime] = None

    unit_price: Optional[float] = None


class DataEditUpdateCommitInvoiceSchedule(BaseModel):
    add_schedule_items: Optional[List[DataEditUpdateCommitInvoiceScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataEditUpdateCommitInvoiceScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataEditUpdateCommitInvoiceScheduleUpdateScheduleItem]] = None


class DataEditUpdateCommit(BaseModel):
    id: str

    access_schedule: Optional[DataEditUpdateCommitAccessSchedule] = None

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

    invoice_schedule: Optional[DataEditUpdateCommitInvoiceSchedule] = None

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


class DataEditUpdateCreditAccessScheduleAddScheduleItem(BaseModel):
    amount: float

    ending_before: datetime
    """RFC 3339 timestamp (exclusive)"""

    starting_at: datetime
    """RFC 3339 timestamp (inclusive)"""


class DataEditUpdateCreditAccessScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataEditUpdateCreditAccessScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    ending_before: Optional[datetime] = None
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Optional[datetime] = None
    """RFC 3339 timestamp (inclusive)"""


class DataEditUpdateCreditAccessSchedule(BaseModel):
    add_schedule_items: Optional[List[DataEditUpdateCreditAccessScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataEditUpdateCreditAccessScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataEditUpdateCreditAccessScheduleUpdateScheduleItem]] = None


class DataEditUpdateCredit(BaseModel):
    id: str

    access_schedule: Optional[DataEditUpdateCreditAccessSchedule] = None

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


class DataEditUpdateDiscountScheduleRecurringSchedule(BaseModel):
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


class DataEditUpdateDiscountScheduleScheduleItem(BaseModel):
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


class DataEditUpdateDiscountSchedule(BaseModel):
    """Must provide either schedule_items or recurring_schedule."""

    credit_type_id: Optional[str] = None
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: Optional[bool] = None
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    recurring_schedule: Optional[DataEditUpdateDiscountScheduleRecurringSchedule] = None
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Optional[List[DataEditUpdateDiscountScheduleScheduleItem]] = None
    """Either provide amount or provide both unit_price and quantity."""


class DataEditUpdateDiscount(BaseModel):
    id: str

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    schedule: Optional[DataEditUpdateDiscountSchedule] = None
    """Must provide either schedule_items or recurring_schedule."""


class DataEditUpdatePrepaidBalanceThresholdConfigurationCommit(UpdateBaseThresholdCommit):
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


class DataEditUpdatePrepaidBalanceThresholdConfigurationDiscountConfigurationCap(BaseModel):
    """Update the discount cap. Set to null to remove an existing cap."""

    amount: float
    """Accumulated spend ceiling above which the discount stops applying."""

    spend_tracker_alias: str
    """Alias of the spend tracker this cap is measured against."""


class DataEditUpdatePrepaidBalanceThresholdConfigurationDiscountConfiguration(BaseModel):
    cap: Optional[DataEditUpdatePrepaidBalanceThresholdConfigurationDiscountConfigurationCap] = None
    """Update the discount cap. Set to null to remove an existing cap."""

    payment_fraction: Optional[float] = None
    """
    The fraction of the original amount that the customer pays after applying the
    discount. Set to null to remove the discount fraction. For example, 0.85 means
    the customer pays 85% of the original amount (a 15% discount).
    """


class DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExcludeCustomFieldFilter(BaseModel):
    entity: Literal["Commit", "ContractCredit", "ContractCreditOrCommit"]

    key: str

    value: str


class DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExclude(BaseModel):
    custom_field_filters: List[
        DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExcludeCustomFieldFilter
    ]


class DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifier(BaseModel):
    exclude: List[DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifierExclude]


class DataEditUpdatePrepaidBalanceThresholdConfiguration(BaseModel):
    commit: Optional[DataEditUpdatePrepaidBalanceThresholdConfigurationCommit] = None

    custom_credit_type_id: Optional[str] = None
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """

    discount_configuration: Optional[DataEditUpdatePrepaidBalanceThresholdConfigurationDiscountConfiguration] = None

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
        List[DataEditUpdatePrepaidBalanceThresholdConfigurationThresholdBalanceSpecifier]
    ] = None
    """
    Determines which balances are excluded from remaining balance calculation for
    threshold billing.
    """


class DataEditUpdateRecurringCommitAccessAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataEditUpdateRecurringCommitInvoiceAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataEditUpdateRecurringCommitProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataEditUpdateRecurringCommitProrationRoundingInvoice(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataEditUpdateRecurringCommitProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring commit amounts."""

    access: Optional[DataEditUpdateRecurringCommitProrationRoundingAccess] = None

    invoice: Optional[DataEditUpdateRecurringCommitProrationRoundingInvoice] = None


class DataEditUpdateRecurringCommit(BaseModel):
    id: str

    access_amount: Optional[DataEditUpdateRecurringCommitAccessAmount] = None

    ending_before: Optional[datetime] = None

    invoice_amount: Optional[DataEditUpdateRecurringCommitInvoiceAmount] = None

    proration_rounding: Optional[DataEditUpdateRecurringCommitProrationRounding] = None
    """Rounding configuration for prorated recurring commit amounts."""

    rate_type: Optional[Literal["LIST_RATE", "COMMIT_RATE"]] = None


class DataEditUpdateRecurringCreditAccessAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataEditUpdateRecurringCreditProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataEditUpdateRecurringCreditProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring credit amounts."""

    access: Optional[DataEditUpdateRecurringCreditProrationRoundingAccess] = None


class DataEditUpdateRecurringCredit(BaseModel):
    id: str

    access_amount: Optional[DataEditUpdateRecurringCreditAccessAmount] = None

    ending_before: Optional[datetime] = None

    proration_rounding: Optional[DataEditUpdateRecurringCreditProrationRounding] = None
    """Rounding configuration for prorated recurring credit amounts."""

    rate_type: Optional[Literal["LIST_RATE", "COMMIT_RATE"]] = None


class DataEditUpdateRefundInvoice(BaseModel):
    date: datetime

    invoice_id: str


class DataEditUpdateScheduledChargeInvoiceScheduleAddScheduleItem(BaseModel):
    timestamp: datetime

    amount: Optional[float] = None

    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataEditUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem(BaseModel):
    id: str


class DataEditUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem(BaseModel):
    id: str

    amount: Optional[float] = None

    quantity: Optional[float] = None

    timestamp: Optional[datetime] = None

    unit_price: Optional[float] = None


class DataEditUpdateScheduledChargeInvoiceSchedule(BaseModel):
    add_schedule_items: Optional[List[DataEditUpdateScheduledChargeInvoiceScheduleAddScheduleItem]] = None

    remove_schedule_items: Optional[List[DataEditUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem]] = None

    update_schedule_items: Optional[List[DataEditUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem]] = None


class DataEditUpdateScheduledCharge(BaseModel):
    id: str

    invoice_schedule: Optional[DataEditUpdateScheduledChargeInvoiceSchedule] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None


class DataEditUpdateSpendThresholdConfigurationDiscountConfigurationCap(BaseModel):
    """Update the discount cap. Set to null to remove an existing cap."""

    amount: float
    """Accumulated spend ceiling above which the discount stops applying."""

    spend_tracker_alias: str
    """Alias of the spend tracker this cap is measured against."""


class DataEditUpdateSpendThresholdConfigurationDiscountConfiguration(BaseModel):
    cap: Optional[DataEditUpdateSpendThresholdConfigurationDiscountConfigurationCap] = None
    """Update the discount cap. Set to null to remove an existing cap."""

    payment_fraction: Optional[float] = None
    """
    The fraction of the original amount that the customer pays after applying the
    discount. Set to null to remove the discount fraction. For example, 0.85 means
    the customer pays 85% of the original amount (a 15% discount).
    """


class DataEditUpdateSpendThresholdConfiguration(BaseModel):
    commit: Optional[UpdateBaseThresholdCommit] = None

    discount_configuration: Optional[DataEditUpdateSpendThresholdConfigurationDiscountConfiguration] = None

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


class DataEditUpdateSubscriptionQuantityUpdate(BaseModel):
    starting_at: datetime

    quantity: Optional[float] = None

    quantity_delta: Optional[float] = None


class DataEditUpdateSubscriptionSeatUpdatesAddSeatID(BaseModel):
    seat_ids: List[str]

    starting_at: datetime
    """Assigned seats will be added/removed starting at this date."""


class DataEditUpdateSubscriptionSeatUpdatesAddUnassignedSeat(BaseModel):
    quantity: float
    """
    The number of unassigned seats on the subscription will increase/decrease by
    this delta. Must be greater than 0.
    """

    starting_at: datetime
    """Unassigned seats will be updated starting at this date."""


class DataEditUpdateSubscriptionSeatUpdatesRemoveSeatID(BaseModel):
    seat_ids: List[str]

    starting_at: datetime
    """Assigned seats will be added/removed starting at this date."""


class DataEditUpdateSubscriptionSeatUpdatesRemoveUnassignedSeat(BaseModel):
    quantity: float
    """
    The number of unassigned seats on the subscription will increase/decrease by
    this delta. Must be greater than 0.
    """

    starting_at: datetime
    """Unassigned seats will be updated starting at this date."""


class DataEditUpdateSubscriptionSeatUpdates(BaseModel):
    """Manage subscription seats for subscriptions in SEAT_BASED mode."""

    add_seat_ids: Optional[List[DataEditUpdateSubscriptionSeatUpdatesAddSeatID]] = None
    """Adds seat IDs to the subscription.

    If there are unassigned seats, the new seat IDs will fill these unassigned seats
    and not increase the total subscription quantity. Otherwise, if there are more
    new seat IDs than unassigned seats, the total subscription quantity will
    increase.
    """

    add_unassigned_seats: Optional[List[DataEditUpdateSubscriptionSeatUpdatesAddUnassignedSeat]] = None
    """Adds unassigned seats to the subscription.

    This will increase the total subscription quantity.
    """

    remove_seat_ids: Optional[List[DataEditUpdateSubscriptionSeatUpdatesRemoveSeatID]] = None
    """Removes seat IDs from the subscription, if possible.

    If a seat ID is removed, the total subscription quantity will decrease.
    Otherwise, if the seat ID is not found on the subscription, this is a no-op.
    """

    remove_unassigned_seats: Optional[List[DataEditUpdateSubscriptionSeatUpdatesRemoveUnassignedSeat]] = None
    """Removes unassigned seats from the subscription.

    This will decrease the total subscription quantity if there are are unassigned
    seats.
    """


class DataEditUpdateSubscription(BaseModel):
    id: str

    ending_before: Optional[datetime] = None

    quantity_updates: Optional[List[DataEditUpdateSubscriptionQuantityUpdate]] = None

    seat_updates: Optional[DataEditUpdateSubscriptionSeatUpdates] = None
    """Manage subscription seats for subscriptions in SEAT_BASED mode."""


class DataEdit(BaseModel):
    id: str

    add_commits: Optional[List[DataEditAddCommit]] = None

    add_credits: Optional[List[DataEditAddCredit]] = None

    add_discounts: Optional[List[Discount]] = None

    add_overrides: Optional[List[DataEditAddOverride]] = None

    add_prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfigurationV2] = None

    add_pro_services: Optional[List[ProService]] = None

    add_recurring_commits: Optional[List[DataEditAddRecurringCommit]] = None

    add_recurring_credits: Optional[List[DataEditAddRecurringCredit]] = None

    add_reseller_royalties: Optional[List[DataEditAddResellerRoyalty]] = None

    add_scheduled_charges: Optional[List[DataEditAddScheduledCharge]] = None

    add_spend_threshold_configuration: Optional[SpendThresholdConfigurationV2] = None

    add_subscriptions: Optional[List[DataEditAddSubscription]] = None
    """List of subscriptions on the contract."""

    add_usage_filters: Optional[List[DataEditAddUsageFilter]] = None

    archive_commits: Optional[List[DataEditArchiveCommit]] = None

    archive_credits: Optional[List[DataEditArchiveCredit]] = None

    archive_scheduled_charges: Optional[List[DataEditArchiveScheduledCharge]] = None

    remove_overrides: Optional[List[DataEditRemoveOverride]] = None

    timestamp: Optional[datetime] = None

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """

    update_commits: Optional[List[DataEditUpdateCommit]] = None

    update_contract_end_date: Optional[datetime] = None

    update_contract_name: Optional[str] = None
    """Value to update the contract name to.

    If not provided, the contract name will remain unchanged.
    """

    update_credits: Optional[List[DataEditUpdateCredit]] = None

    update_discounts: Optional[List[DataEditUpdateDiscount]] = None

    update_prepaid_balance_threshold_configuration: Optional[DataEditUpdatePrepaidBalanceThresholdConfiguration] = None

    update_recurring_commits: Optional[List[DataEditUpdateRecurringCommit]] = None

    update_recurring_credits: Optional[List[DataEditUpdateRecurringCredit]] = None

    update_refund_invoices: Optional[List[DataEditUpdateRefundInvoice]] = None

    update_scheduled_charges: Optional[List[DataEditUpdateScheduledCharge]] = None

    update_spend_threshold_configuration: Optional[DataEditUpdateSpendThresholdConfiguration] = None

    update_subscriptions: Optional[List[DataEditUpdateSubscription]] = None
    """Optional list of subscriptions to update."""


class Data(BaseModel):
    id: str

    edit: Optional[DataEdit] = None


class ContractEditResponse(BaseModel):
    data: Data
