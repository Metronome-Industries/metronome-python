# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ContractRetrieveSubscriptionQuantityHistoryResponse", "Data", "DataHistory", "DataHistoryData"]


class DataHistoryData(BaseModel):
    quantity: float

    total: float

    unit_price: float


class DataHistory(BaseModel):
    data: List[DataHistoryData]

    starting_at: datetime


class Data(BaseModel):
    fiat_credit_type_id: Optional[str] = None

    history: Optional[List[DataHistory]] = None

    subscription_id: Optional[str] = None


class ContractRetrieveSubscriptionQuantityHistoryResponse(BaseModel):
    data: Data
