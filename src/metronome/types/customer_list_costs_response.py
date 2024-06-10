# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CustomerListCostsResponse", "Data", "DataCreditTypes", "DataCreditTypesLineItemBreakdown"]


class DataCreditTypesLineItemBreakdown(BaseModel):
    cost: float

    name: str

    group_key: Optional[str] = None

    group_value: Optional[str] = None


class DataCreditTypes(BaseModel):
    cost: Optional[float] = None

    line_item_breakdown: Optional[List[DataCreditTypesLineItemBreakdown]] = None

    name: Optional[str] = None


class Data(BaseModel):
    credit_types: Dict[str, DataCreditTypes]

    end_timestamp: datetime

    start_timestamp: datetime


class CustomerListCostsResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
