# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from .._models import BaseModel
from .shared.rate import Rate

__all__ = ["ContractRetrieveRateScheduleResponse", "Data"]


class Data(BaseModel):
    entitled: bool

    list_rate: Rate

    product_custom_fields: Dict[str, str]

    product_id: str

    product_name: str

    product_tags: List[str]

    rate_card_id: str

    starting_at: datetime

    ending_before: Optional[datetime] = None

    override_rate: Optional[Rate] = None

    pricing_group_values: Optional[Dict[str, str]] = None


class ContractRetrieveRateScheduleResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
