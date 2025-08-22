# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._utils import PropertyInfo
from ....shared_params.tier import Tier
from ....shared_params.commit_rate import CommitRate

__all__ = ["RateAddParams"]


class RateAddParams(TypedDict, total=False):
    entitled: Required[bool]

    product_id: Required[str]
    """ID of the product to add a rate for"""

    rate_card_id: Required[str]
    """ID of the rate card to update"""

    rate_type: Required[Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"]]

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """inclusive effective date"""

    billing_frequency: Literal["MONTHLY", "QUARTERLY", "ANNUAL", "WEEKLY"]
    """Optional.

    Frequency to bill subscriptions with. Required for subscription type products
    with Flat rate.
    """

    commit_rate: CommitRate
    """A distinct rate on the rate card.

    You can choose to use this rate rather than list rate when consuming a credit or
    commit.
    """

    credit_type_id: str
    """
    The Metronome ID of the credit type to associate with price, defaults to USD
    (cents) if not passed. Used by all rate_types except type PERCENTAGE. PERCENTAGE
    rates use the credit type of associated rates.
    """

    custom_rate: Dict[str, object]
    """Only set for CUSTOM rate_type.

    This field is interpreted by custom rate processors.
    """

    ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """exclusive end date"""

    is_prorated: bool
    """Default proration configuration.

    Only valid for SUBSCRIPTION rate_type. Must be set to true.
    """

    price: float
    """Default price.

    For FLAT and SUBSCRIPTION rate_type, this must be >=0. For PERCENTAGE rate_type,
    this is a decimal fraction, e.g. use 0.1 for 10%; this must be >=0 and <=1.
    """

    pricing_group_values: Dict[str, str]
    """Optional.

    List of pricing group key value pairs which will be used to calculate the price.
    """

    quantity: float
    """Default quantity. For SUBSCRIPTION rate_type, this must be >=0."""

    tiers: Iterable[Tier]
    """Only set for TIERED rate_type."""

    use_list_prices: bool
    """Only set for PERCENTAGE rate_type.

    Defaults to false. If true, rate is computed using list prices rather than the
    standard rates for this product on the contract.
    """
