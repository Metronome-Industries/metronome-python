# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1.customers import (
    plan_add_params,
    plan_end_params,
    plan_list_params,
    plan_list_price_adjustments_params,
)
from ....types.v1.customers.plan_add_response import PlanAddResponse
from ....types.v1.customers.plan_end_response import PlanEndResponse
from ....types.v1.customers.plan_list_response import PlanListResponse
from ....types.v1.customers.plan_list_price_adjustments_response import PlanListPriceAdjustmentsResponse

__all__ = ["PlansResource", "AsyncPlansResource"]


class PlansResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return PlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return PlansResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        customer_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PlanListResponse]:
        """List the given customer's plans in reverse-chronological order.

        This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/plans",
            page=SyncCursorPage[PlanListResponse],
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
                    plan_list_params.PlanListParams,
                ),
            ),
            model=PlanListResponse,
        )

    def add(
        self,
        *,
        customer_id: str,
        plan_id: str,
        starting_on: Union[str, datetime],
        ending_before: Union[str, datetime] | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        overage_rate_adjustments: Iterable[plan_add_params.OverageRateAdjustment] | Omit = omit,
        price_adjustments: Iterable[plan_add_params.PriceAdjustment] | Omit = omit,
        trial_spec: plan_add_params.TrialSpec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanAddResponse:
        """Associate an existing customer with a plan for a specified date range.

        See the
        [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
        for details on the price adjustments. This is a Plans (deprecated) endpoint. New
        clients should implement using Contracts.

        Args:
          starting_on: RFC 3339 timestamp for when the plan becomes active for this customer. Must be
              at 0:00 UTC (midnight).

          ending_before: RFC 3339 timestamp for when the plan ends (exclusive) for this customer. Must be
              at 0:00 UTC (midnight).

          net_payment_terms_days: Number of days after issuance of invoice after which the invoice is due (e.g.
              Net 30).

          overage_rate_adjustments: An optional list of overage rates that override the rates of the original plan
              configuration. These new rates will apply to all pricing ramps.

          price_adjustments: A list of price adjustments can be applied on top of the pricing in the plans.
              See the
              [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
              for details.

          trial_spec: A custom trial can be set for the customer's plan. See the
              [trial configuration documentation](https://docs.metronome.com/provisioning/configure-trials/)
              for details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/v1/customers/{customer_id}/plans/add",
            body=maybe_transform(
                {
                    "plan_id": plan_id,
                    "starting_on": starting_on,
                    "ending_before": ending_before,
                    "net_payment_terms_days": net_payment_terms_days,
                    "overage_rate_adjustments": overage_rate_adjustments,
                    "price_adjustments": price_adjustments,
                    "trial_spec": trial_spec,
                },
                plan_add_params.PlanAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanAddResponse,
        )

    def end(
        self,
        *,
        customer_id: str,
        customer_plan_id: str,
        ending_before: Union[str, datetime] | Omit = omit,
        void_invoices: bool | Omit = omit,
        void_stripe_invoices: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanEndResponse:
        """Change the end date of a customer's plan.

        This is a Plans (deprecated) endpoint.
        New clients should implement using Contracts.

        Args:
          ending_before: RFC 3339 timestamp for when the plan ends (exclusive) for this customer. Must be
              at 0:00 UTC (midnight). If not provided, the plan end date will be cleared.

          void_invoices: If true, plan end date can be before the last finalized invoice date. Any
              invoices generated after the plan end date will be voided.

          void_stripe_invoices: Only applicable when void_invoices is set to true. If true, for every invoice
              that is voided we will also attempt to void/delete the stripe invoice (if any).
              Stripe invoices will be voided if finalized or deleted if still in draft state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not customer_plan_id:
            raise ValueError(f"Expected a non-empty value for `customer_plan_id` but received {customer_plan_id!r}")
        return self._post(
            f"/v1/customers/{customer_id}/plans/{customer_plan_id}/end",
            body=maybe_transform(
                {
                    "ending_before": ending_before,
                    "void_invoices": void_invoices,
                    "void_stripe_invoices": void_stripe_invoices,
                },
                plan_end_params.PlanEndParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanEndResponse,
        )

    def list_price_adjustments(
        self,
        *,
        customer_id: str,
        customer_plan_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PlanListPriceAdjustmentsResponse]:
        """Lists a customer plans adjustments.

        See the
        [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
        for details. This is a Plans (deprecated) endpoint. New clients should implement
        using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not customer_plan_id:
            raise ValueError(f"Expected a non-empty value for `customer_plan_id` but received {customer_plan_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments",
            page=SyncCursorPage[PlanListPriceAdjustmentsResponse],
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
                    plan_list_price_adjustments_params.PlanListPriceAdjustmentsParams,
                ),
            ),
            model=PlanListPriceAdjustmentsResponse,
        )


class AsyncPlansResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlansResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlansResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlansResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncPlansResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        customer_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListResponse, AsyncCursorPage[PlanListResponse]]:
        """List the given customer's plans in reverse-chronological order.

        This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/plans",
            page=AsyncCursorPage[PlanListResponse],
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
                    plan_list_params.PlanListParams,
                ),
            ),
            model=PlanListResponse,
        )

    async def add(
        self,
        *,
        customer_id: str,
        plan_id: str,
        starting_on: Union[str, datetime],
        ending_before: Union[str, datetime] | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        overage_rate_adjustments: Iterable[plan_add_params.OverageRateAdjustment] | Omit = omit,
        price_adjustments: Iterable[plan_add_params.PriceAdjustment] | Omit = omit,
        trial_spec: plan_add_params.TrialSpec | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanAddResponse:
        """Associate an existing customer with a plan for a specified date range.

        See the
        [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
        for details on the price adjustments. This is a Plans (deprecated) endpoint. New
        clients should implement using Contracts.

        Args:
          starting_on: RFC 3339 timestamp for when the plan becomes active for this customer. Must be
              at 0:00 UTC (midnight).

          ending_before: RFC 3339 timestamp for when the plan ends (exclusive) for this customer. Must be
              at 0:00 UTC (midnight).

          net_payment_terms_days: Number of days after issuance of invoice after which the invoice is due (e.g.
              Net 30).

          overage_rate_adjustments: An optional list of overage rates that override the rates of the original plan
              configuration. These new rates will apply to all pricing ramps.

          price_adjustments: A list of price adjustments can be applied on top of the pricing in the plans.
              See the
              [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
              for details.

          trial_spec: A custom trial can be set for the customer's plan. See the
              [trial configuration documentation](https://docs.metronome.com/provisioning/configure-trials/)
              for details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/v1/customers/{customer_id}/plans/add",
            body=await async_maybe_transform(
                {
                    "plan_id": plan_id,
                    "starting_on": starting_on,
                    "ending_before": ending_before,
                    "net_payment_terms_days": net_payment_terms_days,
                    "overage_rate_adjustments": overage_rate_adjustments,
                    "price_adjustments": price_adjustments,
                    "trial_spec": trial_spec,
                },
                plan_add_params.PlanAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanAddResponse,
        )

    async def end(
        self,
        *,
        customer_id: str,
        customer_plan_id: str,
        ending_before: Union[str, datetime] | Omit = omit,
        void_invoices: bool | Omit = omit,
        void_stripe_invoices: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanEndResponse:
        """Change the end date of a customer's plan.

        This is a Plans (deprecated) endpoint.
        New clients should implement using Contracts.

        Args:
          ending_before: RFC 3339 timestamp for when the plan ends (exclusive) for this customer. Must be
              at 0:00 UTC (midnight). If not provided, the plan end date will be cleared.

          void_invoices: If true, plan end date can be before the last finalized invoice date. Any
              invoices generated after the plan end date will be voided.

          void_stripe_invoices: Only applicable when void_invoices is set to true. If true, for every invoice
              that is voided we will also attempt to void/delete the stripe invoice (if any).
              Stripe invoices will be voided if finalized or deleted if still in draft state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not customer_plan_id:
            raise ValueError(f"Expected a non-empty value for `customer_plan_id` but received {customer_plan_id!r}")
        return await self._post(
            f"/v1/customers/{customer_id}/plans/{customer_plan_id}/end",
            body=await async_maybe_transform(
                {
                    "ending_before": ending_before,
                    "void_invoices": void_invoices,
                    "void_stripe_invoices": void_stripe_invoices,
                },
                plan_end_params.PlanEndParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanEndResponse,
        )

    def list_price_adjustments(
        self,
        *,
        customer_id: str,
        customer_plan_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListPriceAdjustmentsResponse, AsyncCursorPage[PlanListPriceAdjustmentsResponse]]:
        """Lists a customer plans adjustments.

        See the
        [price adjustments documentation](https://plans-docs.metronome.com/pricing/managing-plans/#price-adjustments)
        for details. This is a Plans (deprecated) endpoint. New clients should implement
        using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not customer_plan_id:
            raise ValueError(f"Expected a non-empty value for `customer_plan_id` but received {customer_plan_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/plans/{customer_plan_id}/priceAdjustments",
            page=AsyncCursorPage[PlanListPriceAdjustmentsResponse],
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
                    plan_list_price_adjustments_params.PlanListPriceAdjustmentsParams,
                ),
            ),
            model=PlanListPriceAdjustmentsResponse,
        )


class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.list = to_raw_response_wrapper(
            plans.list,
        )
        self.add = to_raw_response_wrapper(
            plans.add,
        )
        self.end = to_raw_response_wrapper(
            plans.end,
        )
        self.list_price_adjustments = to_raw_response_wrapper(
            plans.list_price_adjustments,
        )


class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.list = async_to_raw_response_wrapper(
            plans.list,
        )
        self.add = async_to_raw_response_wrapper(
            plans.add,
        )
        self.end = async_to_raw_response_wrapper(
            plans.end,
        )
        self.list_price_adjustments = async_to_raw_response_wrapper(
            plans.list_price_adjustments,
        )


class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.list = to_streamed_response_wrapper(
            plans.list,
        )
        self.add = to_streamed_response_wrapper(
            plans.add,
        )
        self.end = to_streamed_response_wrapper(
            plans.end,
        )
        self.list_price_adjustments = to_streamed_response_wrapper(
            plans.list_price_adjustments,
        )


class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.list = async_to_streamed_response_wrapper(
            plans.list,
        )
        self.add = async_to_streamed_response_wrapper(
            plans.add,
        )
        self.end = async_to_streamed_response_wrapper(
            plans.end,
        )
        self.list_price_adjustments = async_to_streamed_response_wrapper(
            plans.list_price_adjustments,
        )
