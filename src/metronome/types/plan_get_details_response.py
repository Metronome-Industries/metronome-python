# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from .plan_detail import PlanDetail

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PlanGetDetailsResponse"]

class PlanGetDetailsResponse(BaseModel):
    data: PlanDetail