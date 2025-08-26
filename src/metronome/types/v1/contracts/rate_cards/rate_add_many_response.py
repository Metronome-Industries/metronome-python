# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

__all__ = ["RateAddManyResponse", "Data"]


class Data(BaseModel):
    id: str


class RateAddManyResponse(BaseModel):
    data: Data
    """The ID of the rate card to which the rates were added."""
