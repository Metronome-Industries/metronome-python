# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PlanListCustomersParams"]


class PlanListCustomersParams(TypedDict, total=False):
    plan_id: Required[str]

    limit: int
    """Max number of results that should be returned"""

    next_page: str
    """Cursor that indicates where the next page of results should start."""

    status: Literal["all", "active", "ended", "upcoming"]
    """Status of customers on a given plan. Defaults to `active`.

    - `all` - Return current, past, and upcoming customers of the plan.
    - `active` - Return current customers of the plan.
    - `ended` - Return past customers of the plan.
    - `upcoming` - Return upcoming customers of the plan.

    Multiple statuses can be OR'd together using commas, e.g. `active,ended`.
    **Note:** `ended,upcoming` combination is not yet supported.
    """
