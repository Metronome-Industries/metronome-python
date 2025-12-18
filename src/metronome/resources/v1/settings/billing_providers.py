# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.settings import billing_provider_list_params, billing_provider_create_params
from ....types.v1.settings.billing_provider_list_response import BillingProviderListResponse
from ....types.v1.settings.billing_provider_create_response import BillingProviderCreateResponse

__all__ = ["BillingProvidersResource", "AsyncBillingProvidersResource"]


class BillingProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return BillingProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return BillingProvidersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace"],
        configuration: Dict[str, object],
        delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "aws_sns"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingProviderCreateResponse:
        """Set up account-level configuration for a billing provider.

        Once configured,
        individual contracts across customers can be mapped to this configuration using
        the returned delivery_method_id.

        Args:
          billing_provider: The billing provider set for this configuration.

          configuration: Account-level configuration for the billing provider. The structure of this
              object is specific to the billing provider and delivery provider combination.
              See examples below.

          delivery_method: The method to use for delivering invoices for this configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/setUpBillingProvider",
            body=maybe_transform(
                {
                    "billing_provider": billing_provider,
                    "configuration": configuration,
                    "delivery_method": delivery_method,
                },
                billing_provider_create_params.BillingProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingProviderCreateResponse,
        )

    def list(
        self,
        *,
        next_page: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingProviderListResponse:
        """
        Lists all configured billing providers and their delivery method configurations
        for your account. Returns provider details, delivery method IDs, and
        configuration settings needed for mapping individual customer contracts to
        billing integrations.

        Args:
          next_page: The cursor to the next page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/listConfiguredBillingProviders",
            body=maybe_transform({"next_page": next_page}, billing_provider_list_params.BillingProviderListParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingProviderListResponse,
        )


class AsyncBillingProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillingProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncBillingProvidersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace"],
        configuration: Dict[str, object],
        delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "aws_sns"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingProviderCreateResponse:
        """Set up account-level configuration for a billing provider.

        Once configured,
        individual contracts across customers can be mapped to this configuration using
        the returned delivery_method_id.

        Args:
          billing_provider: The billing provider set for this configuration.

          configuration: Account-level configuration for the billing provider. The structure of this
              object is specific to the billing provider and delivery provider combination.
              See examples below.

          delivery_method: The method to use for delivering invoices for this configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/setUpBillingProvider",
            body=await async_maybe_transform(
                {
                    "billing_provider": billing_provider,
                    "configuration": configuration,
                    "delivery_method": delivery_method,
                },
                billing_provider_create_params.BillingProviderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingProviderCreateResponse,
        )

    async def list(
        self,
        *,
        next_page: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillingProviderListResponse:
        """
        Lists all configured billing providers and their delivery method configurations
        for your account. Returns provider details, delivery method IDs, and
        configuration settings needed for mapping individual customer contracts to
        billing integrations.

        Args:
          next_page: The cursor to the next page of results

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/listConfiguredBillingProviders",
            body=await async_maybe_transform(
                {"next_page": next_page}, billing_provider_list_params.BillingProviderListParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingProviderListResponse,
        )


class BillingProvidersResourceWithRawResponse:
    def __init__(self, billing_providers: BillingProvidersResource) -> None:
        self._billing_providers = billing_providers

        self.create = to_raw_response_wrapper(
            billing_providers.create,
        )
        self.list = to_raw_response_wrapper(
            billing_providers.list,
        )


class AsyncBillingProvidersResourceWithRawResponse:
    def __init__(self, billing_providers: AsyncBillingProvidersResource) -> None:
        self._billing_providers = billing_providers

        self.create = async_to_raw_response_wrapper(
            billing_providers.create,
        )
        self.list = async_to_raw_response_wrapper(
            billing_providers.list,
        )


class BillingProvidersResourceWithStreamingResponse:
    def __init__(self, billing_providers: BillingProvidersResource) -> None:
        self._billing_providers = billing_providers

        self.create = to_streamed_response_wrapper(
            billing_providers.create,
        )
        self.list = to_streamed_response_wrapper(
            billing_providers.list,
        )


class AsyncBillingProvidersResourceWithStreamingResponse:
    def __init__(self, billing_providers: AsyncBillingProvidersResource) -> None:
        self._billing_providers = billing_providers

        self.create = async_to_streamed_response_wrapper(
            billing_providers.create,
        )
        self.list = async_to_streamed_response_wrapper(
            billing_providers.list,
        )
