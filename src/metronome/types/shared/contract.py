# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .commit import Commit
from .credit import Credit
from .discount import Discount
from .override import Override
from ..._models import BaseModel
from .pro_service import ProService
from .subscription import Subscription
from .scheduled_charge import ScheduledCharge
from .contract_without_amendments import ContractWithoutAmendments
from .spend_threshold_configuration import SpendThresholdConfiguration
from .prepaid_balance_threshold_configuration import PrepaidBalanceThresholdConfiguration

__all__ = [
    "Contract",
    "Amendment",
    "AmendmentResellerRoyalty",
    "CustomerBillingProviderConfiguration",
    "CustomerBillingProviderConfigurationUnbillableInvoicesConfiguration",
    "SpendTracker",
    "SpendTrackerApplicableSpendSpecifier",
    "SpendTrackerAccumulatedSpend",
]


class AmendmentResellerRoyalty(BaseModel):
    reseller_type: Literal["AWS", "AWS_PRO_SERVICE", "GCP", "GCP_PRO_SERVICE"]

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


class Amendment(BaseModel):
    id: str

    commits: List[Commit]

    created_at: datetime

    created_by: str

    overrides: List[Override]

    scheduled_charges: List[ScheduledCharge]

    starting_at: datetime

    credits: Optional[List[Credit]] = None

    discounts: Optional[List[Discount]] = None
    """This field's availability is dependent on your client's configuration."""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    professional_services: Optional[List[ProService]] = None
    """This field's availability is dependent on your client's configuration."""

    reseller_royalties: Optional[List[AmendmentResellerRoyalty]] = None
    """This field's availability is dependent on your client's configuration."""

    salesforce_opportunity_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""


class CustomerBillingProviderConfigurationUnbillableInvoicesConfiguration(BaseModel):
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


class CustomerBillingProviderConfiguration(BaseModel):
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
        List[CustomerBillingProviderConfigurationUnbillableInvoicesConfiguration]
    ] = None
    """Rules that stop matching invoices from being sent to the billing provider.

    Only supported for Stripe billing provider configurations. When omitted, every
    invoice is sent to the billing provider.
    """


class SpendTrackerApplicableSpendSpecifier(BaseModel):
    sources: List[Literal["THRESHOLD_RECHARGE", "MANUAL"]]

    spend_type: Literal["COMMIT_PURCHASE"]

    discounted: Optional[Literal["ANY", "DISCOUNTED_ONLY", "UNDISCOUNTED_ONLY"]] = None


class SpendTrackerAccumulatedSpend(BaseModel):
    amount: float

    period_ending_before: datetime

    period_starting_at: datetime


class SpendTracker(BaseModel):
    alias: str
    """Human-readable identifier, unique per contract."""

    applicable_spend_specifiers: List[SpendTrackerApplicableSpendSpecifier]

    credit_type_id: str

    reset_frequency: Literal["BILLING_PERIOD"]

    accumulated_spend: Optional[SpendTrackerAccumulatedSpend] = None


class Contract(BaseModel):
    id: str

    amendments: List[Amendment]

    current: ContractWithoutAmendments

    customer_id: str

    initial: ContractWithoutAmendments

    archived_at: Optional[datetime] = None
    """RFC 3339 timestamp indicating when the contract was archived.

    If not returned, the contract is not archived.
    """

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    customer_billing_provider_configuration: Optional[CustomerBillingProviderConfiguration] = None

    package_id: Optional[str] = None
    """ID of the package this contract was created from, if applicable."""

    prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfiguration] = None

    scheduled_charges_on_usage_invoices: Optional[Literal["ALL"]] = None
    """
    Determines which scheduled and commit charges to consolidate onto the Contract's
    usage invoice. The charge's `timestamp` must match the usage invoice's
    `ending_before` date for consolidation to occur. This field cannot be modified
    after a Contract has been created. If this field is omitted, charges will appear
    on a separate invoice from usage charges.
    """

    spend_threshold_configuration: Optional[SpendThresholdConfiguration] = None

    spend_trackers: Optional[List[SpendTracker]] = None
    """Spend trackers attached to this contract."""

    subscriptions: Optional[List[Subscription]] = None
    """List of subscriptions on the contract."""

    uniqueness_key: Optional[str] = None
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """
