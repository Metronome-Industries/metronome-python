# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AlertArchiveParams"]


class AlertArchiveParams(TypedDict, total=False):
    id: Required[str]
    """The Metronome ID of the alert"""

    release_uniqueness_key: bool
    """If true, resets the uniqueness key on this alert so it can be re-used"""
