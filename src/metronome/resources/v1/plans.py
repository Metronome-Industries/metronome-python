# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ...types.v1 import plan_list_params, plan_list_charges_params, plan_list_customers_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.plan_list_response import PlanListResponse
from ...types.v1.plan_get_details_response import PlanGetDetailsResponse
from ...types.v1.plan_list_charges_response import PlanListChargesResponse
from ...types.v1.plan_list_customers_response import PlanListCustomersResponse

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
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PlanListResponse]:
        """List all available plans.

        This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/plans",
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

    def get_details(
        self,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanGetDetailsResponse:
        """Fetch high level details of a specific plan.

        This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get(
            f"/v1/planDetails/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanGetDetailsResponse,
        )

    def list_charges(
        self,
        *,
        plan_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PlanListChargesResponse]:
        """Fetches a list of charges of a specific plan.

        This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get_api_list(
            f"/v1/planDetails/{plan_id}/charges",
            page=SyncCursorPage[PlanListChargesResponse],
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
                    plan_list_charges_params.PlanListChargesParams,
                ),
            ),
            model=PlanListChargesResponse,
        )

    def list_customers(
        self,
        *,
        plan_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        status: Literal["all", "active", "ended", "upcoming"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PlanListCustomersResponse]:
        """
        Fetches a list of customers on a specific plan (by default, only currently
        active plans are included). This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          status: Status of customers on a given plan. Defaults to `active`.

              - `all` - Return current, past, and upcoming customers of the plan.
              - `active` - Return current customers of the plan.
              - `ended` - Return past customers of the plan.
              - `upcoming` - Return upcoming customers of the plan.

              Multiple statuses can be OR'd together using commas, e.g. `active,ended`.
              **Note:** `ended,upcoming` combination is not yet supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get_api_list(
            f"/v1/planDetails/{plan_id}/customers",
            page=SyncCursorPage[PlanListCustomersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                        "status": status,
                    },
                    plan_list_customers_params.PlanListCustomersParams,
                ),
            ),
            model=PlanListCustomersResponse,
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
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListResponse, AsyncCursorPage[PlanListResponse]]:
        """List all available plans.

        This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/plans",
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

    async def get_details(
        self,
        *,
        plan_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanGetDetailsResponse:
        """Fetch high level details of a specific plan.

        This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return await self._get(
            f"/v1/planDetails/{plan_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanGetDetailsResponse,
        )

    def list_charges(
        self,
        *,
        plan_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListChargesResponse, AsyncCursorPage[PlanListChargesResponse]]:
        """Fetches a list of charges of a specific plan.

        This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get_api_list(
            f"/v1/planDetails/{plan_id}/charges",
            page=AsyncCursorPage[PlanListChargesResponse],
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
                    plan_list_charges_params.PlanListChargesParams,
                ),
            ),
            model=PlanListChargesResponse,
        )

    def list_customers(
        self,
        *,
        plan_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        status: Literal["all", "active", "ended", "upcoming"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PlanListCustomersResponse, AsyncCursorPage[PlanListCustomersResponse]]:
        """
        Fetches a list of customers on a specific plan (by default, only currently
        active plans are included). This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          status: Status of customers on a given plan. Defaults to `active`.

              - `all` - Return current, past, and upcoming customers of the plan.
              - `active` - Return current customers of the plan.
              - `ended` - Return past customers of the plan.
              - `upcoming` - Return upcoming customers of the plan.

              Multiple statuses can be OR'd together using commas, e.g. `active,ended`.
              **Note:** `ended,upcoming` combination is not yet supported.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not plan_id:
            raise ValueError(f"Expected a non-empty value for `plan_id` but received {plan_id!r}")
        return self._get_api_list(
            f"/v1/planDetails/{plan_id}/customers",
            page=AsyncCursorPage[PlanListCustomersResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                        "status": status,
                    },
                    plan_list_customers_params.PlanListCustomersParams,
                ),
            ),
            model=PlanListCustomersResponse,
        )


class PlansResourceWithRawResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.list = to_raw_response_wrapper(
            plans.list,
        )
        self.get_details = to_raw_response_wrapper(
            plans.get_details,
        )
        self.list_charges = to_raw_response_wrapper(
            plans.list_charges,
        )
        self.list_customers = to_raw_response_wrapper(
            plans.list_customers,
        )


class AsyncPlansResourceWithRawResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.list = async_to_raw_response_wrapper(
            plans.list,
        )
        self.get_details = async_to_raw_response_wrapper(
            plans.get_details,
        )
        self.list_charges = async_to_raw_response_wrapper(
            plans.list_charges,
        )
        self.list_customers = async_to_raw_response_wrapper(
            plans.list_customers,
        )


class PlansResourceWithStreamingResponse:
    def __init__(self, plans: PlansResource) -> None:
        self._plans = plans

        self.list = to_streamed_response_wrapper(
            plans.list,
        )
        self.get_details = to_streamed_response_wrapper(
            plans.get_details,
        )
        self.list_charges = to_streamed_response_wrapper(
            plans.list_charges,
        )
        self.list_customers = to_streamed_response_wrapper(
            plans.list_customers,
        )


class AsyncPlansResourceWithStreamingResponse:
    def __init__(self, plans: AsyncPlansResource) -> None:
        self._plans = plans

        self.list = async_to_streamed_response_wrapper(
            plans.list,
        )
        self.get_details = async_to_streamed_response_wrapper(
            plans.get_details,
        )
        self.list_charges = async_to_streamed_response_wrapper(
            plans.list_charges,
        )
        self.list_customers = async_to_streamed_response_wrapper(
            plans.list_customers,
        )
