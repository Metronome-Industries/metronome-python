# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.tier import Tier

__all__ = [
    "ContractEditParams",
    "AddCommit",
    "AddCommitAccessSchedule",
    "AddCommitAccessScheduleScheduleItem",
    "AddCommitInvoiceSchedule",
    "AddCommitInvoiceScheduleRecurringSchedule",
    "AddCommitInvoiceScheduleScheduleItem",
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
    "AddRecurringCredit",
    "AddRecurringCreditAccessAmount",
    "AddRecurringCreditCommitDuration",
    "AddResellerRoyalty",
    "AddResellerRoyaltyAwsOptions",
    "AddResellerRoyaltyGcpOptions",
    "AddScheduledCharge",
    "AddScheduledChargeSchedule",
    "AddScheduledChargeScheduleRecurringSchedule",
    "AddScheduledChargeScheduleScheduleItem",
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
    "UpdateScheduledCharge",
    "UpdateScheduledChargeInvoiceSchedule",
    "UpdateScheduledChargeInvoiceScheduleAddScheduleItem",
    "UpdateScheduledChargeInvoiceScheduleRemoveScheduleItem",
    "UpdateScheduledChargeInvoiceScheduleUpdateScheduleItem",
]


class ContractEditParams(TypedDict, total=False):
    contract_id: Required[str]
    """ID of the contract being edited"""

    customer_id: Required[str]
    """ID of the customer whose contract is being edited"""

    add_commits: Iterable[AddCommit]

    add_credits: Iterable[AddCredit]

    add_discounts: Iterable[AddDiscount]

    add_overrides: Iterable[AddOverride]

    add_professional_services: Iterable[AddProfessionalService]
    """This field's availability is dependent on your client's configuration."""

    add_recurring_commits: Iterable[AddRecurringCommit]

    add_recurring_credits: Iterable[AddRecurringCredit]

    add_reseller_royalties: Iterable[AddResellerRoyalty]

    add_scheduled_charges: Iterable[AddScheduledCharge]

    update_commits: Iterable[UpdateCommit]

    update_credits: Iterable[UpdateCredit]

    update_scheduled_charges: Iterable[UpdateScheduledCharge]


class AddCommitAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class AddCommitAccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[AddCommitAccessScheduleScheduleItem]]

    credit_type_id: str


class AddCommitInvoiceScheduleRecurringSchedule(TypedDict, total=False):
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
    credit_type_id: str
    """Defaults to USD if not passed. Only USD is supported at this time."""

    recurring_schedule: AddCommitInvoiceScheduleRecurringSchedule
    """Enter the unit price and quantity for the charge or instead only send the
    amount.

    If amount is sent, the unit price is assumed to be the amount and quantity is
    inferred to be 1.
    """

    schedule_items: Iterable[AddCommitInvoiceScheduleScheduleItem]
    """Either provide amount or provide both unit_price and quantity."""


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


class AddCreditAccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp (inclusive)"""


class AddCreditAccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[AddCreditAccessScheduleScheduleItem]]

    credit_type_id: str


class AddCredit(TypedDict, total=False):
    access_schedule: Required[AddCreditAccessSchedule]
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


class AddDiscountScheduleRecurringSchedule(TypedDict, total=False):
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
    credit_type_id: str
    """Defaults to USD if not passed. Only USD is supported at this time."""

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

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class AddOverrideOverrideSpecifier(TypedDict, total=False):
    commit_ids: List[str]
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
    will only apply to commits created by the specified recurring credit ids.
    """


class AddOverrideOverwriteRate(TypedDict, total=False):
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

    applicable_product_tags: List[str]
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

    description: str

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


class AddRecurringCommitAccessAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class AddRecurringCommitCommitDuration(TypedDict, total=False):
    unit: Required[Literal["PERIODS"]]

    value: Required[float]


class AddRecurringCommitInvoiceAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class AddRecurringCommit(TypedDict, total=False):
    access_amount: Required[AddRecurringCommitAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[AddRecurringCommitCommitDuration]
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


class AddRecurringCreditAccessAmount(TypedDict, total=False):
    credit_type_id: Required[str]

    quantity: Required[float]

    unit_price: Required[float]


class AddRecurringCreditCommitDuration(TypedDict, total=False):
    unit: Required[Literal["PERIODS"]]

    value: Required[float]


class AddRecurringCredit(TypedDict, total=False):
    access_amount: Required[AddRecurringCreditAccessAmount]
    """The amount of commit to grant."""

    commit_duration: Required[AddRecurringCreditCommitDuration]
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


class AddResellerRoyaltyAwsOptions(TypedDict, total=False):
    aws_account_number: str

    aws_offer_id: str

    aws_payer_reference_id: str


class AddResellerRoyaltyGcpOptions(TypedDict, total=False):
    gcp_account_id: str

    gcp_offer_id: str


class AddResellerRoyalty(TypedDict, total=False):
    reseller_type: Required[Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]]

    applicable_product_ids: List[str]
    """Must provide at least one of applicable_product_ids or applicable_product_tags."""

    applicable_product_tags: List[str]
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
    credit_type_id: str
    """Defaults to USD if not passed. Only USD is supported at this time."""

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

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""


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

    applicable_product_ids: Optional[List[str]]
    """Which products the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]]
    """Which tags the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    invoice_schedule: UpdateCommitInvoiceSchedule

    netsuite_sales_order_id: Optional[str]

    product_id: str

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

    applicable_product_ids: Optional[List[str]]
    """Which products the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]]
    """Which tags the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    netsuite_sales_order_id: Optional[str]

    product_id: str


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
