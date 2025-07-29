# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DashboardGetEmbeddableURLParams", "BmGroupKeyOverride", "ColorOverride", "DashboardOption"]


class DashboardGetEmbeddableURLParams(TypedDict, total=False):
    customer_id: Required[str]

    dashboard: Required[Literal["invoices", "usage", "credits", "commits_and_credits"]]
    """The type of dashboard to retrieve."""

    bm_group_key_overrides: Iterable[BmGroupKeyOverride]
    """Optional list of billable metric group key overrides"""

    color_overrides: Iterable[ColorOverride]
    """Optional list of colors to override"""

    dashboard_options: Iterable[DashboardOption]
    """Optional dashboard specific options"""


class BmGroupKeyOverride(TypedDict, total=False):
    group_key_name: Required[str]
    """The name of the billable metric group key."""

    display_name: str
    """The display name for the billable metric group key"""

    value_display_names: Dict[str, object]
    """
    <key, value> pairs of the billable metric group key values and their display
    names. e.g. {"a": "Asia", "b": "Euro"}
    """


class ColorOverride(TypedDict, total=False):
    name: Literal[
        "Gray_dark",
        "Gray_medium",
        "Gray_light",
        "Gray_extralight",
        "White",
        "Primary_medium",
        "Primary_light",
        "UsageLine_0",
        "UsageLine_1",
        "UsageLine_2",
        "UsageLine_3",
        "UsageLine_4",
        "UsageLine_5",
        "UsageLine_6",
        "UsageLine_7",
        "UsageLine_8",
        "UsageLine_9",
        "Primary_green",
        "Primary_red",
        "Progress_bar",
        "Progress_bar_background",
    ]
    """The color to override"""

    value: str
    """Hex value representation of the color"""


class DashboardOption(TypedDict, total=False):
    key: Required[str]
    """The option key name"""

    value: Required[str]
    """The option value"""
