# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ....types.v1.customers import alert_list_params, alert_reset_params, alert_retrieve_params
from ....types.v1.customers.alert_list_response import AlertListResponse
from ....types.v1.customers.alert_retrieve_response import AlertRetrieveResponse

__all__ = ["AlertsResource", "AsyncAlertsResource"]


class AlertsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AlertsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        alert_id: str,
        customer_id: str,
        plans_or_contracts: Literal["PLANS", "CONTRACTS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertRetrieveResponse:
        """
        Get the customer alert status and alert information for the specified customer
        and alert

        Args:
          alert_id: The Metronome ID of the alert

          customer_id: The Metronome ID of the customer

          plans_or_contracts: When parallel alerts are enabled during migration, this flag denotes whether to
              fetch alerts for plans or contracts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customer-alerts/get",
            body=maybe_transform(
                {
                    "alert_id": alert_id,
                    "customer_id": customer_id,
                    "plans_or_contracts": plans_or_contracts,
                },
                alert_retrieve_params.AlertRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        next_page: str | NotGiven = NOT_GIVEN,
        alert_statuses: List[Literal["ENABLED", "DISABLED", "ARCHIVED"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertListResponse:
        """
        Fetch all customer alert statuses and alert information for a customer

        Args:
          customer_id: The Metronome ID of the customer

          next_page: Cursor that indicates where the next page of results should start.

          alert_statuses: Optionally filter by alert status. If absent, only enabled alerts will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customer-alerts/list",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "alert_statuses": alert_statuses,
                },
                alert_list_params.AlertListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"next_page": next_page}, alert_list_params.AlertListParams),
            ),
            cast_to=AlertListResponse,
        )

    def reset(
        self,
        *,
        alert_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Reset state for an alert by customer id and force re-evaluation

        Args:
          alert_id: The Metronome ID of the alert

          customer_id: The Metronome ID of the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/customer-alerts/reset",
            body=maybe_transform(
                {
                    "alert_id": alert_id,
                    "customer_id": customer_id,
                },
                alert_reset_params.AlertResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAlertsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlertsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlertsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlertsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncAlertsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        alert_id: str,
        customer_id: str,
        plans_or_contracts: Literal["PLANS", "CONTRACTS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertRetrieveResponse:
        """
        Get the customer alert status and alert information for the specified customer
        and alert

        Args:
          alert_id: The Metronome ID of the alert

          customer_id: The Metronome ID of the customer

          plans_or_contracts: When parallel alerts are enabled during migration, this flag denotes whether to
              fetch alerts for plans or contracts.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customer-alerts/get",
            body=await async_maybe_transform(
                {
                    "alert_id": alert_id,
                    "customer_id": customer_id,
                    "plans_or_contracts": plans_or_contracts,
                },
                alert_retrieve_params.AlertRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertRetrieveResponse,
        )

    async def list(
        self,
        *,
        customer_id: str,
        next_page: str | NotGiven = NOT_GIVEN,
        alert_statuses: List[Literal["ENABLED", "DISABLED", "ARCHIVED"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertListResponse:
        """
        Fetch all customer alert statuses and alert information for a customer

        Args:
          customer_id: The Metronome ID of the customer

          next_page: Cursor that indicates where the next page of results should start.

          alert_statuses: Optionally filter by alert status. If absent, only enabled alerts will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customer-alerts/list",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "alert_statuses": alert_statuses,
                },
                alert_list_params.AlertListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"next_page": next_page}, alert_list_params.AlertListParams),
            ),
            cast_to=AlertListResponse,
        )

    async def reset(
        self,
        *,
        alert_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Reset state for an alert by customer id and force re-evaluation

        Args:
          alert_id: The Metronome ID of the alert

          customer_id: The Metronome ID of the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/customer-alerts/reset",
            body=await async_maybe_transform(
                {
                    "alert_id": alert_id,
                    "customer_id": customer_id,
                },
                alert_reset_params.AlertResetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AlertsResourceWithRawResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            alerts.list,
        )
        self.reset = to_raw_response_wrapper(
            alerts.reset,
        )


class AsyncAlertsResourceWithRawResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = async_to_raw_response_wrapper(
            alerts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            alerts.list,
        )
        self.reset = async_to_raw_response_wrapper(
            alerts.reset,
        )


class AlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            alerts.list,
        )
        self.reset = to_streamed_response_wrapper(
            alerts.reset,
        )


class AsyncAlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.retrieve = async_to_streamed_response_wrapper(
            alerts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            alerts.list,
        )
        self.reset = async_to_streamed_response_wrapper(
            alerts.reset,
        )
