# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["UpdateBaseThresholdCommit"]


class UpdateBaseThresholdCommit(TypedDict, total=False):
    description: str

    name: str
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """

    priority: Optional[float]
    """The priority of the commit, used to determine drawdown order.

    Lower priority commits are consumed first. Defaults to 100 if not specified. On
    updates, set to null to clear a previously configured priority.
    """

    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """
