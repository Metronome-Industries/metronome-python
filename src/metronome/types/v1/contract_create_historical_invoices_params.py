# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "ContractCreateHistoricalInvoicesParams",
    "Invoice",
    "InvoiceUsageLineItem",
    "InvoiceUsageLineItemSubtotalsWithQuantity",
]


class ContractCreateHistoricalInvoicesParams(TypedDict, total=False):
    invoices: Required[Iterable[Invoice]]

    preview: Required[bool]


class InvoiceUsageLineItemSubtotalsWithQuantity(TypedDict, total=False):
    exclusive_end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    inclusive_start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    quantity: Required[float]


class InvoiceUsageLineItem(TypedDict, total=False):
    exclusive_end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    inclusive_start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    product_id: Required[str]

    presentation_group_values: Dict[str, str]

    pricing_group_values: Dict[str, str]

    quantity: float

    subtotals_with_quantity: Iterable[InvoiceUsageLineItemSubtotalsWithQuantity]


class Invoice(TypedDict, total=False):
    contract_id: Required[str]

    credit_type_id: Required[str]

    customer_id: Required[str]

    exclusive_end_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    inclusive_start_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    issue_date: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    usage_line_items: Required[Iterable[InvoiceUsageLineItem]]

    billable_status: Literal["billable", "unbillable"]
    """This field's availability is dependent on your client's configuration."""

    breakdown_granularity: Literal["HOUR", "DAY"]

    custom_fields: Dict[str, str]
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""
