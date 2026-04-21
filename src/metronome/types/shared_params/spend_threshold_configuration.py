# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .payment_gate_config import PaymentGateConfig
from .base_threshold_commit import BaseThresholdCommit

__all__ = ["SpendThresholdConfiguration", "DiscountConfiguration"]


class DiscountConfiguration(TypedDict, total=False):
    payment_fraction: Required[float]
    """
    The fraction of the original amount that the customer pays after applying the
    discount. For example, 0.85 means the customer pays 85% of the original amount
    (a 15% discount).
    """


class SpendThresholdConfiguration(TypedDict, total=False):
    commit: Required[BaseThresholdCommit]

    is_enabled: Required[bool]
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: Required[PaymentGateConfig]

    threshold_amount: Required[float]
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """

    discount_configuration: DiscountConfiguration
