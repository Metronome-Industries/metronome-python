# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal, Annotated

from typing import List, Dict, Iterable, Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["CreditCreateParams", "AccessSchedule", "AccessScheduleScheduleItem"]

class CreditCreateParams(TypedDict, total=False):
    access_schedule: Required[AccessSchedule]
    """Schedule for distributing the credit to the customer."""

    customer_id: Required[str]

    priority: Required[float]
    """
    If multiple credits or commits are applicable, the one with the lower priority
    will apply first.
    """

    product_id: Required[str]

    applicable_contract_ids: List[str]
    """Which contract the credit applies to.

    If not provided, the credit applies to all contracts.
    """

    applicable_product_ids: List[str]
    """Which products the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    applicable_product_tags: List[str]
    """Which tags the credit applies to.

    If both applicable_product_ids and applicable_product_tags are not provided, the
    credit applies to all products.
    """

    custom_fields: Dict[str, str]

    description: str
    """Used only in UI/API. It is not exposed to end customers."""

    name: str
    """displayed on invoices"""

    netsuite_sales_order_id: str
    """This field's availability is dependent on your client's configuration."""

    rate_type: Literal["COMMIT_RATE", "LIST_RATE"]

    salesforce_opportunity_id: str
    """This field's availability is dependent on your client's configuration."""

    uniqueness_key: str
    """Prevents the creation of duplicates.

    If a request to create a commit or credit is made with a uniqueness key that was
    previously used to create a commit or credit, a new record will not be created
    and the request will fail with a 409 error.
    """

class AccessScheduleScheduleItem(TypedDict, total=False):
    amount: Required[float]

    ending_before: Required[Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]]
    """RFC 3339 timestamp (exclusive)"""

    starting_at: Required[Annotated[Union[str, datetime], PropertyInfo(format = "iso8601")]]
    """RFC 3339 timestamp (inclusive)"""

class AccessSchedule(TypedDict, total=False):
    schedule_items: Required[Iterable[AccessScheduleScheduleItem]]

    credit_type_id: str
    """Defaults to USD (cents) if not passed"""