# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SystemListResponse", "Data", "DataPolicy"]


class DataPolicy(BaseModel):
    type: str
    """The type of lifecycle event (e.g., "contract.create", "contract.start")"""


class Data(BaseModel):
    policy: DataPolicy

    type: str
    """Indicates this is a system lifecycle event notification"""

    is_enabled: Optional[bool] = None
    """Whether or not webhook publishing for this lifecycle event is enabled"""


class SystemListResponse(BaseModel):
    data: List[Data]

    cursor: Optional[str] = None
