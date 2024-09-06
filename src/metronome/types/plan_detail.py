# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .shared.credit_type import CreditType

__all__ = ["PlanDetail", "CreditGrant", "Minimum", "OverageRate"]


class CreditGrant(BaseModel):
    amount_granted: float

    amount_granted_credit_type: CreditType

    amount_paid: float

    amount_paid_credit_type: CreditType

    effective_duration: float

    name: str

    priority: str

    send_invoice: bool

    reason: Optional[str] = None

    recurrence_duration: Optional[float] = None

    recurrence_interval: Optional[float] = None


class Minimum(BaseModel):
    credit_type: CreditType

    name: str

    start_period: float
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    value: float


class OverageRate(BaseModel):
    credit_type: CreditType

    fiat_credit_type: CreditType

    start_period: float
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    to_fiat_conversion_factor: float


class PlanDetail(BaseModel):
    id: str

    custom_fields: Dict[str, str]

    name: str

    credit_grants: Optional[List[CreditGrant]] = None

    description: Optional[str] = None

    minimums: Optional[List[Minimum]] = None

    overage_rates: Optional[List[OverageRate]] = None
