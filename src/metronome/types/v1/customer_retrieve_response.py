# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomerRetrieveResponse", "Data", "DataCustomerConfig", "DataCurrentBillableStatus"]


class DataCustomerConfig(BaseModel):
    salesforce_account_id: Optional[str] = None
    """The Salesforce account ID for the customer"""


class DataCurrentBillableStatus(BaseModel):
    value: Literal["billable", "unbillable"]

    effective_at: Optional[datetime] = None


class Data(BaseModel):
    id: str
    """the Metronome ID of the customer"""

    created_at: datetime
    """RFC 3339 timestamp indicating when the customer was created."""

    custom_fields: Dict[str, str]

    customer_config: DataCustomerConfig

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

    current_billable_status: Optional[DataCurrentBillableStatus] = None
    """This field's availability is dependent on your client's configuration."""


class CustomerRetrieveResponse(BaseModel):
    data: Data
