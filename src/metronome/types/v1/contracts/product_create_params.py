# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProductCreateParams", "QuantityConversion", "QuantityRounding"]


class ProductCreateParams(TypedDict, total=False):
    name: Required[str]
    """displayed on invoices"""

    type: Required[Literal["FIXED", "USAGE", "COMPOSITE", "SUBSCRIPTION", "PROFESSIONAL_SERVICE", "PRO_SERVICE"]]

    billable_metric_id: str
    """Required for USAGE products"""

    composite_product_ids: List[str]
    """Required for COMPOSITE products"""

    composite_tags: List[str]
    """Required for COMPOSITE products"""

    exclude_free_usage: bool
    """Beta feature only available for composite products.

    If true, products with $0 will not be included when computing composite usage.
    Defaults to false
    """

    is_refundable: bool
    """This field's availability is dependent on your client's configuration.

    Defaults to true.
    """

    netsuite_internal_item_id: str
    """This field's availability is dependent on your client's configuration."""

    netsuite_overage_item_id: str
    """This field's availability is dependent on your client's configuration."""

    presentation_group_key: List[str]
    """For USAGE products only.

    Groups usage line items on invoices. The superset of values in the pricing group
    key and presentation group key must be set as one compound group key on the
    billable metric.
    """

    pricing_group_key: List[str]
    """For USAGE products only.

    If set, pricing for this product will be determined for each pricing_group_key
    value, as opposed to the product as a whole. The superset of values in the
    pricing group key and presentation group key must be set as one compound group
    key on the billable metric.
    """

    quantity_conversion: Optional[QuantityConversion]
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be converted using
    the provided conversion factor and operation. For example, if the operation is
    "multiply" and the conversion factor is 100, then the quantity will be
    multiplied by 100. This can be used in cases where data is sent in one unit and
    priced in another. For example, data could be sent in MB and priced in GB. In
    this case, the conversion factor would be 1024 and the operation would be
    "divide".
    """

    quantity_rounding: Optional[QuantityRounding]
    """Optional.

    Only valid for USAGE products. If provided, the quantity will be rounded using
    the provided rounding method and decimal places. For example, if the method is
    "round up" and the decimal places is 0, then the quantity will be rounded up to
    the nearest integer.
    """

    tags: List[str]


class QuantityConversion(TypedDict, total=False):
    conversion_factor: Required[float]
    """The factor to multiply or divide the quantity by."""

    operation: Required[Literal["MULTIPLY", "DIVIDE"]]
    """The operation to perform on the quantity"""

    name: str
    """Optional name for this conversion."""


class QuantityRounding(TypedDict, total=False):
    decimal_places: Required[float]

    rounding_method: Required[Literal["ROUND_UP", "ROUND_DOWN", "ROUND_HALF_UP"]]
