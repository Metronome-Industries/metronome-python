# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["UsageListWithGroupsResponse"]


class UsageListWithGroupsResponse(BaseModel):
    ending_before: datetime

    group_key: Optional[str] = None
    """Use `group` instead. The group key for single-key grouping."""

    group_value: Optional[str] = None
    """Use `group` instead. The group value for single-key grouping."""

    starting_on: datetime

    value: Optional[float] = None

    group: Optional[Dict[str, str]] = None
    """
    Map of group key to their value for this usage aggregate. For simple group keys,
    this should be a single key e.g. `{"region": "US-East"}` For compound group
    keys, this should contain the values of each group key that forms the compound
    e.g. `{"region": "US-East", "team": "engineering"}`
    """
