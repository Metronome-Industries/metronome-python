# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from typing_extensions import Literal

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ServiceListResponse", "Service"]

class Service(BaseModel):
    ips: List[str]

    name: str

    usage: Literal["makes_connections_from", "accepts_connections_at"]

class ServiceListResponse(BaseModel):
    services: List[Service]