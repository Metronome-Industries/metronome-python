# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LifecycleEventSystemPolicyParam"]


class LifecycleEventSystemPolicyParam(TypedDict, total=False):
    type: Required[str]
    """The type of lifecycle event (e.g., "contract.create", "contract.start")"""
