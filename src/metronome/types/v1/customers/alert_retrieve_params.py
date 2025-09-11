# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertRetrieveParams", "GroupValue"]


class AlertRetrieveParams(TypedDict, total=False):
    alert_id: Required[str]
    """The Metronome ID of the alert"""

    customer_id: Required[str]
    """The Metronome ID of the customer"""

    group_values: Iterable[GroupValue]
    """Only present for `spend_threshold_reached` alerts.

    Retrieve the alert for a specific group key-value pair.
    """

    plans_or_contracts: Literal["PLANS", "CONTRACTS"]
    """
    When parallel alerts are enabled during migration, this flag denotes whether to
    fetch alerts for plans or contracts.
    """


class GroupValue(TypedDict, total=False):
    key: Required[str]

    value: Required[str]
