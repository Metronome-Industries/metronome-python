# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .payment_gate_config_v2 import PaymentGateConfigV2
from .update_base_threshold_commit import UpdateBaseThresholdCommit

__all__ = ["SpendThresholdConfigurationV2"]


class SpendThresholdConfigurationV2(TypedDict, total=False):
    commit: Required[UpdateBaseThresholdCommit]

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
