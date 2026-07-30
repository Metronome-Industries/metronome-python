# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["InvoiceRegenerateParams"]

class InvoiceRegenerateParams(TypedDict, total=False):
    id: Required[str]
    """The invoice id to regenerate"""