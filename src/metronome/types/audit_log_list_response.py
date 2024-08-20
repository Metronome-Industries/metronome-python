# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuditLogListResponse", "Actor"]


class Actor(BaseModel):
    id: str

    name: str

    email: Optional[str] = None


class AuditLogListResponse(BaseModel):
    id: str

    timestamp: datetime

    action: Optional[str] = None

    actor: Optional[Actor] = None

    description: Optional[str] = None

    resource_id: Optional[str] = None

    resource_type: Optional[str] = None

    status: Optional[Literal["success", "failure", "pending"]] = None
