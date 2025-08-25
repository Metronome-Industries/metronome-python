# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomFieldSetValuesParams"]


class CustomFieldSetValuesParams(TypedDict, total=False):
    custom_fields: Required[Dict[str, str]]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""

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
