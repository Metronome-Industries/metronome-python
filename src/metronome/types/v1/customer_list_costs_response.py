# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["CustomerListCostsResponse", "CreditTypes", "CreditTypesLineItemBreakdown"]


class CreditTypesLineItemBreakdown(BaseModel):
    cost: float

    name: str

    group_key: Optional[str] = None

    group_value: Optional[str] = None


class CreditTypes(BaseModel):
    cost: Optional[float] = None

    line_item_breakdown: Optional[List[CreditTypesLineItemBreakdown]] = None

    name: Optional[str] = None


class CustomerListCostsResponse(BaseModel):
    credit_types: Dict[str, CreditTypes]

    end_timestamp: datetime

    start_timestamp: datetime
