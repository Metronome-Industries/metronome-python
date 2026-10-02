# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PricingUnitCreateParams"]


class PricingUnitCreateParams(TypedDict, total=False):
    name: Required[str]
    """The name of the custom pricing unit. This will appear on invoices."""
