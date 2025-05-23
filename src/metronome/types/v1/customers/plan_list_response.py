# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PlanListResponse", "TrialInfo", "TrialInfoSpendingCap", "TrialInfoSpendingCapCreditType"]


class TrialInfoSpendingCapCreditType(BaseModel):
    id: str

    name: str


class TrialInfoSpendingCap(BaseModel):
    amount: float

    amount_remaining: float

    credit_type: TrialInfoSpendingCapCreditType


class TrialInfo(BaseModel):
    ending_before: datetime

    spending_caps: List[TrialInfoSpendingCap]


class PlanListResponse(BaseModel):
    id: str
    """the ID of the customer plan"""

    custom_fields: Dict[str, str]

    plan_description: str

    plan_id: str
    """the ID of the plan"""

    plan_name: str

    starting_on: datetime

    ending_before: Optional[datetime] = None

    net_payment_terms_days: Optional[float] = None

    trial_info: Optional[TrialInfo] = None
