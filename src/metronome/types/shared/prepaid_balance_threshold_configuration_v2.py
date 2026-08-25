# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .base_threshold_commit import BaseThresholdCommit
from .commit_specifier_input import CommitSpecifierInput
from .payment_gate_config_v2 import PaymentGateConfigV2

__all__ = [
    "PrepaidBalanceThresholdConfigurationV2",
    "Commit",
    "CommitDuration",
    "DiscountConfiguration",
    "DiscountConfigurationCap",
    "ThresholdBalanceSpecifier",
    "ThresholdBalanceSpecifierExclude",
    "ThresholdBalanceSpecifierExcludeCustomFieldFilter",
]


class CommitDuration(BaseModel):
    """
    The length of time the created commit will be valid, starting from the end of the invoice's service period. If not provided, defaults to one year.
    """

    unit: Literal["DAYS", "WEEKS", "MONTHS", "YEARS"]

    value: int


class Commit(BaseThresholdCommit):
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

    duration: Optional[CommitDuration] = None
    """
    The length of time the created commit will be valid, starting from the end of
    the invoice's service period. If not provided, defaults to one year.
    """

    rate_type: Optional[Literal["COMMIT_RATE", "LIST_RATE"]] = None
    """Whether the created commits will be charged at commit rate or list rate."""

    rollover_fraction: Optional[float] = None
    """Fraction of the created commit's unused balance that will roll over.

    Must be between 0 and 1.
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


class ThresholdBalanceSpecifierExcludeCustomFieldFilter(BaseModel):
    entity: Literal["Commit", "ContractCredit", "ContractCreditOrCommit"]

    key: str

    value: str


class ThresholdBalanceSpecifierExclude(BaseModel):
    custom_field_filters: List[ThresholdBalanceSpecifierExcludeCustomFieldFilter]


class ThresholdBalanceSpecifier(BaseModel):
    exclude: List[ThresholdBalanceSpecifierExclude]


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

    discount_configuration: Optional[DiscountConfiguration] = None

    threshold_balance_specifiers: Optional[List[ThresholdBalanceSpecifier]] = None
    """
    Determines which balances are excluded from remaining balance calculation for
    threshold billing.
    """
