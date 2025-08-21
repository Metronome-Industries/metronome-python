# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .tier import Tier
from .discount import Discount
from ..._models import BaseModel
from .pro_service import ProService
from .credit_type_data import CreditTypeData
from .scheduled_charge import ScheduledCharge
from .schedule_duration import ScheduleDuration
from .schedule_point_in_time import SchedulePointInTime

__all__ = [
    "ContractV2",
    "Commit",
    "CommitProduct",
    "CommitContract",
    "CommitHierarchyConfiguration",
    "CommitHierarchyConfigurationChildAccess",
    "CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "CommitInvoiceContract",
    "CommitLedger",
    "CommitLedgerPrepaidCommitSegmentStartLedgerEntry",
    "CommitLedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry",
    "CommitLedgerPrepaidCommitRolloverLedgerEntry",
    "CommitLedgerPrepaidCommitExpirationLedgerEntry",
    "CommitLedgerPrepaidCommitCanceledLedgerEntry",
    "CommitLedgerPrepaidCommitCreditedLedgerEntry",
    "CommitLedgerPrepaidCommitSeatBasedAdjustmentLedgerEntry",
    "CommitLedgerPostpaidCommitInitialBalanceLedgerEntry",
    "CommitLedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry",
    "CommitLedgerPostpaidCommitRolloverLedgerEntry",
    "CommitLedgerPostpaidCommitTrueupLedgerEntry",
    "CommitLedgerPrepaidCommitManualLedgerEntry",
    "CommitLedgerPostpaidCommitManualLedgerEntry",
    "CommitLedgerPostpaidCommitExpirationLedgerEntry",
    "CommitRolledOverFrom",
    "CommitSpecifier",
    "Override",
    "OverrideOverrideSpecifier",
    "OverrideOverrideTier",
    "OverrideOverwriteRate",
    "OverrideProduct",
    "Transition",
    "UsageFilter",
    "UsageStatementSchedule",
    "Credit",
    "CreditProduct",
    "CreditContract",
    "CreditHierarchyConfiguration",
    "CreditHierarchyConfigurationChildAccess",
    "CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll",
    "CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone",
    "CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs",
    "CreditLedger",
    "CreditLedgerCreditSegmentStartLedgerEntry",
    "CreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry",
    "CreditLedgerCreditExpirationLedgerEntry",
    "CreditLedgerCreditCanceledLedgerEntry",
    "CreditLedgerCreditCreditedLedgerEntry",
    "CreditLedgerCreditManualLedgerEntry",
    "CreditLedgerCreditSeatBasedAdjustmentLedgerEntry",
    "CreditSpecifier",
    "CustomerBillingProviderConfiguration",
    "HasMore",
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
    "ResellerRoyaltySegment",
    "SpendThresholdConfiguration",
    "SpendThresholdConfigurationCommit",
    "SpendThresholdConfigurationPaymentGateConfig",
    "SpendThresholdConfigurationPaymentGateConfigPrecalculatedTaxConfig",
    "SpendThresholdConfigurationPaymentGateConfigStripeConfig",
    "Subscription",
    "SubscriptionProration",
    "SubscriptionQuantitySchedule",
    "SubscriptionSubscriptionRate",
    "SubscriptionSubscriptionRateProduct",
]


class CommitProduct(BaseModel):
    id: str

    name: str


class CommitContract(BaseModel):
    id: str


class CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


CommitHierarchyConfigurationChildAccess: TypeAlias = Union[
    CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    CommitHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class CommitHierarchyConfiguration(BaseModel):
    child_access: CommitHierarchyConfigurationChildAccess


class CommitInvoiceContract(BaseModel):
    id: str


class CommitLedgerPrepaidCommitSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEGMENT_START"]


class CommitLedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class CommitLedgerPrepaidCommitRolloverLedgerEntry(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_ROLLOVER"]


class CommitLedgerPrepaidCommitExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_EXPIRATION"]


class CommitLedgerPrepaidCommitCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CANCELED"]

    contract_id: Optional[str] = None


class CommitLedgerPrepaidCommitCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_CREDITED"]

    contract_id: Optional[str] = None


class CommitLedgerPrepaidCommitSeatBasedAdjustmentLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_SEAT_BASED_ADJUSTMENT"]


class CommitLedgerPostpaidCommitInitialBalanceLedgerEntry(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_INITIAL_BALANCE"]


class CommitLedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class CommitLedgerPostpaidCommitRolloverLedgerEntry(BaseModel):
    amount: float

    new_contract_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_ROLLOVER"]


class CommitLedgerPostpaidCommitTrueupLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_TRUEUP"]

    contract_id: Optional[str] = None


class CommitLedgerPrepaidCommitManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["PREPAID_COMMIT_MANUAL"]


class CommitLedgerPostpaidCommitManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_MANUAL"]


class CommitLedgerPostpaidCommitExpirationLedgerEntry(BaseModel):
    amount: float

    timestamp: datetime

    type: Literal["POSTPAID_COMMIT_EXPIRATION"]


CommitLedger: TypeAlias = Union[
    CommitLedgerPrepaidCommitSegmentStartLedgerEntry,
    CommitLedgerPrepaidCommitAutomatedInvoiceDeductionLedgerEntry,
    CommitLedgerPrepaidCommitRolloverLedgerEntry,
    CommitLedgerPrepaidCommitExpirationLedgerEntry,
    CommitLedgerPrepaidCommitCanceledLedgerEntry,
    CommitLedgerPrepaidCommitCreditedLedgerEntry,
    CommitLedgerPrepaidCommitSeatBasedAdjustmentLedgerEntry,
    CommitLedgerPostpaidCommitInitialBalanceLedgerEntry,
    CommitLedgerPostpaidCommitAutomatedInvoiceDeductionLedgerEntry,
    CommitLedgerPostpaidCommitRolloverLedgerEntry,
    CommitLedgerPostpaidCommitTrueupLedgerEntry,
    CommitLedgerPrepaidCommitManualLedgerEntry,
    CommitLedgerPostpaidCommitManualLedgerEntry,
    CommitLedgerPostpaidCommitExpirationLedgerEntry,
]


class CommitRolledOverFrom(BaseModel):
    commit_id: str

    contract_id: str


class CommitSpecifier(BaseModel):
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


class Commit(BaseModel):
    id: str

    product: CommitProduct

    type: Literal["PREPAID", "POSTPAID"]

    access_schedule: Optional[ScheduleDuration] = None
    """
    The schedule that the customer will gain access to the credits purposed with
    this commit.
    """

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    archived_at: Optional[datetime] = None

    balance: Optional[float] = None
    """The current balance of the credit or commit.

    This balance reflects the amount of credit or commit that the customer has
    access to use at this moment - thus, expired and upcoming credit or commit
    segments contribute 0 to the balance. The balance will match the sum of all
    ledger entries with the exception of the case where the sum of negative manual
    ledger entries exceeds the positive amount remaining on the credit or commit -
    in that case, the balance will be 0. All manual ledger entries associated with
    active credit or commit segments are included in the balance, including
    future-dated manual ledger entries.
    """

    contract: Optional[CommitContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    hierarchy_configuration: Optional[CommitHierarchyConfiguration] = None
    """Optional configuration for commit hierarchy access control"""

    invoice_contract: Optional[CommitInvoiceContract] = None
    """The contract that this commit will be billed on."""

    invoice_schedule: Optional[SchedulePointInTime] = None
    """The schedule that the customer will be invoiced for this commit."""

    ledger: Optional[List[CommitLedger]] = None
    """A list of ordered events that impact the balance of a commit.

    For example, an invoice deduction or a rollover.
    """

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    priority: Optional[float] = None
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    rolled_over_from: Optional[CommitRolledOverFrom] = None

    rollover_fraction: Optional[float] = None

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    specifiers: Optional[List[CommitSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class OverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_ids: Optional[List[str]] = None

    presentation_group_values: Optional[Dict[str, Optional[str]]] = None

    pricing_group_values: Optional[Dict[str, str]] = None

    product_id: Optional[str] = None

    product_tags: Optional[List[str]] = None

    recurring_commit_ids: Optional[List[str]] = None

    recurring_credit_ids: Optional[List[str]] = None


class OverrideOverrideTier(BaseModel):
    multiplier: float

    size: Optional[float] = None


class OverrideOverwriteRate(BaseModel):
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


class OverrideProduct(BaseModel):
    id: str

    name: str


class Override(BaseModel):
    id: str

    starting_at: datetime

    applicable_product_tags: Optional[List[str]] = None

    ending_before: Optional[datetime] = None

    entitled: Optional[bool] = None

    is_commit_specific: Optional[bool] = None

    multiplier: Optional[float] = None

    override_specifiers: Optional[List[OverrideOverrideSpecifier]] = None

    override_tiers: Optional[List[OverrideOverrideTier]] = None

    overwrite_rate: Optional[OverrideOverwriteRate] = None

    priority: Optional[float] = None

    product: Optional[OverrideProduct] = None

    target: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None

    type: Optional[Literal["OVERWRITE", "MULTIPLIER", "TIERED"]] = None


class Transition(BaseModel):
    from_contract_id: str

    to_contract_id: str

    type: Literal["SUPERSEDE", "RENEWAL"]


class UsageFilter(BaseModel):
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


class UsageStatementSchedule(BaseModel):
    billing_anchor_date: datetime
    """Contract usage statements follow a selected cadence based on this date."""

    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]


class CreditProduct(BaseModel):
    id: str

    name: str


class CreditContract(BaseModel):
    id: str


class CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]


class CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]


class CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]


CreditHierarchyConfigurationChildAccess: TypeAlias = Union[
    CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessAll,
    CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessNone,
    CreditHierarchyConfigurationChildAccessCommitHierarchyChildAccessContractIDs,
]


class CreditHierarchyConfiguration(BaseModel):
    child_access: CreditHierarchyConfigurationChildAccess


class CreditLedgerCreditSegmentStartLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEGMENT_START"]


class CreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_AUTOMATED_INVOICE_DEDUCTION"]

    contract_id: Optional[str] = None


class CreditLedgerCreditExpirationLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_EXPIRATION"]


class CreditLedgerCreditCanceledLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CANCELED"]

    contract_id: Optional[str] = None


class CreditLedgerCreditCreditedLedgerEntry(BaseModel):
    amount: float

    invoice_id: str

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_CREDITED"]

    contract_id: Optional[str] = None


class CreditLedgerCreditManualLedgerEntry(BaseModel):
    amount: float

    reason: str

    timestamp: datetime

    type: Literal["CREDIT_MANUAL"]


class CreditLedgerCreditSeatBasedAdjustmentLedgerEntry(BaseModel):
    amount: float

    segment_id: str

    timestamp: datetime

    type: Literal["CREDIT_SEAT_BASED_ADJUSTMENT"]


CreditLedger: TypeAlias = Union[
    CreditLedgerCreditSegmentStartLedgerEntry,
    CreditLedgerCreditAutomatedInvoiceDeductionLedgerEntry,
    CreditLedgerCreditExpirationLedgerEntry,
    CreditLedgerCreditCanceledLedgerEntry,
    CreditLedgerCreditCreditedLedgerEntry,
    CreditLedgerCreditManualLedgerEntry,
    CreditLedgerCreditSeatBasedAdjustmentLedgerEntry,
]


class CreditSpecifier(BaseModel):
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


class Credit(BaseModel):
    id: str

    product: CreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[ScheduleDuration] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_contract_ids: Optional[List[str]] = None

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    balance: Optional[float] = None
    """The current balance of the credit or commit.

    This balance reflects the amount of credit or commit that the customer has
    access to use at this moment - thus, expired and upcoming credit or commit
    segments contribute 0 to the balance. The balance will match the sum of all
    ledger entries with the exception of the case where the sum of negative manual
    ledger entries exceeds the positive amount remaining on the credit or commit -
    in that case, the balance will be 0. All manual ledger entries associated with
    active credit or commit segments are included in the balance, including
    future-dated manual ledger entries.
    """

    contract: Optional[CreditContract] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    hierarchy_configuration: Optional[CreditHierarchyConfiguration] = None
    """Optional configuration for credit hierarchy access control"""

    ledger: Optional[List[CreditLedger]] = None
    """A list of ordered events that impact the balance of a credit.

    For example, an invoice deduction or an expiration.
    """

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

    specifiers: Optional[List[CreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """


class CustomerBillingProviderConfiguration(BaseModel):
    id: str
    """ID of Customer's billing provider configuration."""

    billing_provider: Literal[
        "aws_marketplace",
        "stripe",
        "netsuite",
        "custom",
        "azure_marketplace",
        "quickbooks_online",
        "workday",
        "gcp_marketplace",
    ]

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]


class HasMore(BaseModel):
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
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
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
    """Only applicable if using STRIPE as your payment gateway type."""

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

    Each time the contract's balance lowers to this amount, a threshold charge will
    be initiated.
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
    """Optional configuration for recurring credit hierarchy access control"""

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

    specifiers: Optional[List[RecurringCreditSpecifier]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown.
    """

    subscription_config: Optional[RecurringCreditSubscriptionConfig] = None
    """Attach a subscription to the recurring commit/credit."""


class ResellerRoyaltySegment(BaseModel):
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


class ResellerRoyalty(BaseModel):
    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

    segments: List[ResellerRoyaltySegment]


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
    """Only applicable if using STRIPE as your payment gateway type."""

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


class SubscriptionProration(BaseModel):
    invoice_behavior: Literal["BILL_IMMEDIATELY", "BILL_ON_NEXT_COLLECTION_DATE"]

    is_prorated: bool


class SubscriptionQuantitySchedule(BaseModel):
    quantity: float

    starting_at: datetime

    ending_before: Optional[datetime] = None


class SubscriptionSubscriptionRateProduct(BaseModel):
    id: str

    name: str


class SubscriptionSubscriptionRate(BaseModel):
    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]

    product: SubscriptionSubscriptionRateProduct


class Subscription(BaseModel):
    collection_schedule: Literal["ADVANCE", "ARREARS"]

    proration: SubscriptionProration

    quantity_schedule: List[SubscriptionQuantitySchedule]
    """List of quantity schedule items for the subscription.

    Only includes the current quantity and future quantity changes.
    """

    starting_at: datetime

    subscription_rate: SubscriptionSubscriptionRate

    id: Optional[str] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    ending_before: Optional[datetime] = None

    fiat_credit_type_id: Optional[str] = None

    name: Optional[str] = None


class ContractV2(BaseModel):
    id: str

    commits: List[Commit]

    created_at: datetime

    created_by: str

    customer_id: str

    overrides: List[Override]

    scheduled_charges: List[ScheduledCharge]

    starting_at: datetime

    transitions: List[Transition]

    usage_filter: List[UsageFilter]

    usage_statement_schedule: UsageStatementSchedule

    archived_at: Optional[datetime] = None

    credits: Optional[List[Credit]] = None

    custom_fields: Optional[Dict[str, str]] = None

    customer_billing_provider_configuration: Optional[CustomerBillingProviderConfiguration] = None
    """This field's availability is dependent on your client's configuration."""

    discounts: Optional[List[Discount]] = None
    """This field's availability is dependent on your client's configuration."""

    ending_before: Optional[datetime] = None

    has_more: Optional[HasMore] = None
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

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfiguration] = None

    priority: Optional[float] = None
    """Priority of the contract."""

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

    subscriptions: Optional[List[Subscription]] = None
    """List of subscriptions on the contract."""

    total_contract_value: Optional[float] = None

    uniqueness_key: Optional[str] = None
    """Optional uniqueness key to prevent duplicate contract creations."""
