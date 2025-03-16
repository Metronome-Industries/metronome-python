# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import Optional, List

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["NamedScheduleRetrieveResponse", "Data"]

class Data(BaseModel):
    starting_at: datetime

    value: object

    ending_before: Optional[datetime] = None

class NamedScheduleRetrieveResponse(BaseModel):
    data: List[Data]