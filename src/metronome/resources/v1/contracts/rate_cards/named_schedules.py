# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncBodyCursorPage, AsyncBodyCursorPage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.v1.contracts.rate_cards import (
    named_schedule_list_params,
    named_schedule_update_params,
    named_schedule_retrieve_params,
)
from .....types.v1.contracts.rate_cards.named_schedule_list_response import NamedScheduleListResponse
from .....types.v1.contracts.rate_cards.named_schedule_retrieve_response import NamedScheduleRetrieveResponse

__all__ = ["NamedSchedulesResource", "AsyncNamedSchedulesResource"]


class NamedSchedulesResource(SyncAPIResource):
    """Named schedules are used for storing custom data that can change over time.

    Named schedules are often used in custom pricing logic.
    """

    @cached_property
    def with_raw_response(self) -> NamedSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return NamedSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamedSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return NamedSchedulesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        contract_id: str,
        customer_id: str,
        schedule_name: str,
        covering_date: Union[str, datetime] | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedScheduleRetrieveResponse:
        """Get a named schedule for the given contract.

        This endpoint's availability is
        dependent on your client's configuration.

        Args:
          contract_id: ID of the contract whose named schedule is to be retrieved

          customer_id: ID of the customer whose named schedule is to be retrieved

          schedule_name: The identifier for the schedule to be retrieved

          covering_date: If provided, at most one schedule segment will be returned (the one that covers
              this date). If not provided, all segments will be returned.

          properties: A set of key-value pairs that qualifies which schedule should be applied when
              looking up a schedule by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contracts/getNamedSchedule",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "schedule_name": schedule_name,
                    "covering_date": covering_date,
                    "properties": properties,
                },
                named_schedule_retrieve_params.NamedScheduleRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedScheduleRetrieveResponse,
        )

    def update(
        self,
        *,
        contract_id: str,
        customer_id: str,
        schedule_name: str,
        starting_at: Union[str, datetime],
        value: object,
        ending_before: Union[str, datetime] | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update a named schedule for the given contract.

        This endpoint's availability is
        dependent on your client's configuration.

        Args:
          contract_id: ID of the contract whose named schedule is to be updated

          customer_id: ID of the customer whose named schedule is to be updated

          schedule_name: The identifier for the schedule to be updated

          value: The value to set for the named schedule. The structure of this object is
              specific to the named schedule.

          properties: A set of key-value pairs that qualifies which schedule should be applied when
              looking up a schedule by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/contracts/updateNamedSchedule",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "schedule_name": schedule_name,
                    "starting_at": starting_at,
                    "value": value,
                    "ending_before": ending_before,
                    "properties": properties,
                },
                named_schedule_update_params.NamedScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        customer_id: str,
        contract_id: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        schedule_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncBodyCursorPage[NamedScheduleListResponse]:
        """
        List contract-level named schedules for a customer, optionally scoped to a
        single contract.

        Args:
          customer_id: ID of the customer to list contract named schedules for

          contract_id: Optional ID of a contract to scope the results to a single contract

          covering_date: If provided, result contains at most one segment covering this date for each
              schedule.

          limit: Maximum number of named schedules to return.

          next_page: Cursor for pagination. Use the value from a previous response's next_page.

          properties: Optional key-value filters. A schedule matches when it contains at least this
              subset of properties.

          schedule_name: Optional filter to scope the results to a single schedule name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/listNamedSchedules",
            page=SyncBodyCursorPage[NamedScheduleListResponse],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "contract_id": contract_id,
                    "covering_date": covering_date,
                    "limit": limit,
                    "next_page": next_page,
                    "properties": properties,
                    "schedule_name": schedule_name,
                },
                named_schedule_list_params.NamedScheduleListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=NamedScheduleListResponse,
            method="post",
        )


class AsyncNamedSchedulesResource(AsyncAPIResource):
    """Named schedules are used for storing custom data that can change over time.

    Named schedules are often used in custom pricing logic.
    """

    @cached_property
    def with_raw_response(self) -> AsyncNamedSchedulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamedSchedulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamedSchedulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncNamedSchedulesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        contract_id: str,
        customer_id: str,
        schedule_name: str,
        covering_date: Union[str, datetime] | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedScheduleRetrieveResponse:
        """Get a named schedule for the given contract.

        This endpoint's availability is
        dependent on your client's configuration.

        Args:
          contract_id: ID of the contract whose named schedule is to be retrieved

          customer_id: ID of the customer whose named schedule is to be retrieved

          schedule_name: The identifier for the schedule to be retrieved

          covering_date: If provided, at most one schedule segment will be returned (the one that covers
              this date). If not provided, all segments will be returned.

          properties: A set of key-value pairs that qualifies which schedule should be applied when
              looking up a schedule by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contracts/getNamedSchedule",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "schedule_name": schedule_name,
                    "covering_date": covering_date,
                    "properties": properties,
                },
                named_schedule_retrieve_params.NamedScheduleRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedScheduleRetrieveResponse,
        )

    async def update(
        self,
        *,
        contract_id: str,
        customer_id: str,
        schedule_name: str,
        starting_at: Union[str, datetime],
        value: object,
        ending_before: Union[str, datetime] | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Update a named schedule for the given contract.

        This endpoint's availability is
        dependent on your client's configuration.

        Args:
          contract_id: ID of the contract whose named schedule is to be updated

          customer_id: ID of the customer whose named schedule is to be updated

          schedule_name: The identifier for the schedule to be updated

          value: The value to set for the named schedule. The structure of this object is
              specific to the named schedule.

          properties: A set of key-value pairs that qualifies which schedule should be applied when
              looking up a schedule by name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/contracts/updateNamedSchedule",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "schedule_name": schedule_name,
                    "starting_at": starting_at,
                    "value": value,
                    "ending_before": ending_before,
                    "properties": properties,
                },
                named_schedule_update_params.NamedScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        customer_id: str,
        contract_id: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        properties: Dict[str, str] | Omit = omit,
        schedule_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[NamedScheduleListResponse, AsyncBodyCursorPage[NamedScheduleListResponse]]:
        """
        List contract-level named schedules for a customer, optionally scoped to a
        single contract.

        Args:
          customer_id: ID of the customer to list contract named schedules for

          contract_id: Optional ID of a contract to scope the results to a single contract

          covering_date: If provided, result contains at most one segment covering this date for each
              schedule.

          limit: Maximum number of named schedules to return.

          next_page: Cursor for pagination. Use the value from a previous response's next_page.

          properties: Optional key-value filters. A schedule matches when it contains at least this
              subset of properties.

          schedule_name: Optional filter to scope the results to a single schedule name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/listNamedSchedules",
            page=AsyncBodyCursorPage[NamedScheduleListResponse],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "contract_id": contract_id,
                    "covering_date": covering_date,
                    "limit": limit,
                    "next_page": next_page,
                    "properties": properties,
                    "schedule_name": schedule_name,
                },
                named_schedule_list_params.NamedScheduleListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=NamedScheduleListResponse,
            method="post",
        )


class NamedSchedulesResourceWithRawResponse:
    def __init__(self, named_schedules: NamedSchedulesResource) -> None:
        self._named_schedules = named_schedules

        self.retrieve = to_raw_response_wrapper(
            named_schedules.retrieve,
        )
        self.update = to_raw_response_wrapper(
            named_schedules.update,
        )
        self.list = to_raw_response_wrapper(
            named_schedules.list,
        )


class AsyncNamedSchedulesResourceWithRawResponse:
    def __init__(self, named_schedules: AsyncNamedSchedulesResource) -> None:
        self._named_schedules = named_schedules

        self.retrieve = async_to_raw_response_wrapper(
            named_schedules.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            named_schedules.update,
        )
        self.list = async_to_raw_response_wrapper(
            named_schedules.list,
        )


class NamedSchedulesResourceWithStreamingResponse:
    def __init__(self, named_schedules: NamedSchedulesResource) -> None:
        self._named_schedules = named_schedules

        self.retrieve = to_streamed_response_wrapper(
            named_schedules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            named_schedules.update,
        )
        self.list = to_streamed_response_wrapper(
            named_schedules.list,
        )


class AsyncNamedSchedulesResourceWithStreamingResponse:
    def __init__(self, named_schedules: AsyncNamedSchedulesResource) -> None:
        self._named_schedules = named_schedules

        self.retrieve = async_to_streamed_response_wrapper(
            named_schedules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            named_schedules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            named_schedules.list,
        )
