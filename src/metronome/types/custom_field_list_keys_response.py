# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomFieldListKeysResponse", "Data"]


class Data(BaseModel):
    enforce_uniqueness: bool

    entity: Literal[
        "alert",
        "billable_metric",
        "charge",
        "commit",
        "contract_credit",
        "contract_product",
        "contract",
        "credit_grant",
        "customer_plan",
        "customer",
        "invoice",
        "plan",
        "professional_service",
        "product",
        "rate_card",
        "scheduled_charge",
    ]

    key: str


class CustomFieldListKeysResponse(BaseModel):
    data: List[Data]

    next_page: Optional[str] = None
