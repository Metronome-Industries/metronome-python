# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CustomerSetIngestAliasesParams"]


class CustomerSetIngestAliasesParams(TypedDict, total=False):
    customer_id: Required[str]

    ingest_aliases: Required[SequenceNotStr[str]]
