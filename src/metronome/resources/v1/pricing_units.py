# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ...types.v1 import pricing_unit_list_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.pricing_unit_list_response import PricingUnitListResponse

__all__ = ["PricingUnitsResource", "AsyncPricingUnitsResource"]


class PricingUnitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PricingUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return PricingUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PricingUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return PricingUnitsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PricingUnitListResponse]:
        """List all pricing units.

        All fiat currency types (for example, USD or GBP) will
        be included, as well as any custom pricing units that were configured. Custom
        pricing units can be used to charge for usage in a non-fiat pricing unit, for
        example AI credits.

        Note: The USD (cents) pricing unit is 2714e483-4ff1-48e4-9e25-ac732e8f24f2.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/credit-types/list",
            page=SyncCursorPage[PricingUnitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                    },
                    pricing_unit_list_params.PricingUnitListParams,
                ),
            ),
            model=PricingUnitListResponse,
        )


class AsyncPricingUnitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPricingUnitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPricingUnitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPricingUnitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncPricingUnitsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PricingUnitListResponse, AsyncCursorPage[PricingUnitListResponse]]:
        """List all pricing units.

        All fiat currency types (for example, USD or GBP) will
        be included, as well as any custom pricing units that were configured. Custom
        pricing units can be used to charge for usage in a non-fiat pricing unit, for
        example AI credits.

        Note: The USD (cents) pricing unit is 2714e483-4ff1-48e4-9e25-ac732e8f24f2.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/credit-types/list",
            page=AsyncCursorPage[PricingUnitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                    },
                    pricing_unit_list_params.PricingUnitListParams,
                ),
            ),
            model=PricingUnitListResponse,
        )


class PricingUnitsResourceWithRawResponse:
    def __init__(self, pricing_units: PricingUnitsResource) -> None:
        self._pricing_units = pricing_units

        self.list = to_raw_response_wrapper(
            pricing_units.list,
        )


class AsyncPricingUnitsResourceWithRawResponse:
    def __init__(self, pricing_units: AsyncPricingUnitsResource) -> None:
        self._pricing_units = pricing_units

        self.list = async_to_raw_response_wrapper(
            pricing_units.list,
        )


class PricingUnitsResourceWithStreamingResponse:
    def __init__(self, pricing_units: PricingUnitsResource) -> None:
        self._pricing_units = pricing_units

        self.list = to_streamed_response_wrapper(
            pricing_units.list,
        )


class AsyncPricingUnitsResourceWithStreamingResponse:
    def __init__(self, pricing_units: AsyncPricingUnitsResource) -> None:
        self._pricing_units = pricing_units

        self.list = async_to_streamed_response_wrapper(
            pricing_units.list,
        )
