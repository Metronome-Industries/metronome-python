# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BillableMetricUpdateParams"]


class BillableMetricUpdateParams(TypedDict, total=False):
    billable_metric_id: Required[str]

    name: Required[str]
    """The new name of the metric"""
