# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from ....shared.id import ID

__all__ = ["RateAddManyResponse"]


class RateAddManyResponse(BaseModel):
    data: ID
    """The ID of the rate card to which the rates were added."""
