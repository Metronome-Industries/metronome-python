# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .plan_detail import PlanDetail

__all__ = ["PlanGetDetailsResponse"]


class PlanGetDetailsResponse(BaseModel):
    data: PlanDetail
