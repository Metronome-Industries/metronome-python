# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.tier import Tier
from ..shared.discount import Discount
from ..shared.pro_service import ProService
from ..shared.credit_type_data import CreditTypeData
from ..shared.schedule_duration import ScheduleDuration
from ..shared.schedule_point_in_time import SchedulePointInTime

__all__ = [
    "ContractGetEditHistoryResponse",
    "Data",
    "DataAddCommit",
    "DataAddCommitProduct",
    "DataAddCommitHierarchyConfiguration",
    "DataAddCommitHierarchyConfigurationChildAccess",
    "DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "DataAddCommitSpecifier",
    "DataAddCredit",
    "DataAddCreditProduct",
    "DataAddCreditHierarchyConfiguration",
    "DataAddCreditHierarchyConfigurationChildAccess",
    "DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "DataAddCreditSpecifier",
    "DataAddOverride",
    "DataAddOverrideOverrideSpecifier",
    "DataAddOverrideOverrideTier",
    "DataAddOverrideOverwriteRate",
    "DataAddOverrideProduct",
    "DataAddPrepaidBalanceThresholdConfiguration",
    "DataAddPrepaidBalanceThresholdConfigurationCommit",
    "DataAddPrepaidBalanceThresholdConfigurationCommitSpecifier",
    "DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfig",
    "DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataAddRecurringCommit",
    "DataAddRecurringCommitAccessAmount",
    "DataAddRecurringCommitCommitDuration",
    "DataAddRecurringCommitProduct",
    "DataAddRecurringCommitContract",
    "DataAddRecurringCommitHierarchyConfiguration",
    "DataAddRecurringCommitHierarchyConfigurationChildAccess",
    "DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "DataAddRecurringCommitInvoiceAmount",
    "DataAddRecurringCommitSpecifier",
    "DataAddRecurringCommitSubscriptionConfig",
    "DataAddRecurringCommitSubscriptionConfigApplySeatIncreaseConfig",
    "DataAddRecurringCredit",
    "DataAddRecurringCreditAccessAmount",
    "DataAddRecurringCreditCommitDuration",
    "DataAddRecurringCreditProduct",
    "DataAddRecurringCreditContract",
    "DataAddRecurringCreditHierarchyConfiguration",
    "DataAddRecurringCreditHierarchyConfigurationChildAccess",
    "DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "DataAddRecurringCreditSpecifier",
    "DataAddRecurringCreditSubscriptionConfig",
    "DataAddRecurringCreditSubscriptionConfigApplySeatIncreaseConfig",
    "DataAddResellerRoyalty",
    "DataAddScheduledCharge",
    "DataAddScheduledChargeProduct",
    "DataAddSpendThresholdConfiguration",
    "DataAddSpendThresholdConfigurationCommit",
    "DataAddSpendThresholdConfigurationPaymentGateConfig",
    "DataAddSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "DataAddSpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataAddSubscription",
    "DataAddSubscriptionProration",
    "DataAddSubscriptionQuantitySchedule",
    "DataAddSubscriptionSubscriptionRate",
    "DataAddSubscriptionSubscriptionRateProduct",
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
    "DataUpdateCommitHierarchyConfiguration",
    "DataUpdateCommitHierarchyConfigurationChildAccess",
    "DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "DataUpdateCommitInvoiceSchedule",
    "DataUpdateCommitInvoiceScheduleAddScheduleItem",
    "DataUpdateCommitInvoiceScheduleRemoveScheduleItem",
    "DataUpdateCommitInvoiceScheduleUpdateScheduleItem",
    "DataUpdateCommitSpecifier",
    "DataUpdateCredit",
    "DataUpdateCreditAccessSchedule",
    "DataUpdateCreditAccessScheduleAddScheduleItem",
    "DataUpdateCreditAccessScheduleRemoveScheduleItem",
    "DataUpdateCreditAccessScheduleUpdateScheduleItem",
    "DataUpdateCreditHierarchyConfiguration",
    "DataUpdateCreditHierarchyConfigurationChildAccess",
    "DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "DataUpdateDiscount",
    "DataUpdateDiscountSchedule",
    "DataUpdateDiscountScheduleRecurringSchedule",
    "DataUpdateDiscountScheduleScheduleItem",
    "DataUpdatePrepaidBalanceThresholdConfiguration",
    "DataUpdatePrepaidBalanceThresholdConfigurationCommit",
    "DataUpdatePrepaidBalanceThresholdConfigurationCommitSpecifier",
    "DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfig",
    "DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataUpdateRecurringCommit",
    "DataUpdateRecurringCommitAccessAmount",
    "DataUpdateRecurringCommitInvoiceAmount",
    "DataUpdateRecurringCredit",
    "DataUpdateRecurringCreditAccessAmount",
    "DataUpdateRefundInvoice",
    "DataUpdateScheduledCharge",
    "DataUpdateScheduledChargeInvoiceSchedule",
    "DataUpdateScheduledChargeInvoiceScheduleAddScheduleItem",
    "DataUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem",
    "DataUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem",
    "DataUpdateSpendThresholdConfiguration",
    "DataUpdateSpendThresholdConfigurationCommit",
    "DataUpdateSpendThresholdConfigurationPaymentGateConfig",
    "DataUpdateSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "DataUpdateSpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "DataUpdateSubscription",
    "DataUpdateSubscriptionQuantityUpdate",
]


class DataAddCommitProduct(BaseModel):
    id: str

    name: str


class DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataAddCommitHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    DataAddCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class DataAddCommitHierarchyConfiguration(BaseModel):
    child_access: DataAddCommitHierarchyConfigurationChildAccess


class DataAddCommitSpecifier(BaseModel):
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

    hierarchy_configuration: Optional[DataAddCommitHierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

    invoice_schedule: Optional[SchedulePointInTime] = None
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

    specifiers: Optional[List[DataAddCommitSpecifier]] = None
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


class DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataAddCreditHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    DataAddCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class DataAddCreditHierarchyConfiguration(BaseModel):
    child_access: DataAddCreditHierarchyConfigurationChildAccess


class DataAddCreditSpecifier(BaseModel):
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


class DataAddCredit(BaseModel):
    id: str

    product: DataAddCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[ScheduleDuration] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    description: Optional[str] = None

    hierarchy_configuration: Optional[DataAddCreditHierarchyConfiguration] = None
    """Optional configuration for recurring credit hierarchy access control"""

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

    specifiers: Optional[List[DataAddCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataAddOverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None

    recurring_credit_ids: Optional[List[str]] = None


class DataAddOverrideOverrideTier(BaseModel):
    multiplier: float

    size: Optional[float] = None


class DataAddOverrideOverwriteRate(BaseModel):
    rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]

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

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[DataAddOverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[DataAddOverrideOverrideTier]] = None

    overwrite_rate: Optional[DataAddOverrideOverwriteRate] = None

    priority: Optional[float] = None

    product: Optional[DataAddOverrideProduct] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None


class DataAddPrepaidBalanceThresholdConfigurationCommitSpecifier(BaseModel):
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


class DataAddPrepaidBalanceThresholdConfigurationCommit(BaseModel):
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

    specifiers: Optional[List[DataAddPrepaidBalanceThresholdConfigurationCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[
        DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig
    ] = None
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataAddPrepaidBalanceThresholdConfiguration(BaseModel):
    commit: DataAddPrepaidBalanceThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataAddPrepaidBalanceThresholdConfigurationPaymentGateConfig

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


class DataAddRecurringCommitAccessAmount(BaseModel):
    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataAddRecurringCommitCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataAddRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataAddRecurringCommitContract(BaseModel):
    id: str


class DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataAddRecurringCommitHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    DataAddRecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class DataAddRecurringCommitHierarchyConfiguration(BaseModel):
    child_access: DataAddRecurringCommitHierarchyConfigurationChildAccess


class DataAddRecurringCommitInvoiceAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataAddRecurringCommitSpecifier(BaseModel):
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


class DataAddRecurringCommitSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class DataAddRecurringCommitSubscriptionConfig(BaseModel):
    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: DataAddRecurringCommitSubscriptionConfigApplySeatIncreaseConfig

    subscription_id: str


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

    hierarchy_configuration: Optional[DataAddRecurringCommitHierarchyConfiguration] = None
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

    specifiers: Optional[List[DataAddRecurringCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[DataAddRecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class DataAddRecurringCreditAccessAmount(BaseModel):
    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataAddRecurringCreditCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataAddRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataAddRecurringCreditContract(BaseModel):
    id: str


class DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataAddRecurringCreditHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    DataAddRecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class DataAddRecurringCreditHierarchyConfiguration(BaseModel):
    child_access: DataAddRecurringCreditHierarchyConfigurationChildAccess


class DataAddRecurringCreditSpecifier(BaseModel):
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


class DataAddRecurringCreditSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class DataAddRecurringCreditSubscriptionConfig(BaseModel):
    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: DataAddRecurringCreditSubscriptionConfigApplySeatIncreaseConfig

    subscription_id: str


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

    hierarchy_configuration: Optional[DataAddRecurringCreditHierarchyConfiguration] = None
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

    specifiers: Optional[List[DataAddRecurringCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[DataAddRecurringCreditSubscriptionConfig] = None
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


class DataAddSpendThresholdConfigurationCommit(BaseModel):
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


class DataAddSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class DataAddSpendThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class DataAddSpendThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[DataAddSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig] = None
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[DataAddSpendThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataAddSpendThresholdConfiguration(BaseModel):
    commit: DataAddSpendThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: DataAddSpendThresholdConfigurationPaymentGateConfig

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class DataAddSubscriptionProration(BaseModel):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]

    is_prorated: bool


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


class DataAddSubscription(BaseModel):
    collection_schedule: Literal["ADVANCE", "ARREARS"]

    proration: DataAddSubscriptionProration

    quantity_schedule: List[DataAddSubscriptionQuantitySchedule]
    """List of quantity schedule items for the subscription.

    Only includes the current quantity and future quantity changes.
    """

    starting_at: datetime

    subscription_rate: DataAddSubscriptionSubscriptionRate

    id: Optional[str] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ending_before: Optional[datetime] = None

    fiat_credit_type_id: Optional[str] = None

    name: Optional[str] = None


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


class DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataUpdateCommitHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    DataUpdateCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class DataUpdateCommitHierarchyConfiguration(BaseModel):
    child_access: DataUpdateCommitHierarchyConfigurationChildAccess


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


class DataUpdateCommitSpecifier(BaseModel):
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

    hierarchy_configuration: Optional[DataUpdateCommitHierarchyConfiguration] = None
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

    rollover_fraction: Optional[float] = None

    specifiers: Optional[List[DataUpdateCommitSpecifier]] = None
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


class DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


DataUpdateCreditHierarchyConfigurationChildAccess: TypeAlias = Union[
    DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    DataUpdateCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class DataUpdateCreditHierarchyConfiguration(BaseModel):
    child_access: DataUpdateCreditHierarchyConfigurationChildAccess


class DataUpdateCredit(BaseModel):
    id: str

    access_schedule: Optional[DataUpdateCreditAccessSchedule] = None

    hierarchy_configuration: Optional[DataUpdateCreditHierarchyConfiguration] = None
    """Optional configuration for credit hierarchy access control"""

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    priority: Optional[float] = None
    """
    If multiple credits are applicable, the one with the lower priority will apply
    first.
    """

    rollover_fraction: Optional[float] = None


class DataUpdateDiscountScheduleRecurringSchedule(BaseModel):
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

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    schedule: Optional[DataUpdateDiscountSchedule] = None
    """Must provide either schedule_items or recurring_schedule."""


class DataUpdatePrepaidBalanceThresholdConfigurationCommitSpecifier(BaseModel):
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


class DataUpdatePrepaidBalanceThresholdConfigurationCommit(BaseModel):
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

    product_id: Optional[str] = None
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """

    specifiers: Optional[List[DataUpdatePrepaidBalanceThresholdConfigurationCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[
        DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig
    ] = None
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataUpdatePrepaidBalanceThresholdConfiguration(BaseModel):
    commit: Optional[DataUpdatePrepaidBalanceThresholdConfigurationCommit] = None

    custom_credit_type_id: Optional[str] = None
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """

    is_enabled: Optional[bool] = None
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: Optional[DataUpdatePrepaidBalanceThresholdConfigurationPaymentGateConfig] = None

    recharge_to_amount: Optional[float] = None
    """Specify the amount the balance should be recharged to."""

    threshold_amount: Optional[float] = None
    """Specify the threshold amount for the contract.

    Each time the contract's balance lowers to this amount, a threshold charge will
    be initiated.
    """


class DataUpdateRecurringCommitAccessAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateRecurringCommitInvoiceAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateRecurringCommit(BaseModel):
    id: str

    access_amount: Optional[DataUpdateRecurringCommitAccessAmount] = None

    ending_before: Optional[datetime] = None

    invoice_amount: Optional[DataUpdateRecurringCommitInvoiceAmount] = None


class DataUpdateRecurringCreditAccessAmount(BaseModel):
    quantity: Optional[float] = None

    unit_price: Optional[float] = None


class DataUpdateRecurringCredit(BaseModel):
    id: str

    access_amount: Optional[DataUpdateRecurringCreditAccessAmount] = None

    ending_before: Optional[datetime] = None


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


class DataUpdateSpendThresholdConfigurationCommit(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """

    product_id: Optional[str] = None
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """


class DataUpdateSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class DataUpdateSpendThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class DataUpdateSpendThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[DataUpdateSpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig] = (
        None
    )
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[DataUpdateSpendThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gateway type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class DataUpdateSpendThresholdConfiguration(BaseModel):
    commit: Optional[DataUpdateSpendThresholdConfigurationCommit] = None

    is_enabled: Optional[bool] = None
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: Optional[DataUpdateSpendThresholdConfigurationPaymentGateConfig] = None

    threshold_amount: Optional[float] = None
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class DataUpdateSubscriptionQuantityUpdate(BaseModel):
    starting_at: datetime

    quantity: Optional[float] = None

    quantity_delta: Optional[float] = None


class DataUpdateSubscription(BaseModel):
    id: str

    ending_before: Optional[datetime] = None

    quantity_updates: Optional[List[DataUpdateSubscriptionQuantityUpdate]] = None


class Data(BaseModel):
    id: str

    add_commits: Optional[List[DataAddCommit]] = None

    add_credits: Optional[List[DataAddCredit]] = None

    add_discounts: Optional[List[Discount]] = None

    add_overrides: Optional[List[DataAddOverride]] = None

    add_prepaid_balance_threshold_configuration: Optional[DataAddPrepaidBalanceThresholdConfiguration] = None

    add_pro_services: Optional[List[ProService]] = None

    add_recurring_commits: Optional[List[DataAddRecurringCommit]] = None

    add_recurring_credits: Optional[List[DataAddRecurringCredit]] = None

    add_reseller_royalties: Optional[List[DataAddResellerRoyalty]] = None

    add_scheduled_charges: Optional[List[DataAddScheduledCharge]] = None

    add_spend_threshold_configuration: Optional[DataAddSpendThresholdConfiguration] = None

    add_subscriptions: Optional[List[DataAddSubscription]] = None
    """List of subscriptions on the contract."""

    add_usage_filters: Optional[List[DataAddUsageFilter]] = None

    archive_commits: Optional[List[DataArchiveCommit]] = None

    archive_credits: Optional[List[DataArchiveCredit]] = None

    archive_scheduled_charges: Optional[List[DataArchiveScheduledCharge]] = None

    remove_overrides: Optional[List[DataRemoveOverride]] = None

    timestamp: Optional[datetime] = None

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
