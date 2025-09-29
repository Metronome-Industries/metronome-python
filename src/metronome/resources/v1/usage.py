# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...pagination import SyncCursorPage, AsyncCursorPage, SyncCursorPageWithoutLimit, AsyncCursorPageWithoutLimit
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
        next_page: str | Omit = omit,
        billable_metrics: Iterable[usage_list_params.BillableMetric] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPageWithoutLimit[UsageListResponse]:
        """
        Retrieve aggregated usage data across multiple customers and billable metrics in
        a single query. This batch endpoint enables you to fetch usage patterns at
        scale, broken down by time windows, making it ideal for building analytics
        dashboards, generating reports, and monitoring platform-wide usage trends.

        ### Use this endpoint to:

        - Generate platform-wide usage reports for internal teams
        - Monitor aggregate usage trends across your entire customer base
        - Create comparative usage analyses between customers or time periods
        - Support capacity planning with historical usage patterns

        ### Key response fields:

        An array of `UsageBatchAggregate` objects containing:

        - `customer_id`: The customer this usage belongs to
        - `billable_metric_id` and `billable_metric_name`: What was measured
        - `start_timestamp` and `end_timestamp`: Time window for this data point
        - `value`: Aggregated usage amount for the period
        - `groups` (optional): Usage broken down by group keys with values
        - `next_page`: Pagination cursor for large result sets

        ### Usage guidelines:

        - Time windows: Set `window_size` to `hour`, `day`, or `none` (entire period)
        - Required parameters: Must specify `starting_on`, `ending_before`, and
          `window_size`
        - Filtering options:
          - `customer_ids`: Limit to specific customers (omit for all customers)
          - `billable_metrics`: Limit to specific metrics (omit for all metrics)
        - Pagination: Use `next_page` cursor to retrieve large datasets
        - Null values: Group values may be null when no usage matches that group

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
        return self._get_api_list(
            "/v1/usage",
            page=SyncCursorPageWithoutLimit[UsageListResponse],
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
            model=UsageListResponse,
            method="post",
        )

    def ingest(
        self,
        *,
        usage: Iterable[usage_ingest_params.Usage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        The ingest endpoint is the primary method for sending usage events to Metronome,
        serving as the foundation for all billing calculations in your usage-based
        pricing model. This high-throughput endpoint is designed for real-time streaming
        ingestion, supports backdating 34 days, and is built to handle mission-critical
        usage data with enterprise-grade reliability. Metronome supports 100,000 events
        per second without requiring pre-aggregation or rollups and can scale up from
        there. See the [Send usage events](/guides/events/send-usage-events) guide to
        learn more about usage events.

        ### Use this endpoint to:

        Create a customer usage pipeline into Metronome that drives billable metrics,
        credit drawdown, and invoicing. Track customer behavior, resource consumption,
        and feature usage

        ### What happens when you send events:

        - Events are validated and processed in real-time
        - Events are matched to customers using customer IDs or customer ingest aliases
        - Events are matched to billable metrics and are immediately available for usage
          and spend calculations

        ### Usage guidelines:

        - Historical events can be backdated up to 34 days and will immediately impact
          live customer spend
        - Duplicate events are automatically detected and ignored (34-day deduplication
          window)

        #### Event structure:

        Usage events are simple JSON objects designed for flexibility and ease of
        integration:

        ```json
        {
          "transaction_id": "2021-01-01T00:00:00Z_cluster42",
          "customer_id": "team@example.com",
          "event_type": "api_request",
          "timestamp": "2021-01-01T00:00:00Z",
          "properties": {
            "endpoint": "/v1/users",
            "method": "POST",
            "response_time_ms": 45,
            "region": "us-west-2"
          }
        }
        ```

        Learn more about
        [usage event structure definitions](/guides/events/design-usage-events).

        #### Transaction ID

        The transaction_id serves as your idempotency key, ensuring events are processed
        exactly once. Metronome maintains a 34-day deduplication window - significantly
        longer than typical 12-hour windows - enabling robust backfill scenarios without
        duplicate billing.

        - Best Practices:
          - Use UUIDs for one-time events: uuid4()
          - For heartbeat events, use deterministic IDs
          - Include enough context to avoid collisions across different event sources

        #### Customer ID

        Identifies which customer should be billed for this usage. Supports two
        identification methods:

        - Metronome Customer ID: The UUID returned when creating a customer
        - Ingest Alias: Your system's identifier (email, account number, etc.)

        Ingest aliases enable seamless integration without requiring ID mapping, and
        customers can have multiple aliases for flexibility.

        #### Event Type:

        Categorizes the event type for billable metric matching. Choose descriptive
        names that aligns with the product surface area.

        #### Properties:

        Flexible metadata also used to match billable metrics or to be used to serve as
        group keys to create multiple pricing dimensions or breakdown costs by novel
        properties for end customers or internal finance teams measuring underlying
        COGs.

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
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        current_period: bool | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        group_by: usage_list_with_groups_params.GroupBy | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[UsageListWithGroupsResponse]:
        """
        Retrieve granular usage data for a specific customer and billable metric, with
        the ability to break down usage by custom grouping dimensions. This endpoint
        enables deep usage analytics by segmenting data across attributes like region,
        user, model type, or any custom dimension defined in your billable metrics.

        ### Use this endpoint to:

        - Analyze usage patterns broken down by specific attributes (region, user,
          department, etc.)
        - Build detailed usage dashboards with dimensional filtering
        - Identify high-usage segments for optimization opportunities

        ### Key response fields:

        An array of `PagedUsageAggregate` objects containing:

        - `starting_on` and `ending_before`: Time window boundaries
        - `group_key`: The dimension being grouped by (e.g., "region")
        - `group_value`: The specific value for this group (e.g., "US-East")
        - `value`: Aggregated usage for this group and time window
        - `next_page`: Pagination cursor for large datasets

        ### Usage guidelines:

        - Required parameters: Must specify `customer_id`, `billable_metric_id`, and
          `window_size`
        - Time windows: Set `window_size` to hour, day, or none for different
          granularities
        - Group filtering: Use `group_by` to specify:
          - key: The dimension to group by (must be set on the billable metric as a
            group key)
          - values: Optional array to filter to specific values only
        - Pagination: Use limit and `next_page` for large result sets
        - Null handling: `group_value` may be null for unmatched data

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
        transaction_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSearchResponse:
        """
        This endpoint retrieves events by transaction ID for events that occurred within
        the last 34 days. It is specifically designed for sampling-based testing
        workflows to detect revenue leakage. The Event Search API provides a critical
        observability tool that validates the integrity of your usage pipeline by
        allowing you to sample raw events and verify their matching against active
        billable metrics.

        Why event observability matters for revenue leakage: Silent revenue loss occurs
        when events are dropped, delayed, or fail to match billable metrics due to:

        - Upstream system failures
        - Event format changes
        - Misconfigured billable metrics

        ### Use this endpoint to:

        - Sample raw events and validate they match the expected billable metrics
        - Build custom leakage detection alerts to prevent silent revenue loss
        - Verify event processing accuracy during system changes or metric updates
        - Debug event matching issues in real-time

        ### Key response fields:

        - Complete event details including transaction ID, customer ID, and properties
        - Matched Metronome customer (if any)
        - Matched billable metric information (if any)
        - Processing status and duplicate detection flags

        ### Usage guidelines:

        ⚠️ Important: This endpoint is heavily rate limited and designed for sampling
        workflows only. Do not use this endpoint to check every event in your system.
        Instead, implement a sampling strategy to randomly validate a subset of events
        for observability purposes.

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

    def list(
        self,
        *,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        window_size: Literal["HOUR", "DAY", "NONE"],
        next_page: str | Omit = omit,
        billable_metrics: Iterable[usage_list_params.BillableMetric] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UsageListResponse, AsyncCursorPageWithoutLimit[UsageListResponse]]:
        """
        Retrieve aggregated usage data across multiple customers and billable metrics in
        a single query. This batch endpoint enables you to fetch usage patterns at
        scale, broken down by time windows, making it ideal for building analytics
        dashboards, generating reports, and monitoring platform-wide usage trends.

        ### Use this endpoint to:

        - Generate platform-wide usage reports for internal teams
        - Monitor aggregate usage trends across your entire customer base
        - Create comparative usage analyses between customers or time periods
        - Support capacity planning with historical usage patterns

        ### Key response fields:

        An array of `UsageBatchAggregate` objects containing:

        - `customer_id`: The customer this usage belongs to
        - `billable_metric_id` and `billable_metric_name`: What was measured
        - `start_timestamp` and `end_timestamp`: Time window for this data point
        - `value`: Aggregated usage amount for the period
        - `groups` (optional): Usage broken down by group keys with values
        - `next_page`: Pagination cursor for large result sets

        ### Usage guidelines:

        - Time windows: Set `window_size` to `hour`, `day`, or `none` (entire period)
        - Required parameters: Must specify `starting_on`, `ending_before`, and
          `window_size`
        - Filtering options:
          - `customer_ids`: Limit to specific customers (omit for all customers)
          - `billable_metrics`: Limit to specific metrics (omit for all metrics)
        - Pagination: Use `next_page` cursor to retrieve large datasets
        - Null values: Group values may be null when no usage matches that group

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
        return self._get_api_list(
            "/v1/usage",
            page=AsyncCursorPageWithoutLimit[UsageListResponse],
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
            model=UsageListResponse,
            method="post",
        )

    async def ingest(
        self,
        *,
        usage: Iterable[usage_ingest_params.Usage] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        The ingest endpoint is the primary method for sending usage events to Metronome,
        serving as the foundation for all billing calculations in your usage-based
        pricing model. This high-throughput endpoint is designed for real-time streaming
        ingestion, supports backdating 34 days, and is built to handle mission-critical
        usage data with enterprise-grade reliability. Metronome supports 100,000 events
        per second without requiring pre-aggregation or rollups and can scale up from
        there. See the [Send usage events](/guides/events/send-usage-events) guide to
        learn more about usage events.

        ### Use this endpoint to:

        Create a customer usage pipeline into Metronome that drives billable metrics,
        credit drawdown, and invoicing. Track customer behavior, resource consumption,
        and feature usage

        ### What happens when you send events:

        - Events are validated and processed in real-time
        - Events are matched to customers using customer IDs or customer ingest aliases
        - Events are matched to billable metrics and are immediately available for usage
          and spend calculations

        ### Usage guidelines:

        - Historical events can be backdated up to 34 days and will immediately impact
          live customer spend
        - Duplicate events are automatically detected and ignored (34-day deduplication
          window)

        #### Event structure:

        Usage events are simple JSON objects designed for flexibility and ease of
        integration:

        ```json
        {
          "transaction_id": "2021-01-01T00:00:00Z_cluster42",
          "customer_id": "team@example.com",
          "event_type": "api_request",
          "timestamp": "2021-01-01T00:00:00Z",
          "properties": {
            "endpoint": "/v1/users",
            "method": "POST",
            "response_time_ms": 45,
            "region": "us-west-2"
          }
        }
        ```

        Learn more about
        [usage event structure definitions](/guides/events/design-usage-events).

        #### Transaction ID

        The transaction_id serves as your idempotency key, ensuring events are processed
        exactly once. Metronome maintains a 34-day deduplication window - significantly
        longer than typical 12-hour windows - enabling robust backfill scenarios without
        duplicate billing.

        - Best Practices:
          - Use UUIDs for one-time events: uuid4()
          - For heartbeat events, use deterministic IDs
          - Include enough context to avoid collisions across different event sources

        #### Customer ID

        Identifies which customer should be billed for this usage. Supports two
        identification methods:

        - Metronome Customer ID: The UUID returned when creating a customer
        - Ingest Alias: Your system's identifier (email, account number, etc.)

        Ingest aliases enable seamless integration without requiring ID mapping, and
        customers can have multiple aliases for flexibility.

        #### Event Type:

        Categorizes the event type for billable metric matching. Choose descriptive
        names that aligns with the product surface area.

        #### Properties:

        Flexible metadata also used to match billable metrics or to be used to serve as
        group keys to create multiple pricing dimensions or breakdown costs by novel
        properties for end customers or internal finance teams measuring underlying
        COGs.

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
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        current_period: bool | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        group_by: usage_list_with_groups_params.GroupBy | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[UsageListWithGroupsResponse, AsyncCursorPage[UsageListWithGroupsResponse]]:
        """
        Retrieve granular usage data for a specific customer and billable metric, with
        the ability to break down usage by custom grouping dimensions. This endpoint
        enables deep usage analytics by segmenting data across attributes like region,
        user, model type, or any custom dimension defined in your billable metrics.

        ### Use this endpoint to:

        - Analyze usage patterns broken down by specific attributes (region, user,
          department, etc.)
        - Build detailed usage dashboards with dimensional filtering
        - Identify high-usage segments for optimization opportunities

        ### Key response fields:

        An array of `PagedUsageAggregate` objects containing:

        - `starting_on` and `ending_before`: Time window boundaries
        - `group_key`: The dimension being grouped by (e.g., "region")
        - `group_value`: The specific value for this group (e.g., "US-East")
        - `value`: Aggregated usage for this group and time window
        - `next_page`: Pagination cursor for large datasets

        ### Usage guidelines:

        - Required parameters: Must specify `customer_id`, `billable_metric_id`, and
          `window_size`
        - Time windows: Set `window_size` to hour, day, or none for different
          granularities
        - Group filtering: Use `group_by` to specify:
          - key: The dimension to group by (must be set on the billable metric as a
            group key)
          - values: Optional array to filter to specific values only
        - Pagination: Use limit and `next_page` for large result sets
        - Null handling: `group_value` may be null for unmatched data

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
        transaction_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageSearchResponse:
        """
        This endpoint retrieves events by transaction ID for events that occurred within
        the last 34 days. It is specifically designed for sampling-based testing
        workflows to detect revenue leakage. The Event Search API provides a critical
        observability tool that validates the integrity of your usage pipeline by
        allowing you to sample raw events and verify their matching against active
        billable metrics.

        Why event observability matters for revenue leakage: Silent revenue loss occurs
        when events are dropped, delayed, or fail to match billable metrics due to:

        - Upstream system failures
        - Event format changes
        - Misconfigured billable metrics

        ### Use this endpoint to:

        - Sample raw events and validate they match the expected billable metrics
        - Build custom leakage detection alerts to prevent silent revenue loss
        - Verify event processing accuracy during system changes or metric updates
        - Debug event matching issues in real-time

        ### Key response fields:

        - Complete event details including transaction ID, customer ID, and properties
        - Matched Metronome customer (if any)
        - Matched billable metric information (if any)
        - Processing status and duplicate detection flags

        ### Usage guidelines:

        ⚠️ Important: This endpoint is heavily rate limited and designed for sampling
        workflows only. Do not use this endpoint to check every event in your system.
        Instead, implement a sampling strategy to randomly validate a subset of events
        for observability purposes.

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
