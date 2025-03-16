# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from ..shared.id import ID

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RateCardUpdateResponse"]

class RateCardUpdateResponse(BaseModel):
    data: ID