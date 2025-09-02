# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from .quantity_rounding_param import QuantityRoundingParam
from .quantity_conversion_param import QuantityConversionParam

__all__ = ["ProductUpdateParams"]


class ProductUpdateParams(TypedDict, total=False):
    product_id: Required[str]
    """ID of the product to update"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp representing when the update should go into effect.

    It must be on an hour boundary (e.g. 1:00, not 1:30).
    """

    billable_metric_id: str
    """Available for USAGE products only.

    If not provided, defaults to product's current billable metric.
    """

    composite_product_ids: SequenceNotStr[str]
    """Available for COMPOSITE products only.

    If not provided, defaults to product's current composite_product_ids.
    """

    composite_tags: SequenceNotStr[str]
    """Available for COMPOSITE products only.

    If not provided, defaults to product's current composite_tags.
    """

    exclude_free_usage: bool
    """Beta feature only available for composite products.

    If true, products with $0 will not be included when computing composite usage.
    Defaults to false
    """

    is_refundable: bool
    """Defaults to product's current refundability status.

    This field's availability is dependent on your client's configuration.
    """

    name: str
    """displayed on invoices. If not provided, defaults to product's current name."""

    netsuite_internal_item_id: str
    """If not provided, defaults to product's current netsuite_internal_item_id.

    This field's availability is dependent on your client's configuration.
    """

    netsuite_overage_item_id: str
    """Available for USAGE and COMPOSITE products only.

    If not provided, defaults to product's current netsuite_overage_item_id. This
    field's availability is dependent on your client's configuration.
    """

    presentation_group_key: SequenceNotStr[str]
    """For USAGE products only.

    Groups usage line items on invoices. The superset of values in the pricing group
    key and presentation group key must be set as one compound group key on the
    billable metric.
    """

    pricing_group_key: SequenceNotStr[str]
    """For USAGE products only.

    If set, pricing for this product will be determined for each pricing_group_key
    value, as opposed to the product as a whole. The superset of values in the
    pricing group key and presentation group key must be set as one compound group
    key on the billable metric.
    """

    quantity_conversion: Optional[QuantityConversionParam]
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be converted using
    the provided conversion factor and operation. For example, if the operation is
    "multiply" and the conversion factor is 100, then the quantity will be
    multiplied by 100. This can be used in cases where data is sent in one unit and
    priced in another. For example, data could be sent in MB and priced in GB. In
    this case, the conversion factor would be 1024 and the operation would be
    "divide".
    """

    quantity_rounding: Optional[QuantityRoundingParam]
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be rounded using
    the provided rounding method and decimal places. For example, if the method is
    "round up" and the decimal places is 0, then the quantity will be rounded up to
    the nearest integer.
    """

    tags: SequenceNotStr[str]
    """If not provided, defaults to product's current tags"""
