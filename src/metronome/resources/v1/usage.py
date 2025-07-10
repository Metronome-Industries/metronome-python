# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import usage_list_params, usage_ingest_params, usage_search_params, usage_list_with_groups_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.usage_list_response import UsageListResponse
from ...types.v1.usage_search_response import UsageSearchResponse
from ...types.v1.usage_list_with_groups_response import UsageListWithGroupsResponse

__all__ = ["UsageResource", "AsyncUsageResource"]


class UsageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return UsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return UsageResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        window_size: Literal["HOUR", "DAY", "NONE"],
        next_page: str | NotGiven = NOT_GIVEN,
        billable_metrics: Iterable[usage_list_params.BillableMetric] | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageListResponse:
        """
        Fetch aggregated usage data for multiple customers and billable-metrics, broken
        into intervals of the specified length.

        Args:
          window_size: A window_size of "day" or "hour" will return the usage for the specified period
              segmented into daily or hourly aggregates. A window_size of "none" will return a
              single usage aggregate for the entirety of the specified period.

          next_page: Cursor that indicates where the next page of results should start.

          billable_metrics: A list of billable metrics to fetch usage for. If absent, all billable metrics
              will be returned.

          customer_ids: A list of Metronome customer IDs to fetch usage for. If absent, usage for all
              customers will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/usage",
            body=maybe_transform(
                {
                    "ending_before": ending_before,
                    "starting_on": starting_on,
                    "window_size": window_size,
                    "billable_metrics": billable_metrics,
                    "customer_ids": customer_ids,
                },
                usage_list_params.UsageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_page": next_page}, usage_list_params.UsageListParams),
            ),
            cast_to=UsageListResponse,
        )

    def ingest(
        self,
        *,
        usage: Iterable[usage_ingest_params.Usage] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Send usage events to Metronome.

        The body of this request is expected to be a
        JSON array of between 1 and 100 usage events. Compressed request bodies are
        supported with a `Content-Encoding: gzip` header. See
        [Getting usage into Metronome](https://docs.metronome.com/connect-metronome/) to
        learn more about usage events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/ingest",
            body=maybe_transform(usage, Iterable[usage_ingest_params.Usage]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_with_groups(
        self,
        *,
        billable_metric_id: str,
        customer_id: str,
        window_size: Literal["HOUR", "DAY", "NONE"],
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        current_period: bool | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        group_by: usage_list_with_groups_params.GroupBy | NotGiven = NOT_GIVEN,
        starting_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[UsageListWithGroupsResponse]:
        """
        Fetch aggregated usage data for the specified customer, billable-metric, and
        optional group, broken into intervals of the specified length.

        Args:
          window_size: A window_size of "day" or "hour" will return the usage for the specified period
              segmented into daily or hourly aggregates. A window_size of "none" will return a
              single usage aggregate for the entirety of the specified period.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          current_period: If true, will return the usage for the current billing period. Will return an
              error if the customer is currently uncontracted or starting_on and ending_before
              are specified when this is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/usage/groups",
            page=SyncCursorPage[UsageListWithGroupsResponse],
            body=maybe_transform(
                {
                    "billable_metric_id": billable_metric_id,
                    "customer_id": customer_id,
                    "window_size": window_size,
                    "current_period": current_period,
                    "ending_before": ending_before,
                    "group_by": group_by,
                    "starting_on": starting_on,
                },
                usage_list_with_groups_params.UsageListWithGroupsParams,
            ),
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
                    usage_list_with_groups_params.UsageListWithGroupsParams,
                ),
            ),
            model=UsageListWithGroupsResponse,
            method="post",
        )

    def search(
        self,
        *,
        transaction_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageSearchResponse:
        """
        For a set of events, look up matched billable metrics and customers by
        transaction id. This endpoint looks at transactions that occurred in the last 34
        days, and is intended for sampling-based testing workflows. It is heavily rate
        limited.

        Args:
          transaction_ids: The transaction IDs of the events to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/events/search",
            body=maybe_transform({"transaction_ids": transaction_ids}, usage_search_params.UsageSearchParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageSearchResponse,
        )


class AsyncUsageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncUsageResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        window_size: Literal["HOUR", "DAY", "NONE"],
        next_page: str | NotGiven = NOT_GIVEN,
        billable_metrics: Iterable[usage_list_params.BillableMetric] | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageListResponse:
        """
        Fetch aggregated usage data for multiple customers and billable-metrics, broken
        into intervals of the specified length.

        Args:
          window_size: A window_size of "day" or "hour" will return the usage for the specified period
              segmented into daily or hourly aggregates. A window_size of "none" will return a
              single usage aggregate for the entirety of the specified period.

          next_page: Cursor that indicates where the next page of results should start.

          billable_metrics: A list of billable metrics to fetch usage for. If absent, all billable metrics
              will be returned.

          customer_ids: A list of Metronome customer IDs to fetch usage for. If absent, usage for all
              customers will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/usage",
            body=await async_maybe_transform(
                {
                    "ending_before": ending_before,
                    "starting_on": starting_on,
                    "window_size": window_size,
                    "billable_metrics": billable_metrics,
                    "customer_ids": customer_ids,
                },
                usage_list_params.UsageListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"next_page": next_page}, usage_list_params.UsageListParams),
            ),
            cast_to=UsageListResponse,
        )

    async def ingest(
        self,
        *,
        usage: Iterable[usage_ingest_params.Usage] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Send usage events to Metronome.

        The body of this request is expected to be a
        JSON array of between 1 and 100 usage events. Compressed request bodies are
        supported with a `Content-Encoding: gzip` header. See
        [Getting usage into Metronome](https://docs.metronome.com/connect-metronome/) to
        learn more about usage events.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/ingest",
            body=await async_maybe_transform(usage, Iterable[usage_ingest_params.Usage]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_with_groups(
        self,
        *,
        billable_metric_id: str,
        customer_id: str,
        window_size: Literal["HOUR", "DAY", "NONE"],
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        current_period: bool | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        group_by: usage_list_with_groups_params.GroupBy | NotGiven = NOT_GIVEN,
        starting_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[UsageListWithGroupsResponse, AsyncCursorPage[UsageListWithGroupsResponse]]:
        """
        Fetch aggregated usage data for the specified customer, billable-metric, and
        optional group, broken into intervals of the specified length.

        Args:
          window_size: A window_size of "day" or "hour" will return the usage for the specified period
              segmented into daily or hourly aggregates. A window_size of "none" will return a
              single usage aggregate for the entirety of the specified period.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          current_period: If true, will return the usage for the current billing period. Will return an
              error if the customer is currently uncontracted or starting_on and ending_before
              are specified when this is true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/usage/groups",
            page=AsyncCursorPage[UsageListWithGroupsResponse],
            body=maybe_transform(
                {
                    "billable_metric_id": billable_metric_id,
                    "customer_id": customer_id,
                    "window_size": window_size,
                    "current_period": current_period,
                    "ending_before": ending_before,
                    "group_by": group_by,
                    "starting_on": starting_on,
                },
                usage_list_with_groups_params.UsageListWithGroupsParams,
            ),
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
                    usage_list_with_groups_params.UsageListWithGroupsParams,
                ),
            ),
            model=UsageListWithGroupsResponse,
            method="post",
        )

    async def search(
        self,
        *,
        transaction_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UsageSearchResponse:
        """
        For a set of events, look up matched billable metrics and customers by
        transaction id. This endpoint looks at transactions that occurred in the last 34
        days, and is intended for sampling-based testing workflows. It is heavily rate
        limited.

        Args:
          transaction_ids: The transaction IDs of the events to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/events/search",
            body=await async_maybe_transform(
                {"transaction_ids": transaction_ids}, usage_search_params.UsageSearchParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UsageSearchResponse,
        )


class UsageResourceWithRawResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.list = to_raw_response_wrapper(
            usage.list,
        )
        self.ingest = to_raw_response_wrapper(
            usage.ingest,
        )
        self.list_with_groups = to_raw_response_wrapper(
            usage.list_with_groups,
        )
        self.search = to_raw_response_wrapper(
            usage.search,
        )


class AsyncUsageResourceWithRawResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.list = async_to_raw_response_wrapper(
            usage.list,
        )
        self.ingest = async_to_raw_response_wrapper(
            usage.ingest,
        )
        self.list_with_groups = async_to_raw_response_wrapper(
            usage.list_with_groups,
        )
        self.search = async_to_raw_response_wrapper(
            usage.search,
        )


class UsageResourceWithStreamingResponse:
    def __init__(self, usage: UsageResource) -> None:
        self._usage = usage

        self.list = to_streamed_response_wrapper(
            usage.list,
        )
        self.ingest = to_streamed_response_wrapper(
            usage.ingest,
        )
        self.list_with_groups = to_streamed_response_wrapper(
            usage.list_with_groups,
        )
        self.search = to_streamed_response_wrapper(
            usage.search,
        )


class AsyncUsageResourceWithStreamingResponse:
    def __init__(self, usage: AsyncUsageResource) -> None:
        self._usage = usage

        self.list = async_to_streamed_response_wrapper(
            usage.list,
        )
        self.ingest = async_to_streamed_response_wrapper(
            usage.ingest,
        )
        self.list_with_groups = async_to_streamed_response_wrapper(
            usage.list_with_groups,
        )
        self.search = async_to_streamed_response_wrapper(
            usage.search,
        )
