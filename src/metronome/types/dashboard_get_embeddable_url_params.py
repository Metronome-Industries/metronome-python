# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DashboardGetEmbeddableURLParams", "ColorOverride", "DashboardOption"]


class DashboardGetEmbeddableURLParams(TypedDict, total=False):
    customer_id: Required[str]

    dashboard: Required[Literal["invoices", "usage", "credits"]]
    """The type of dashboard to retrieve."""

    color_overrides: Iterable[ColorOverride]
    """Optional list of colors to override"""

    dashboard_options: Iterable[DashboardOption]
    """Optional dashboard specific options"""


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
    ]
    """The color to override"""

    value: str
    """Hex value representation of the color"""


class DashboardOption(TypedDict, total=False):
    key: Required[str]
    """The option key name"""

    value: Required[str]
    """The option value"""
