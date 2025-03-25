# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

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
    "DataAddCredit",
    "DataAddCreditProduct",
    "DataAddOverride",
    "DataAddOverrideOverrideSpecifier",
    "DataAddOverrideOverrideTier",
    "DataAddOverrideOverwriteRate",
    "DataAddOverrideProduct",
    "DataAddRecurringCommit",
    "DataAddRecurringCommitAccessAmount",
    "DataAddRecurringCommitCommitDuration",
    "DataAddRecurringCommitProduct",
    "DataAddRecurringCommitContract",
    "DataAddRecurringCommitInvoiceAmount",
    "DataAddRecurringCredit",
    "DataAddRecurringCreditAccessAmount",
    "DataAddRecurringCreditCommitDuration",
    "DataAddRecurringCreditProduct",
    "DataAddRecurringCreditContract",
    "DataAddResellerRoyalty",
    "DataAddScheduledCharge",
    "DataAddScheduledChargeProduct",
    "DataAddUsageFilter",
    "DataUpdateCommit",
    "DataUpdateCommitAccessSchedule",
    "DataUpdateCommitAccessScheduleAddScheduleItem",
    "DataUpdateCommitAccessScheduleRemoveScheduleItem",
    "DataUpdateCommitAccessScheduleUpdateScheduleItem",
    "DataUpdateCommitInvoiceSchedule",
    "DataUpdateCommitInvoiceScheduleAddScheduleItem",
    "DataUpdateCommitInvoiceScheduleRemoveScheduleItem",
    "DataUpdateCommitInvoiceScheduleUpdateScheduleItem",
    "DataUpdateCredit",
    "DataUpdateCreditAccessSchedule",
    "DataUpdateCreditAccessScheduleAddScheduleItem",
    "DataUpdateCreditAccessScheduleRemoveScheduleItem",
    "DataUpdateCreditAccessScheduleUpdateScheduleItem",
    "DataUpdateDiscount",
    "DataUpdateDiscountSchedule",
    "DataUpdateDiscountScheduleRecurringSchedule",
    "DataUpdateDiscountScheduleScheduleItem",
    "DataUpdateRefundInvoice",
    "DataUpdateScheduledCharge",
    "DataUpdateScheduledChargeInvoiceSchedule",
    "DataUpdateScheduledChargeInvoiceScheduleAddScheduleItem",
    "DataUpdateScheduledChargeInvoiceScheduleRemoveScheduleItem",
    "DataUpdateScheduledChargeInvoiceScheduleUpdateScheduleItem",
]


class DataAddCommitProduct(BaseModel):
    id: str

    name: str


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


class DataAddCreditProduct(BaseModel):
    id: str

    name: str


class DataAddCredit(BaseModel):
    id: str

    product: DataAddCreditProduct

    type: Literal["CREDIT"]

    access_schedule: Optional[ScheduleDuration] = None
    """The schedule that the customer will gain access to the credits."""

    applicable_product_ids: Optional[List[str]] = None

    applicable_product_tags: Optional[List[str]] = None

    description: Optional[str] = None

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


class DataAddOverrideOverrideSpecifier(BaseModel):
    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL"]] = None

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


class DataAddRecurringCommitAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataAddRecurringCommitCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataAddRecurringCommitProduct(BaseModel):
    id: str

    name: str


class DataAddRecurringCommitContract(BaseModel):
    id: str


class DataAddRecurringCommitInvoiceAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


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


class DataAddRecurringCreditAccessAmount(BaseModel):
    credit_type_id: str

    quantity: float

    unit_price: float


class DataAddRecurringCreditCommitDuration(BaseModel):
    value: float

    unit: Optional[Literal["PERIODS"]] = None


class DataAddRecurringCreditProduct(BaseModel):
    id: str

    name: str


class DataAddRecurringCreditContract(BaseModel):
    id: str


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


class DataUpdateCommit(BaseModel):
    id: str

    access_schedule: Optional[DataUpdateCommitAccessSchedule] = None

    applicable_product_ids: Optional[List[str]] = None
    """Which products the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the commit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    commit applies to all products.
    """

    invoice_schedule: Optional[DataUpdateCommitInvoiceSchedule] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    product_id: Optional[str] = None

    rollover_fraction: Optional[float] = None


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


class DataUpdateCredit(BaseModel):
    id: str

    access_schedule: Optional[DataUpdateCreditAccessSchedule] = None

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None

    rollover_fraction: Optional[float] = None


class DataUpdateDiscountScheduleRecurringSchedule(BaseModel):
    amount_distribution: Literal["DIVIDED", "DIVIDED_ROUNDED", "EACH"]

    ending_before: datetime
    """RFC 3339 timestamp (exclusive)."""

    frequency: Literal["MONTHLY", "QUARTERLY", "SEMI_ANNUAL", "ANNUAL"]

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
    """Defaults to USD if not passed. Only USD is supported at this time."""

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


class Data(BaseModel):
    id: str

    add_commits: Optional[List[DataAddCommit]] = None

    add_credits: Optional[List[DataAddCredit]] = None

    add_discounts: Optional[List[Discount]] = None

    add_overrides: Optional[List[DataAddOverride]] = None

    add_pro_services: Optional[List[ProService]] = None

    add_recurring_commits: Optional[List[DataAddRecurringCommit]] = None

    add_recurring_credits: Optional[List[DataAddRecurringCredit]] = None

    add_reseller_royalties: Optional[List[DataAddResellerRoyalty]] = None

    add_scheduled_charges: Optional[List[DataAddScheduledCharge]] = None

    add_usage_filters: Optional[List[DataAddUsageFilter]] = None

    timestamp: Optional[datetime] = None

    update_commits: Optional[List[DataUpdateCommit]] = None

    update_contract_end_date: Optional[datetime] = None

    update_credits: Optional[List[DataUpdateCredit]] = None

    update_discounts: Optional[List[DataUpdateDiscount]] = None

    update_refund_invoices: Optional[List[DataUpdateRefundInvoice]] = None

    update_scheduled_charges: Optional[List[DataUpdateScheduledCharge]] = None


class ContractGetEditHistoryResponse(BaseModel):
    data: List[Data]
