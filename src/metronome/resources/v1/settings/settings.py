# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import setting_upsert_avalara_credentials_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .billing_providers import (
    BillingProvidersResource,
    AsyncBillingProvidersResource,
    BillingProvidersResourceWithRawResponse,
    AsyncBillingProvidersResourceWithRawResponse,
    BillingProvidersResourceWithStreamingResponse,
    AsyncBillingProvidersResourceWithStreamingResponse,
)
from ....types.v1.setting_upsert_avalara_credentials_response import SettingUpsertAvalaraCredentialsResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]


class SettingsResource(SyncAPIResource):
    @cached_property
    def billing_providers(self) -> BillingProvidersResource:
        return BillingProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return SettingsResourceWithStreamingResponse(self)

    def upsert_avalara_credentials(
        self,
        *,
        avalara_environment: Literal["PRODUCTION", "SANDBOX"],
        avalara_password: str,
        avalara_username: str,
        delivery_method_ids: SequenceNotStr[str],
        commit_transactions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpsertAvalaraCredentialsResponse:
        """
        Set the Avalara credentials for some specified `delivery_method_ids`, which can
        be found in the `/listConfiguredBillingProviders` response. This maps the
        Avalara credentials to the appropriate billing entity. These credentials are
        only used for PLG Invoicing today.

        Args:
          avalara_environment: The Avalara environment to use (SANDBOX or PRODUCTION).

          avalara_password: The password for the Avalara account.

          avalara_username: The username for the Avalara account.

          delivery_method_ids: The delivery method IDs of the billing provider configurations to update, can be
              found in the response of the `/listConfiguredBillingProviders` endpoint.

          commit_transactions: Commit transactions if you want Metronome tax calculations used for reporting
              and tax filings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/upsertAvalaraCredentials",
            body=maybe_transform(
                {
                    "avalara_environment": avalara_environment,
                    "avalara_password": avalara_password,
                    "avalara_username": avalara_username,
                    "delivery_method_ids": delivery_method_ids,
                    "commit_transactions": commit_transactions,
                },
                setting_upsert_avalara_credentials_params.SettingUpsertAvalaraCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpsertAvalaraCredentialsResponse,
        )


class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def billing_providers(self) -> AsyncBillingProvidersResource:
        return AsyncBillingProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncSettingsResourceWithStreamingResponse(self)

    async def upsert_avalara_credentials(
        self,
        *,
        avalara_environment: Literal["PRODUCTION", "SANDBOX"],
        avalara_password: str,
        avalara_username: str,
        delivery_method_ids: SequenceNotStr[str],
        commit_transactions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SettingUpsertAvalaraCredentialsResponse:
        """
        Set the Avalara credentials for some specified `delivery_method_ids`, which can
        be found in the `/listConfiguredBillingProviders` response. This maps the
        Avalara credentials to the appropriate billing entity. These credentials are
        only used for PLG Invoicing today.

        Args:
          avalara_environment: The Avalara environment to use (SANDBOX or PRODUCTION).

          avalara_password: The password for the Avalara account.

          avalara_username: The username for the Avalara account.

          delivery_method_ids: The delivery method IDs of the billing provider configurations to update, can be
              found in the response of the `/listConfiguredBillingProviders` endpoint.

          commit_transactions: Commit transactions if you want Metronome tax calculations used for reporting
              and tax filings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/upsertAvalaraCredentials",
            body=await async_maybe_transform(
                {
                    "avalara_environment": avalara_environment,
                    "avalara_password": avalara_password,
                    "avalara_username": avalara_username,
                    "delivery_method_ids": delivery_method_ids,
                    "commit_transactions": commit_transactions,
                },
                setting_upsert_avalara_credentials_params.SettingUpsertAvalaraCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettingUpsertAvalaraCredentialsResponse,
        )


class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.upsert_avalara_credentials = to_raw_response_wrapper(
            settings.upsert_avalara_credentials,
        )

    @cached_property
    def billing_providers(self) -> BillingProvidersResourceWithRawResponse:
        return BillingProvidersResourceWithRawResponse(self._settings.billing_providers)


class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.upsert_avalara_credentials = async_to_raw_response_wrapper(
            settings.upsert_avalara_credentials,
        )

    @cached_property
    def billing_providers(self) -> AsyncBillingProvidersResourceWithRawResponse:
        return AsyncBillingProvidersResourceWithRawResponse(self._settings.billing_providers)


class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

        self.upsert_avalara_credentials = to_streamed_response_wrapper(
            settings.upsert_avalara_credentials,
        )

    @cached_property
    def billing_providers(self) -> BillingProvidersResourceWithStreamingResponse:
        return BillingProvidersResourceWithStreamingResponse(self._settings.billing_providers)


class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

        self.upsert_avalara_credentials = async_to_streamed_response_wrapper(
            settings.upsert_avalara_credentials,
        )

    @cached_property
    def billing_providers(self) -> AsyncBillingProvidersResourceWithStreamingResponse:
        return AsyncBillingProvidersResourceWithStreamingResponse(self._settings.billing_providers)
