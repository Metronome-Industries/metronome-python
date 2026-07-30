# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, Dict

__all__ = ["PlanListResponse"]

class PlanListResponse(BaseModel):
    id: str

    description: str

    name: str

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""