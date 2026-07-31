# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from ..shared.credit_type_data import CreditTypeData

__all__ = ["PlanDetail", "CreditGrant", "Minimum", "OverageRate"]


class CreditGrant(BaseModel):
    amount_granted: float

    amount_granted_credit_type: CreditTypeData

    amount_paid: float

    amount_paid_credit_type: CreditTypeData

    effective_duration: float

    name: str

    priority: str

    send_invoice: bool

    reason: Optional[str] = None

    recurrence_duration: Optional[float] = None

    recurrence_interval: Optional[float] = None


class Minimum(BaseModel):
    credit_type: CreditTypeData

    name: str

    start_period: float
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    value: float


class OverageRate(BaseModel):
    credit_type: CreditTypeData

    fiat_credit_type: CreditTypeData

    start_period: float
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    to_fiat_conversion_factor: float


class PlanDetail(BaseModel):
    id: str

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    name: str

    credit_grants: Optional[List[CreditGrant]] = None

    description: Optional[str] = None

    minimums: Optional[List[Minimum]] = None

    overage_rates: Optional[List[OverageRate]] = None
