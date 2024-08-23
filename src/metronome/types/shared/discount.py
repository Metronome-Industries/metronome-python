# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .schedule_point_in_time import SchedulePointInTime

__all__ = ["Discount", "Product"]


class Product(BaseModel):
    id: str

    name: str


class Discount(BaseModel):
    id: str

    product: Product

    schedule: SchedulePointInTime

    name: Optional[str] = None

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""
