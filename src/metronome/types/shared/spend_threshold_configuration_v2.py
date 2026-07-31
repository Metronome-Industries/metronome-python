# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .base_threshold_commit import BaseThresholdCommit
from .payment_gate_config_v2 import PaymentGateConfigV2

__all__ = ["SpendThresholdConfigurationV2", "DiscountConfiguration", "DiscountConfigurationCap"]


class DiscountConfigurationCap(BaseModel):
    """
    If provided, the discount stops applying once the spend tracker has accumulated this much spend in the billing period.
    """

    amount: float
    """Accumulated spend ceiling above which the discount stops applying."""

    spend_tracker_alias: str
    """Alias of the spend tracker this cap is measured against."""


class DiscountConfiguration(BaseModel):
    payment_fraction: float
    """
    The fraction of the original amount that the customer pays after applying the
    discount. For example, 0.85 means the customer pays 85% of the original amount
    (a 15% discount).
    """

    cap: Optional[DiscountConfigurationCap] = None
    """
    If provided, the discount stops applying once the spend tracker has accumulated
    this much spend in the billing period.
    """


class SpendThresholdConfigurationV2(BaseModel):
    commit: BaseThresholdCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: PaymentGateConfigV2

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """

    discount_configuration: Optional[DiscountConfiguration] = None
