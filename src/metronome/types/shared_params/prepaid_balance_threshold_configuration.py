# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr
from .payment_gate_config import PaymentGateConfig
from .base_threshold_commit import BaseThresholdCommit
from .commit_specifier_input import CommitSpecifierInput

__all__ = ["PrepaidBalanceThresholdConfiguration", "Commit"]


class Commit(BaseThresholdCommit, total=False):
    applicable_product_ids: SequenceNotStr[str]
    """Which products the threshold commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    applicable_product_tags: SequenceNotStr[str]
    """Which tags the threshold commit applies to.

    If applicable_product_ids, applicable_product_tags or specifiers are not
    provided, the commit applies to all products.
    """

    specifiers: Iterable[CommitSpecifierInput]
    """
    List of filters that determine what kind of customer usage draws down a commit
    or credit. A customer's usage needs to meet the condition of at least one of the
    specifiers to contribute to a commit's or credit's drawdown. This field cannot
    be used together with `applicable_product_ids` or `applicable_product_tags`.
    """


class PrepaidBalanceThresholdConfiguration(TypedDict, total=False):
    commit: Required[Commit]

    is_enabled: Required[bool]
    """
    When set to false, the contract will not be evaluated against the
    threshold_amount. Toggling to true will result an immediate evaluation,
    regardless of prior state.
    """

    payment_gate_config: Required[PaymentGateConfig]

    recharge_to_amount: Required[float]
    """Specify the amount the balance should be recharged to."""

    threshold_amount: Required[float]
    """Specify the threshold amount for the contract.

    Each time the contract's prepaid balance lowers to this amount, a threshold
    charge will be initiated.
    """

    custom_credit_type_id: str
    """
    If provided, the threshold, recharge-to amount, and the resulting threshold
    commit amount will be in terms of this credit type instead of the fiat currency.
    """
