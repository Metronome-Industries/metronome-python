# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.notifications import offset_list_params
from ...types.notifications.offset_list_response import OffsetListResponse

__all__ = ["OffsetResource", "AsyncOffsetResource"]


class OffsetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OffsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return OffsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OffsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return OffsetResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetListResponse:
        """List offset lifecycle event notification configurations.

        These are user-created
        notifications that trigger at a specified time offset relative to lifecycle
        events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/notifications/offset/list",
            body=maybe_transform(
                {
                    "cursor": cursor,
                    "limit": limit,
                },
                offset_list_params.OffsetListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetListResponse,
        )


class AsyncOffsetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOffsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOffsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOffsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncOffsetResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetListResponse:
        """List offset lifecycle event notification configurations.

        These are user-created
        notifications that trigger at a specified time offset relative to lifecycle
        events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/notifications/offset/list",
            body=await async_maybe_transform(
                {
                    "cursor": cursor,
                    "limit": limit,
                },
                offset_list_params.OffsetListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetListResponse,
        )


class OffsetResourceWithRawResponse:
    def __init__(self, offset: OffsetResource) -> None:
        self._offset = offset

        self.list = to_raw_response_wrapper(
            offset.list,
        )


class AsyncOffsetResourceWithRawResponse:
    def __init__(self, offset: AsyncOffsetResource) -> None:
        self._offset = offset

        self.list = async_to_raw_response_wrapper(
            offset.list,
        )


class OffsetResourceWithStreamingResponse:
    def __init__(self, offset: OffsetResource) -> None:
        self._offset = offset

        self.list = to_streamed_response_wrapper(
            offset.list,
        )


class AsyncOffsetResourceWithStreamingResponse:
    def __init__(self, offset: AsyncOffsetResource) -> None:
        self._offset = offset

        self.list = async_to_streamed_response_wrapper(
            offset.list,
        )
