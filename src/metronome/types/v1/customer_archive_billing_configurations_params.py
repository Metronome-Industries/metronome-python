# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CustomerArchiveBillingConfigurationsParams"]


class CustomerArchiveBillingConfigurationsParams(TypedDict, total=False):
    customer_billing_provider_configuration_ids: Required[SequenceNotStr[str]]
    """Array of billing provider configuration IDs to archive"""

    customer_id: Required[str]
    """The customer ID the billing provider configurations belong to"""
