# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .shared_params.tier import Tier
from .shared_params.commit_specifier_input import CommitSpecifierInput
from .shared_params.spend_threshold_configuration import SpendThresholdConfiguration
from .shared_params.prepaid_balance_threshold_configuration import PrepaidBalanceThresholdConfiguration

__all__ = [
    "PackageCreateParams",
    "Commit",
    "CommitAccessSchedule",
    "CommitAccessScheduleScheduleItem",
    "CommitAccessScheduleScheduleItemDuration",
    "CommitAccessScheduleScheduleItemStartingAtOffset",
    "CommitInvoiceSchedule",
    "CommitInvoiceScheduleScheduleItem",
    "CommitInvoiceScheduleScheduleItemDateOffset",
    "CommitPaymentGateConfig",
    "CommitPaymentGateConfigPrecalculatedTaxConfig",
    "CommitPaymentGateConfigStripeConfig",
    "Credit",
    "CreditAccessSchedule",
    "CreditAccessScheduleScheduleItem",
    "CreditAccessScheduleScheduleItemDuration",
    "CreditAccessScheduleScheduleItemStartingAtOffset",
    "Duration",
    "Override",
    "OverrideOverrideSpecifier",
    "OverrideStartingOffset",
    "OverrideDuration",
    "OverrideOverwriteRate",
    "OverrideTier",
    "RecurringCommit",
    "RecurringCommitAccessAmount",
    "RecurringCommitCommitDuration",
    "RecurringCommitStartingOffset",
    "RecurringCommitEndingOffset",
    "RecurringCommitInvoiceAmount",
    "RecurringCommitSubscriptionConfig",
    "RecurringCommitSubscriptionConfigApplySeatIncreaseConfig",
    "RecurringCredit",
    "RecurringCreditAccessAmount",
    "RecurringCreditCommitDuration",
    "RecurringCreditStartingOffset",
    "RecurringCreditEndingOffset",
    "RecurringCreditSubscriptionConfig",
    "RecurringCreditSubscriptionConfigApplySeatIncreaseConfig",
    "ScheduledCharge",
    "ScheduledChargeSchedule",
    "ScheduledChargeScheduleScheduleItem",
    "ScheduledChargeScheduleScheduleItemDateOffset",
    "Subscription",
    "SubscriptionProration",
    "SubscriptionSubscriptionRate",
    "SubscriptionDuration",
    "SubscriptionStartingOffset",
    "UsageStatementSchedule",
    "UsageStatementScheduleInvoiceGenerationStartingAtOffset",
]


class PackageCreateParams(TypedDict, total=False):
    name: Required[str]

    billing_anchor_date: Literal["contract_start_date", "first_billing_period"]

    billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]

    commits: Iterable[Commit]

    contract_name: str

    credits: Iterable[Credit]

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]

    duration: Duration

    multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"]
    """
    Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
    prices automatically. EXPLICIT prioritization requires specifying priorities for
    each multiplier; the one with the lowest priority value will be prioritized
    first. If tiered overrides are used, prioritization must be explicit.
    """

    net_payment_terms_days: float

    overrides: Iterable[Override]

    prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfiguration

    priority: float
    """Priority of the generated contract."""

    rate_card_alias: str
    """
    Selects the rate card linked to the specified alias as of the contract's start
    date.
    """

    rate_card_id: str

    recurring_commits: Iterable[RecurringCommit]

    recurring_credits: Iterable[RecurringCredit]

    scheduled_charges: Iterable[ScheduledCharge]

    scheduled_charges_on_usage_invoices: Literal["ALL"]
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    spend_threshold_configuration: SpendThresholdConfiguration

    subscriptions: Iterable[Subscription]

    uniqueness_key: str
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """

    usage_statement_schedule: UsageStatementSchedule


class CommitAccessScheduleScheduleItemDuration(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class CommitAccessScheduleScheduleItemStartingAtOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class CommitAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    duration: Required[CommitAccessScheduleScheduleItemDuration]
    """Offset relative to the start of this segment indicating when it should end."""

    starting_at_offset: Required[CommitAccessScheduleScheduleItemStartingAtOffset]
    """
    Date relative to the contract start date indicating the start of this schedule
    segment.
    """


class CommitAccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[CommitAccessScheduleScheduleItem]]

    credit_type_id: str
    """Defaults to USD (cents) if not passed"""


class CommitInvoiceScheduleScheduleItemDateOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class CommitInvoiceScheduleScheduleItem(TypedDict, total=False):
    date_offset: Required[CommitInvoiceScheduleScheduleItemDateOffset]
    """Date relative to the contract start date."""

    amount: float
    """Amount for the charge.

    Can be provided instead of unit_price and quantity. If amount is sent, the
    unit_price is assumed to be the amount and quantity is inferred to be 1.
    """

    quantity: float
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount and must be specified
    with unit_price. If specified amount cannot be provided.
    """

    unit_price: float
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified
    with quantity. If specified amount cannot be provided.
    """


class CommitInvoiceSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[CommitInvoiceScheduleScheduleItem]]
    """Either provide amount or provide both unit_price and quantity."""

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""


class CommitPaymentGateConfigPrecalculatedTaxConfig(TypedDict, total=False):
    tax_amount: Required[float]
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: str
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class CommitPaymentGateConfigStripeConfig(TypedDict, total=False):
    payment_type: Required[Literal["INVOICE", "PAYMENT_INTENT"]]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Dict[str, str]
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """

    on_session_payment: bool
    """If true, the payment will be made assuming the customer is present (i.e.

    on session).

    If false, the payment will be made assuming the customer is not present (i.e.
    off session). For cardholders from a country with an e-mandate requirement (e.g.
    India), the payment may be declined.

    If left blank, will default to false.
    """


class CommitPaymentGateConfig(TypedDict, total=False):
    payment_gate_type: Required[Literal["NONE", "STRIPE", "EXTERNAL"]]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: CommitPaymentGateConfigPrecalculatedTaxConfig
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: CommitPaymentGateConfigStripeConfig
    """Only applicable if using STRIPE as your payment gate type."""

    tax_type: Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class Commit(TypedDict, total=False):
    product_id: Required[str]

    type: Required[Literal["PREPAID", "POSTPAID"]]

    access_schedule: CommitAccessSchedule
    """Required: Schedule for distributing the commit to the customer.

    For "POSTPAID" commits only one schedule item is allowed and amount must match
    invoice_schedule total.
    """

    applicable_product_ids: SequenceNotStr[str]
    """Which products the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: SequenceNotStr[str]
    """Which tags the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str
    """Used only in UI/API. It is not exposed to end customers."""

    invoice_schedule: CommitInvoiceSchedule
    """
    Required for "POSTPAID" commits: the true up invoice will be generated at this
    time and only one schedule item is allowed; the total must match access_schedule
    amount. Optional for "PREPAID" commits: if not provided, this will be a
    "complimentary" commit with no invoice.
    """

    name: str
    """displayed on invoices"""

    payment_gate_config: CommitPaymentGateConfig
    """optionally payment gate this commit"""

    priority: float
    """
    If multiple commits are applicable, the one with the lower priority will apply
    first.
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]

    rollover_fraction: float
    """Fraction of unused segments that will be rolled over. Must be between 0 and 1."""

    specifiers: Iterable[CommitSpecifierInput]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """

    temporary_id: str
    """
    A temporary ID for the commit that can be used to reference the commit for
    commit specific overrides.
    """


class CreditAccessScheduleScheduleItemDuration(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class CreditAccessScheduleScheduleItemStartingAtOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class CreditAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    duration: Required[CreditAccessScheduleScheduleItemDuration]
    """Offset relative to the start of this segment indicating when it should end."""

    starting_at_offset: Required[CreditAccessScheduleScheduleItemStartingAtOffset]
    """
    Date relative to the contract start date indicating the start of this schedule
    segment.
    """


class CreditAccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[CreditAccessScheduleScheduleItem]]

    credit_type_id: str
    """Defaults to USD (cents) if not passed"""


class Credit(TypedDict, total=False):
    access_schedule: Required[CreditAccessSchedule]
    """Schedule for distributing the credit to the customer."""

    product_id: Required[str]

    applicable_product_ids: SequenceNotStr[str]
    """Which products the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    applicable_product_tags: SequenceNotStr[str]
    """Which tags the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str
    """Used only in UI/API. It is not exposed to end customers."""

    name: str
    """displayed on invoices"""

    priority: float
    """
    If multiple credits are applicable, the one with the lower priority will apply
    first.
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]

    specifiers: Iterable[CommitSpecifierInput]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """


class Duration(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class OverrideOverrideSpecifier(TypedDict, total=False):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    commit_ids: SequenceNotStr[str]
    """Can only be used for commit specific overrides.

    Must be used in conjunction with one of `product_id`, `product_tags`,
    `pricing_group_values`, or `presentation_group_values`. If provided, the
    override will only apply to the specified commits. If not provided, the override
    will apply to all commits.
    """

    presentation_group_values: Dict[str, str]
    """A map of group names to values.

    The override will only apply to line items with the specified presentation group
    values.
    """

    pricing_group_values: Dict[str, str]
    """A map of pricing group names to values.

    The override will only apply to products with the specified pricing group
    values.
    """

    product_id: str
    """If provided, the override will only apply to the product with the specified ID."""

    product_tags: SequenceNotStr[str]
    """
    If provided, the override will only apply to products with all the specified
    tags.
    """

    recurring_commit_ids: SequenceNotStr[str]
    """Can only be used for commit specific overrides.

    Must be used in conjunction with one of `product_id`, `product_tags`,
    `pricing_group_values`, or `presentation_group_values`. If provided, the
    override will only apply to commits created by the specified recurring commit
    ids.
    """

    recurring_credit_ids: SequenceNotStr[str]
    """Can only be used for commit specific overrides.

    Must be used in conjunction with one of `product_id`, `product_tags`,
    `pricing_group_values`, or `presentation_group_values`. If provided, the
    override will only apply to credits created by the specified recurring credit
    ids.
    """


class OverrideStartingOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class OverrideDuration(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class OverrideOverwriteRate(TypedDict, total=False):
    rate_type: Required[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]]

    credit_type_id: str

    custom_rate: Dict[str, object]
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    is_prorated: bool
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    price: float
    """Default price.

    For FLAT rate_type, this must be >=0. For PERCENTAGE rate_type, this is a
    decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    quantity: float
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Iterable[Tier]
    """Only set for TIERED rate_type."""


class OverrideTier(TypedDict, total=False):
    multiplier: Required[float]

    size: float


class Override(TypedDict, total=False):
    override_specifiers: Required[Iterable[OverrideOverrideSpecifier]]
    """Specifies which products the override will apply to."""

    starting_offset: Required[OverrideStartingOffset]
    """
    Offset relative to contract start date indicating when the override will start
    applying (inclusive)
    """

    duration: OverrideDuration
    """
    Offset relative to override start indicating when the override will stop
    applying (exclusive)
    """

    entitled: bool

    is_commit_specific: bool
    """Indicates whether the override should only apply to commits.

    Defaults to `false`. If `true`, you can specify relevant commits in
    `override_specifiers` by passing `commit_ids`. if you do not specify
    `commit_ids`, then the override will apply when consuming any prepaid or
    postpaid commit.
    """

    multiplier: float
    """Required for MULTIPLIER type. Must be >=0."""

    overwrite_rate: OverrideOverwriteRate
    """Required for OVERWRITE type."""

    priority: float
    """Required for EXPLICIT multiplier prioritization scheme and all TIERED overrides.

    Under EXPLICIT prioritization, overwrites are prioritized first, and then tiered
    and multiplier overrides are prioritized by their priority value (lowest first).
    Must be > 0.
    """

    target: Literal["COMMIT_RATE", "LIST_RATE"]
    """Indicates whether the override applies to commit rates or list rates.

    Can only be used for overrides that have `is_commit_specific` set to `true`.
    Defaults to `"LIST_RATE"`.
    """

    tiers: Iterable[OverrideTier]
    """Required for TIERED type. Must have at least one tier."""

    type: Literal["OVERWRITE", "MULTIPLIER", "TIERED"]
    """Overwrites are prioritized over multipliers and tiered overrides."""


class RecurringCommitAccessAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    unit_price: Required[float]

    quantity: float
    """
    This field is required unless a subscription is attached via
    `subscription_config`.
    """


class RecurringCommitCommitDuration(TypedDict, total=False):
    value: Required[float]

    unit: Literal["PERIODS"]


class RecurringCommitStartingOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class RecurringCommitEndingOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class RecurringCommitInvoiceAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class RecurringCommitSubscriptionConfigApplySeatIncreaseConfig(TypedDict, total=False):
    is_prorated: Required[bool]
    """Indicates whether a mid-period seat increase should be prorated."""


class RecurringCommitSubscriptionConfig(TypedDict, total=False):
    apply_seat_increase_config: Required[RecurringCommitSubscriptionConfigApplySeatIncreaseConfig]

    subscription_id: Required[str]
    """ID of the subscription to configure on the recurring commit/credit."""

    allocation: Literal["INDIVIDUAL", "POOLED"]
    """If set to POOLED, allocation added per seat is pooled across the account."""


class RecurringCommit(TypedDict, total=False):
    access_amount: Required[RecurringCommitAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[RecurringCommitCommitDuration]
    """Defines the length of the access schedule for each created commit/credit.

    The value represents the number of units. Unit defaults to "PERIODS", where the
    length of a period is determined by the recurrence_frequency.
    """

    priority: Required[float]
    """Will be passed down to the individual commits"""

    product_id: Required[str]

    starting_offset: Required[RecurringCommitStartingOffset]
    """Determines the start time for the first commit"""

    applicable_product_ids: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    applicable_product_tags: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    description: str
    """Will be passed down to the individual commits"""

    ending_offset: RecurringCommitEndingOffset
    """Determines when the contract will stop creating recurring commits. optional"""

    invoice_amount: RecurringCommitInvoiceAmount
    """The amount the customer should be billed for the commit. Not required."""

    name: str
    """displayed on invoices. will be passed through to the individual commits"""

    proration: Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    recurrence_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates.
    """

    rollover_fraction: float
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Iterable[CommitSpecifierInput]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """

    subscription_config: RecurringCommitSubscriptionConfig
    """Attach a subscription to the recurring commit/credit."""

    temporary_id: str
    """
    A temporary ID that can be used to reference the recurring commit for commit
    specific overrides.
    """


class RecurringCreditAccessAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    unit_price: Required[float]

    quantity: float
    """
    This field is required unless a subscription is attached via
    `subscription_config`.
    """


class RecurringCreditCommitDuration(TypedDict, total=False):
    value: Required[float]

    unit: Literal["PERIODS"]


class RecurringCreditStartingOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class RecurringCreditEndingOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class RecurringCreditSubscriptionConfigApplySeatIncreaseConfig(TypedDict, total=False):
    is_prorated: Required[bool]
    """Indicates whether a mid-period seat increase should be prorated."""


class RecurringCreditSubscriptionConfig(TypedDict, total=False):
    apply_seat_increase_config: Required[RecurringCreditSubscriptionConfigApplySeatIncreaseConfig]

    subscription_id: Required[str]
    """ID of the subscription to configure on the recurring commit/credit."""

    allocation: Literal["INDIVIDUAL", "POOLED"]
    """If set to POOLED, allocation added per seat is pooled across the account."""


class RecurringCredit(TypedDict, total=False):
    access_amount: Required[RecurringCreditAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[RecurringCreditCommitDuration]
    """Defines the length of the access schedule for each created commit/credit.

    The value represents the number of units. Unit defaults to "PERIODS", where the
    length of a period is determined by the recurrence_frequency.
    """

    priority: Required[float]
    """Will be passed down to the individual commits"""

    product_id: Required[str]

    starting_offset: Required[RecurringCreditStartingOffset]
    """Determines the start time for the first commit"""

    applicable_product_ids: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    applicable_product_tags: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    description: str
    """Will be passed down to the individual commits"""

    ending_offset: RecurringCreditEndingOffset
    """Determines when the contract will stop creating recurring commits. optional"""

    name: str
    """displayed on invoices. will be passed through to the individual commits"""

    proration: Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    recurrence_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    starting_at rather than the usage invoice dates.
    """

    rollover_fraction: float
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    specifiers: Iterable[CommitSpecifierInput]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """

    subscription_config: RecurringCreditSubscriptionConfig
    """Attach a subscription to the recurring commit/credit."""

    temporary_id: str
    """
    A temporary ID that can be used to reference the recurring commit for commit
    specific overrides.
    """


class ScheduledChargeScheduleScheduleItemDateOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class ScheduledChargeScheduleScheduleItem(TypedDict, total=False):
    date_offset: Required[ScheduledChargeScheduleScheduleItemDateOffset]
    """Date relative to the contract start date."""

    amount: float
    """Amount for the charge.

    Can be provided instead of unit_price and quantity. If amount is sent, the
    unit_price is assumed to be the amount and quantity is inferred to be 1.
    """

    quantity: float
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount and must be specified
    with unit_price. If specified amount cannot be provided.
    """

    unit_price: float
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified
    with quantity. If specified amount cannot be provided.
    """


class ScheduledChargeSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[ScheduledChargeScheduleScheduleItem]]
    """Either provide amount or provide both unit_price and quantity."""

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""


class ScheduledCharge(TypedDict, total=False):
    product_id: Required[str]

    schedule: Required[ScheduledChargeSchedule]
    """Must provide schedule_items."""

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: str
    """displayed on invoices"""


class SubscriptionProration(TypedDict, total=False):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]
    """Indicates how mid-period quantity adjustments are invoiced.

    **BILL_IMMEDIATELY**: Only available when collection schedule is `ADVANCE`. The
    quantity increase will be billed immediately on the scheduled date.
    **BILL_ON_NEXT_COLLECTION_DATE**: The quantity increase will be billed for
    in-arrears at the end of the period.
    """

    is_prorated: bool
    """Indicates if the partial period will be prorated or charged a full amount."""


class SubscriptionSubscriptionRate(TypedDict, total=False):
    billing_frequency: Required[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]]
    """Frequency to bill subscription with.

    Together with product_id, must match existing rate on the rate card.
    """

    product_id: Required[str]
    """Must be subscription type product"""


class SubscriptionDuration(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class SubscriptionStartingOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class Subscription(TypedDict, total=False):
    collection_schedule: Required[Literal["ADVANCE", "ARREARS"]]

    initial_quantity: Required[float]
    """The initial quantity for the subscription. It must be non-negative value."""

    proration: Required[SubscriptionProration]

    subscription_rate: Required[SubscriptionSubscriptionRate]

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str

    duration: SubscriptionDuration
    """Lifetime of the subscription from its start.

    If not provided, subscription inherits contract end date.
    """

    name: str

    starting_offset: SubscriptionStartingOffset
    """
    Relative date from contract start date corresponding to the inclusive start time
    for the subscription. If not provided, defaults to contract start date
    """

    temporary_id: str
    """
    A temporary ID used to reference the subscription in recurring commit/credit
    subscription configs created within the same payload.
    """


class UsageStatementScheduleInvoiceGenerationStartingAtOffset(TypedDict, total=False):
    unit: Required[Literal["DAYS", "WEEKS", "MONTHS", "QUARTERS", "YEARS"]]

    value: Required[int]


class UsageStatementSchedule(TypedDict, total=False):
    frequency: Required[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]]

    day: Literal["FIRST_OF_MONTH", "CONTRACT_START"]
    """If not provided, defaults to the first day of the month."""

    invoice_generation_starting_at_offset: UsageStatementScheduleInvoiceGenerationStartingAtOffset
    """
    The offset at which Metronome should start generating usage invoices, relative
    to the contract start date. If unspecified, contract start date will be used.
    This is useful to set if you want to import historical invoices via our 'Create
    Historical Invoices' API rather than having Metronome automatically generate
    them.
    """
