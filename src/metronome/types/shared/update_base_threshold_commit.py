# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UpdateBaseThresholdCommit"]


class UpdateBaseThresholdCommit(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None
    """Specify the name of the line item for the threshold charge.

    If left blank, it will default to the commit product name.
    """

    product_id: Optional[str] = None
    """
    The commit product that will be used to generate the line item for commit
    payment.
    """
