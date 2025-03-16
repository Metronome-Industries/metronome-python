# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from .schedule_point_in_time import SchedulePointInTime

from typing import Optional, Dict

from typing_extensions import Literal

from pydantic import Field as FieldInfo

__all__ = ["ScheduledCharge", "Product"]

class Product(BaseModel):
    id: str

    name: str

class ScheduledCharge(BaseModel):
    id: str

    product: Product

    schedule: SchedulePointInTime

    custom_fields: Optional[Dict[str, str]] = None

    name: Optional[str] = None
    """displayed on invoices"""

    netsuite_sales_order_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""