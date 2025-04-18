# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["CustomFieldListKeysParams"]


class CustomFieldListKeysParams(TypedDict, total=False):
    next_page: str
    """Cursor that indicates where the next page of results should start."""

    entities: List[
        Literal[
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
    ]
    """Optional list of entity types to return keys for"""
