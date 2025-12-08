# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AlertRetrieveParams", "GroupValue", "SeatFilter"]


class AlertRetrieveParams(TypedDict, total=False):
    alert_id: Required[str]
    """The Metronome ID of the threshold notification"""

    customer_id: Required[str]
    """The Metronome ID of the customer"""

    group_values: Iterable[GroupValue]
    """Only present for `spend_threshold_reached` notifications.

    Retrieve the notification for a specific group key-value pair.
    """

    plans_or_contracts: Literal["PLANS", "CONTRACTS"]
    """
    When parallel threshold notifications are enabled during migration, this flag
    denotes whether to fetch notifications for plans or contracts.
    """

    seat_filter: SeatFilter
    """Only allowed for `low_remaining_seat_balance_reached` notifications.

    This filters alerts by the seat group key-value pair.
    """


class GroupValue(TypedDict, total=False):
    """
    Scopes threshold notification evaluation to a specific presentation group key on individual line items. Only present for spend notifications.
    """

    key: Required[str]

    value: Required[str]


class SeatFilter(TypedDict, total=False):
    """Only allowed for `low_remaining_seat_balance_reached` notifications.

    This filters alerts by the seat group key-value pair.
    """

    seat_group_key: Required[str]
    """The seat group key (e.g., "seat_id", "user_id")"""

    seat_group_value: Required[str]
    """The specific seat identifier to filter by"""
