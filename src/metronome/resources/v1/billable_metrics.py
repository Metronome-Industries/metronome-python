# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import billable_metric_list_params, billable_metric_create_params, billable_metric_archive_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.shared_params.property_filter import PropertyFilter
from ...types.shared_params.event_type_filter import EventTypeFilter
from ...types.v1.billable_metric_list_response import BillableMetricListResponse
from ...types.v1.billable_metric_create_response import BillableMetricCreateResponse
from ...types.v1.billable_metric_archive_response import BillableMetricArchiveResponse
from ...types.v1.billable_metric_retrieve_response import BillableMetricRetrieveResponse

__all__ = ["BillableMetricsResource", "AsyncBillableMetricsResource"]


class BillableMetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillableMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return BillableMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillableMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return BillableMetricsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        aggregation_key: str | Omit = omit,
        aggregation_type: Literal["COUNT", "LATEST", "MAX", "SUM", "UNIQUE"] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        event_type_filter: EventTypeFilter | Omit = omit,
        group_keys: Iterable[SequenceNotStr[str]] | Omit = omit,
        property_filters: Iterable[PropertyFilter] | Omit = omit,
        sql: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetricCreateResponse:
        """
        Create billable metrics programmatically with this endpoint—an essential step in
        configuring your pricing and packaging in Metronome.

        A billable metric is a customizable query that filters and aggregates events
        from your event stream. These metrics are continuously tracked as usage data
        enters Metronome through the ingestion pipeline. The ingestion process
        transforms raw usage data into actionable pricing metrics, enabling accurate
        metering and billing for your products.

        ### Use this endpoint to:

        - Create individual or multiple billable metrics as part of a setup workflow.
        - Automate the entire pricing configuration process, from metric creation to
          customer contract setup.
        - Define metrics using either standard filtering/aggregation or a custom SQL
          query.

        ### Key response fields:

        - The ID of the billable metric that was created
        - The created billable metric will be available to be used in Products, usage
          endpoints, and alerts.

        ### Usage guidelines:

        - Metrics defined using standard filtering and aggregation are Streaming
          billable metrics, which have been optimized for ultra low latency and high
          throughput workflows.
        - Use SQL billable metrics if you require more flexible aggregation options.

        Args:
          name: The display name of the billable metric.

          aggregation_key: Specifies the type of aggregation performed on matching events. Required if
              `sql` is not provided.

          aggregation_type: Specifies the type of aggregation performed on matching events.

          custom_fields: Custom fields to attach to the billable metric.

          event_type_filter: An optional filtering rule to match the 'event_type' property of an event.

          group_keys: Property names that are used to group usage costs on an invoice. Each entry
              represents a set of properties used to slice events into distinct buckets.

          property_filters: A list of filters to match events to this billable metric. Each filter defines a
              rule on an event property. All rules must pass for the event to match the
              billable metric.

          sql: The SQL query associated with the billable metric. This field is mutually
              exclusive with aggregation_type, event_type_filter, property_filters,
              aggregation_key, and group_keys. If provided, these other fields must be
              omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/billable-metrics/create",
            body=maybe_transform(
                {
                    "name": name,
                    "aggregation_key": aggregation_key,
                    "aggregation_type": aggregation_type,
                    "custom_fields": custom_fields,
                    "event_type_filter": event_type_filter,
                    "group_keys": group_keys,
                    "property_filters": property_filters,
                    "sql": sql,
                },
                billable_metric_create_params.BillableMetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricCreateResponse,
        )

    def retrieve(
        self,
        *,
        billable_metric_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetricRetrieveResponse:
        """
        Retrieves the complete configuration for a specific billable metric by its ID.
        Use this to review billable metric setup before associating it with products.
        Returns the metric's `name`, `event_type_filter`, `property_filters`,
        `aggregation_type`, `aggregation_key`, `group_keys`, `custom fields`, and
        `SQL query` (if it's a SQL billable metric).

        Important:

        - Archived billable metrics will include an `archived_at` timestamp; they no
          longer process new usage events but remain accessible for historical
          reference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billable_metric_id:
            raise ValueError(f"Expected a non-empty value for `billable_metric_id` but received {billable_metric_id!r}")
        return self._get(
            f"/v1/billable-metrics/{billable_metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricRetrieveResponse,
        )

    def list(
        self,
        *,
        include_archived: bool | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[BillableMetricListResponse]:
        """Retrieves all billable metrics with their complete configurations.

        Use this for
        programmatic discovery and management of billable metrics, such as associating
        metrics to products and auditing for orphaned or archived metrics. Important:
        Archived metrics are excluded by default; use `include_archived`=`true`
        parameter to include them.

        Args:
          include_archived: If true, the list of returned metrics will include archived metrics

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/billable-metrics",
            page=SyncCursorPage[BillableMetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_archived": include_archived,
                        "limit": limit,
                        "next_page": next_page,
                    },
                    billable_metric_list_params.BillableMetricListParams,
                ),
            ),
            model=BillableMetricListResponse,
        )

    def archive(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetricArchiveResponse:
        """Use this endpoint to retire billable metrics that are no longer used.

        After a
        billable metric is archived, that billable metric can no longer be used in any
        new Products to define how that product should be metered. If you archive a
        billable metric that is already associated with a Product, the Product will
        continue to function as usual, metering based on the definition of the archived
        billable metric.

        Archived billable metrics will be returned on the `getBillableMetric` and
        `listBillableMetrics` endpoints with a populated `archived_at` field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/billable-metrics/archive",
            body=maybe_transform({"id": id}, billable_metric_archive_params.BillableMetricArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricArchiveResponse,
        )


class AsyncBillableMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillableMetricsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBillableMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillableMetricsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncBillableMetricsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        aggregation_key: str | Omit = omit,
        aggregation_type: Literal["COUNT", "LATEST", "MAX", "SUM", "UNIQUE"] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        event_type_filter: EventTypeFilter | Omit = omit,
        group_keys: Iterable[SequenceNotStr[str]] | Omit = omit,
        property_filters: Iterable[PropertyFilter] | Omit = omit,
        sql: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetricCreateResponse:
        """
        Create billable metrics programmatically with this endpoint—an essential step in
        configuring your pricing and packaging in Metronome.

        A billable metric is a customizable query that filters and aggregates events
        from your event stream. These metrics are continuously tracked as usage data
        enters Metronome through the ingestion pipeline. The ingestion process
        transforms raw usage data into actionable pricing metrics, enabling accurate
        metering and billing for your products.

        ### Use this endpoint to:

        - Create individual or multiple billable metrics as part of a setup workflow.
        - Automate the entire pricing configuration process, from metric creation to
          customer contract setup.
        - Define metrics using either standard filtering/aggregation or a custom SQL
          query.

        ### Key response fields:

        - The ID of the billable metric that was created
        - The created billable metric will be available to be used in Products, usage
          endpoints, and alerts.

        ### Usage guidelines:

        - Metrics defined using standard filtering and aggregation are Streaming
          billable metrics, which have been optimized for ultra low latency and high
          throughput workflows.
        - Use SQL billable metrics if you require more flexible aggregation options.

        Args:
          name: The display name of the billable metric.

          aggregation_key: Specifies the type of aggregation performed on matching events. Required if
              `sql` is not provided.

          aggregation_type: Specifies the type of aggregation performed on matching events.

          custom_fields: Custom fields to attach to the billable metric.

          event_type_filter: An optional filtering rule to match the 'event_type' property of an event.

          group_keys: Property names that are used to group usage costs on an invoice. Each entry
              represents a set of properties used to slice events into distinct buckets.

          property_filters: A list of filters to match events to this billable metric. Each filter defines a
              rule on an event property. All rules must pass for the event to match the
              billable metric.

          sql: The SQL query associated with the billable metric. This field is mutually
              exclusive with aggregation_type, event_type_filter, property_filters,
              aggregation_key, and group_keys. If provided, these other fields must be
              omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/billable-metrics/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "aggregation_key": aggregation_key,
                    "aggregation_type": aggregation_type,
                    "custom_fields": custom_fields,
                    "event_type_filter": event_type_filter,
                    "group_keys": group_keys,
                    "property_filters": property_filters,
                    "sql": sql,
                },
                billable_metric_create_params.BillableMetricCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricCreateResponse,
        )

    async def retrieve(
        self,
        *,
        billable_metric_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetricRetrieveResponse:
        """
        Retrieves the complete configuration for a specific billable metric by its ID.
        Use this to review billable metric setup before associating it with products.
        Returns the metric's `name`, `event_type_filter`, `property_filters`,
        `aggregation_type`, `aggregation_key`, `group_keys`, `custom fields`, and
        `SQL query` (if it's a SQL billable metric).

        Important:

        - Archived billable metrics will include an `archived_at` timestamp; they no
          longer process new usage events but remain accessible for historical
          reference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billable_metric_id:
            raise ValueError(f"Expected a non-empty value for `billable_metric_id` but received {billable_metric_id!r}")
        return await self._get(
            f"/v1/billable-metrics/{billable_metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricRetrieveResponse,
        )

    def list(
        self,
        *,
        include_archived: bool | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[BillableMetricListResponse, AsyncCursorPage[BillableMetricListResponse]]:
        """Retrieves all billable metrics with their complete configurations.

        Use this for
        programmatic discovery and management of billable metrics, such as associating
        metrics to products and auditing for orphaned or archived metrics. Important:
        Archived metrics are excluded by default; use `include_archived`=`true`
        parameter to include them.

        Args:
          include_archived: If true, the list of returned metrics will include archived metrics

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/billable-metrics",
            page=AsyncCursorPage[BillableMetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_archived": include_archived,
                        "limit": limit,
                        "next_page": next_page,
                    },
                    billable_metric_list_params.BillableMetricListParams,
                ),
            ),
            model=BillableMetricListResponse,
        )

    async def archive(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BillableMetricArchiveResponse:
        """Use this endpoint to retire billable metrics that are no longer used.

        After a
        billable metric is archived, that billable metric can no longer be used in any
        new Products to define how that product should be metered. If you archive a
        billable metric that is already associated with a Product, the Product will
        continue to function as usual, metering based on the definition of the archived
        billable metric.

        Archived billable metrics will be returned on the `getBillableMetric` and
        `listBillableMetrics` endpoints with a populated `archived_at` field.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/billable-metrics/archive",
            body=await async_maybe_transform({"id": id}, billable_metric_archive_params.BillableMetricArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricArchiveResponse,
        )


class BillableMetricsResourceWithRawResponse:
    def __init__(self, billable_metrics: BillableMetricsResource) -> None:
        self._billable_metrics = billable_metrics

        self.create = to_raw_response_wrapper(
            billable_metrics.create,
        )
        self.retrieve = to_raw_response_wrapper(
            billable_metrics.retrieve,
        )
        self.list = to_raw_response_wrapper(
            billable_metrics.list,
        )
        self.archive = to_raw_response_wrapper(
            billable_metrics.archive,
        )


class AsyncBillableMetricsResourceWithRawResponse:
    def __init__(self, billable_metrics: AsyncBillableMetricsResource) -> None:
        self._billable_metrics = billable_metrics

        self.create = async_to_raw_response_wrapper(
            billable_metrics.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            billable_metrics.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            billable_metrics.list,
        )
        self.archive = async_to_raw_response_wrapper(
            billable_metrics.archive,
        )


class BillableMetricsResourceWithStreamingResponse:
    def __init__(self, billable_metrics: BillableMetricsResource) -> None:
        self._billable_metrics = billable_metrics

        self.create = to_streamed_response_wrapper(
            billable_metrics.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            billable_metrics.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            billable_metrics.list,
        )
        self.archive = to_streamed_response_wrapper(
            billable_metrics.archive,
        )


class AsyncBillableMetricsResourceWithStreamingResponse:
    def __init__(self, billable_metrics: AsyncBillableMetricsResource) -> None:
        self._billable_metrics = billable_metrics

        self.create = async_to_streamed_response_wrapper(
            billable_metrics.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            billable_metrics.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            billable_metrics.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            billable_metrics.archive,
        )
