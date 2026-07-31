# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SettingUpsertAvalaraCredentialsParams"]


class SettingUpsertAvalaraCredentialsParams(TypedDict, total=False):
    avalara_environment: Required[Literal["PRODUCTION", "SANDBOX"]]
    """The Avalara environment to use (SANDBOX or PRODUCTION)."""

    avalara_password: Required[str]
    """The password for the Avalara account."""

    avalara_username: Required[str]
    """The username for the Avalara account."""

    delivery_method_ids: Required[SequenceNotStr[str]]
    """
    The delivery method IDs of the billing provider configurations to update, can be
    found in the response of the `/listConfiguredBillingProviders` endpoint.
    """

    commit_transactions: bool
    """
    Commit transactions if you want Metronome tax calculations used for reporting
    and tax filings.
    """
