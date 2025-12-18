# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPageWithoutLimit, AsyncCursorPageWithoutLimit
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1.customers import alert_list_params, alert_reset_params, alert_retrieve_params
from ....types.v1.customers.customer_alert import CustomerAlert
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
        group_values: Iterable[alert_retrieve_params.GroupValue] | Omit = omit,
        plans_or_contracts: Literal["PLANS", "CONTRACTS"] | Omit = omit,
        seat_filter: alert_retrieve_params.SeatFilter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertRetrieveResponse:
        """
        Retrieve the real-time evaluation status for a specific threshold
        notification-customer pair. This endpoint provides instant visibility into
        whether a customer has triggered a threshold notification condition, enabling
        you to monitor account health and take proactive action based on current
        threshold notification states.

        ### Use this endpoint to:

        - Check if a specific customer is currently violating an threshold notification
          (`in_alarm` status)
        - Verify threshold notification configuration details and threshold values for a
          customer
        - Monitor the evaluation state of newly created or recently modified threshold
          notification
        - Build dashboards or automated workflows that respond to specific threshold
          notification conditions
        - Validate threshold notification behavior before deploying to production
          customers
        - Integrate threshold notification status checks into customer support tools or
          admin interfaces

        ### Key response fields:

        A CustomerAlert object containing:

        - `customer_status`: The current evaluation state

        - `ok` - Customer is within acceptable thresholds
        - `in_alarm` - Customer has breached the threshold for the notification
        - `evaluating` - Notification is currently being evaluated (typically during
          initial setup)
        - `null` - Notification has been archived
        - `triggered_by`: Additional context about what caused the notification to
          trigger (when applicable)
        - alert: Complete threshold notification configuration including:
          - Notification ID, name, and type
          - Current threshold values and credit type information
          - Notification status (enabled, disabled, or archived)
          - Last update timestamp
          - Any applied filters (credit grant types, custom fields, group values)

        ### Usage guidelines:

        - Customer status: Returns the current evaluation state, not historical data.
          For threshold notification history, use webhook notifications or event logs
        - Required parameters: Both customer_id and alert_id must be valid UUIDs that
          exist in your organization
        - Archived notifications: Returns null for customer_status if the notification
          has been archived, but still includes the notification configuration details
        - Performance considerations: This endpoint queries live evaluation state,
          making it ideal for real-time monitoring but not for bulk status checks
        - Integration patterns: Best used for on-demand status checks in response to
          user actions or as part of targeted monitoring workflows
        - Error handling: Returns 404 if either the customer or alert_id doesn't exist
          or isn't accessible to your organization

        Args:
          alert_id: The Metronome ID of the threshold notification

          customer_id: The Metronome ID of the customer

          group_values: Only present for `spend_threshold_reached` notifications. Retrieve the
              notification for a specific group key-value pair.

          plans_or_contracts: When parallel threshold notifications are enabled during migration, this flag
              denotes whether to fetch notifications for plans or contracts.

          seat_filter: Only allowed for `low_remaining_seat_balance_reached` notifications. This
              filters alerts by the seat group key-value pair.

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
                    "group_values": group_values,
                    "plans_or_contracts": plans_or_contracts,
                    "seat_filter": seat_filter,
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
        next_page: str | Omit = omit,
        alert_statuses: List[Literal["ENABLED", "DISABLED", "ARCHIVED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPageWithoutLimit[CustomerAlert]:
        """
        Retrieve all threshold notification configurations and their current statuses
        for a specific customer in a single API call. This endpoint provides a
        comprehensive view of all threshold notification monitoring a customer account.

        ### Use this endpoint to:

        - Display all active threshold notifications for a customer in dashboards or
          admin panels
        - Quickly identify which threshold notifications a customer is currently
          triggering
        - Audit threshold notification coverage for specific accounts
        - Filter threshold notifications by status (enabled, disabled, or archived)

        ### Key response fields:

        - data: Array of CustomerAlert objects, each containing:
          - Current evaluation status (`ok`, `in_alarm`, `evaluating`, or `null`)
          - Complete threshold notification configuration and threshold details
          - Threshold notification metadata including type, name, and last update time
        - next_page: Pagination cursor for retrieving additional results

        ### Usage guidelines:

        - Default behavior: Returns only enabled threshold notifications unless
          `alert_statuses` filter is specified
        - Pagination: Use the `next_page` cursor to retrieve all results for customers
          with many notifications
        - Performance: Efficiently retrieves multiple threshold notification statuses in
          a single request instead of making individual calls
        - Filtering: Pass the `alert_statuses` array to include disabled or archived
          threshold notifications in results

        Args:
          customer_id: The Metronome ID of the customer

          next_page: Cursor that indicates where the next page of results should start.

          alert_statuses: Optionally filter by threshold notification status. If absent, only enabled
              notifications will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customer-alerts/list",
            page=SyncCursorPageWithoutLimit[CustomerAlert],
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
            model=CustomerAlert,
            method="post",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Force an immediate re-evaluation of a specific threshold notification for a
        customer, clearing any previous state and triggering a fresh assessment against
        current thresholds. This endpoint ensures threshold notification accuracy after
        configuration changes or data corrections.

        ### Use this endpoint to:

        - Clear false positive threshold notifications after fixing data issues
        - Re-evaluate threshold notifications after adjusting customer balances or
          credits
        - Test threshold notification behavior during development and debugging
        - Resolve stuck threshold notification that may be in an incorrect state
        - Trigger immediate evaluation after threshold modifications

        ### Key response fields:

        - 200 Success: Confirmation that the threshold notification has been reset and
          re-evaluation initiated
        - No response body is returned - the operation completes asynchronously

        ### Usage guidelines:

        - Immediate effect: Triggers re-evaluation instantly, which may result in new
          webhook notifications if thresholds are breached
        - State clearing: Removes any cached evaluation state, ensuring a fresh
          assessment
        - Use sparingly: Intended for exceptional cases, not routine operations
        - Asynchronous processing: The reset completes immediately, but re-evaluation
          happens in the background

        Args:
          alert_id: The Metronome ID of the threshold notification

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
        group_values: Iterable[alert_retrieve_params.GroupValue] | Omit = omit,
        plans_or_contracts: Literal["PLANS", "CONTRACTS"] | Omit = omit,
        seat_filter: alert_retrieve_params.SeatFilter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertRetrieveResponse:
        """
        Retrieve the real-time evaluation status for a specific threshold
        notification-customer pair. This endpoint provides instant visibility into
        whether a customer has triggered a threshold notification condition, enabling
        you to monitor account health and take proactive action based on current
        threshold notification states.

        ### Use this endpoint to:

        - Check if a specific customer is currently violating an threshold notification
          (`in_alarm` status)
        - Verify threshold notification configuration details and threshold values for a
          customer
        - Monitor the evaluation state of newly created or recently modified threshold
          notification
        - Build dashboards or automated workflows that respond to specific threshold
          notification conditions
        - Validate threshold notification behavior before deploying to production
          customers
        - Integrate threshold notification status checks into customer support tools or
          admin interfaces

        ### Key response fields:

        A CustomerAlert object containing:

        - `customer_status`: The current evaluation state

        - `ok` - Customer is within acceptable thresholds
        - `in_alarm` - Customer has breached the threshold for the notification
        - `evaluating` - Notification is currently being evaluated (typically during
          initial setup)
        - `null` - Notification has been archived
        - `triggered_by`: Additional context about what caused the notification to
          trigger (when applicable)
        - alert: Complete threshold notification configuration including:
          - Notification ID, name, and type
          - Current threshold values and credit type information
          - Notification status (enabled, disabled, or archived)
          - Last update timestamp
          - Any applied filters (credit grant types, custom fields, group values)

        ### Usage guidelines:

        - Customer status: Returns the current evaluation state, not historical data.
          For threshold notification history, use webhook notifications or event logs
        - Required parameters: Both customer_id and alert_id must be valid UUIDs that
          exist in your organization
        - Archived notifications: Returns null for customer_status if the notification
          has been archived, but still includes the notification configuration details
        - Performance considerations: This endpoint queries live evaluation state,
          making it ideal for real-time monitoring but not for bulk status checks
        - Integration patterns: Best used for on-demand status checks in response to
          user actions or as part of targeted monitoring workflows
        - Error handling: Returns 404 if either the customer or alert_id doesn't exist
          or isn't accessible to your organization

        Args:
          alert_id: The Metronome ID of the threshold notification

          customer_id: The Metronome ID of the customer

          group_values: Only present for `spend_threshold_reached` notifications. Retrieve the
              notification for a specific group key-value pair.

          plans_or_contracts: When parallel threshold notifications are enabled during migration, this flag
              denotes whether to fetch notifications for plans or contracts.

          seat_filter: Only allowed for `low_remaining_seat_balance_reached` notifications. This
              filters alerts by the seat group key-value pair.

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
                    "group_values": group_values,
                    "plans_or_contracts": plans_or_contracts,
                    "seat_filter": seat_filter,
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
        next_page: str | Omit = omit,
        alert_statuses: List[Literal["ENABLED", "DISABLED", "ARCHIVED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerAlert, AsyncCursorPageWithoutLimit[CustomerAlert]]:
        """
        Retrieve all threshold notification configurations and their current statuses
        for a specific customer in a single API call. This endpoint provides a
        comprehensive view of all threshold notification monitoring a customer account.

        ### Use this endpoint to:

        - Display all active threshold notifications for a customer in dashboards or
          admin panels
        - Quickly identify which threshold notifications a customer is currently
          triggering
        - Audit threshold notification coverage for specific accounts
        - Filter threshold notifications by status (enabled, disabled, or archived)

        ### Key response fields:

        - data: Array of CustomerAlert objects, each containing:
          - Current evaluation status (`ok`, `in_alarm`, `evaluating`, or `null`)
          - Complete threshold notification configuration and threshold details
          - Threshold notification metadata including type, name, and last update time
        - next_page: Pagination cursor for retrieving additional results

        ### Usage guidelines:

        - Default behavior: Returns only enabled threshold notifications unless
          `alert_statuses` filter is specified
        - Pagination: Use the `next_page` cursor to retrieve all results for customers
          with many notifications
        - Performance: Efficiently retrieves multiple threshold notification statuses in
          a single request instead of making individual calls
        - Filtering: Pass the `alert_statuses` array to include disabled or archived
          threshold notifications in results

        Args:
          customer_id: The Metronome ID of the customer

          next_page: Cursor that indicates where the next page of results should start.

          alert_statuses: Optionally filter by threshold notification status. If absent, only enabled
              notifications will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customer-alerts/list",
            page=AsyncCursorPageWithoutLimit[CustomerAlert],
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
            model=CustomerAlert,
            method="post",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Force an immediate re-evaluation of a specific threshold notification for a
        customer, clearing any previous state and triggering a fresh assessment against
        current thresholds. This endpoint ensures threshold notification accuracy after
        configuration changes or data corrections.

        ### Use this endpoint to:

        - Clear false positive threshold notifications after fixing data issues
        - Re-evaluate threshold notifications after adjusting customer balances or
          credits
        - Test threshold notification behavior during development and debugging
        - Resolve stuck threshold notification that may be in an incorrect state
        - Trigger immediate evaluation after threshold modifications

        ### Key response fields:

        - 200 Success: Confirmation that the threshold notification has been reset and
          re-evaluation initiated
        - No response body is returned - the operation completes asynchronously

        ### Usage guidelines:

        - Immediate effect: Triggers re-evaluation instantly, which may result in new
          webhook notifications if thresholds are breached
        - State clearing: Removes any cached evaluation state, ensuring a fresh
          assessment
        - Use sparingly: Intended for exceptional cases, not routine operations
        - Asynchronous processing: The reset completes immediately, but re-evaluation
          happens in the background

        Args:
          alert_id: The Metronome ID of the threshold notification

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
