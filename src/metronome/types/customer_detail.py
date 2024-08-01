# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomerDetail", "CustomerConfig", "CurrentBillableStatus"]


class CustomerConfig(BaseModel):
    salesforce_account_id: Optional[str] = None
    """The Salesforce account ID for the customer"""


class CurrentBillableStatus(BaseModel):
    value: Literal["billable", "unbillable"]

    effective_at: Optional[datetime] = None


class CustomerDetail(BaseModel):
    id: str
    """the Metronome ID of the customer"""

    custom_fields: Dict[str, str]

    customer_config: CustomerConfig

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

    current_billable_status: Optional[CurrentBillableStatus] = None
    """This field's availability is dependent on your client's configuration."""
