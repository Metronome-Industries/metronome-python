# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal

import httpx

from ..types import (
    billable_metric_list_params,
    billable_metric_create_params,
    billable_metric_archive_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.billable_metric_list_response import BillableMetricListResponse
from ..types.billable_metric_create_response import BillableMetricCreateResponse
from ..types.billable_metric_archive_response import BillableMetricArchiveResponse
from ..types.billable_metric_retrieve_response import BillableMetricRetrieveResponse

__all__ = ["BillableMetricsResource", "AsyncBillableMetricsResource"]


class BillableMetricsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillableMetricsResourceWithRawResponse:
        return BillableMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillableMetricsResourceWithStreamingResponse:
        return BillableMetricsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        aggregation_type: Literal[
            "count",
            "Count",
            "COUNT",
            "latest",
            "Latest",
            "LATEST",
            "max",
            "Max",
            "MAX",
            "sum",
            "Sum",
            "SUM",
            "unique",
            "Unique",
            "UNIQUE",
        ],
        name: str,
        aggregation_key: str | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        event_type_filter: billable_metric_create_params.EventTypeFilter | NotGiven = NOT_GIVEN,
        group_keys: Iterable[List[str]] | NotGiven = NOT_GIVEN,
        property_filters: Iterable[billable_metric_create_params.PropertyFilter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillableMetricCreateResponse:
        """
        Creates a new Billable Metric.

        Args:
          aggregation_type: Specifies the type of aggregation performed on matching events.

          name: The display name of the billable metric.

          aggregation_key: A key that specifies which property of the event is used to aggregate data. This
              key must be one of the property filter names and is not applicable when the
              aggregation type is 'count'.

          custom_fields: Custom fields to attach to the billable metric.

          event_type_filter: An optional filtering rule to match the 'event_type' property of an event.

          group_keys: Property names that are used to group usage costs on an invoice. Each entry
              represents a set of properties used to slice events into distinct buckets.

          property_filters: A list of filters to match events to this billable metric. Each filter defines a
              rule on an event property. All rules must pass for the event to match the
              billable metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billable-metrics/create",
            body=maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "name": name,
                    "aggregation_key": aggregation_key,
                    "custom_fields": custom_fields,
                    "event_type_filter": event_type_filter,
                    "group_keys": group_keys,
                    "property_filters": property_filters,
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
        billable_metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillableMetricRetrieveResponse:
        """
        Get a billable metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billable_metric_id:
            raise ValueError(f"Expected a non-empty value for `billable_metric_id` but received {billable_metric_id!r}")
        return self._get(
            f"/billable-metrics/{billable_metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricRetrieveResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        on_current_plan: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[BillableMetricListResponse]:
        """
        Get all billable metrics for a given customer.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          on_current_plan: If true, the list of metrics will be filtered to just ones that are on the
              customer's current plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/billable-metrics",
            page=SyncCursorPage[BillableMetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                        "on_current_plan": on_current_plan,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillableMetricArchiveResponse:
        """
        Archive an existing billable metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/billable-metrics/archive",
            body=maybe_transform({"id": id}, billable_metric_archive_params.BillableMetricArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricArchiveResponse,
        )


class AsyncBillableMetricsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillableMetricsResourceWithRawResponse:
        return AsyncBillableMetricsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillableMetricsResourceWithStreamingResponse:
        return AsyncBillableMetricsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        aggregation_type: Literal[
            "count",
            "Count",
            "COUNT",
            "latest",
            "Latest",
            "LATEST",
            "max",
            "Max",
            "MAX",
            "sum",
            "Sum",
            "SUM",
            "unique",
            "Unique",
            "UNIQUE",
        ],
        name: str,
        aggregation_key: str | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        event_type_filter: billable_metric_create_params.EventTypeFilter | NotGiven = NOT_GIVEN,
        group_keys: Iterable[List[str]] | NotGiven = NOT_GIVEN,
        property_filters: Iterable[billable_metric_create_params.PropertyFilter] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillableMetricCreateResponse:
        """
        Creates a new Billable Metric.

        Args:
          aggregation_type: Specifies the type of aggregation performed on matching events.

          name: The display name of the billable metric.

          aggregation_key: A key that specifies which property of the event is used to aggregate data. This
              key must be one of the property filter names and is not applicable when the
              aggregation type is 'count'.

          custom_fields: Custom fields to attach to the billable metric.

          event_type_filter: An optional filtering rule to match the 'event_type' property of an event.

          group_keys: Property names that are used to group usage costs on an invoice. Each entry
              represents a set of properties used to slice events into distinct buckets.

          property_filters: A list of filters to match events to this billable metric. Each filter defines a
              rule on an event property. All rules must pass for the event to match the
              billable metric.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billable-metrics/create",
            body=await async_maybe_transform(
                {
                    "aggregation_type": aggregation_type,
                    "name": name,
                    "aggregation_key": aggregation_key,
                    "custom_fields": custom_fields,
                    "event_type_filter": event_type_filter,
                    "group_keys": group_keys,
                    "property_filters": property_filters,
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
        billable_metric_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillableMetricRetrieveResponse:
        """
        Get a billable metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not billable_metric_id:
            raise ValueError(f"Expected a non-empty value for `billable_metric_id` but received {billable_metric_id!r}")
        return await self._get(
            f"/billable-metrics/{billable_metric_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillableMetricRetrieveResponse,
        )

    def list(
        self,
        customer_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        on_current_plan: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BillableMetricListResponse, AsyncCursorPage[BillableMetricListResponse]]:
        """
        Get all billable metrics for a given customer.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          on_current_plan: If true, the list of metrics will be filtered to just ones that are on the
              customer's current plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/billable-metrics",
            page=AsyncCursorPage[BillableMetricListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                        "on_current_plan": on_current_plan,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillableMetricArchiveResponse:
        """
        Archive an existing billable metric.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/billable-metrics/archive",
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
