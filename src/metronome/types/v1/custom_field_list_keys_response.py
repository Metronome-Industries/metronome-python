# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CustomFieldListKeysResponse"]


class CustomFieldListKeysResponse(BaseModel):
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
        "discount",
        "invoice",
        "plan",
        "professional_service",
        "product",
        "rate_card",
        "scheduled_charge",
        "subscription",
    ]

    key: str
