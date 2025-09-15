# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel
from ....shared.rate import Rate
from ....shared.commit_rate import CommitRate

__all__ = ["RateListResponse"]


class RateListResponse(BaseModel):
    entitled: bool

    product_custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

    product_id: str

    product_name: str

    product_tags: List[str]

    rate: Rate

    starting_at: datetime

    billing_frequency: Optional[Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]] = None

    commit_rate: Optional[CommitRate] = None
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or
    commit.
    """

    ending_before: Optional[datetime] = None

    pricing_group_values: Optional[Dict[str, str]] = None
