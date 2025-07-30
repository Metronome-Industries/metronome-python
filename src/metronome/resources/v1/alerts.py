# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
        ],
        name: str,
        threshold: float,
        billable_metric_id: str | NotGiven = NOT_GIVEN,
        credit_grant_type_filters: List[str] | NotGiven = NOT_GIVEN,
        credit_type_id: str | NotGiven = NOT_GIVEN,
        custom_field_filters: Iterable[alert_create_params.CustomFieldFilter] | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        evaluate_on_create: bool | NotGiven = NOT_GIVEN,
        group_values: Iterable[alert_create_params.GroupValue] | NotGiven = NOT_GIVEN,
        invoice_types_filter: List[str] | NotGiven = NOT_GIVEN,
        plan_id: str | NotGiven = NOT_GIVEN,
        uniqueness_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertCreateResponse:
        """
        Create a new alert

        Args:
          alert_type: Type of the alert

          name: Name of the alert

          threshold: Threshold value of the alert policy. Depending upon the alert type, this number
              may represent a financial amount, the days remaining, or a percentage reached.

          billable_metric_id: For alerts of type `usage_threshold_reached`, specifies which billable metric to
              track the usage for.

          credit_grant_type_filters: An array of strings, representing a way to filter the credit grant this alert
              applies to, by looking at the credit_grant_type field on the credit grant. This
              field is only defined for CreditPercentage and CreditBalance alerts

          credit_type_id: ID of the credit's currency, defaults to USD. If the specific alert type
              requires a pricing unit/currency, find the ID in the
              [Metronome app](https://app.metronome.com/offering/pricing-units).

          custom_field_filters: A list of custom field filters for alert types that support advanced filtering.
              Only present for contract invoices.

          customer_id: If provided, will create this alert for this specific customer. To create an
              alert for all customers, do not specify a `customer_id`.

          evaluate_on_create: If true, the alert will evaluate immediately on customers that already meet the
              alert threshold. If false, it will only evaluate on future customers that
              trigger the alert threshold. Defaults to true.

          group_values: Only present for `spend_threshold_reached` alerts. Scope alert to a specific
              group key on individual line items.

          invoice_types_filter: Only supported for invoice_total_reached alerts. A list of invoice types to
              evaluate.

          plan_id: If provided, will create this alert for this specific plan. To create an alert
              for all customers, do not specify a `plan_id`.

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
        release_uniqueness_key: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertArchiveResponse:
        """
        Archive an existing alert

        Args:
          id: The Metronome ID of the alert

          release_uniqueness_key: If true, resets the uniqueness key on this alert so it can be re-used

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
        ],
        name: str,
        threshold: float,
        billable_metric_id: str | NotGiven = NOT_GIVEN,
        credit_grant_type_filters: List[str] | NotGiven = NOT_GIVEN,
        credit_type_id: str | NotGiven = NOT_GIVEN,
        custom_field_filters: Iterable[alert_create_params.CustomFieldFilter] | NotGiven = NOT_GIVEN,
        customer_id: str | NotGiven = NOT_GIVEN,
        evaluate_on_create: bool | NotGiven = NOT_GIVEN,
        group_values: Iterable[alert_create_params.GroupValue] | NotGiven = NOT_GIVEN,
        invoice_types_filter: List[str] | NotGiven = NOT_GIVEN,
        plan_id: str | NotGiven = NOT_GIVEN,
        uniqueness_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertCreateResponse:
        """
        Create a new alert

        Args:
          alert_type: Type of the alert

          name: Name of the alert

          threshold: Threshold value of the alert policy. Depending upon the alert type, this number
              may represent a financial amount, the days remaining, or a percentage reached.

          billable_metric_id: For alerts of type `usage_threshold_reached`, specifies which billable metric to
              track the usage for.

          credit_grant_type_filters: An array of strings, representing a way to filter the credit grant this alert
              applies to, by looking at the credit_grant_type field on the credit grant. This
              field is only defined for CreditPercentage and CreditBalance alerts

          credit_type_id: ID of the credit's currency, defaults to USD. If the specific alert type
              requires a pricing unit/currency, find the ID in the
              [Metronome app](https://app.metronome.com/offering/pricing-units).

          custom_field_filters: A list of custom field filters for alert types that support advanced filtering.
              Only present for contract invoices.

          customer_id: If provided, will create this alert for this specific customer. To create an
              alert for all customers, do not specify a `customer_id`.

          evaluate_on_create: If true, the alert will evaluate immediately on customers that already meet the
              alert threshold. If false, it will only evaluate on future customers that
              trigger the alert threshold. Defaults to true.

          group_values: Only present for `spend_threshold_reached` alerts. Scope alert to a specific
              group key on individual line items.

          invoice_types_filter: Only supported for invoice_total_reached alerts. A list of invoice types to
              evaluate.

          plan_id: If provided, will create this alert for this specific plan. To create an alert
              for all customers, do not specify a `plan_id`.

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
        release_uniqueness_key: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlertArchiveResponse:
        """
        Archive an existing alert

        Args:
          id: The Metronome ID of the alert

          release_uniqueness_key: If true, resets the uniqueness key on this alert so it can be re-used

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
