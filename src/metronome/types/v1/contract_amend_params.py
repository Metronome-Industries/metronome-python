# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.tier import Tier
from ..shared_params.commit_specifier_input import CommitSpecifierInput
from ..shared_params.commit_hierarchy_configuration import CommitHierarchyConfiguration

__all__ = [
    "ContractAmendParams",
    "Commit",
    "CommitAccessSchedule",
    "CommitAccessScheduleScheduleItem",
    "CommitInvoiceSchedule",
    "CommitInvoiceScheduleRecurringSchedule",
    "CommitInvoiceScheduleScheduleItem",
    "CommitPaymentGateConfig",
    "CommitPaymentGateConfigPrecalculatedTaxConfig",
    "CommitPaymentGateConfigStripeConfig",
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
    "ResellerRoyalty",
    "ResellerRoyaltyAwsOptions",
    "ResellerRoyaltyGcpOptions",
    "ScheduledCharge",
    "ScheduledChargeSchedule",
    "ScheduledChargeScheduleRecurringSchedule",
    "ScheduledChargeScheduleScheduleItem",
]


class ContractAmendParams(TypedDict, total=False):
    contract_id: Required[str]
    """ID of the contract to amend"""

    customer_id: Required[str]
    """ID of the customer whose contract is to be amended"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """inclusive start time for the amendment"""

    commits: Iterable[Commit]

    credits: Iterable[Credit]

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    discounts: Iterable[Discount]
    """This field's availability is dependent on your client's configuration."""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""

    overrides: Iterable[Override]

    professional_services: Iterable[ProfessionalService]
    """This field's availability is dependent on your client's configuration."""

    reseller_royalties: Iterable[ResellerRoyalty]
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: str
    """This field's availability is dependent on your client's configuration."""

    scheduled_charges: Iterable[ScheduledCharge]

    total_contract_value: float
    """This field's availability is dependent on your client's configuration."""


class CommitAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class CommitAccessSchedule(TypedDict, total=False):
    """Required: Schedule for distributing the commit to the customer.

    For "POSTPAID" commits only one schedule item is allowed and amount must match invoice_schedule total.
    """

    schedule_items: Required[Iterable[CommitAccessScheduleScheduleItem]]

    credit_type_id: str
    """Defaults to USD (cents) if not passed"""


class CommitInvoiceScheduleRecurringSchedule(TypedDict, total=False):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

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
    """
    Required for "POSTPAID" commits: the true up invoice will be generated at this time and only one schedule item is allowed; the total must match access_schedule amount. Optional for "PREPAID" commits: if not provided, this will be a "complimentary" commit with no invoice.
    """

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: bool
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

    recurring_schedule: CommitInvoiceScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[CommitInvoiceScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


class CommitPaymentGateConfigPrecalculatedTaxConfig(TypedDict, total=False):
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


class CommitPaymentGateConfigStripeConfig(TypedDict, total=False):
    """Only applicable if using STRIPE as your payment gate type."""

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
    """optionally payment gate this commit"""

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

    tax_type: Literal["NONE", "STRIPE", "ANROK", "AVALARA", "PRECALCULATED"]
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


class CreditAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class CreditAccessSchedule(TypedDict, total=False):
    """Schedule for distributing the credit to the customer."""

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
    """


class DiscountScheduleRecurringSchedule(TypedDict, total=False):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

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
    """Must provide either schedule_items or recurring_schedule."""

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: bool
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

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
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


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


class OverrideOverwriteRate(TypedDict, total=False):
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


class OverrideTier(TypedDict, total=False):
    multiplier: Required[float]

    size: float


class Override(TypedDict, total=False):
    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp indicating when the override will start applying (inclusive)"""

    applicable_product_tags: SequenceNotStr[str]
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
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    description: str

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class ResellerRoyaltyAwsOptions(TypedDict, total=False):
    aws_account_number: str

    aws_offer_id: str

    aws_payer_reference_id: str


class ResellerRoyaltyGcpOptions(TypedDict, total=False):
    gcp_account_id: str

    gcp_offer_id: str


class ResellerRoyalty(TypedDict, total=False):
    reseller_type: Required[Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]]

    applicable_product_ids: SequenceNotStr[str]
    """Must provide at least one of applicable_product_ids or applicable_product_tags."""

    applicable_product_tags: SequenceNotStr[str]
    """Must provide at least one of applicable_product_ids or applicable_product_tags."""

    aws_options: ResellerRoyaltyAwsOptions

    ending_before: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Use null to indicate that the existing end timestamp should be removed."""

    fraction: float

    gcp_options: ResellerRoyaltyGcpOptions

    netsuite_reseller_id: str

    reseller_contract_value: float

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]


class ScheduledChargeScheduleRecurringSchedule(TypedDict, total=False):
    """Enter the unit price and quantity for the charge or instead only send the amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is inferred to be 1.
    """

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
    """Must provide either schedule_items or recurring_schedule."""

    credit_type_id: str
    """Defaults to USD (cents) if not passed."""

    do_not_invoice: bool
    """This field is only applicable to commit invoice schedules.

    If true, this schedule will not generate an invoice.
    """

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

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""
