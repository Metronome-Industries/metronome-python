# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .customer_detail import CustomerDetail

__all__ = ["PlanListCustomersResponse", "Data", "DataPlanDetails"]


class DataPlanDetails(BaseModel):
    id: str

    custom_fields: Dict[str, str]

    customer_plan_id: str

    name: str

    starting_on: datetime
    """The start date of the plan"""

    ending_before: Optional[datetime] = None
    """The end date of the plan"""


class Data(BaseModel):
    customer_details: CustomerDetail

    plan_details: DataPlanDetails


class PlanListCustomersResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
