# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ...._models import BaseModel
from ...shared.rate import Rate

__all__ = ["RateAddResponse"]


class RateAddResponse(BaseModel):
    data: Rate
