# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from datetime import datetime

from typing import Optional, List, Dict

from .quantity_conversion import QuantityConversion

from .quantity_rounding import QuantityRounding

from .product_list_item_state import ProductListItemState

from typing_extensions import Literal

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ProductRetrieveResponse", "Data", "DataUpdate"]

class DataUpdate(BaseModel):
    created_at: datetime

    created_by: str

    billable_metric_id: Optional[str] = None

    composite_product_ids: Optional[List[str]] = None

    composite_tags: Optional[List[str]] = None

    exclude_free_usage: Optional[bool] = None

    is_refundable: Optional[bool] = None

    name: Optional[str] = None

    netsuite_internal_item_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    netsuite_overage_item_id: Optional[str] = None
    """This field's availability is dependent on your client's configuration."""

    presentation_group_key: Optional[List[str]] = None
    """For USAGE products only.

    Groups usage line items on invoices. The superset of values in the pricing group
    key and presentation group key must be set as one compound group key on the
    billable metric.
    """

    pricing_group_key: Optional[List[str]] = None
    """For USAGE products only.

    If set, pricing for this product will be determined for each pricing_group_key
    value, as opposed to the product as a whole. The superset of values in the
    pricing group key and presentation group key must be set as one compound group
    key on the billable metric.
    """

    quantity_conversion: Optional[QuantityConversion] = None
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be converted using
    the provided conversion factor and operation. For example, if the operation is
    "multiply" and the conversion factor is 100, then the quantity will be
    multiplied by 100. This can be used in cases where data is sent in one unit and
    priced in another. For example, data could be sent in MB and priced in GB. In
    this case, the conversion factor would be 1024 and the operation would be
    "divide".
    """

    quantity_rounding: Optional[QuantityRounding] = None
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be rounded using
    the provided rounding method and decimal places. For example, if the method is
    "round up" and the decimal places is 0, then the quantity will be rounded up to
    the nearest integer.
    """

    starting_at: Optional[datetime] = None

    tags: Optional[List[str]] = None

class Data(BaseModel):
    id: str

    current: ProductListItemState

    initial: ProductListItemState

    type: Literal["USAGE", "SUBSCRIPTION", "COMPOSITE", "FIXED", "PRO_SERVICE"]

    updates: List[DataUpdate]

    archived_at: Optional[datetime] = None

    custom_fields: Optional[Dict[str, str]] = None

class ProductRetrieveResponse(BaseModel):
    data: Data