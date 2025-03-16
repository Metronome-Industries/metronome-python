# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["CustomerSetIngestAliasesParams"]

class CustomerSetIngestAliasesParams(TypedDict, total=False):
    customer_id: Required[str]

    ingest_aliases: Required[List[str]]