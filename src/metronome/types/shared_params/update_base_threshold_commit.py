# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UpdateBaseThresholdCommit"]


class UpdateBaseThresholdCommit(TypedDict, total=False):
    description: str

    name: str
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """

    product_id: str
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """
