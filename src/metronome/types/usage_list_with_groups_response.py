# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from datetime import datetime

from typing import Optional

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["UsageListWithGroupsResponse"]

class UsageListWithGroupsResponse(BaseModel):
    ending_before: datetime

    group_key: Optional[str] = None

    group_value: Optional[str] = None

    starting_on: datetime

    value: Optional[float] = None