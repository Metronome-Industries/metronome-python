# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .commit_specifier_input import CommitSpecifierInput
from .payment_gate_config_v2 import PaymentGateConfigV2
from .update_base_threshold_commit import UpdateBaseThresholdCommit

__all__ = ["PrepaidBalanceThresholdConfigurationV2", "Commit"]


class Commit(UpdateBaseThresholdCommit):
    applicable_product_ids: Optional[List[str]] = None
    """Which products the threshold commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: Optional[List[str]] = None
    """Which tags the threshold commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    specifiers: Optional[List[CommitSpecifierInput]] = None
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    Instead, to target usage by product or product tag, pass those values in the
    body of `specifiers`.
    """


class PrepaidBalanceThresholdConfigurationV2(BaseModel):
    commit: Commit

    is_enabled: bool
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: PaymentGateConfigV2

    recharge_to_amount: float
    """Specify the amount the balance should be recharged to."""

    threshold_amount: float
    """Specify the threshold amount for the contract.

    Each time the contract's balance lowers to this amount, a threshold charge will
    be initiated.
    """

    custom_credit_type_id: Optional[str] = None
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """
