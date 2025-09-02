# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BaseUsageFilter"]


class BaseUsageFilter(TypedDict, total=False):
    group_key: Required[str]

    group_values: Required[SequenceNotStr[str]]

    starting_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
