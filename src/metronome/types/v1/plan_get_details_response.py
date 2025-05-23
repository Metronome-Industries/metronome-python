# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel

__all__ = [
    "PlanGetDetailsResponse",
    "Data",
    "DataCreditGrant",
    "DataCreditGrantAmountGrantedCreditType",
    "DataCreditGrantAmountPaidCreditType",
    "DataMinimum",
    "DataMinimumCreditType",
    "DataOverageRate",
    "DataOverageRateCreditType",
    "DataOverageRateFiatCreditType",
]


class DataCreditGrantAmountGrantedCreditType(BaseModel):
    id: str

    name: str


class DataCreditGrantAmountPaidCreditType(BaseModel):
    id: str

    name: str


class DataCreditGrant(BaseModel):
    amount_granted: float

    amount_granted_credit_type: DataCreditGrantAmountGrantedCreditType

    amount_paid: float

    amount_paid_credit_type: DataCreditGrantAmountPaidCreditType

    effective_duration: float

    name: str

    priority: str

    send_invoice: bool

    reason: Optional[str] = None

    recurrence_duration: Optional[float] = None

    recurrence_interval: Optional[float] = None


class DataMinimumCreditType(BaseModel):
    id: str

    name: str


class DataMinimum(BaseModel):
    credit_type: DataMinimumCreditType

    name: str

    start_period: float
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    value: float


class DataOverageRateCreditType(BaseModel):
    id: str

    name: str


class DataOverageRateFiatCreditType(BaseModel):
    id: str

    name: str


class DataOverageRate(BaseModel):
    credit_type: DataOverageRateCreditType

    fiat_credit_type: DataOverageRateFiatCreditType

    start_period: float
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    to_fiat_conversion_factor: float


class Data(BaseModel):
    id: str

    custom_fields: Dict[str, str]

    name: str

    credit_grants: Optional[List[DataCreditGrant]] = None

    description: Optional[str] = None

    minimums: Optional[List[DataMinimum]] = None

    overage_rates: Optional[List[DataOverageRate]] = None


class PlanGetDetailsResponse(BaseModel):
    data: Data
