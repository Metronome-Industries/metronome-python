# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel
from ..shared.rate import Rate

__all__ = ["RateCardRetrieveRateScheduleResponse", "Data"]


class Data(BaseModel):
    entitled: bool

    product_id: str

    product_name: str

    product_tags: List[str]

    rate: Rate

    starting_at: datetime

    ending_before: Optional[datetime] = None

    pricing_group_values: Optional[Dict[str, str]] = None


class RateCardRetrieveRateScheduleResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
