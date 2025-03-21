# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["CommitUpdateEndDateParams"]


class CommitUpdateEndDateParams(TypedDict, total=False):
    commit_id: Required[str]
    """ID of the commit to update. Only supports "PREPAID" commits."""

    customer_id: Required[str]
    """ID of the customer whose commit is to be updated"""

    access_ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    RFC 3339 timestamp indicating when access to the commit will end and it will no
    longer be possible to draw it down (exclusive). If not provided, the access will
    not be updated.
    """

    invoices_ending_before: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    RFC 3339 timestamp indicating when the commit will stop being invoiced
    (exclusive). If not provided, the invoice schedule will not be updated.
    """
