# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import alert_create_params, alert_archive_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.alert_create_response import AlertCreateResponse
from ...types.v1.alert_archive_response import AlertArchiveResponse

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

    def create(
        self,
        *,
        alert_type: Literal[
            "low_credit_balance_reached",
            "spend_threshold_reached",
            "monthly_invoice_total_spend_threshold_reached",
            "low_remaining_days_in_plan_reached",
            "low_remaining_credit_percentage_reached",
            "usage_threshold_reached",
            "low_remaining_days_for_commit_segment_reached",
            "low_remaining_commit_balance_reached",
            "low_remaining_commit_percentage_reached",
            "low_remaining_days_for_contract_credit_segment_reached",
            "low_remaining_contract_credit_balance_reached",
            "low_remaining_contract_credit_percentage_reached",
            "low_remaining_contract_credit_and_commit_balance_reached",
            "invoice_total_reached",
            "low_remaining_seat_balance_reached",
        ],
        name: str,
        threshold: float,
        billable_metric_id: str | Omit = omit,
        credit_grant_type_filters: SequenceNotStr[str] | Omit = omit,
        credit_type_id: str | Omit = omit,
        custom_field_filters: Iterable[alert_create_params.CustomFieldFilter] | Omit = omit,
        customer_id: str | Omit = omit,
        evaluate_on_create: bool | Omit = omit,
        group_values: Iterable[alert_create_params.GroupValue] | Omit = omit,
        invoice_types_filter: SequenceNotStr[str] | Omit = omit,
        plan_id: str | Omit = omit,
        seat_filter: alert_create_params.SeatFilter | Omit = omit,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertCreateResponse:
        """
        Create a new threshold notification to monitor customer spending, balances, and
        billing metrics in real-time. Metronome's notification system provides
        industry-leading speed with immediate evaluation capabilities, enabling you to
        proactively manage customer accounts and prevent revenue leakage.

        This endpoint creates configurable threshold notifications that continuously
        monitor various billing thresholds including spend limits, credit balances,
        commitment utilization, and invoice totals. Threshold notifications can be
        configured globally for all customers or targeted to specific customer accounts.

        ### Use this endpoint to:

        - Proactively monitor customer spending patterns to prevent unexpected overages
          or credit exhaustion
        - Automate notifications when customers approach commitment limits or credit
          thresholds
        - Enable real-time intervention for accounts at risk of churn or payment issues
        - Scale billing operations by automating threshold-based workflows and
          notifications

        ### Key response fields:

        A successful response returns a CustomerAlert object containing:

        - The threshold notification configuration with its unique ID and current status
        - The customer's evaluation status (ok, in_alarm, or evaluating)
        - Threshold notification metadata including type, threshold values, and update
          timestamps

        ### Usage guidelines:

        - Immediate evaluation: Set `evaluate_on_create` : `true` (default) for instant
          evaluation against existing customers
        - Uniqueness constraints: Each threshold notification must have a unique
          `uniqueness_key` within your organization. Use `release_uniqueness_key` :
          `true` when archiving to reuse keys
        - Notification type requirements: Different threshold notification types require
          specific fields (e.g., `billable_metric_id` for usage notifications,
          `credit_type_id` for credit-based threshold notifications)
        - Webhook delivery: Threshold notifications trigger webhook notifications for
          real-time integration with your systems. Configure webhook endpoints before
          creating threshold notifications
        - Performance at scale: Metronome's event-driven architecture processes
          threshold notification evaluations in real-time as usage events stream in,
          unlike competitors who rely on periodic polling or batch evaluation cycles

        Args:
          alert_type: Type of the threshold notification

          name: Name of the threshold notification

          threshold: Threshold value of the notification policy. Depending upon the notification
              type, this number may represent a financial amount, the days remaining, or a
              percentage reached.

          billable_metric_id: For threshold notifications of type `usage_threshold_reached`, specifies which
              billable metric to track the usage for.

          credit_grant_type_filters: An array of strings, representing a way to filter the credit grant this
              threshold notification applies to, by looking at the credit_grant_type field on
              the credit grant. This field is only defined for CreditPercentage and
              CreditBalance notifications

          credit_type_id: ID of the credit's currency, defaults to USD. If the specific notification type
              requires a pricing unit/currency, find the ID in the
              [Metronome app](https://app.metronome.com/offering/pricing-units).

          custom_field_filters: A list of custom field filters for threshold notification types that support
              advanced filtering. Only present for contract invoices.

          customer_id: If provided, will create this threshold notification for this specific customer.
              To create a notification for all customers, do not specify a `customer_id`.

          evaluate_on_create: If true, the threshold notification will evaluate immediately on customers that
              already meet the notification threshold. If false, it will only evaluate on
              future customers that trigger the threshold. Defaults to true.

          group_values: Only present for `spend_threshold_reached` notifications. Scope notification to
              a specific group key on individual line items.

          invoice_types_filter: Only supported for invoice_total_reached threshold notifications. A list of
              invoice types to evaluate.

          plan_id: If provided, will create this threshold notification for this specific plan. To
              create a notification for all customers, do not specify a `plan_id`.

          seat_filter: Required for `low_remaining_seat_balance_reached` notifications. The alert is
              scoped to this seat group key-value pair.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/alerts/create",
            body=maybe_transform(
                {
                    "alert_type": alert_type,
                    "name": name,
                    "threshold": threshold,
                    "billable_metric_id": billable_metric_id,
                    "credit_grant_type_filters": credit_grant_type_filters,
                    "credit_type_id": credit_type_id,
                    "custom_field_filters": custom_field_filters,
                    "customer_id": customer_id,
                    "evaluate_on_create": evaluate_on_create,
                    "group_values": group_values,
                    "invoice_types_filter": invoice_types_filter,
                    "plan_id": plan_id,
                    "seat_filter": seat_filter,
                    "uniqueness_key": uniqueness_key,
                },
                alert_create_params.AlertCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertCreateResponse,
        )

    def archive(
        self,
        *,
        id: str,
        release_uniqueness_key: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertArchiveResponse:
        """
        Permanently disable a threshold notification and remove it from active
        monitoring across all customers. Archived threshold notifications stop
        evaluating immediately and can optionally release their uniqueness key for reuse
        in future threshold notification configurations.

        ### Use this endpoint to:

        - Decommission threshold notifications that are no longer needed
        - Clean up test or deprecated threshold notification configurations
        - Free up uniqueness keys for reuse with new threshold notifications
        - Stop threshold notification evaluations without losing historical
          configuration data
        - Disable outdated monitoring rules during pricing model transitions

        ### Key response fields:

        - data: Object containing the archived threshold notification's ID

        ### Usage guidelines:

        - Irreversible for evaluation: Archived threshold notifications cannot be
          re-enabled; create a new threshold notification to resume monitoring
        - Uniqueness key handling: Set `release_uniqueness_key` : `true` to reuse the
          key in future threshold notifications
        - Immediate effect: Threshold notification evaluation stops instantly across all
          customers
        - Historical preservation: Archive operation maintains threshold notification
          history and configuration for compliance and auditing

        Args:
          id: The Metronome ID of the threshold notification

          release_uniqueness_key: If true, resets the uniqueness key on this threshold notification so it can be
              re-used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/alerts/archive",
            body=maybe_transform(
                {
                    "id": id,
                    "release_uniqueness_key": release_uniqueness_key,
                },
                alert_archive_params.AlertArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertArchiveResponse,
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

    async def create(
        self,
        *,
        alert_type: Literal[
            "low_credit_balance_reached",
            "spend_threshold_reached",
            "monthly_invoice_total_spend_threshold_reached",
            "low_remaining_days_in_plan_reached",
            "low_remaining_credit_percentage_reached",
            "usage_threshold_reached",
            "low_remaining_days_for_commit_segment_reached",
            "low_remaining_commit_balance_reached",
            "low_remaining_commit_percentage_reached",
            "low_remaining_days_for_contract_credit_segment_reached",
            "low_remaining_contract_credit_balance_reached",
            "low_remaining_contract_credit_percentage_reached",
            "low_remaining_contract_credit_and_commit_balance_reached",
            "invoice_total_reached",
            "low_remaining_seat_balance_reached",
        ],
        name: str,
        threshold: float,
        billable_metric_id: str | Omit = omit,
        credit_grant_type_filters: SequenceNotStr[str] | Omit = omit,
        credit_type_id: str | Omit = omit,
        custom_field_filters: Iterable[alert_create_params.CustomFieldFilter] | Omit = omit,
        customer_id: str | Omit = omit,
        evaluate_on_create: bool | Omit = omit,
        group_values: Iterable[alert_create_params.GroupValue] | Omit = omit,
        invoice_types_filter: SequenceNotStr[str] | Omit = omit,
        plan_id: str | Omit = omit,
        seat_filter: alert_create_params.SeatFilter | Omit = omit,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertCreateResponse:
        """
        Create a new threshold notification to monitor customer spending, balances, and
        billing metrics in real-time. Metronome's notification system provides
        industry-leading speed with immediate evaluation capabilities, enabling you to
        proactively manage customer accounts and prevent revenue leakage.

        This endpoint creates configurable threshold notifications that continuously
        monitor various billing thresholds including spend limits, credit balances,
        commitment utilization, and invoice totals. Threshold notifications can be
        configured globally for all customers or targeted to specific customer accounts.

        ### Use this endpoint to:

        - Proactively monitor customer spending patterns to prevent unexpected overages
          or credit exhaustion
        - Automate notifications when customers approach commitment limits or credit
          thresholds
        - Enable real-time intervention for accounts at risk of churn or payment issues
        - Scale billing operations by automating threshold-based workflows and
          notifications

        ### Key response fields:

        A successful response returns a CustomerAlert object containing:

        - The threshold notification configuration with its unique ID and current status
        - The customer's evaluation status (ok, in_alarm, or evaluating)
        - Threshold notification metadata including type, threshold values, and update
          timestamps

        ### Usage guidelines:

        - Immediate evaluation: Set `evaluate_on_create` : `true` (default) for instant
          evaluation against existing customers
        - Uniqueness constraints: Each threshold notification must have a unique
          `uniqueness_key` within your organization. Use `release_uniqueness_key` :
          `true` when archiving to reuse keys
        - Notification type requirements: Different threshold notification types require
          specific fields (e.g., `billable_metric_id` for usage notifications,
          `credit_type_id` for credit-based threshold notifications)
        - Webhook delivery: Threshold notifications trigger webhook notifications for
          real-time integration with your systems. Configure webhook endpoints before
          creating threshold notifications
        - Performance at scale: Metronome's event-driven architecture processes
          threshold notification evaluations in real-time as usage events stream in,
          unlike competitors who rely on periodic polling or batch evaluation cycles

        Args:
          alert_type: Type of the threshold notification

          name: Name of the threshold notification

          threshold: Threshold value of the notification policy. Depending upon the notification
              type, this number may represent a financial amount, the days remaining, or a
              percentage reached.

          billable_metric_id: For threshold notifications of type `usage_threshold_reached`, specifies which
              billable metric to track the usage for.

          credit_grant_type_filters: An array of strings, representing a way to filter the credit grant this
              threshold notification applies to, by looking at the credit_grant_type field on
              the credit grant. This field is only defined for CreditPercentage and
              CreditBalance notifications

          credit_type_id: ID of the credit's currency, defaults to USD. If the specific notification type
              requires a pricing unit/currency, find the ID in the
              [Metronome app](https://app.metronome.com/offering/pricing-units).

          custom_field_filters: A list of custom field filters for threshold notification types that support
              advanced filtering. Only present for contract invoices.

          customer_id: If provided, will create this threshold notification for this specific customer.
              To create a notification for all customers, do not specify a `customer_id`.

          evaluate_on_create: If true, the threshold notification will evaluate immediately on customers that
              already meet the notification threshold. If false, it will only evaluate on
              future customers that trigger the threshold. Defaults to true.

          group_values: Only present for `spend_threshold_reached` notifications. Scope notification to
              a specific group key on individual line items.

          invoice_types_filter: Only supported for invoice_total_reached threshold notifications. A list of
              invoice types to evaluate.

          plan_id: If provided, will create this threshold notification for this specific plan. To
              create a notification for all customers, do not specify a `plan_id`.

          seat_filter: Required for `low_remaining_seat_balance_reached` notifications. The alert is
              scoped to this seat group key-value pair.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/alerts/create",
            body=await async_maybe_transform(
                {
                    "alert_type": alert_type,
                    "name": name,
                    "threshold": threshold,
                    "billable_metric_id": billable_metric_id,
                    "credit_grant_type_filters": credit_grant_type_filters,
                    "credit_type_id": credit_type_id,
                    "custom_field_filters": custom_field_filters,
                    "customer_id": customer_id,
                    "evaluate_on_create": evaluate_on_create,
                    "group_values": group_values,
                    "invoice_types_filter": invoice_types_filter,
                    "plan_id": plan_id,
                    "seat_filter": seat_filter,
                    "uniqueness_key": uniqueness_key,
                },
                alert_create_params.AlertCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertCreateResponse,
        )

    async def archive(
        self,
        *,
        id: str,
        release_uniqueness_key: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlertArchiveResponse:
        """
        Permanently disable a threshold notification and remove it from active
        monitoring across all customers. Archived threshold notifications stop
        evaluating immediately and can optionally release their uniqueness key for reuse
        in future threshold notification configurations.

        ### Use this endpoint to:

        - Decommission threshold notifications that are no longer needed
        - Clean up test or deprecated threshold notification configurations
        - Free up uniqueness keys for reuse with new threshold notifications
        - Stop threshold notification evaluations without losing historical
          configuration data
        - Disable outdated monitoring rules during pricing model transitions

        ### Key response fields:

        - data: Object containing the archived threshold notification's ID

        ### Usage guidelines:

        - Irreversible for evaluation: Archived threshold notifications cannot be
          re-enabled; create a new threshold notification to resume monitoring
        - Uniqueness key handling: Set `release_uniqueness_key` : `true` to reuse the
          key in future threshold notifications
        - Immediate effect: Threshold notification evaluation stops instantly across all
          customers
        - Historical preservation: Archive operation maintains threshold notification
          history and configuration for compliance and auditing

        Args:
          id: The Metronome ID of the threshold notification

          release_uniqueness_key: If true, resets the uniqueness key on this threshold notification so it can be
              re-used

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/alerts/archive",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "release_uniqueness_key": release_uniqueness_key,
                },
                alert_archive_params.AlertArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlertArchiveResponse,
        )


class AlertsResourceWithRawResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.create = to_raw_response_wrapper(
            alerts.create,
        )
        self.archive = to_raw_response_wrapper(
            alerts.archive,
        )


class AsyncAlertsResourceWithRawResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.create = async_to_raw_response_wrapper(
            alerts.create,
        )
        self.archive = async_to_raw_response_wrapper(
            alerts.archive,
        )


class AlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AlertsResource) -> None:
        self._alerts = alerts

        self.create = to_streamed_response_wrapper(
            alerts.create,
        )
        self.archive = to_streamed_response_wrapper(
            alerts.archive,
        )


class AsyncAlertsResourceWithStreamingResponse:
    def __init__(self, alerts: AsyncAlertsResource) -> None:
        self._alerts = alerts

        self.create = async_to_streamed_response_wrapper(
            alerts.create,
        )
        self.archive = async_to_streamed_response_wrapper(
            alerts.archive,
        )
