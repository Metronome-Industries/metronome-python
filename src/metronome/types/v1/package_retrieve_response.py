# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.override_tier import OverrideTier
from ..shared.overwrite_rate import OverwriteRate
from ..shared.commit_specifier import CommitSpecifier
from ..shared.credit_type_data import CreditTypeData
from ..shared.spend_threshold_configuration import SpendThresholdConfiguration
from ..shared.prepaid_balance_threshold_configuration import PrepaidBalanceThresholdConfiguration

__all__ = [
    "PackageRetrieveResponse",
    "Data",
    "DataCommit",
    "DataCommitProduct",
    "DataCommitAccessSchedule",
    "DataCommitAccessScheduleScheduleItem",
    "DataCommitAccessScheduleScheduleItemDuration",
    "DataCommitAccessScheduleScheduleItemStartingAtOffset",
    "DataCommitInvoiceSchedule",
    "DataCommitInvoiceScheduleScheduleItem",
    "DataCommitInvoiceScheduleScheduleItemDateOffset",
    "DataOverride",
    "DataOverrideOverrideSpecifier",
    "DataOverrideStartingAtOffset",
    "DataOverrideDuration",
    "DataOverrideProduct",
    "DataScheduledCharge",
    "DataScheduledChargeProduct",
    "DataScheduledChargeSchedule",
    "DataScheduledChargeScheduleScheduleItem",
    "DataScheduledChargeScheduleScheduleItemDateOffset",
    "DataUsageStatementSchedule",
    "DataAlias",
    "DataCredit",
    "DataCreditProduct",
    "DataCreditAccessSchedule",
    "DataCreditAccessScheduleScheduleItem",
    "DataCreditAccessScheduleScheduleItemDuration",
    "DataCreditAccessScheduleScheduleItemStartingAtOffset",
    "DataDuration",
    "DataRecurringCommit",
    "DataRecurringCommitAccessAmount",
    "DataRecurringCommitCommitDuration",
    "DataRecurringCommitProduct",
    "DataRecurringCommitStartingAtOffset",
    "DataRecurringCommitDuration",
    "DataRecurringCommitInvoiceAmount",
    "DataRecurringCommitSubscriptionConfig",
    "DataRecurringCommitSubscriptionConfigApplySeatIncreaseConfig",
    "DataRecurringCredit",
    "DataRecurringCreditAccessAmount",
    "DataRecurringCreditCommitDuration",
    "DataRecurringCreditProduct",
    "DataRecurringCreditStartingAtOffset",
    "DataRecurringCreditDuration",
    "DataRecurringCreditSubscriptionConfig",
    "DataRecurringCreditSubscriptionConfigApplySeatIncreaseConfig",
    "DataSubscription",
    "DataSubscriptionProration",
    "DataSubscriptionSubscriptionRate",
    "DataSubscriptionSubscriptionRateProduct",
    "DataSubscriptionDuration",
    "DataSubscriptionSeatConfig",
    "DataSubscriptionStartingAtOffset",
]


class DataCommitProduct(BaseModel):
    id: str

    name: str


class DataCommitAccessScheduleScheduleItemDuration(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataCommitAccessScheduleScheduleItemStartingAtOffset(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataCommitAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    duration: DataCommitAccessScheduleScheduleItemDuration

    starting_at_offset: DataCommitAccessScheduleScheduleItemStartingAtOffset


class DataCommitAccessSchedule(BaseModel):
    """
    The schedule that the customer will gain access to the credits purposed with this commit.
    """

    credit_type: CreditTypeData

    schedule_items: List[DataCommitAccessScheduleScheduleItem]


class DataCommitInvoiceScheduleScheduleItemDateOffset(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataCommitInvoiceScheduleScheduleItem(BaseModel):
    id: str

    date_offset: DataCommitInvoiceScheduleScheduleItemDateOffset

    quantity: float

    unit_price: float


class DataCommitInvoiceSchedule(BaseModel):
    """The schedule that the customer will be invoiced for this commit."""

    credit_type: CreditTypeData

    do_not_invoice: bool
    """If true, this schedule will not generate an invoice."""

    schedule_items: List[DataCommitInvoiceScheduleScheduleItem]


class DataCommit(BaseModel):
    id: str

    product: DataCommitProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[DataCommitAccessSchedule] = None
    """
    The schedule that the customer will gain access to the credits purposed with
    this commit.
    """

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    invoice_schedule: Optional[DataCommitInvoiceSchedule] = None
    """The schedule that the customer will be invoiced for this commit."""

    name: Optional[str] = None

    priority: Optional[float] = None
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    rollover_fraction: Optional[float] = None

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataOverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_template_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_template_ids: Optional[List[str]] = None

    recurring_credit_template_ids: Optional[List[str]] = None


class DataOverrideStartingAtOffset(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataOverrideDuration(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataOverrideProduct(BaseModel):
    id: str

    name: str


class DataOverride(BaseModel):
    id: str

    override_specifiers: List[DataOverrideOverrideSpecifier]

    starting_at_offset: DataOverrideStartingAtOffset

    applicable_product_tags: Optional[List[str]] = None

    duration: Optional[DataOverrideDuration] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    multiplier: Optional[float] = None

    override_tiers: Optional[List[OverrideTier]] = None

    overwrite_rate: Optional[OverwriteRate] = None

    priority: Optional[float] = None

    product: Optional[DataOverrideProduct] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None


class DataScheduledChargeProduct(BaseModel):
    id: str

    name: str


class DataScheduledChargeScheduleScheduleItemDateOffset(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataScheduledChargeScheduleScheduleItem(BaseModel):
    id: str

    date_offset: DataScheduledChargeScheduleScheduleItemDateOffset

    quantity: float

    unit_price: float


class DataScheduledChargeSchedule(BaseModel):
    credit_type: CreditTypeData

    schedule_items: List[DataScheduledChargeScheduleScheduleItem]


class DataScheduledCharge(BaseModel):
    id: str

    product: DataScheduledChargeProduct

    schedule: DataScheduledChargeSchedule

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    name: Optional[str] = None


class DataUsageStatementSchedule(BaseModel):
    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]


class DataAlias(BaseModel):
    name: str

    ending_before: Optional[datetime] = None

    starting_at: Optional[datetime] = None


class DataCreditProduct(BaseModel):
    id: str

    name: str


class DataCreditAccessScheduleScheduleItemDuration(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataCreditAccessScheduleScheduleItemStartingAtOffset(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataCreditAccessScheduleScheduleItem(BaseModel):
    id: str

    amount: float

    duration: DataCreditAccessScheduleScheduleItemDuration

    starting_at_offset: DataCreditAccessScheduleScheduleItemStartingAtOffset


class DataCreditAccessSchedule(BaseModel):
    credit_type: CreditTypeData

    schedule_items: List[DataCreditAccessScheduleScheduleItem]


class DataCredit(BaseModel):
    id: str

    product: DataCreditProduct

    access_schedule: Optional[DataCreditAccessSchedule] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    name: Optional[str] = None

    priority: Optional[float] = None

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class DataDuration(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataRecurringCommitAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataRecurringCommitCommitDuration(BaseModel):
    """The amount of time each of the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataRecurringCommitStartingAtOffset(BaseModel):
    """
    Offset relative to the contract start date that determines the start time for the first commit
    """

    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataRecurringCommitDuration(BaseModel):
    """
    Offset relative to the recurring credit start that determines when the contract will stop creating recurring commits. optional
    """

    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataRecurringCommitInvoiceAmount(BaseModel):
    """The amount the customer should be billed for the commit."""

    credit_type_id: str

    quantity: float

    unit_price: float


class DataRecurringCommitSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class DataRecurringCommitSubscriptionConfig(BaseModel):
    """Attach a subscription to the recurring commit/credit."""

    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: DataRecurringCommitSubscriptionConfigApplySeatIncreaseConfig

    subscription_template_id: str


class DataRecurringCommit(BaseModel):
    id: str

    access_amount: DataRecurringCommitAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataRecurringCommitCommitDuration
    """The amount of time each of the created commits will be valid for"""

    priority: float

    product: DataRecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at_offset: DataRecurringCommitStartingAtOffset
    """
    Offset relative to the contract start date that determines the start time for
    the first commit
    """

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    description: Optional[str] = None

    duration: Optional[DataRecurringCommitDuration] = None
    """
    Offset relative to the recurring credit start that determines when the contract
    will stop creating recurring commits. optional
    """

    invoice_amount: Optional[DataRecurringCommitInvoiceAmount] = None
    """The amount the customer should be billed for the commit."""

    name: Optional[str] = None

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

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[DataRecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataRecurringCreditAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataRecurringCreditCommitDuration(BaseModel):
    """The amount of time each of the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataRecurringCreditStartingAtOffset(BaseModel):
    """
    Offset relative to the contract start date that determines the start time for the first commit
    """

    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataRecurringCreditDuration(BaseModel):
    """
    Offset relative to the recurring credit start that determines when the contract will stop creating recurring commits. optional
    """

    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataRecurringCreditSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class DataRecurringCreditSubscriptionConfig(BaseModel):
    """Attach a subscription to the recurring commit/credit."""

    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: DataRecurringCreditSubscriptionConfigApplySeatIncreaseConfig

    subscription_template_id: str


class DataRecurringCredit(BaseModel):
    id: str

    access_amount: DataRecurringCreditAccessAmount
    """The amount of commit to grant."""

    commit_duration: DataRecurringCreditCommitDuration
    """The amount of time each of the created commits will be valid for"""

    priority: float

    product: DataRecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at_offset: DataRecurringCreditStartingAtOffset
    """
    Offset relative to the contract start date that determines the start time for
    the first commit
    """

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    description: Optional[str] = None

    duration: Optional[DataRecurringCreditDuration] = None
    """
    Offset relative to the recurring credit start that determines when the contract
    will stop creating recurring commits. optional
    """

    name: Optional[str] = None

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

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[DataRecurringCreditSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataSubscriptionProration(BaseModel):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]

    is_prorated: bool


class DataSubscriptionSubscriptionRateProduct(BaseModel):
    id: str

    name: str


class DataSubscriptionSubscriptionRate(BaseModel):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    product: DataSubscriptionSubscriptionRateProduct


class DataSubscriptionDuration(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataSubscriptionSeatConfig(BaseModel):
    seat_group_key: str
    """
    The property name, sent on usage events, that identifies the seat ID associated
    with the usage event. For example, the property name might be seat_id or
    user_id. The property must be set as a group key on billable metrics and a
    presentation/pricing group key on contract products. This allows linked
    recurring credits with an allocation per seat to be consumed by only one seat's
    usage.
    """


class DataSubscriptionStartingAtOffset(BaseModel):
    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class DataSubscription(BaseModel):
    collection_schedule: Literal["ADVANCE", "ARREARS"]

    proration: DataSubscriptionProration

    subscription_rate: DataSubscriptionSubscriptionRate

    id: Optional[str] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: Optional[str] = None

    duration: Optional[DataSubscriptionDuration] = None

    fiat_credit_type_id: Optional[str] = None

    initial_quantity: Optional[float] = None

    name: Optional[str] = None

    quantity_management_mode: Optional[Literal["SEAT_BASED", "QUANTITY_ONLY"]] = None
    """Determines how the subscription's quantity is controlled.

    Defaults to QUANTITY_ONLY. **QUANTITY_ONLY**: The subscription quantity is
    specified directly on the subscription. `initial_quantity` must be provided with
    this option. Compatible with recurring commits/credits that use POOLED
    allocation. **SEAT_BASED**: Use when you want to pass specific seat identifiers
    (e.g. add user_123) to increment and decrement a subscription quantity, rather
    than directly providing the quantity. You must use a SEAT_BASED subscription to
    use a linked recurring credit with an allocation per seat. `seat_config` must be
    provided with this option.
    """

    seat_config: Optional[DataSubscriptionSeatConfig] = None

    starting_at_offset: Optional[DataSubscriptionStartingAtOffset] = None


class Data(BaseModel):
    id: str

    commits: List[DataCommit]

    created_at: datetime

    created_by: str

    overrides: List[DataOverride]

    scheduled_charges: List[DataScheduledCharge]

    usage_statement_schedule: DataUsageStatementSchedule

    aliases: Optional[List[DataAlias]] = None

    archived_at: Optional[datetime] = None

    billing_provider: Optional[
        Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
            "metronome",
        ]
    ] = None

    credits: Optional[List[DataCredit]] = None

    delivery_method: Optional[Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]] = None

    duration: Optional[DataDuration] = None

    multiplier_override_prioritization: Optional[Literal["LOWEST_MULTIPLIER", "EXPLICIT"]] = None
    """
    Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
    prices automatically. EXPLICIT prioritization requires specifying priorities for
    each multiplier; the one with the lowest priority value will be prioritized
    first.
    """

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfiguration] = None

    rate_card_id: Optional[str] = None

    recurring_commits: Optional[List[DataRecurringCommit]] = None

    recurring_credits: Optional[List[DataRecurringCredit]] = None

    scheduled_charges_on_usage_invoices: Optional[Literal["ALL"]] = None
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    spend_threshold_configuration: Optional[SpendThresholdConfiguration] = None

    subscriptions: Optional[List[DataSubscription]] = None

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """


class PackageRetrieveResponse(BaseModel):
    data: Data
