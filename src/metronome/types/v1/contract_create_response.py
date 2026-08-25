# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.commit import Commit
from ..shared.credit import Credit
from ..shared.override import Override
from ..shared.subscription import Subscription
from ..shared.commit_specifier import CommitSpecifier
from ..shared.scheduled_charge import ScheduledCharge
from ..shared.hierarchy_configuration import HierarchyConfiguration
from ..shared.spend_threshold_configuration import SpendThresholdConfiguration
from ..shared.commit_hierarchy_configuration import CommitHierarchyConfiguration
from ..shared.recurring_commit_subscription_config import RecurringCommitSubscriptionConfig
from ..shared.prepaid_balance_threshold_configuration import PrepaidBalanceThresholdConfiguration

__all__ = [
    "ContractCreateResponse",
    "Data",
    "DataContract",
    "DataContractTransition",
    "DataContractUsageFilter",
    "DataContractUsageStatementSchedule",
    "DataContractCustomerBillingProviderConfiguration",
    "DataContractCustomerBillingProviderConfigurationUnbillableInvoicesConfiguration",
    "DataContractHasMore",
    "DataContractRecurringCommit",
    "DataContractRecurringCommitAccessAmount",
    "DataContractRecurringCommitCommitDuration",
    "DataContractRecurringCommitProduct",
    "DataContractRecurringCommitContract",
    "DataContractRecurringCommitInvoiceAmount",
    "DataContractRecurringCommitProrationRounding",
    "DataContractRecurringCommitProrationRoundingAccess",
    "DataContractRecurringCommitProrationRoundingInvoice",
    "DataContractRecurringCredit",
    "DataContractRecurringCreditAccessAmount",
    "DataContractRecurringCreditCommitDuration",
    "DataContractRecurringCreditProduct",
    "DataContractRecurringCreditContract",
    "DataContractRecurringCreditProrationRounding",
    "DataContractRecurringCreditProrationRoundingAccess",
]


class DataContractTransition(BaseModel):
    from_contract_id: str

    to_contract_id: str

    type: Literal["RENEWAL"]


class DataContractUsageFilter(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: datetime

    ending_before: Optional[datetime] = None


class DataContractUsageStatementSchedule(BaseModel):
    billing_anchor_date: datetime
    """Contract usage statements follow a selected cadence based on this date."""

    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]


class DataContractCustomerBillingProviderConfigurationUnbillableInvoicesConfiguration(BaseModel):
    """
    An individual rule that, when evaluated to true, indicates that any invoices for this billing provider will not be sent to its associated destination for the associated contract. Rules only apply to the specified `invoice_type` (or all invoices if omitted) and `fiat_credit_type_id` (or all invoices if omitted). Rule precedence is evaluated from more specific to less specific. This method will fail with a 400 if multiple rules with the same specificity are included.
    """

    invoice_type: Literal["usage", "scheduled"]
    """The type of invoice this rule applies to."""

    fiat_credit_type_id: Optional[str] = None
    """Restricts the rule to invoices in this fiat currency.

    Omit for a catch-all rule that applies to every currency of the `invoice_type`.
    Required when `max_amount` is set.
    """

    max_amount: Optional[float] = None
    """A positive decimal, in the units of `fiat_credit_type_id`.

    Only invoices whose total is at or below this amount are suppressed; a higher
    total is still sent to the billing provider. When omitted, every matching
    invoice is suppressed regardless of amount.
    """


class DataContractCustomerBillingProviderConfiguration(BaseModel):
    id: str
    """
    ID of this configuration; can be provided as the
    billing_provider_configuration_id when creating a contract.
    """

    archived_at: Optional[datetime] = None

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
    """The billing provider set for this configuration."""

    configuration: Dict[str, object]
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider.
    """

    customer_id: str

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]
    """The method to use for delivering invoices to this customer."""

    delivery_method_configuration: Dict[str, object]
    """Configuration for the delivery method.

    The structure of this object is specific to the delivery method.
    """

    delivery_method_id: str
    """ID of the delivery method to use for this customer."""

    unbillable_invoices_configuration: Optional[
        List[DataContractCustomerBillingProviderConfigurationUnbillableInvoicesConfiguration]
    ] = None
    """Rules that stop matching invoices from being sent to the billing provider.

    Only supported for Stripe billing provider configurations. When omitted, every
    invoice is sent to the billing provider.
    """


class DataContractHasMore(BaseModel):
    """Indicates whether there are more items than the limit for this endpoint.

    Use the respective list endpoints to get the full lists.
    """

    commits: bool
    """Whether there are more commits on this contract than the limit for this
    endpoint.

    Use the /contracts/customerCommits/list endpoint to get the full list of
    commits.
    """

    credits: bool
    """Whether there are more credits on this contract than the limit for this
    endpoint.

    Use the /contracts/customerCredits/list endpoint to get the full list of
    credits.
    """


class DataContractRecurringCommitAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataContractRecurringCommitCommitDuration(BaseModel):
    """The amount of time the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataContractRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataContractRecurringCommitContract(BaseModel):
    id: str


class DataContractRecurringCommitInvoiceAmount(BaseModel):
    """The amount the customer should be billed for the commit. Not required."""

    credit_type_id: str

    quantity: float

    unit_price: float


class DataContractRecurringCommitProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit. For USD, this
    means rounding to the nearest dollar).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataContractRecurringCommitProrationRoundingInvoice(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit. For USD, this
    means rounding to the nearest dollar).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataContractRecurringCommitProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring commit amounts."""

    access: Optional[DataContractRecurringCommitProrationRoundingAccess] = None

    invoice: Optional[DataContractRecurringCommitProrationRoundingInvoice] = None


class DataContractRecurringCommit(BaseModel):
    id: str

    access_amount: DataContractRecurringCommitAccessAmount
    """The amount of commit to grant."""

    anchor_date: datetime
    """The date this recurring commit's billing periods are anchored to."""

    commit_duration: DataContractRecurringCommitCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataContractRecurringCommitProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataContractRecurringCommitContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for recurring commit/credit hierarchy access control"""

    invoice_amount: Optional[DataContractRecurringCommitInvoiceAmount] = None
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

    proration_rounding: Optional[DataContractRecurringCommitProrationRounding] = None
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


class DataContractRecurringCreditAccessAmount(BaseModel):
    """The amount of commit to grant."""

    credit_type_id: str

    unit_price: float

    quantity: Optional[float] = None


class DataContractRecurringCreditCommitDuration(BaseModel):
    """The amount of time the created commits will be valid for"""

    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataContractRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataContractRecurringCreditContract(BaseModel):
    id: str


class DataContractRecurringCreditProrationRoundingAccess(BaseModel):
    decimal_places: float
    """Number of decimal places to round to.

    Applied directly to the stored monetary representation. Negative values round to
    powers of 10 (e.g., -2 rounds to nearest 100 in the stored unit. For USD, this
    means rounding to the nearest dollar).
    """

    rounding_method: Literal["HALF_UP", "FLOOR", "CEILING"]


class DataContractRecurringCreditProrationRounding(BaseModel):
    """Rounding configuration for prorated recurring credit amounts."""

    access: Optional[DataContractRecurringCreditProrationRoundingAccess] = None


class DataContractRecurringCredit(BaseModel):
    id: str

    access_amount: DataContractRecurringCreditAccessAmount
    """The amount of commit to grant."""

    anchor_date: datetime
    """The date this recurring commit's billing periods are anchored to."""

    commit_duration: DataContractRecurringCreditCommitDuration
    """The amount of time the created commits will be valid for"""

    priority: float
    """Will be passed down to the individual commits"""

    product: DataContractRecurringCreditProduct

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]
    """Whether the created commits will use the commit rate or list rate"""

    starting_at: datetime
    """Determines the start time for the first commit"""

    applicable_product_ids: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    applicable_product_tags: Optional[List[str]] = None
    """Will be passed down to the individual commits"""

    contract: Optional[DataContractRecurringCreditContract] = None

    description: Optional[str] = None
    """Will be passed down to the individual commits"""

    ending_before: Optional[datetime] = None
    """Determines when the contract will stop creating recurring commits. Optional"""

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
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

    proration_rounding: Optional[DataContractRecurringCreditProrationRounding] = None
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


class DataContract(BaseModel):
    """The created contract."""

    id: str

    commits: List[Commit]

    created_at: datetime

    created_by: str

    customer_id: str

    overrides: List[Override]

    scheduled_charges: List[ScheduledCharge]

    starting_at: datetime

    transitions: List[DataContractTransition]

    usage_filter: List[DataContractUsageFilter]

    usage_statement_schedule: DataContractUsageStatementSchedule

    credits: Optional[List[Credit]] = None

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    customer_billing_provider_configuration: Optional[DataContractCustomerBillingProviderConfiguration] = None

    ending_before: Optional[datetime] = None

    has_more: Optional[DataContractHasMore] = None
    """Indicates whether there are more items than the limit for this endpoint.

    Use the respective list endpoints to get the full lists.
    """

    hierarchy_configuration: Optional[HierarchyConfiguration] = None
    """
    Either a **parent** configuration with a list of children or a **child**
    configuration with a single parent.
    """

    multiplier_override_prioritization: Optional[Literal["LOWEST_MULTIPLIER", "EXPLICIT"]] = None
    """
    Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
    prices automatically. EXPLICIT prioritization requires specifying priorities for
    each multiplier; the one with the lowest priority value will be prioritized
    first.
    """

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    package_id: Optional[str] = None
    """ID of the package this contract was created from, if applicable."""

    prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfiguration] = None

    rate_card_id: Optional[str] = None

    recurring_commits: Optional[List[DataContractRecurringCommit]] = None

    recurring_credits: Optional[List[DataContractRecurringCredit]] = None

    scheduled_charges_on_usage_invoices: Optional[Literal["ALL"]] = None
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    spend_threshold_configuration: Optional[SpendThresholdConfiguration] = None

    subscriptions: Optional[List[Subscription]] = None
    """List of subscriptions on the contract."""

    uniqueness_key: Optional[str] = None
    """Optional uniqueness key to prevent duplicate contract creations."""


class Data(BaseModel):
    id: str

    contract: Optional[DataContract] = None
    """The created contract."""


class ContractCreateResponse(BaseModel):
    data: Data
