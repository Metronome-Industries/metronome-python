# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["PackageArchiveParams"]

class PackageArchiveParams(TypedDict, total=False):
    package_id: Required[str]
    """ID of the package to archive"""