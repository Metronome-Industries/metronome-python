# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Dict

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["CustomFieldSetValuesParams"]

class CustomFieldSetValuesParams(TypedDict, total=False):
    custom_fields: Required[Dict[str, str]]

    entity: Required[Literal["alert", "billable_metric", "charge", "commit", "contract_credit", "contract_product", "contract", "credit_grant", "customer_plan", "customer", "discount", "invoice", "plan", "professional_service", "product", "rate_card", "scheduled_charge"]]

    entity_id: Required[str]