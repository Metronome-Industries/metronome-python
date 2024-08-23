# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ContractArchiveParams"]


class ContractArchiveParams(TypedDict, total=False):
    contract_id: Required[str]
    """ID of the contract to archive"""

    customer_id: Required[str]
    """ID of the customer whose contract is to be archived"""

    void_invoices: Required[bool]
    """
    If false, the existing finalized invoices will remain after the contract is
    archived.
    """
