# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, Dict

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PlanListResponse"]

class PlanListResponse(BaseModel):
    id: str

    description: str

    name: str

    custom_fields: Optional[Dict[str, str]] = None