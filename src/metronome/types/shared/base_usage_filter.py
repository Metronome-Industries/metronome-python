# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from datetime import datetime

from typing_extensions import Literal

from pydantic import Field as FieldInfo

__all__ = ["BaseUsageFilter"]

class BaseUsageFilter(BaseModel):
    group_key: str

    group_values: List[str]

    starting_at: Optional[datetime] = None