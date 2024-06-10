# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuditLogListResponse", "Data", "DataActor"]


class DataActor(BaseModel):
    id: str

    name: str

    email: Optional[str] = None


class Data(BaseModel):
    id: str

    timestamp: datetime

    action: Optional[str] = None

    actor: Optional[DataActor] = None

    description: Optional[str] = None

    resource_id: Optional[str] = None

    resource_type: Optional[str] = None

    status: Optional[Literal["success", "failure", "pending"]] = None


class AuditLogListResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
    """The next_page parameter is always returned to support ongoing log retrieval.

    It enables continuous querying, even when some requests return no new data. Save
    the next_page token from each response and use it for future requests to ensure
    no logs are missed. This setup is ideal for regular updates via automated
    processes, like cron jobs, to fetch logs continuously as they become available.
    When you receive an empty data array, it indicates a temporary absence of new
    logs, but subsequent requests might return new data.
    """
