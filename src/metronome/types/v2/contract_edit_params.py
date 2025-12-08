# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.tier import Tier
from ..shared_params.commit_specifier_input import CommitSpecifierInput
from ..shared_params.payment_gate_config_v2 import PaymentGateConfigV2
from ..shared_params.update_base_threshold_commit import UpdateBaseThresholdCommit
from ..shared_params.commit_hierarchy_configuration import CommitHierarchyConfiguration
from ..shared_params.spend_threshold_configuration_v2 import SpendThresholdConfigurationV2
from ..shared_params.prepaid_balance_threshold_configuration_v2 import PrepaidBalanceThresholdConfigurationV2

__all__ = [
    "ContractEditParams",
    "AddBillingProviderConfigurationUpdate",
    "AddBillingProviderConfigurationUpdateBillingProviderConfiguration",
    "AddBillingProviderConfigurationUpdateSchedule",
    "AddCommit",
    "AddCommitAccessSchedule",
    "AddCommitAccessScheduleScheduleItem",
    "AddCommitInvoiceSchedule",
    "AddCommitInvoiceScheduleRecurringSchedule",
    "AddCommitInvoiceScheduleScheduleItem",
    "AddCommitPaymentGateConfig",
    "AddCommitPaymentGateConfigPrecalculatedTaxConfig",
    "AddCommitPaymentGateConfigStripeConfig",
    "AddCredit",
    "AddCreditAccessSchedule",
    "AddCreditAccessScheduleScheduleItem",
    "AddDiscount",
    "AddDiscountSchedule",
    "AddDiscountScheduleRecurringSchedule",
    "AddDiscountScheduleScheduleItem",
    "AddOverride",
    "AddOverrideOverrideSpecifier",
    "AddOverrideOverwriteRate",
    "AddOverrideTier",
    "AddProfessionalService",
    "AddRecurringCommit",
    "AddRecurringCommitAccessAmount",
    "AddRecurringCommitCommitDuration",
    "AddRecurringCommitInvoiceAmount",
    "AddRecurringCommitSubscriptionConfig",
    "AddRecurringCommitSubscriptionConfigApplySeatIncreaseConfig",
    "AddRecurringCredit",
    "AddRecurringCreditAccessAmount",
    "AddRecurringCreditCommitDuration",
    "AddRecurringCreditSubscriptionConfig",
    "AddRecurringCreditSubscriptionConfigApplySeatIncreaseConfig",
    "AddResellerRoyalty",
    "AddResellerRoyaltyAwsOptions",
    "AddResellerRoyaltyGcpOptions",
    "AddScheduledCharge",
    "AddScheduledChargeSchedule",
    "AddScheduledChargeScheduleRecurringSchedule",
    "AddScheduledChargeScheduleScheduleItem",
    "AddSubscription",
    "AddSubscriptionProration",
    "AddSubscriptionSubscriptionRate",
    "AddSubscriptionSeatConfig",
    "ArchiveCommit",
    "ArchiveCredit",
    "ArchiveScheduledCharge",
    "RemoveOverride",
    "UpdateCommit",
    "UpdateCommitAccessSchedule",
    "UpdateCommitAccessScheduleAddScheduleItem",
    "UpdateCommitAccessScheduleRemoveScheduleItem",
    "UpdateCommitAccessScheduleUpdateScheduleItem",
    "UpdateCommitInvoiceSchedule",
    "UpdateCommitInvoiceScheduleAddScheduleItem",
    "UpdateCommitInvoiceScheduleRemoveScheduleItem",
    "UpdateCommitInvoiceScheduleUpdateScheduleItem",
    "UpdateCredit",
    "UpdateCreditAccessSchedule",
    "UpdateCreditAccessScheduleAddScheduleItem",
    "UpdateCreditAccessScheduleRemoveScheduleItem",
    "UpdateCreditAccessScheduleUpdateScheduleItem",
    "UpdatePrepaidBalanceThresholdConfiguration",
    "UpdatePrepaidBalanceThresholdConfigurationCommit",
    "UpdateRecurringCommit",
    "UpdateRecurringCommitAccessAmount",
    "UpdateRecurringCommitInvoiceAmount",
    "UpdateRecurringCredit",
    "UpdateRecurringCreditAccessAmount",
    "UpdateScheduledCharge",
    "UpdateScheduledChargeInvoiceSchedule",
    "UpdateScheduledChargeInvoiceScheduleAddScheduleItem",
    "UpdateScheduledChargeInvoiceScheduleRemoveScheduleItem",
    "UpdateScheduledChargeInvoiceScheduleUpdateScheduleItem",
    "UpdateSpendThresholdConfiguration",
    "UpdateSubscription",
    "UpdateSubscriptionQuantityManagementModeUpdate",
    "UpdateSubscriptionQuantityManagementModeUpdateSeatConfig",
    "UpdateSubscriptionQuantityUpdate",
    "UpdateSubscriptionSeatUpdates",
    "UpdateSubscriptionSeatUpdatesAddSeatID",
    "UpdateSubscriptionSeatUpdatesAddUnassignedSeat",
    "UpdateSubscriptionSeatUpdatesRemoveSeatID",
    "UpdateSubscriptionSeatUpdatesRemoveUnassignedSeat",
]


class ContractEditParams(TypedDict, total=False):
    contract_id: Required[str]
    """ID of the contract being edited"""

    customer_id: Required[str]
    """ID of the customer whose contract is being edited"""

    add_billing_provider_configuration_update: AddBillingProviderConfigurationUpdate
    """Update the billing provider configuration on the contract.

    Currently only supports adding a billing provider configuration to a contract
    that does not already have one.
    """

    add_commits: Iterable[AddCommit]

    add_credits: Iterable[AddCredit]

    add_discounts: Iterable[AddDiscount]

    add_overrides: Iterable[AddOverride]

    add_prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfigurationV2

    add_professional_services: Iterable[AddProfessionalService]
    """This field's availability is dependent on your client's configuration."""

    add_recurring_commits: Iterable[AddRecurringCommit]

    add_recurring_credits: Iterable[AddRecurringCredit]

    add_reseller_royalties: Iterable[AddResellerRoyalty]

    add_scheduled_charges: Iterable[AddScheduledCharge]

    add_spend_threshold_configuration: SpendThresholdConfigurationV2

    add_subscriptions: Iterable[AddSubscription]
    """
    Optional list of
    [subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/)
    to add to the contract.
    """

    allow_contract_ending_before_finalized_invoice: bool
    """
    If true, allows setting the contract end date earlier than the end_timestamp of
    existing finalized invoices. Finalized invoices will be unchanged; if you want
    to incorporate the new end date, you can void and regenerate finalized usage
    invoices. Defaults to true.
    """

    archive_commits: Iterable[ArchiveCommit]
    """IDs of commits to archive"""

    archive_credits: Iterable[ArchiveCredit]
    """IDs of credits to archive"""

    archive_scheduled_charges: Iterable[ArchiveScheduledCharge]
    """IDs of scheduled charges to archive"""

    remove_overrides: Iterable[RemoveOverride]
    """IDs of overrides to remove"""

    uniqueness_key: str
    """Optional uniqueness key to prevent duplicate contract edits."""

    update_commits: Iterable[UpdateCommit]

    update_contract_end_date: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp indicating when the contract will end (exclusive)."""

    update_contract_name: Optional[str]
    """Value to update the contract name to.

    If not provided, the contract name will remain unchanged.
    """

    update_credits: Iterable[UpdateCredit]

    update_prepaid_balance_threshold_configuration: UpdatePrepaidBalanceThresholdConfiguration

    update_recurring_commits: Iterable[UpdateRecurringCommit]
    """
    Edits to these recurring commits will only affect commits whose access schedules
    has not started. Expired commits, and commits with an active access schedule
    will remain unchanged.
    """

    update_recurring_credits: Iterable[UpdateRecurringCredit]
    """
    Edits to these recurring credits will only affect credits whose access schedules
    has not started. Expired credits, and credits with an active access schedule
    will remain unchanged.
    """

    update_scheduled_charges: Iterable[UpdateScheduledCharge]

    update_spend_threshold_configuration: UpdateSpendThresholdConfiguration

    update_subscriptions: Iterable[UpdateSubscription]
    """Optional list of subscriptions to update."""


class AddBillingProviderConfigurationUpdateBillingProviderConfiguration(TypedDict, total=False):
    billing_provider: Literal[
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

    billing_provider_configuration_id: str

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]


class AddBillingProviderConfigurationUpdateSchedule(TypedDict, total=False):
    """Indicates when the billing provider will be active on the contract.

    Any charges accrued during the schedule will be billed to the indicated billing provider.
    """

    effective_at: Required[Literal["START_OF_CURRENT_PERIOD"]]
    """When the billing provider update will take effect."""


class AddBillingProviderConfigurationUpdate(TypedDict, total=False):
    """Update the billing provider configuration on the contract.

    Currently only supports adding a billing provider configuration to a contract that does not already have one.
    """

    billing_provider_configuration: Required[AddBillingProviderConfigurationUpdateBillingProviderConfiguration]

    schedule: Required[AddBillingProviderConfigurationUpdateSchedule]
    """Indicates when the billing provider will be active on the contract.

    Any charges accrued during the schedule will be billed to the indicated billing
    provider.
    """


class AddCommitAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class AddCommitAccessSchedule(TypedDict, total=False):
    """Required: Schedule for distributing the commit to the customer.

    For "POSTPAID" commits only one schedule item is allowed and amount must match invoice_schedule total.
    """

    schedule_items: Required[Iterable[AddCommitAccessScheduleScheduleItem]]

    credit_type_id: str


class AddCommitInvoiceScheduleRecurringSchedule(TypedDict, total=False):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

    amount_distribution: Required[Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)."""

    frequency: Required[Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL", "WEEKLY"]]

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


class AddCommitInvoiceScheduleScheduleItem(TypedDict, total=False):
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


class AddCommitInvoiceSchedule(TypedDict, total=False):
    """
    Required for "POSTPAID" commits: the true up invoice will be generated at this time and only one schedule item is allowed; the total must match access_schedule amount. Optional for "PREPAID" commits: if not provided, this will be a "complimentary" commit with no invoice.
    """

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: bool
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    recurring_schedule: AddCommitInvoiceScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[AddCommitInvoiceScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


class AddCommitPaymentGateConfigPrecalculatedTaxConfig(TypedDict, total=False):
    """Only applicable if using PRECALCULATED as your tax type."""

    tax_amount: Required[float]
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: str
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class AddCommitPaymentGateConfigStripeConfig(TypedDict, total=False):
    """Only applicable if using STRIPE as your payment gateway type."""

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


class AddCommitPaymentGateConfig(TypedDict, total=False):
    """optionally payment gate this commit"""

    payment_gate_type: Required[Literal["NONE", "STRIPE", "EXTERNAL"]]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: AddCommitPaymentGateConfigPrecalculatedTaxConfig
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: AddCommitPaymentGateConfigStripeConfig
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Literal["NONE", "STRIPE", "ANROK", "AVALARA", "PRECALCULATED"]
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class AddCommit(TypedDict, total=False):
    product_id: Required[str]

    type: Required[Literal["PREPAID", "POSTPAID"]]

    access_schedule: AddCommitAccessSchedule
    """Required: Schedule for distributing the commit to the customer.

    For "POSTPAID" commits only one schedule item is allowed and amount must match
    invoice_schedule total.
    """

    amount: float
    """(DEPRECATED) Use access_schedule and invoice_schedule instead."""

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

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for commit hierarchy access control"""

    invoice_schedule: AddCommitInvoiceSchedule
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

    payment_gate_config: AddCommitPaymentGateConfig
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
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """

    temporary_id: str
    """
    A temporary ID for the commit that can be used to reference the commit for
    commit specific overrides.
    """


class AddCreditAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class AddCreditAccessSchedule(TypedDict, total=False):
    """Schedule for distributing the credit to the customer."""

    schedule_items: Required[Iterable[AddCreditAccessScheduleScheduleItem]]

    credit_type_id: str


class AddCredit(TypedDict, total=False):
    access_schedule: Required[AddCreditAccessSchedule]
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

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for credit hierarchy access control"""

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

    specifiers: Iterable[CommitSpecifierInput]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class AddDiscountScheduleRecurringSchedule(TypedDict, total=False):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

    amount_distribution: Required[Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)."""

    frequency: Required[Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL", "WEEKLY"]]

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


class AddDiscountScheduleScheduleItem(TypedDict, total=False):
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


class AddDiscountSchedule(TypedDict, total=False):
    """Must provide either schedule_items or recurring_schedule."""

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: bool
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    recurring_schedule: AddDiscountScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[AddDiscountScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


class AddDiscount(TypedDict, total=False):
    product_id: Required[str]

    schedule: Required[AddDiscountSchedule]
    """Must provide either schedule_items or recurring_schedule."""

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class AddOverrideOverrideSpecifier(TypedDict, total=False):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    commit_ids: SequenceNotStr[str]
    """If provided, the override will only apply to the specified commits.

    Can only be used for commit specific overrides. If not provided, the override
    will apply to all commits.
    """

    presentation_group_values: Dict[str, str]
    """A map of group names to values.

    The override will only apply to line items with the specified presentation group
    values. Can only be used for multiplier overrides.
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

    Must be used in conjunction with one of product_id, product_tags,
    pricing_group_values, or presentation_group_values. If provided, the override
    will only apply to commits created by the specified recurring commit ids.
    """

    recurring_credit_ids: SequenceNotStr[str]
    """Can only be used for commit specific overrides.

    Must be used in conjunction with one of product_id, product_tags,
    pricing_group_values, or presentation_group_values. If provided, the override
    will only apply to commits created by the specified recurring credit ids.
    """


class AddOverrideOverwriteRate(TypedDict, total=False):
    """Required for OVERWRITE type."""

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


class AddOverrideTier(TypedDict, total=False):
    multiplier: Required[float]

    size: float


class AddOverride(TypedDict, total=False):
    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp indicating when the override will start applying (inclusive)"""

    applicable_product_tags: SequenceNotStr[str]
    """tags identifying products whose rates are being overridden"""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp indicating when the override will stop applying (exclusive)"""

    entitled: bool

    is_commit_specific: bool
    """Indicates whether the override should only apply to commits.

    Defaults to `false`. If `true`, you can specify relevant commits in
    `override_specifiers` by passing `commit_ids`.
    """

    multiplier: float
    """Required for MULTIPLIER type. Must be >=0."""

    override_specifiers: Iterable[AddOverrideOverrideSpecifier]
    """Cannot be used in conjunction with product_id or applicable_product_tags.

    If provided, the override will apply to all products with the specified
    specifiers.
    """

    overwrite_rate: AddOverrideOverwriteRate
    """Required for OVERWRITE type."""

    priority: float
    """Required for EXPLICIT multiplier prioritization scheme and all TIERED overrides.

    Under EXPLICIT prioritization, overwrites are prioritized first, and then tiered
    and multiplier overrides are prioritized by their priority value (lowest first).
    Must be > 0.
    """

    product_id: str
    """ID of the product whose rate is being overridden"""

    target: Literal["COMMIT_RATE", "LIST_RATE"]
    """Indicates whether the override applies to commit rates or list rates.

    Can only be used for overrides that have `is_commit_specific` set to `true`.
    Defaults to `"LIST_RATE"`.
    """

    tiers: Iterable[AddOverrideTier]
    """Required for TIERED type. Must have at least one tier."""

    type: Literal["OVERWRITE", "MULTIPLIER", "TIERED"]
    """Overwrites are prioritized over multipliers and tiered overrides."""


class AddProfessionalService(TypedDict, total=False):
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
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class AddRecurringCommitAccessAmount(TypedDict, total=False):
    """The amount of commit to grant."""

    credit_type_id: Required[str]

    unit_price: Required[float]

    quantity: float
    """
    This field is required unless a subscription is attached via
    `subscription_config`.
    """


class AddRecurringCommitCommitDuration(TypedDict, total=False):
    """Defines the length of the access schedule for each created commit/credit.

    The value represents the number of units. Unit defaults to "PERIODS", where the length of a period is determined by the recurrence_frequency.
    """

    value: Required[float]

    unit: Literal["PERIODS"]


class AddRecurringCommitInvoiceAmount(TypedDict, total=False):
    """The amount the customer should be billed for the commit. Not required."""

    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class AddRecurringCommitSubscriptionConfigApplySeatIncreaseConfig(TypedDict, total=False):
    is_prorated: Required[bool]
    """Indicates whether a mid-period seat increase should be prorated."""


class AddRecurringCommitSubscriptionConfig(TypedDict, total=False):
    """Attach a subscription to the recurring commit/credit."""

    apply_seat_increase_config: Required[AddRecurringCommitSubscriptionConfigApplySeatIncreaseConfig]

    subscription_id: Required[str]
    """ID of the subscription to configure on the recurring commit/credit."""

    allocation: Literal["POOLED", "INDIVIDUAL"]
    """If set to POOLED, allocation added per seat is pooled across the account.

    If set to INDIVIDUAL, each seat in the subscription will have its own
    allocation.
    """


class AddRecurringCommit(TypedDict, total=False):
    access_amount: Required[AddRecurringCommitAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[AddRecurringCommitCommitDuration]
    """Defines the length of the access schedule for each created commit/credit.

    The value represents the number of units. Unit defaults to "PERIODS", where the
    length of a period is determined by the recurrence_frequency.
    """

    priority: Required[float]
    """Will be passed down to the individual commits"""

    product_id: Required[str]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """determines the start time for the first commit"""

    applicable_product_ids: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    applicable_product_tags: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    description: str
    """Will be passed down to the individual commits"""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Determines when the contract will stop creating recurring commits. optional"""

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for recurring credit hierarchy access control"""

    invoice_amount: AddRecurringCommitInvoiceAmount
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
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """

    subscription_config: AddRecurringCommitSubscriptionConfig
    """Attach a subscription to the recurring commit/credit."""

    temporary_id: str
    """
    A temporary ID that can be used to reference the recurring commit for commit
    specific overrides.
    """


class AddRecurringCreditAccessAmount(TypedDict, total=False):
    """The amount of commit to grant."""

    credit_type_id: Required[str]

    unit_price: Required[float]

    quantity: float
    """
    This field is required unless a subscription is attached via
    `subscription_config`.
    """


class AddRecurringCreditCommitDuration(TypedDict, total=False):
    """Defines the length of the access schedule for each created commit/credit.

    The value represents the number of units. Unit defaults to "PERIODS", where the length of a period is determined by the recurrence_frequency.
    """

    value: Required[float]

    unit: Literal["PERIODS"]


class AddRecurringCreditSubscriptionConfigApplySeatIncreaseConfig(TypedDict, total=False):
    is_prorated: Required[bool]
    """Indicates whether a mid-period seat increase should be prorated."""


class AddRecurringCreditSubscriptionConfig(TypedDict, total=False):
    """Attach a subscription to the recurring commit/credit."""

    apply_seat_increase_config: Required[AddRecurringCreditSubscriptionConfigApplySeatIncreaseConfig]

    subscription_id: Required[str]
    """ID of the subscription to configure on the recurring commit/credit."""

    allocation: Literal["POOLED", "INDIVIDUAL"]
    """If set to POOLED, allocation added per seat is pooled across the account.

    If set to INDIVIDUAL, each seat in the subscription will have its own
    allocation.
    """


class AddRecurringCredit(TypedDict, total=False):
    access_amount: Required[AddRecurringCreditAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[AddRecurringCreditCommitDuration]
    """Defines the length of the access schedule for each created commit/credit.

    The value represents the number of units. Unit defaults to "PERIODS", where the
    length of a period is determined by the recurrence_frequency.
    """

    priority: Required[float]
    """Will be passed down to the individual commits"""

    product_id: Required[str]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """determines the start time for the first commit"""

    applicable_product_ids: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    applicable_product_tags: SequenceNotStr[str]
    """Will be passed down to the individual commits"""

    description: str
    """Will be passed down to the individual commits"""

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Determines when the contract will stop creating recurring commits. optional"""

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for recurring credit hierarchy access control"""

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
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """

    subscription_config: AddRecurringCreditSubscriptionConfig
    """Attach a subscription to the recurring commit/credit."""

    temporary_id: str
    """
    A temporary ID that can be used to reference the recurring commit for commit
    specific overrides.
    """


class AddResellerRoyaltyAwsOptions(TypedDict, total=False):
    aws_account_number: str

    aws_offer_id: str

    aws_payer_reference_id: str


class AddResellerRoyaltyGcpOptions(TypedDict, total=False):
    gcp_account_id: str

    gcp_offer_id: str


class AddResellerRoyalty(TypedDict, total=False):
    reseller_type: Required[Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]]

    applicable_product_ids: SequenceNotStr[str]
    """Must provide at least one of applicable_product_ids or applicable_product_tags."""

    applicable_product_tags: SequenceNotStr[str]
    """Must provide at least one of applicable_product_ids or applicable_product_tags."""

    aws_options: AddResellerRoyaltyAwsOptions

    ending_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Use null to indicate that the existing end timestamp should be removed."""

    fraction: float

    gcp_options: AddResellerRoyaltyGcpOptions

    netsuite_reseller_id: str

    reseller_contract_value: float

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class AddScheduledChargeScheduleRecurringSchedule(TypedDict, total=False):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

    amount_distribution: Required[Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)."""

    frequency: Required[Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL", "WEEKLY"]]

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


class AddScheduledChargeScheduleScheduleItem(TypedDict, total=False):
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


class AddScheduledChargeSchedule(TypedDict, total=False):
    """Must provide either schedule_items or recurring_schedule."""

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: bool
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    recurring_schedule: AddScheduledChargeScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[AddScheduledChargeScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


class AddScheduledCharge(TypedDict, total=False):
    product_id: Required[str]

    schedule: Required[AddScheduledChargeSchedule]
    """Must provide either schedule_items or recurring_schedule."""

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class AddSubscriptionProration(TypedDict, total=False):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]
    """Indicates how mid-period quantity adjustments are invoiced.

    **BILL_IMMEDIATELY**: Only available when collection schedule is `ADVANCE`. The
    quantity increase will be billed immediately on the scheduled date.
    **BILL_ON_NEXT_COLLECTION_DATE**: The quantity increase will be billed for
    in-arrears at the end of the period.
    """

    is_prorated: bool
    """Indicates if the partial period will be prorated or charged a full amount."""


class AddSubscriptionSubscriptionRate(TypedDict, total=False):
    billing_frequency: Required[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]]
    """Frequency to bill subscription with.

    Together with product_id, must match existing rate on the rate card.
    """

    product_id: Required[str]
    """Must be subscription type product"""


class AddSubscriptionSeatConfig(TypedDict, total=False):
    initial_seat_ids: Required[SequenceNotStr[str]]
    """The initial assigned seats on this subscription."""

    seat_group_key: Required[str]
    """
    The property name, sent on usage events, that identifies the seat ID associated
    with the usage event. For example, the property name might be seat_id or
    user_id. The property must be set as a group key on billable metrics and a
    presentation/pricing group key on contract products. This allows linked
    recurring credits with an allocation per seat to be consumed by only one seat's
    usage.
    """

    initial_unassigned_seats: float
    """The initial amount of unassigned seats on this subscription."""


class AddSubscription(TypedDict, total=False):
    collection_schedule: Required[Literal["ADVANCE", "ARREARS"]]

    proration: Required[AddSubscriptionProration]

    subscription_rate: Required[AddSubscriptionSubscriptionRate]

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Exclusive end time for the subscription.

    If not provided, subscription inherits contract end date.
    """

    initial_quantity: float
    """The initial quantity for the subscription.

    It must be non-negative value. Required if quantity_management_mode is
    QUANTITY_ONLY.
    """

    name: str

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

    seat_config: AddSubscriptionSeatConfig

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Inclusive start time for the subscription.

    If not provided, defaults to contract start date
    """

    temporary_id: str
    """
    A temporary ID used to reference the subscription in recurring commit/credit
    subscription configs created within the same payload.
    """


class ArchiveCommit(TypedDict, total=False):
    id: Required[str]


class ArchiveCredit(TypedDict, total=False):
    id: Required[str]


class ArchiveScheduledCharge(TypedDict, total=False):
    id: Required[str]


class RemoveOverride(TypedDict, total=False):
    id: Required[str]


class UpdateCommitAccessScheduleAddScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


class UpdateCommitAccessScheduleRemoveScheduleItem(TypedDict, total=False):
    id: Required[str]


class UpdateCommitAccessScheduleUpdateScheduleItem(TypedDict, total=False):
    id: Required[str]

    amount: float

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class UpdateCommitAccessSchedule(TypedDict, total=False):
    add_schedule_items: Iterable[UpdateCommitAccessScheduleAddScheduleItem]

    remove_schedule_items: Iterable[UpdateCommitAccessScheduleRemoveScheduleItem]

    update_schedule_items: Iterable[UpdateCommitAccessScheduleUpdateScheduleItem]


class UpdateCommitInvoiceScheduleAddScheduleItem(TypedDict, total=False):
    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    amount: float

    quantity: float

    unit_price: float


class UpdateCommitInvoiceScheduleRemoveScheduleItem(TypedDict, total=False):
    id: Required[str]


class UpdateCommitInvoiceScheduleUpdateScheduleItem(TypedDict, total=False):
    id: Required[str]

    amount: float

    quantity: float

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    unit_price: float


class UpdateCommitInvoiceSchedule(TypedDict, total=False):
    add_schedule_items: Iterable[UpdateCommitInvoiceScheduleAddScheduleItem]

    remove_schedule_items: Iterable[UpdateCommitInvoiceScheduleRemoveScheduleItem]

    update_schedule_items: Iterable[UpdateCommitInvoiceScheduleUpdateScheduleItem]


class UpdateCommit(TypedDict, total=False):
    commit_id: Required[str]

    access_schedule: UpdateCommitAccessSchedule

    applicable_product_ids: Optional[SequenceNotStr[str]]
    """Which products the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: Optional[SequenceNotStr[str]]
    """Which tags the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    description: str

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for commit hierarchy access control"""

    invoice_schedule: UpdateCommitInvoiceSchedule

    name: str

    netsuite_sales_order_id: Optional[str]

    priority: Optional[float]

    product_id: str

    rate_type: Literal["LIST_RATE", "COMMIT_RATE"]
    """
    If provided, updates the commit to use the specified rate type for current and
    future invoices. Previously finalized invoices will need to be voided and
    regenerated to reflect the rate type change.
    """

    rollover_fraction: Optional[float]


class UpdateCreditAccessScheduleAddScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]


class UpdateCreditAccessScheduleRemoveScheduleItem(TypedDict, total=False):
    id: Required[str]


class UpdateCreditAccessScheduleUpdateScheduleItem(TypedDict, total=False):
    id: Required[str]

    amount: float

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class UpdateCreditAccessSchedule(TypedDict, total=False):
    add_schedule_items: Iterable[UpdateCreditAccessScheduleAddScheduleItem]

    remove_schedule_items: Iterable[UpdateCreditAccessScheduleRemoveScheduleItem]

    update_schedule_items: Iterable[UpdateCreditAccessScheduleUpdateScheduleItem]


class UpdateCredit(TypedDict, total=False):
    credit_id: Required[str]

    access_schedule: UpdateCreditAccessSchedule

    applicable_product_ids: Optional[SequenceNotStr[str]]
    """Which products the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: Optional[SequenceNotStr[str]]
    """Which tags the commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    description: str

    hierarchy_configuration: CommitHierarchyConfiguration
    """Optional configuration for commit hierarchy access control"""

    name: str

    netsuite_sales_order_id: Optional[str]

    priority: Optional[float]

    product_id: str

    rate_type: Literal["LIST_RATE", "COMMIT_RATE"]
    """
    If provided, updates the credit to use the specified rate type for current and
    future invoices. Previously finalized invoices will need to be voided and
    regenerated to reflect the rate type change.
    """


class UpdatePrepaidBalanceThresholdConfigurationCommit(UpdateBaseThresholdCommit, total=False):
    applicable_product_ids: Optional[SequenceNotStr[str]]
    """Which products the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[SequenceNotStr[str]]
    """Which tags the threshold commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    specifiers: Optional[Iterable[CommitSpecifierInput]]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class UpdatePrepaidBalanceThresholdConfiguration(TypedDict, total=False):
    commit: UpdatePrepaidBalanceThresholdConfigurationCommit

    custom_credit_type_id: Optional[str]
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: PaymentGateConfigV2

    recharge_to_amount: float
    """Specify the amount the balance should be recharged to."""

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's balance lowers to this amount, a threshold charge will
    be initiated.
    """


class UpdateRecurringCommitAccessAmount(TypedDict, total=False):
    quantity: float

    unit_price: float


class UpdateRecurringCommitInvoiceAmount(TypedDict, total=False):
    quantity: float

    unit_price: float


class UpdateRecurringCommit(TypedDict, total=False):
    recurring_commit_id: Required[str]

    access_amount: UpdateRecurringCommitAccessAmount

    ending_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    invoice_amount: UpdateRecurringCommitInvoiceAmount

    rate_type: Literal["LIST_RATE", "COMMIT_RATE"]
    """
    If provided, updates the recurring commit to use the specified rate type when
    generating future commits.
    """


class UpdateRecurringCreditAccessAmount(TypedDict, total=False):
    quantity: float

    unit_price: float


class UpdateRecurringCredit(TypedDict, total=False):
    recurring_credit_id: Required[str]

    access_amount: UpdateRecurringCreditAccessAmount

    ending_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    rate_type: Literal["LIST_RATE", "COMMIT_RATE"]
    """
    If provided, updates the recurring credit to use the specified rate type when
    generating future credits.
    """


class UpdateScheduledChargeInvoiceScheduleAddScheduleItem(TypedDict, total=False):
    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    amount: float

    quantity: float

    unit_price: float


class UpdateScheduledChargeInvoiceScheduleRemoveScheduleItem(TypedDict, total=False):
    id: Required[str]


class UpdateScheduledChargeInvoiceScheduleUpdateScheduleItem(TypedDict, total=False):
    id: Required[str]

    amount: float

    quantity: float

    timestamp: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    unit_price: float


class UpdateScheduledChargeInvoiceSchedule(TypedDict, total=False):
    add_schedule_items: Iterable[UpdateScheduledChargeInvoiceScheduleAddScheduleItem]

    remove_schedule_items: Iterable[UpdateScheduledChargeInvoiceScheduleRemoveScheduleItem]

    update_schedule_items: Iterable[UpdateScheduledChargeInvoiceScheduleUpdateScheduleItem]


class UpdateScheduledCharge(TypedDict, total=False):
    scheduled_charge_id: Required[str]

    invoice_schedule: UpdateScheduledChargeInvoiceSchedule

    netsuite_sales_order_id: Optional[str]


class UpdateSpendThresholdConfiguration(TypedDict, total=False):
    commit: UpdateBaseThresholdCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: PaymentGateConfigV2

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class UpdateSubscriptionQuantityManagementModeUpdateSeatConfig(TypedDict, total=False):
    seat_group_key: Required[str]


class UpdateSubscriptionQuantityManagementModeUpdate(TypedDict, total=False):
    """
    Update the subscription's quantity management mode from QUANTITY_ONLY to SEAT_BASED with the provided seat_group_key.
    """

    quantity_management_mode: Required[Literal["SEAT_BASED"]]

    seat_config: Required[UpdateSubscriptionQuantityManagementModeUpdateSeatConfig]


class UpdateSubscriptionQuantityUpdate(TypedDict, total=False):
    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    quantity: float
    """The new quantity for the subscription.

    Must be provided if quantity_delta is not provided. Must be non-negative.
    """

    quantity_delta: float
    """The delta to add to the subscription's quantity.

    Must be provided if quantity is not provided. Can't be zero. It also can't
    result in a negative quantity on the subscription.
    """


class UpdateSubscriptionSeatUpdatesAddSeatID(TypedDict, total=False):
    seat_ids: Required[SequenceNotStr[str]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Assigned seats will be added/removed starting at this date."""


class UpdateSubscriptionSeatUpdatesAddUnassignedSeat(TypedDict, total=False):
    quantity: Required[float]
    """
    The number of unassigned seats on the subscription will increase/decrease by
    this delta. Must be greater than 0.
    """

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Unassigned seats will be updated starting at this date."""


class UpdateSubscriptionSeatUpdatesRemoveSeatID(TypedDict, total=False):
    seat_ids: Required[SequenceNotStr[str]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Assigned seats will be added/removed starting at this date."""


class UpdateSubscriptionSeatUpdatesRemoveUnassignedSeat(TypedDict, total=False):
    quantity: Required[float]
    """
    The number of unassigned seats on the subscription will increase/decrease by
    this delta. Must be greater than 0.
    """

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Unassigned seats will be updated starting at this date."""


class UpdateSubscriptionSeatUpdates(TypedDict, total=False):
    add_seat_ids: Iterable[UpdateSubscriptionSeatUpdatesAddSeatID]
    """Adds seat IDs to the subscription.

    If there are unassigned seats, the new seat IDs will fill these unassigned seats
    and not increase the total subscription quantity. Otherwise, if there are more
    new seat IDs than unassigned seats, the total subscription quantity will
    increase.
    """

    add_unassigned_seats: Iterable[UpdateSubscriptionSeatUpdatesAddUnassignedSeat]
    """Adds unassigned seats to the subscription.

    This will increase the total subscription quantity.
    """

    remove_seat_ids: Iterable[UpdateSubscriptionSeatUpdatesRemoveSeatID]
    """Removes seat IDs from the subscription, if possible.

    If a seat ID is removed, the total subscription quantity will decrease.
    Otherwise, if the seat ID is not found on the subscription, this is a no-op.
    """

    remove_unassigned_seats: Iterable[UpdateSubscriptionSeatUpdatesRemoveUnassignedSeat]
    """Removes unassigned seats from the subscription.

    This will decrease the total subscription quantity if there are are unassigned
    seats.
    """


class UpdateSubscription(TypedDict, total=False):
    subscription_id: Required[str]

    ending_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]

    quantity_management_mode_update: UpdateSubscriptionQuantityManagementModeUpdate
    """
    Update the subscription's quantity management mode from QUANTITY_ONLY to
    SEAT_BASED with the provided seat_group_key.
    """

    quantity_updates: Iterable[UpdateSubscriptionQuantityUpdate]
    """
    Quantity changes are applied on the effective date based on the order which they
    are sent. For example, if I scheduled the quantity to be 12 on May 21 and then
    scheduled a quantity delta change of -1, the result from that day would be 11.
    """

    seat_updates: UpdateSubscriptionSeatUpdates
