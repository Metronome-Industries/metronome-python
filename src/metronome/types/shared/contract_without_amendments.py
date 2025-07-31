# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .commit import Commit
from .credit import Credit
from .discount import Discount
from .override import Override
from ..._models import BaseModel
from .pro_service import ProService
from .scheduled_charge import ScheduledCharge
from .base_usage_filter import BaseUsageFilter

__all__ = [
    "ContractWithoutAmendments",
    "Transition",
    "UsageStatementSchedule",
    "HierarchyConfiguration",
    "HierarchyConfigurationParentHierarchyConfiguration",
    "HierarchyConfigurationParentHierarchyConfigurationChild",
    "HierarchyConfigurationChildHierarchyConfiguration",
    "HierarchyConfigurationChildHierarchyConfigurationParent",
    "PrepaidBalanceThresholdConfiguration",
    "PrepaidBalanceThresholdConfigurationCommit",
    "PrepaidBalanceThresholdConfigurationCommitSpecifier",
    "PrepaidBalanceThresholdConfigurationPaymentGateConfig",
    "PrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "PrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig",
    "RecurringCommit",
    "RecurringCommitAccessAmount",
    "RecurringCommitCommitDuration",
    "RecurringCommitProduct",
    "RecurringCommitContract",
    "RecurringCommitHierarchyConfiguration",
    "RecurringCommitHierarchyConfigurationChildAccess",
    "RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "RecurringCommitInvoiceAmount",
    "RecurringCommitSpecifier",
    "RecurringCommitSubscriptionConfig",
    "RecurringCommitSubscriptionConfigApplySeatIncreaseConfig",
    "RecurringCredit",
    "RecurringCreditAccessAmount",
    "RecurringCreditCommitDuration",
    "RecurringCreditProduct",
    "RecurringCreditContract",
    "RecurringCreditHierarchyConfiguration",
    "RecurringCreditHierarchyConfigurationChildAccess",
    "RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "RecurringCreditSpecifier",
    "RecurringCreditSubscriptionConfig",
    "RecurringCreditSubscriptionConfigApplySeatIncreaseConfig",
    "ResellerRoyalty",
    "SpendThresholdConfiguration",
    "SpendThresholdConfigurationCommit",
    "SpendThresholdConfigurationPaymentGateConfig",
    "SpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "SpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "UsageFilter",
    "UsageFilterUpdate",
]


class Transition(BaseModel):
    from_contract_id: str

    to_contract_id: str

    type: Literal["SUPERSEDE", "RENEWAL"]


class UsageStatementSchedule(BaseModel):
    billing_anchor_date: datetime
    """Contract usage statements follow a selected cadence based on this date."""

    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]


class HierarchyConfigurationParentHierarchyConfigurationChild(BaseModel):
    contract_id: str

    customer_id: str


class HierarchyConfigurationParentHierarchyConfiguration(BaseModel):
    children: List[HierarchyConfigurationParentHierarchyConfigurationChild]
    """List of contracts that belong to this parent."""


class HierarchyConfigurationChildHierarchyConfigurationParent(BaseModel):
    contract_id: str

    customer_id: str


class HierarchyConfigurationChildHierarchyConfiguration(BaseModel):
    parent: HierarchyConfigurationChildHierarchyConfigurationParent
    """The single parent contract/customer for this child."""


HierarchyConfiguration: TypeAlias = Union[
    HierarchyConfigurationParentHierarchyConfiguration, HierarchyConfigurationChildHierarchyConfiguration
]


class PrepaidBalanceThresholdConfigurationCommitSpecifier(BaseModel):
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


class PrepaidBalanceThresholdConfigurationCommit(BaseModel):
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

    specifiers: Optional[List[PrepaidBalanceThresholdConfigurationCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """


class PrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class PrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class PrepaidBalanceThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[PrepaidBalanceThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig] = (
        None
    )
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[PrepaidBalanceThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gate type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class PrepaidBalanceThresholdConfiguration(BaseModel):
    commit: PrepaidBalanceThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: PrepaidBalanceThresholdConfigurationPaymentGateConfig

    recharge_to_amount: float
    """Specify the amount the balance should be recharged to."""

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's prepaid balance lowers to this amount, a threshold
    charge will be initiated.
    """

    custom_credit_type_id: Optional[str] = None
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """


class RecurringCommitAccessAmount(BaseModel):
    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class RecurringCommitCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class RecurringCommitProduct(BaseModel):
    id: str

    name: str


class RecurringCommitContract(BaseModel):
    id: str


class RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


RecurringCommitHierarchyConfigurationChildAccess: TypeAlias = Union[
    RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    RecurringCommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class RecurringCommitHierarchyConfiguration(BaseModel):
    child_access: RecurringCommitHierarchyConfigurationChildAccess


class RecurringCommitInvoiceAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class RecurringCommitSpecifier(BaseModel):
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


class RecurringCommitSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class RecurringCommitSubscriptionConfig(BaseModel):
    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: RecurringCommitSubscriptionConfigApplySeatIncreaseConfig

    subscription_id: str


class RecurringCommit(BaseModel):
    id: str

    access_amount: RecurringCommitAccessAmount
    """The amount of commit to grant."""

    commit_duration: RecurringCommitCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: RecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[RecurringCommitContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[RecurringCommitHierarchyConfiguration] = None
    """Optional configuration for recurring commit/credit hierarchy access control"""

    invoice_amount: Optional[RecurringCommitInvoiceAmount] = None
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

    specifiers: Optional[List[RecurringCommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[RecurringCommitSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class RecurringCreditAccessAmount(BaseModel):
    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class RecurringCreditCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class RecurringCreditProduct(BaseModel):
    id: str

    name: str


class RecurringCreditContract(BaseModel):
    id: str


class RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


RecurringCreditHierarchyConfigurationChildAccess: TypeAlias = Union[
    RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    RecurringCreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class RecurringCreditHierarchyConfiguration(BaseModel):
    child_access: RecurringCreditHierarchyConfigurationChildAccess


class RecurringCreditSpecifier(BaseModel):
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


class RecurringCreditSubscriptionConfigApplySeatIncreaseConfig(BaseModel):
    is_prorated: bool
    """Indicates whether a mid-period seat increase should be prorated."""


class RecurringCreditSubscriptionConfig(BaseModel):
    allocation: Literal["INDIVIDUAL", "POOLED"]

    apply_seat_increase_config: RecurringCreditSubscriptionConfigApplySeatIncreaseConfig

    subscription_id: str


class RecurringCredit(BaseModel):
    id: str

    access_amount: RecurringCreditAccessAmount
    """The amount of commit to grant."""

    commit_duration: RecurringCreditCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: RecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[RecurringCreditContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[RecurringCreditHierarchyConfiguration] = None
    """Optional configuration for recurring commit/credit hierarchy access control"""

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

    specifiers: Optional[List[RecurringCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[RecurringCreditSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class ResellerRoyalty(BaseModel):
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


class SpendThresholdConfigurationCommit(BaseModel):
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


class SpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig(BaseModel):
    tax_amount: float
    """Amount of tax to be applied.

    This should be in the same currency and denomination as the commit's invoice
    schedule
    """

    tax_name: Optional[str] = None
    """Name of the tax to be applied.

    This may be used in an invoice line item description.
    """


class SpendThresholdConfigurationPaymentGateConfigStripeConfig(BaseModel):
    payment_type: Literal["INVOICE", "PAYMENT_INTENT"]
    """If left blank, will default to INVOICE"""

    invoice_metadata: Optional[Dict[str, str]] = None
    """Metadata to be added to the Stripe invoice.

    Only applicable if using INVOICE as your payment type.
    """


class SpendThresholdConfigurationPaymentGateConfig(BaseModel):
    payment_gate_type: Literal["NONE", "STRIPE", "EXTERNAL"]
    """Gate access to the commit balance based on successful collection of payment.

    Select STRIPE for Metronome to facilitate payment via Stripe. Select EXTERNAL to
    facilitate payment using your own payment integration. Select NONE if you do not
    wish to payment gate the commit balance.
    """

    precalculated_tax_config: Optional[SpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig] = None
    """Only applicable if using PRECALCULATED as your tax type."""

    stripe_config: Optional[SpendThresholdConfigurationPaymentGateConfigStripeConfig] = None
    """Only applicable if using STRIPE as your payment gate type."""

    tax_type: Optional[Literal["NONE", "STRIPE", "ANROK", "PRECALCULATED"]] = None
    """Stripe tax is only supported for Stripe payment gateway.

    Select NONE if you do not wish Metronome to calculate tax on your behalf.
    Leaving this field blank will default to NONE.
    """


class SpendThresholdConfiguration(BaseModel):
    commit: SpendThresholdConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: SpendThresholdConfigurationPaymentGateConfig

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """


class UsageFilterUpdate(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: datetime


class UsageFilter(BaseModel):
    current: Optional[BaseUsageFilter] = None

    initial: BaseUsageFilter

    updates: List[UsageFilterUpdate]


class ContractWithoutAmendments(BaseModel):
    commits: List[Commit]

    created_at: datetime

    created_by: str

    overrides: List[Override]

    scheduled_charges: List[ScheduledCharge]

    starting_at: datetime

    transitions: List[Transition]

    usage_statement_schedule: UsageStatementSchedule

    credits: Optional[List[Credit]] = None

    discounts: Optional[List[Discount]] = None
    """This field's availability is dependent on your client's configuration."""

    ending_before: Optional[datetime] = None

    hierarchy_configuration: Optional[HierarchyConfiguration] = None
    """
    Either a **parent** configuration with a list of children or a **child**
    configuration with a single parent.
    """

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfiguration] = None

    professional_services: Optional[List[ProService]] = None
    """This field's availability is dependent on your client's configuration."""

    rate_card_id: Optional[str] = None

    recurring_commits: Optional[List[RecurringCommit]] = None

    recurring_credits: Optional[List[RecurringCredit]] = None

    reseller_royalties: Optional[List[ResellerRoyalty]] = None
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

    spend_threshold_configuration: Optional[SpendThresholdConfiguration] = None

    total_contract_value: Optional[float] = None
    """This field's availability is dependent on your client's configuration."""

    usage_filter: Optional[UsageFilter] = None
