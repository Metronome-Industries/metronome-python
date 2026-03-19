# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .payment_gate_config import PaymentGateConfig
from .base_threshold_commit import BaseThresholdCommit

__all__ = ["SpendThresholdConfiguration", "DiscountConfiguration"]


class DiscountConfiguration(BaseModel):
    payment_fraction: float
    """
    The fraction of the original amount that the customer pays after applying the
    discount. For example, 0.85 means the customer pays 85% of the original amount
    (a 15% discount).
    """


class SpendThresholdConfiguration(BaseModel):
    commit: BaseThresholdCommit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: PaymentGateConfig

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's usage hits this amount, a threshold charge will be
    initiated.
    """

    discount_configuration: Optional[DiscountConfiguration] = None
