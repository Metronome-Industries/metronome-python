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

__all__ = ["Contract", "Amendment", "AmendmentResellerRoyalty", "CustomerBillingProviderConfiguration"]


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


class CustomerBillingProviderConfiguration(BaseModel):
    """The billing provider configuration associated with a contract."""

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

    delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"]

    id: Optional[str] = None

    configuration: Optional[Dict[str, object]] = None
    """Configuration for the billing provider.

    The structure of this object is specific to the billing provider.
    """


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
    """The billing provider configuration associated with a contract."""

    prepaid_balance_threshold_configuration: Optional[PrepaidBalanceThresholdConfiguration] = None

    priority: Optional[float] = None
    """Priority of the contract."""

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
    """Prevents the creation of duplicates.

    If a request to create a record is made with a previously used uniqueness key, a
    new record will not be created and the request will fail with a 409 error.
    """
