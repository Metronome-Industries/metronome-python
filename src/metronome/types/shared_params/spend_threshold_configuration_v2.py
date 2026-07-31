# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .base_threshold_commit import BaseThresholdCommit
from .payment_gate_config_v2 import PaymentGateConfigV2

__all__ = ["SpendThresholdConfigurationV2", "DiscountConfiguration", "DiscountConfigurationCap"]


class DiscountConfigurationCap(TypedDict, total=False):
    """
    If provided, the discount stops applying once the spend tracker has accumulated this much spend in the billing period.
    """

    amount: Required[float]
    """Accumulated spend ceiling above which the discount stops applying."""

    spend_tracker_alias: Required[str]
    """Alias of the spend tracker this cap is measured against."""


class DiscountConfiguration(TypedDict, total=False):
    payment_fraction: Required[float]
    """
    The fraction of the original amount that the customer pays after applying the
    discount. For example, 0.85 means the customer pays 85% of the original amount
    (a 15% discount).
    """

    cap: DiscountConfigurationCap
    """
    If provided, the discount stops applying once the spend tracker has accumulated
    this much spend in the billing period.
    """


class SpendThresholdConfigurationV2(TypedDict, total=False):
    commit: Required[BaseThresholdCommit]

    is_enabled: Required[bool]
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: Required[PaymentGateConfigV2]

    threshold_amount: Required[float]
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """

    discount_configuration: DiscountConfiguration
