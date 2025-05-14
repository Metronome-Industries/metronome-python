# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomFieldDeleteValuesParams"]


class CustomFieldDeleteValuesParams(TypedDict, total=False):
    entity: Required[
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

    entity_id: Required[str]

    keys: Required[List[str]]
