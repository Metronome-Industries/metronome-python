# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime

import httpx

from .rates import (
    RatesResource,
    AsyncRatesResource,
    RatesResourceWithRawResponse,
    AsyncRatesResourceWithRawResponse,
    RatesResourceWithStreamingResponse,
    AsyncRatesResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncCursorPage, AsyncCursorPage
from .product_orders import (
    ProductOrdersResource,
    AsyncProductOrdersResource,
    ProductOrdersResourceWithRawResponse,
    AsyncProductOrdersResourceWithRawResponse,
    ProductOrdersResourceWithStreamingResponse,
    AsyncProductOrdersResourceWithStreamingResponse,
)
from .named_schedules import (
    NamedSchedulesResource,
    AsyncNamedSchedulesResource,
    NamedSchedulesResourceWithRawResponse,
    AsyncNamedSchedulesResourceWithRawResponse,
    NamedSchedulesResourceWithStreamingResponse,
    AsyncNamedSchedulesResourceWithStreamingResponse,
)
from ....._base_client import AsyncPaginator, make_request_options
from .....types.v1.contracts import (
    rate_card_list_params,
    rate_card_create_params,
    rate_card_update_params,
    rate_card_archive_params,
    rate_card_retrieve_params,
    rate_card_retrieve_rate_schedule_params,
)
from .....types.v1.contracts.rate_card_list_response import RateCardListResponse
from .....types.v1.contracts.rate_card_create_response import RateCardCreateResponse
from .....types.v1.contracts.rate_card_update_response import RateCardUpdateResponse
from .....types.v1.contracts.rate_card_archive_response import RateCardArchiveResponse
from .....types.v1.contracts.rate_card_retrieve_response import RateCardRetrieveResponse
from .....types.v1.contracts.rate_card_retrieve_rate_schedule_response import RateCardRetrieveRateScheduleResponse

__all__ = ["RateCardsResource", "AsyncRateCardsResource"]


class RateCardsResource(SyncAPIResource):
    @cached_property
    def product_orders(self) -> ProductOrdersResource:
        return ProductOrdersResource(self._client)

    @cached_property
    def rates(self) -> RatesResource:
        return RatesResource(self._client)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResource:
        return NamedSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RateCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return RateCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RateCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return RateCardsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        aliases: Iterable[rate_card_create_params.Alias] | NotGiven = NOT_GIVEN,
        credit_type_conversions: Iterable[rate_card_create_params.CreditTypeConversion] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        fiat_credit_type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardCreateResponse:
        """Create a new rate card

        Args:
          name: Used only in UI/API.

        It is not exposed to end customers.

          aliases: Reference this alias when creating a contract. If the same alias is assigned to
              multiple rate cards, it will reference the rate card to which it was most
              recently assigned. It is not exposed to end customers.

          credit_type_conversions: Required when using custom pricing units in rates.

          fiat_credit_type_id: The Metronome ID of the credit type to associate with the rate card, defaults to
              USD (cents) if not passed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/rate-cards/create",
            body=maybe_transform(
                {
                    "name": name,
                    "aliases": aliases,
                    "credit_type_conversions": credit_type_conversions,
                    "custom_fields": custom_fields,
                    "description": description,
                    "fiat_credit_type_id": fiat_credit_type_id,
                },
                rate_card_create_params.RateCardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardCreateResponse,
        )

    def retrieve(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardRetrieveResponse:
        """
        Get a specific rate card NOTE: Use `/contract-pricing/rate-cards/getRates` to
        retrieve rate card rates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/rate-cards/get",
            body=maybe_transform({"id": id}, rate_card_retrieve_params.RateCardRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardRetrieveResponse,
        )

    def update(
        self,
        *,
        rate_card_id: str,
        aliases: Iterable[rate_card_update_params.Alias] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardUpdateResponse:
        """
        Update a rate card

        Args:
          rate_card_id: ID of the rate card to update

          aliases: Reference this alias when creating a contract. If the same alias is assigned to
              multiple rate cards, it will reference the rate card to which it was most
              recently assigned. It is not exposed to end customers.

          name: Used only in UI/API. It is not exposed to end customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/rate-cards/update",
            body=maybe_transform(
                {
                    "rate_card_id": rate_card_id,
                    "aliases": aliases,
                    "description": description,
                    "name": name,
                },
                rate_card_update_params.RateCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        body: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[RateCardListResponse]:
        """
        List rate cards NOTE: Use `/contract-pricing/rate-cards/getRates` to retrieve
        rate card rates.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contract-pricing/rate-cards/list",
            page=SyncCursorPage[RateCardListResponse],
            body=maybe_transform(body, rate_card_list_params.RateCardListParams),
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
                    rate_card_list_params.RateCardListParams,
                ),
            ),
            model=RateCardListResponse,
            method="post",
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
    ) -> RateCardArchiveResponse:
        """
        Archive a rate card

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/rate-cards/archive",
            body=maybe_transform({"id": id}, rate_card_archive_params.RateCardArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardArchiveResponse,
        )

    def retrieve_rate_schedule(
        self,
        *,
        rate_card_id: str,
        starting_at: Union[str, datetime],
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        selectors: Iterable[rate_card_retrieve_rate_schedule_params.Selector] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardRetrieveRateScheduleResponse:
        """
        Get all rates for a rate card from starting_at (either in perpetuity or until
        ending_before, if provided)

        Args:
          rate_card_id: ID of the rate card to get the schedule for

          starting_at: inclusive starting point for the rates schedule

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          ending_before: optional exclusive end date for the rates schedule. When not specified rates
              will show all future schedule segments.

          selectors: List of rate selectors, rates matching ANY of the selector will be included in
              the response Passing no selectors will result in all rates being returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/rate-cards/getRateSchedule",
            body=maybe_transform(
                {
                    "rate_card_id": rate_card_id,
                    "starting_at": starting_at,
                    "ending_before": ending_before,
                    "selectors": selectors,
                },
                rate_card_retrieve_rate_schedule_params.RateCardRetrieveRateScheduleParams,
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
                    rate_card_retrieve_rate_schedule_params.RateCardRetrieveRateScheduleParams,
                ),
            ),
            cast_to=RateCardRetrieveRateScheduleResponse,
        )


class AsyncRateCardsResource(AsyncAPIResource):
    @cached_property
    def product_orders(self) -> AsyncProductOrdersResource:
        return AsyncProductOrdersResource(self._client)

    @cached_property
    def rates(self) -> AsyncRatesResource:
        return AsyncRatesResource(self._client)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResource:
        return AsyncNamedSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRateCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRateCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRateCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncRateCardsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        aliases: Iterable[rate_card_create_params.Alias] | NotGiven = NOT_GIVEN,
        credit_type_conversions: Iterable[rate_card_create_params.CreditTypeConversion] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        fiat_credit_type_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardCreateResponse:
        """Create a new rate card

        Args:
          name: Used only in UI/API.

        It is not exposed to end customers.

          aliases: Reference this alias when creating a contract. If the same alias is assigned to
              multiple rate cards, it will reference the rate card to which it was most
              recently assigned. It is not exposed to end customers.

          credit_type_conversions: Required when using custom pricing units in rates.

          fiat_credit_type_id: The Metronome ID of the credit type to associate with the rate card, defaults to
              USD (cents) if not passed.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/rate-cards/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "aliases": aliases,
                    "credit_type_conversions": credit_type_conversions,
                    "custom_fields": custom_fields,
                    "description": description,
                    "fiat_credit_type_id": fiat_credit_type_id,
                },
                rate_card_create_params.RateCardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardCreateResponse,
        )

    async def retrieve(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardRetrieveResponse:
        """
        Get a specific rate card NOTE: Use `/contract-pricing/rate-cards/getRates` to
        retrieve rate card rates.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/rate-cards/get",
            body=await async_maybe_transform({"id": id}, rate_card_retrieve_params.RateCardRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardRetrieveResponse,
        )

    async def update(
        self,
        *,
        rate_card_id: str,
        aliases: Iterable[rate_card_update_params.Alias] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardUpdateResponse:
        """
        Update a rate card

        Args:
          rate_card_id: ID of the rate card to update

          aliases: Reference this alias when creating a contract. If the same alias is assigned to
              multiple rate cards, it will reference the rate card to which it was most
              recently assigned. It is not exposed to end customers.

          name: Used only in UI/API. It is not exposed to end customers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/rate-cards/update",
            body=await async_maybe_transform(
                {
                    "rate_card_id": rate_card_id,
                    "aliases": aliases,
                    "description": description,
                    "name": name,
                },
                rate_card_update_params.RateCardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        body: object | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RateCardListResponse, AsyncCursorPage[RateCardListResponse]]:
        """
        List rate cards NOTE: Use `/contract-pricing/rate-cards/getRates` to retrieve
        rate card rates.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contract-pricing/rate-cards/list",
            page=AsyncCursorPage[RateCardListResponse],
            body=maybe_transform(body, rate_card_list_params.RateCardListParams),
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
                    rate_card_list_params.RateCardListParams,
                ),
            ),
            model=RateCardListResponse,
            method="post",
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
    ) -> RateCardArchiveResponse:
        """
        Archive a rate card

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/rate-cards/archive",
            body=await async_maybe_transform({"id": id}, rate_card_archive_params.RateCardArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateCardArchiveResponse,
        )

    async def retrieve_rate_schedule(
        self,
        *,
        rate_card_id: str,
        starting_at: Union[str, datetime],
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        selectors: Iterable[rate_card_retrieve_rate_schedule_params.Selector] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateCardRetrieveRateScheduleResponse:
        """
        Get all rates for a rate card from starting_at (either in perpetuity or until
        ending_before, if provided)

        Args:
          rate_card_id: ID of the rate card to get the schedule for

          starting_at: inclusive starting point for the rates schedule

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          ending_before: optional exclusive end date for the rates schedule. When not specified rates
              will show all future schedule segments.

          selectors: List of rate selectors, rates matching ANY of the selector will be included in
              the response Passing no selectors will result in all rates being returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/rate-cards/getRateSchedule",
            body=await async_maybe_transform(
                {
                    "rate_card_id": rate_card_id,
                    "starting_at": starting_at,
                    "ending_before": ending_before,
                    "selectors": selectors,
                },
                rate_card_retrieve_rate_schedule_params.RateCardRetrieveRateScheduleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                    },
                    rate_card_retrieve_rate_schedule_params.RateCardRetrieveRateScheduleParams,
                ),
            ),
            cast_to=RateCardRetrieveRateScheduleResponse,
        )


class RateCardsResourceWithRawResponse:
    def __init__(self, rate_cards: RateCardsResource) -> None:
        self._rate_cards = rate_cards

        self.create = to_raw_response_wrapper(
            rate_cards.create,
        )
        self.retrieve = to_raw_response_wrapper(
            rate_cards.retrieve,
        )
        self.update = to_raw_response_wrapper(
            rate_cards.update,
        )
        self.list = to_raw_response_wrapper(
            rate_cards.list,
        )
        self.archive = to_raw_response_wrapper(
            rate_cards.archive,
        )
        self.retrieve_rate_schedule = to_raw_response_wrapper(
            rate_cards.retrieve_rate_schedule,
        )

    @cached_property
    def product_orders(self) -> ProductOrdersResourceWithRawResponse:
        return ProductOrdersResourceWithRawResponse(self._rate_cards.product_orders)

    @cached_property
    def rates(self) -> RatesResourceWithRawResponse:
        return RatesResourceWithRawResponse(self._rate_cards.rates)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResourceWithRawResponse:
        return NamedSchedulesResourceWithRawResponse(self._rate_cards.named_schedules)


class AsyncRateCardsResourceWithRawResponse:
    def __init__(self, rate_cards: AsyncRateCardsResource) -> None:
        self._rate_cards = rate_cards

        self.create = async_to_raw_response_wrapper(
            rate_cards.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            rate_cards.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            rate_cards.update,
        )
        self.list = async_to_raw_response_wrapper(
            rate_cards.list,
        )
        self.archive = async_to_raw_response_wrapper(
            rate_cards.archive,
        )
        self.retrieve_rate_schedule = async_to_raw_response_wrapper(
            rate_cards.retrieve_rate_schedule,
        )

    @cached_property
    def product_orders(self) -> AsyncProductOrdersResourceWithRawResponse:
        return AsyncProductOrdersResourceWithRawResponse(self._rate_cards.product_orders)

    @cached_property
    def rates(self) -> AsyncRatesResourceWithRawResponse:
        return AsyncRatesResourceWithRawResponse(self._rate_cards.rates)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResourceWithRawResponse:
        return AsyncNamedSchedulesResourceWithRawResponse(self._rate_cards.named_schedules)


class RateCardsResourceWithStreamingResponse:
    def __init__(self, rate_cards: RateCardsResource) -> None:
        self._rate_cards = rate_cards

        self.create = to_streamed_response_wrapper(
            rate_cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            rate_cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            rate_cards.update,
        )
        self.list = to_streamed_response_wrapper(
            rate_cards.list,
        )
        self.archive = to_streamed_response_wrapper(
            rate_cards.archive,
        )
        self.retrieve_rate_schedule = to_streamed_response_wrapper(
            rate_cards.retrieve_rate_schedule,
        )

    @cached_property
    def product_orders(self) -> ProductOrdersResourceWithStreamingResponse:
        return ProductOrdersResourceWithStreamingResponse(self._rate_cards.product_orders)

    @cached_property
    def rates(self) -> RatesResourceWithStreamingResponse:
        return RatesResourceWithStreamingResponse(self._rate_cards.rates)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResourceWithStreamingResponse:
        return NamedSchedulesResourceWithStreamingResponse(self._rate_cards.named_schedules)


class AsyncRateCardsResourceWithStreamingResponse:
    def __init__(self, rate_cards: AsyncRateCardsResource) -> None:
        self._rate_cards = rate_cards

        self.create = async_to_streamed_response_wrapper(
            rate_cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            rate_cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            rate_cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            rate_cards.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            rate_cards.archive,
        )
        self.retrieve_rate_schedule = async_to_streamed_response_wrapper(
            rate_cards.retrieve_rate_schedule,
        )

    @cached_property
    def product_orders(self) -> AsyncProductOrdersResourceWithStreamingResponse:
        return AsyncProductOrdersResourceWithStreamingResponse(self._rate_cards.product_orders)

    @cached_property
    def rates(self) -> AsyncRatesResourceWithStreamingResponse:
        return AsyncRatesResourceWithStreamingResponse(self._rate_cards.rates)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResourceWithStreamingResponse:
        return AsyncNamedSchedulesResourceWithStreamingResponse(self._rate_cards.named_schedules)
