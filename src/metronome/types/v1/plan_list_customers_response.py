# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "PlanListCustomersResponse",
    "CustomerDetails",
    "CustomerDetailsCustomerConfig",
    "CustomerDetailsCurrentBillableStatus",
    "PlanDetails",
]


class CustomerDetailsCustomerConfig(BaseModel):
    salesforce_account_id: Optional[str] = None
    """The Salesforce account ID for the customer"""


class CustomerDetailsCurrentBillableStatus(BaseModel):
    value: Literal["billable", "unbillable"]

    effective_at: Optional[datetime] = None


class CustomerDetails(BaseModel):
    id: str
    """the Metronome ID of the customer"""

    created_at: datetime
    """RFC 3339 timestamp indicating when the customer was created."""

    custom_fields: Dict[str, str]

    customer_config: CustomerDetailsCustomerConfig

    external_id: str
    """
    (deprecated, use ingest_aliases instead) the first ID (Metronome or ingest
    alias) that can be used in usage events
    """

    ingest_aliases: List[str]
    """
    aliases for this customer that can be used instead of the Metronome customer ID
    in usage events
    """

    name: str

    archived_at: Optional[datetime] = None
    """RFC 3339 timestamp indicating when the customer was archived.

    Null if the customer is active.
    """

    current_billable_status: Optional[CustomerDetailsCurrentBillableStatus] = None
    """This field's availability is dependent on your client's configuration."""


class PlanDetails(BaseModel):
    id: str

    custom_fields: Dict[str, str]

    customer_plan_id: str

    name: str

    starting_on: datetime
    """The start date of the plan"""

    ending_before: Optional[datetime] = None
    """The end date of the plan"""


class PlanListCustomersResponse(BaseModel):
    customer_details: CustomerDetails

    plan_details: PlanDetails
