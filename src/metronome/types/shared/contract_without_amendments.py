# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

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
    "RecurringCommit",
    "RecurringCommitAccessAmount",
    "RecurringCommitCommitDuration",
    "RecurringCommitProduct",
    "RecurringCommitContract",
    "RecurringCommitInvoiceAmount",
    "RecurringCredit",
    "RecurringCreditAccessAmount",
    "RecurringCreditCommitDuration",
    "RecurringCreditProduct",
    "RecurringCreditContract",
    "ResellerRoyalty",
    "ThresholdBillingConfiguration",
    "ThresholdBillingConfigurationCommit",
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

    frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL"]


class RecurringCommitAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class RecurringCommitCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class RecurringCommitProduct(BaseModel):
    id: str

    name: str


class RecurringCommitContract(BaseModel):
    id: str


class RecurringCommitInvoiceAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


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

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    start_date rather than the usage invoice dates.
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """


class RecurringCreditAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class RecurringCreditCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class RecurringCreditProduct(BaseModel):
    id: str

    name: str


class RecurringCreditContract(BaseModel):
    id: str


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

    name: Optional[str] = None
    """Displayed on invoices. Will be passed through to the individual commits"""

    netsuite_sales_order_id: Optional[str] = None
    """Will be passed down to the individual commits"""

    proration: Optional[Literal["NONE", "FIRST", "LAST", "FIRST_AND_LAST"]] = None
    """Determines whether the first and last commit will be prorated.

    If not provided, the default is FIRST_AND_LAST (i.e. prorate both the first and
    last commits).
    """

    recurrence_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL"]] = None
    """The frequency at which the recurring commits will be created.

    If not provided: - The commits will be created on the usage invoice frequency.
    If provided: - The period defined in the duration will correspond to this
    frequency. - Commits will be created aligned with the recurring commit's
    start_date rather than the usage invoice dates.
    """

    rollover_fraction: Optional[float] = None
    """Will be passed down to the individual commits.

    This controls how much of an individual unexpired commit will roll over upon
    contract transition. Must be between 0 and 1.
    """


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


class ThresholdBillingConfigurationCommit(BaseModel):
    product_id: str

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


class ThresholdBillingConfiguration(BaseModel):
    commit: ThresholdBillingConfigurationCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state
    """

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

    name: Optional[str] = None

    net_payment_terms_days: Optional[float] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

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

    threshold_billing_configuration: Optional[ThresholdBillingConfiguration] = None

    total_contract_value: Optional[float] = None
    """This field's availability is dependent on your client's configuration."""

    usage_filter: Optional[UsageFilter] = None
