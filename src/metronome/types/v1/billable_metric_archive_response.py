# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from ..shared.id import ID

__all__ = ["BillableMetricArchiveResponse"]


class BillableMetricArchiveResponse(BaseModel):
    data: ID
