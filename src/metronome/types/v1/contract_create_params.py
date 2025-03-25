# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.tier import Tier
from ..shared_params.base_usage_filter import BaseUsageFilter

__all__ = [
    "ContractCreateParams",
    "BillingProviderConfiguration",
    "Commit",
    "CommitAccessSchedule",
    "CommitAccessScheduleScheduleItem",
    "CommitInvoiceSchedule",
    "CommitInvoiceScheduleRecurringSchedule",
    "CommitInvoiceScheduleScheduleItem",
    "Credit",
    "CreditAccessSchedule",
    "CreditAccessScheduleScheduleItem",
    "Discount",
    "DiscountSchedule",
    "DiscountScheduleRecurringSchedule",
    "DiscountScheduleScheduleItem",
    "Override",
    "OverrideOverrideSpecifier",
    "OverrideOverwriteRate",
    "OverrideTier",
    "ProfessionalService",
    "RecurringCommit",
    "RecurringCommitAccessAmount",
    "RecurringCommitCommitDuration",
    "RecurringCommitInvoiceAmount",
    "RecurringCredit",
    "RecurringCreditAccessAmount",
    "RecurringCreditCommitDuration",
    "ResellerRoyalty",
    "ResellerRoyaltyAwsOptions",
    "ResellerRoyaltyGcpOptions",
    "ScheduledCharge",
    "ScheduledChargeSchedule",
    "ScheduledChargeScheduleRecurringSchedule",
    "ScheduledChargeScheduleScheduleItem",
    "Subscription",
    "SubscriptionProration",
    "SubscriptionSubscriptionRate",
    "ThresholdBillingConfiguration",
    "ThresholdBillingConfigurationCommit",
    "Transition",
    "TransitionFutureInvoiceBehavior",
    "UsageStatementSchedule",
]


class ContractCreateParams(TypedDict, total=False):
    customer_id: Required[str]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """inclusive contract start time"""

    billing_provider_configuration: BillingProviderConfiguration
    """The billing provider configuration associated with a contract."""

    commits: Iterable[Commit]

    credits: Iterable[Credit]

    custom_fields: Dict[str, str]

    discounts: Iterable[Discount]
    """This field's availability is dependent on your client's configuration."""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """exclusive contract end time"""

    multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"]
    """
    Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
    prices automatically. EXPLICIT prioritization requires specifying priorities for
    each multiplier; the one with the lowest priority value will be prioritized
    first. If tiered overrides are used, prioritization must be explicit.
    """

    name: str

    net_payment_terms_days: float

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""

    overrides: Iterable[Override]

    professional_services: Iterable[ProfessionalService]
    """This field's availability is dependent on your client's configuration."""

    rate_card_alias: str
    """
    Selects the rate card linked to the specified alias as of the contract's start
    date.
    """

    rate_card_id: str

    recurring_commits: Iterable[RecurringCommit]

    recurring_credits: Iterable[RecurringCredit]

    reseller_royalties: Iterable[ResellerRoyalty]
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: str
    """This field's availability is dependent on your client's configuration."""

    scheduled_charges: Iterable[ScheduledCharge]

    scheduled_charges_on_usage_invoices: Literal["ALL"]
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    subscriptions: Iterable[Subscription]

    threshold_billing_configuration: ThresholdBillingConfiguration

    total_contract_value: float
    """This field's availability is dependent on your client's configuration."""

    transition: Transition

    uniqueness_key: str
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """

    usage_filter: BaseUsageFilter

    usage_statement_schedule: UsageStatementSchedule


class BillingProviderConfiguration(TypedDict, total=False):
    billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]

    billing_provider_configuration_id: str
    """The Metronome ID of the billing provider configuration"""

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]


class CommitAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class CommitAccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[CommitAccessScheduleScheduleItem]]

    credit_type_id: str
    """Defaults to USD (cents) if not passed"""


class CommitInvoiceScheduleRecurringSchedule(TypedDict, total=False):
    amount_distribution: Required[Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)."""

    frequency: Required[Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL"]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)."""

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


class CommitInvoiceScheduleScheduleItem(TypedDict, total=False):
    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """timestamp of the scheduled event"""

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
    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    recurring_schedule: CommitInvoiceScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[CommitInvoiceScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


class Commit(TypedDict, total=False):
    product_id: Required[str]

    type: Required[Literal["PREPAID", "POSTPAID"]]

    access_schedule: CommitAccessSchedule
    """Required: Schedule for distributing the commit to the customer.

    For "POSTPAID" commits only one schedule item is allowed and amount must match
    invoice_schedule total.
    """

    amount: float
    """(DEPRECATED) Use access_schedule and invoice_schedule instead."""

    applicable_product_ids: List[str]
    """Which products the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: List[str]
    """Which tags the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    custom_fields: Dict[str, str]

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

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""

    priority: float
    """
    If multiple commits are applicable, the one with the lower priority will apply
    first.
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]

    rollover_fraction: float
    """Fraction of unused segments that will be rolled over. Must be between 0 and 1."""

    temporary_id: str
    """
    A temporary ID for the commit that can be used to reference the commit for
    commit specific overrides.
    """


class CreditAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class CreditAccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[CreditAccessScheduleScheduleItem]]

    credit_type_id: str
    """Defaults to USD (cents) if not passed"""


class Credit(TypedDict, total=False):
    access_schedule: Required[CreditAccessSchedule]
    """Schedule for distributing the credit to the customer."""

    product_id: Required[str]

    applicable_product_ids: List[str]
    """Which products the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    applicable_product_tags: List[str]
    """Which tags the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    custom_fields: Dict[str, str]

    description: str
    """Used only in UI/API. It is not exposed to end customers."""

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""

    priority: float
    """
    If multiple credits are applicable, the one with the lower priority will apply
    first.
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]


class DiscountScheduleRecurringSchedule(TypedDict, total=False):
    amount_distribution: Required[Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)."""

    frequency: Required[Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL"]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)."""

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


class DiscountScheduleScheduleItem(TypedDict, total=False):
    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """timestamp of the scheduled event"""

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


class DiscountSchedule(TypedDict, total=False):
    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    recurring_schedule: DiscountScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[DiscountScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


class Discount(TypedDict, total=False):
    product_id: Required[str]

    schedule: Required[DiscountSchedule]
    """Must provide either schedule_items or recurring_schedule."""

    custom_fields: Dict[str, str]

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class OverrideOverrideSpecifier(TypedDict, total=False):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL"]

    commit_ids: List[str]
    """Can only be used for commit specific overrides.

    Must be used in conjunction with one of product_id, product_tags,
    pricing_group_values, or presentation_group_values. If provided, the override
    will only apply to the specified commits. If not provided, the override will
    apply to all commits.
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

    product_tags: List[str]
    """
    If provided, the override will only apply to products with all the specified
    tags.
    """

    recurring_commit_ids: List[str]
    """Can only be used for commit specific overrides.

    Must be used in conjunction with one of product_id, product_tags,
    pricing_group_values, or presentation_group_values. If provided, the override
    will only apply to commits created by the specified recurring commit ids.
    """

    recurring_credit_ids: List[str]
    """Can only be used for commit specific overrides.

    Must be used in conjunction with one of product_id, product_tags,
    pricing_group_values, or presentation_group_values. If provided, the override
    will only apply to credits created by the specified recurring credit ids.
    """


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
    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp indicating when the override will start applying (inclusive)"""

    applicable_product_tags: List[str]
    """tags identifying products whose rates are being overridden.

    Cannot be used in conjunction with override_specifiers.
    """

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp indicating when the override will stop applying (exclusive)"""

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

    override_specifiers: Iterable[OverrideOverrideSpecifier]
    """Cannot be used in conjunction with product_id or applicable_product_tags.

    If provided, the override will apply to all products with the specified
    specifiers.
    """

    overwrite_rate: OverrideOverwriteRate
    """Required for OVERWRITE type."""

    priority: float
    """Required for EXPLICIT multiplier prioritization scheme and all TIERED overrides.

    Under EXPLICIT prioritization, overwrites are prioritized first, and then tiered
    and multiplier overrides are prioritized by their priority value (lowest first).
    Must be > 0.
    """

    product_id: str
    """ID of the product whose rate is being overridden.

    Cannot be used in conjunction with override_specifiers.
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


class ProfessionalService(TypedDict, total=False):
    max_amount: Required[float]
    """Maximum amount for the term."""

    product_id: Required[str]

    quantity: Required[float]
    """Quantity for the charge.

    Will be multiplied by unit_price to determine the amount.
    """

    unit_price: Required[float]
    """Unit price for the charge.

    Will be multiplied by quantity to determine the amount and must be specified.
    """

    custom_fields: Dict[str, str]

    description: str

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class RecurringCommitAccessAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class RecurringCommitCommitDuration(TypedDict, total=False):
    unit: Required[Literal["PERIODS"]]

    value: Required[float]


class RecurringCommitInvoiceAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class RecurringCommit(TypedDict, total=False):
    access_amount: Required[RecurringCommitAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[RecurringCommitCommitDuration]
    """The amount of time the created commits will be valid for."""

    priority: Required[float]
    """Will be passed down to the individual commits"""

    product_id: Required[str]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """determines the start time for the first commit"""

    applicable_product_ids: List[str]
    """Will be passed down to the individual commits"""

    applicable_product_tags: List[str]
    """Will be passed down to the individual commits"""

    description: str
    """Will be passed down to the individual commits"""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Determines when the contract will stop creating recurring commits. optional"""

    invoice_amount: RecurringCommitInvoiceAmount
    """The amount the customer should be billed for the commit. Not required."""

    name: str
    """displayed on invoices. will be passed through to the individual commits"""

    netsuite_sales_order_id: str
    """Will be passed down to the individual commits"""

    proration: Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    recurrence_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL"]
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    start_date rather than the usage invoice dates.
    """

    rollover_fraction: float
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    temporary_id: str
    """
    A temporary ID that can be used to reference the recurring commit for commit
    specific overrides.
    """


class RecurringCreditAccessAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class RecurringCreditCommitDuration(TypedDict, total=False):
    unit: Required[Literal["PERIODS"]]

    value: Required[float]


class RecurringCredit(TypedDict, total=False):
    access_amount: Required[RecurringCreditAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[RecurringCreditCommitDuration]
    """The amount of time the created commits will be valid for."""

    priority: Required[float]
    """Will be passed down to the individual commits"""

    product_id: Required[str]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """determines the start time for the first commit"""

    applicable_product_ids: List[str]
    """Will be passed down to the individual commits"""

    applicable_product_tags: List[str]
    """Will be passed down to the individual commits"""

    description: str
    """Will be passed down to the individual commits"""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Determines when the contract will stop creating recurring commits. optional"""

    name: str
    """displayed on invoices. will be passed through to the individual commits"""

    netsuite_sales_order_id: str
    """Will be passed down to the individual commits"""

    proration: Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    recurrence_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL"]
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    start_date rather than the usage invoice dates.
    """

    rollover_fraction: float
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """

    temporary_id: str
    """
    A temporary ID that can be used to reference the recurring commit for commit
    specific overrides.
    """


class ResellerRoyaltyAwsOptions(TypedDict, total=False):
    aws_account_number: str

    aws_offer_id: str

    aws_payer_reference_id: str


class ResellerRoyaltyGcpOptions(TypedDict, total=False):
    gcp_account_id: str

    gcp_offer_id: str


class ResellerRoyalty(TypedDict, total=False):
    fraction: Required[float]

    netsuite_reseller_id: Required[str]

    reseller_type: Required[Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    applicable_product_ids: List[str]
    """Must provide at least one of applicable_product_ids or applicable_product_tags."""

    applicable_product_tags: List[str]
    """Must provide at least one of applicable_product_ids or applicable_product_tags."""

    aws_options: ResellerRoyaltyAwsOptions

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    gcp_options: ResellerRoyaltyGcpOptions

    reseller_contract_value: float


class ScheduledChargeScheduleRecurringSchedule(TypedDict, total=False):
    amount_distribution: Required[Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)."""

    frequency: Required[Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL"]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)."""

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


class ScheduledChargeScheduleScheduleItem(TypedDict, total=False):
    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """timestamp of the scheduled event"""

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
    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    recurring_schedule: ScheduledChargeScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[ScheduledChargeScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


class ScheduledCharge(TypedDict, total=False):
    product_id: Required[str]

    schedule: Required[ScheduledChargeSchedule]
    """Must provide either schedule_items or recurring_schedule."""

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class SubscriptionProration(TypedDict, total=False):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]
    """Indicates how mid-period quantity adjustments are invoiced.

    If BILL_IMMEDIATELY is selected, the quantity increase will be billed on the
    scheduled date. If BILL_ON_NEXT_COLLECTION_DATE is selected, the quantity
    increase will be billed for in-arrears at the end of the period.
    """

    is_prorated: bool
    """Indicates if the partial period will be prorated or charged a full amount."""


class SubscriptionSubscriptionRate(TypedDict, total=False):
    billing_frequency: Required[Literal["MONTHLY", "QUARTERLY", "ANNUAL"]]
    """Frequency to bill subscription with.

    Together with product_id, must match existing rate on the rate card.
    """

    product_id: Required[str]
    """Must be subscription type product"""


class Subscription(TypedDict, total=False):
    collection_schedule: Required[Literal["ADVANCE", "ARREARS"]]

    initial_quantity: Required[float]

    proration: Required[SubscriptionProration]

    subscription_rate: Required[SubscriptionSubscriptionRate]

    description: str

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Exclusive end time for the subscription.

    If not provided, subscription inherits contract end date.
    """

    name: str

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Inclusive start time for the subscription.

    If not provided, defaults to contract start date
    """


class ThresholdBillingConfigurationCommit(TypedDict, total=False):
    product_id: Required[str]

    applicable_product_ids: List[str]
    """Which products the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: List[str]
    """Which tags the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    description: str

    name: str
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """


class ThresholdBillingConfiguration(TypedDict, total=False):
    commit: Required[ThresholdBillingConfigurationCommit]

    is_enabled: Required[bool]
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state
    """

    threshold_amount: Required[float]
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class TransitionFutureInvoiceBehavior(TypedDict, total=False):
    trueup: Optional[Literal["REMOVE", "AS_IS"]]
    """Controls whether future trueup invoices are billed or removed.

    Default behavior is AS_IS if not specified.
    """


class Transition(TypedDict, total=False):
    from_contract_id: Required[str]

    type: Required[Literal["SUPERSEDE", "RENEWAL"]]
    """This field's available values may vary based on your client's configuration."""

    future_invoice_behavior: TransitionFutureInvoiceBehavior


class UsageStatementSchedule(TypedDict, total=False):
    frequency: Required[Literal["MONTHLY", "QUARTERLY", "ANNUAL"]]

    billing_anchor_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Required when using CUSTOM_DATE.

    This option lets you set a historical billing anchor date, aligning future
    billing cycles with a chosen cadence. For example, if a contract starts on
    2024-09-15 and you set the anchor date to 2024-09-10 with a MONTHLY frequency,
    the first usage statement will cover 09-15 to 10-10. Subsequent statements will
    follow the 10th of each month.
    """

    day: Literal["FIRST_OF_MONTH", "CONTRACT_START", "CUSTOM_DATE"]
    """If not provided, defaults to the first day of the month."""

    invoice_generation_starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The date Metronome should start generating usage invoices.

    If unspecified, contract start date will be used. This is useful to set if you
    want to import historical invoices via our 'Create Historical Invoices' API
    rather than having Metronome automatically generate them.
    """
