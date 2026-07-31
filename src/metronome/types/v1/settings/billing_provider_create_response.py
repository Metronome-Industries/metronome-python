# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["BillingProviderCreateResponse", "Data"]


class Data(BaseModel):
    delivery_method_id: str


class BillingProviderCreateResponse(BaseModel):
    data: Data
