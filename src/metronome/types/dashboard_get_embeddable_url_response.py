# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DashboardGetEmbeddableURLResponse", "Data"]

class Data(BaseModel):
    url: Optional[str] = None

class DashboardGetEmbeddableURLResponse(BaseModel):
    data: Data