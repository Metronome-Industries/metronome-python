# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PlanAddParams", "OverageRateAdjustment", "PriceAdjustment", "TrialSpec", "TrialSpecSpendingCap"]


class PlanAddParams(TypedDict, total=False):
    customer_id: Required[str]

    plan_id: Required[str]

    starting_on: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """RFC 3339 timestamp for when the plan becomes active for this customer.

    Must be at 0:00 UTC (midnight).
    """

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp for when the plan ends (exclusive) for this customer.

    Must be at 0:00 UTC (midnight).
    """

    net_payment_terms_days: float
    """Number of days after issuance of invoice after which the invoice is due (e.g.

    Net 30).
    """

    overage_rate_adjustments: Iterable[OverageRateAdjustment]
    """
    An optional list of overage rates that override the rates of the original plan
    configuration. These new rates will apply to all pricing ramps.
    """

    price_adjustments: Iterable[PriceAdjustment]
    """A list of price adjustments can be applied on top of the pricing in the plans.

    See the
    [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
    for details.
    """

    trial_spec: TrialSpec
    """A custom trial can be set for the customer's plan.

    See the
    [trial configuration documentation](https://docs.metronome.com/provisioning/configure-trials/)
    for details.
    """


class OverageRateAdjustment(TypedDict, total=False):
    custom_credit_type_id: Required[str]

    fiat_currency_credit_type_id: Required[str]

    to_fiat_conversion_factor: Required[float]
    """The overage cost in fiat currency for each credit of the custom credit type."""


class PriceAdjustment(TypedDict, total=False):
    adjustment_type: Required[Literal["percentage", "fixed", "override", "quantity"]]

    charge_id: Required[str]

    start_period: Required[float]
    """Used in price ramps.

    Indicates how many billing periods pass before the charge applies.
    """

    quantity: float
    """the overridden quantity for a fixed charge"""

    tier: float
    """Used in pricing tiers. Indicates at what metric value the price applies."""

    value: float
    """The amount of change to a price.

    Percentage and fixed adjustments can be positive or negative. Percentage-based
    adjustments should be decimals, e.g. -0.05 for a 5% discount.
    """


class TrialSpecSpendingCap(TypedDict, total=False):
    amount: Required[float]
    """The credit amount in the given denomination based on the credit type, e.g.

    US cents.
    """

    credit_type_id: Required[str]
    """The credit type ID for the spending cap."""


class TrialSpec(TypedDict, total=False):
    """A custom trial can be set for the customer's plan.

    See the [trial configuration documentation](https://docs.metronome.com/provisioning/configure-trials/) for details.
    """

    length_in_days: Required[float]
    """Length of the trial period in days."""

    spending_cap: TrialSpecSpendingCap
