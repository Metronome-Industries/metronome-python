# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["CustomerSetNameParams"]

class CustomerSetNameParams(TypedDict, total=False):
    customer_id: Required[str]

    name: Required[str]
    """The new name for the customer.

    This will be truncated to 160 characters if the provided name is longer.
    """