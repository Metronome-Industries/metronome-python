# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "DashboardGetEmbeddableURLParams",
    "BmGroupKeyDisplayNameOverrides",
    "BmGroupKeyValuesDisplayNameOverrides",
    "BmGroupKeyValuesDisplayNameOverridesValueDisplayName",
    "ColorOverride",
    "DashboardOption",
]


class DashboardGetEmbeddableURLParams(TypedDict, total=False):
    customer_id: Required[str]

    dashboard: Required[Literal["invoices", "usage", "credits"]]
    """The type of dashboard to retrieve."""

    bm_group_key_display_name_overrides: BmGroupKeyDisplayNameOverrides

    bm_group_key_values_display_name_overrides: BmGroupKeyValuesDisplayNameOverrides

    color_overrides: Iterable[ColorOverride]
    """Optional list of colors to override"""

    dashboard_options: Iterable[DashboardOption]
    """Optional dashboard specific options"""


class BmGroupKeyDisplayNameOverrides(TypedDict, total=False):
    display_name: str
    """The new display name for the group key. e.g. "Tenant ID" """

    group_key_name: str
    """The current name of the group key. e.g. "tenant_id" """


class BmGroupKeyValuesDisplayNameOverridesValueDisplayName(TypedDict, total=False):
    display_name: str
    """The new display name for the group key value. e.g. "EU-Cluster-A" """

    group_key_value: str
    """The actual value of the group key. e.g. "123-xyz-abc" """


class BmGroupKeyValuesDisplayNameOverrides(TypedDict, total=False):
    group_key_name: str
    """The actual value of the group key.

    e.g. "123-xyz-abc". If group key is not used, it is the BM's name.
    """

    value_display_name: BmGroupKeyValuesDisplayNameOverridesValueDisplayName
    """
    An object containing the group key value and the new display name for the group
    key value.
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
    ]
    """The color to override"""

    value: str
    """Hex value representation of the color"""


class DashboardOption(TypedDict, total=False):
    key: Required[str]
    """The option key name"""

    value: Required[str]
    """The option value"""
