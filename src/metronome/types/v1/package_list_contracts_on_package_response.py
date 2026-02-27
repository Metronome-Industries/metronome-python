# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["PackageListContractsOnPackageResponse"]


class PackageListContractsOnPackageResponse(BaseModel):
    contract_id: str

    customer_id: str

    starting_at: datetime

    archived_at: Optional[datetime] = None

    ending_before: Optional[datetime] = None
