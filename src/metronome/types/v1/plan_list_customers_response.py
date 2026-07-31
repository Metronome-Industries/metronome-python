# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from .customer_detail import CustomerDetail

__all__ = ["PlanListCustomersResponse", "PlanDetails"]


class PlanDetails(BaseModel):
    id: str

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    customer_plan_id: str

    name: str

    starting_on: datetime
    """The start date of the plan"""

    ending_before: Optional[datetime] = None
    """The end date of the plan"""


class PlanListCustomersResponse(BaseModel):
    customer_details: CustomerDetail

    plan_details: PlanDetails
