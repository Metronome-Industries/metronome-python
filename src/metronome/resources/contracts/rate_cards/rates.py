# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.shared_params.tier import Tier
from ....types.contracts.rate_cards import rate_add_params, rate_list_params, rate_add_many_params
from ....types.contracts.rate_cards.rate_add_response import RateAddResponse
from ....types.contracts.rate_cards.rate_list_response import RateListResponse
from ....types.contracts.rate_cards.rate_add_many_response import RateAddManyResponse

__all__ = ["RatesResource", "AsyncRatesResource"]


class RatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RatesResourceWithRawResponse:
        return RatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatesResourceWithStreamingResponse:
        return RatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        at: Union[str, datetime],
        rate_card_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        selectors: Iterable[rate_list_params.Selector] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[RateListResponse]:
        """
        Get rate card rates for a specific time.

        Args:
          at: inclusive starting point for the rates schedule

          rate_card_id: ID of the rate card to get the schedule for

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          selectors: List of rate selectors, rates matching ANY of the selector will be included in
              the response Passing no selectors will result in all rates being returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/contract-pricing/rate-cards/getRates",
            page=SyncCursorPage[RateListResponse],
            body=maybe_transform(
                {
                    "at": at,
                    "rate_card_id": rate_card_id,
                    "selectors": selectors,
                },
                rate_list_params.RateListParams,
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
                    rate_list_params.RateListParams,
                ),
            ),
            model=RateListResponse,
            method="post",
        )

    def add(
        self,
        *,
        entitled: bool,
        product_id: str,
        rate_card_id: str,
        rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"],
        starting_at: Union[str, datetime],
        credit_type_id: str | NotGiven = NOT_GIVEN,
        custom_rate: Dict[str, object] | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        is_prorated: bool | NotGiven = NOT_GIVEN,
        price: float | NotGiven = NOT_GIVEN,
        pricing_group_values: Dict[str, str] | NotGiven = NOT_GIVEN,
        quantity: float | NotGiven = NOT_GIVEN,
        tiers: Iterable[Tier] | NotGiven = NOT_GIVEN,
        use_list_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateAddResponse:
        """
        Add a new rate

        Args:
          product_id: ID of the product to add a rate for

          rate_card_id: ID of the rate card to update

          starting_at: inclusive effective date

          credit_type_id: "The Metronome ID of the credit type to associate with price, defaults to USD
              (cents) if not passed. Used by all rate_types except type PERCENTAGE. PERCENTAGE
              rates use the credit type of associated rates."

          custom_rate: Only set for CUSTOM rate_type. This field is interpreted by custom rate
              processors.

          ending_before: exclusive end date

          is_prorated: Default proration configuration. Only valid for SUBSCRIPTION rate_type.

          price: Default price. For FLAT and SUBSCRIPTION rate_type, this must be >=0. For
              PERCENTAGE rate_type, this is a decimal fraction, e.g. use 0.1 for 10%; this
              must be >=0 and <=1.

          pricing_group_values: Optional. List of pricing group key value pairs which will be used to calculate
              the price.

          quantity: Default quantity. For SUBSCRIPTION rate_type, this must be >=0.

          tiers: Only set for TIERED rate_type.

          use_list_prices: Only set for PERCENTAGE rate_type. Defaults to false. If true, rate is computed
              using list prices rather than the standard rates for this product on the
              contract.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contract-pricing/rate-cards/addRate",
            body=maybe_transform(
                {
                    "entitled": entitled,
                    "product_id": product_id,
                    "rate_card_id": rate_card_id,
                    "rate_type": rate_type,
                    "starting_at": starting_at,
                    "credit_type_id": credit_type_id,
                    "custom_rate": custom_rate,
                    "ending_before": ending_before,
                    "is_prorated": is_prorated,
                    "price": price,
                    "pricing_group_values": pricing_group_values,
                    "quantity": quantity,
                    "tiers": tiers,
                    "use_list_prices": use_list_prices,
                },
                rate_add_params.RateAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateAddResponse,
        )

    def add_many(
        self,
        *,
        rate_card_id: str | NotGiven = NOT_GIVEN,
        rates: Iterable[rate_add_many_params.Rate] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateAddManyResponse:
        """
        Add new rates

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contract-pricing/rate-cards/addRates",
            body=maybe_transform(
                {
                    "rate_card_id": rate_card_id,
                    "rates": rates,
                },
                rate_add_many_params.RateAddManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateAddManyResponse,
        )


class AsyncRatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRatesResourceWithRawResponse:
        return AsyncRatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatesResourceWithStreamingResponse:
        return AsyncRatesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        at: Union[str, datetime],
        rate_card_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        selectors: Iterable[rate_list_params.Selector] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RateListResponse, AsyncCursorPage[RateListResponse]]:
        """
        Get rate card rates for a specific time.

        Args:
          at: inclusive starting point for the rates schedule

          rate_card_id: ID of the rate card to get the schedule for

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          selectors: List of rate selectors, rates matching ANY of the selector will be included in
              the response Passing no selectors will result in all rates being returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/contract-pricing/rate-cards/getRates",
            page=AsyncCursorPage[RateListResponse],
            body=maybe_transform(
                {
                    "at": at,
                    "rate_card_id": rate_card_id,
                    "selectors": selectors,
                },
                rate_list_params.RateListParams,
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
                    rate_list_params.RateListParams,
                ),
            ),
            model=RateListResponse,
            method="post",
        )

    async def add(
        self,
        *,
        entitled: bool,
        product_id: str,
        rate_card_id: str,
        rate_type: Literal["FLAT", "PERCENTAGE", "SUBSCRIPTION", "TIERED", "CUSTOM"],
        starting_at: Union[str, datetime],
        credit_type_id: str | NotGiven = NOT_GIVEN,
        custom_rate: Dict[str, object] | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        is_prorated: bool | NotGiven = NOT_GIVEN,
        price: float | NotGiven = NOT_GIVEN,
        pricing_group_values: Dict[str, str] | NotGiven = NOT_GIVEN,
        quantity: float | NotGiven = NOT_GIVEN,
        tiers: Iterable[Tier] | NotGiven = NOT_GIVEN,
        use_list_prices: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateAddResponse:
        """
        Add a new rate

        Args:
          product_id: ID of the product to add a rate for

          rate_card_id: ID of the rate card to update

          starting_at: inclusive effective date

          credit_type_id: "The Metronome ID of the credit type to associate with price, defaults to USD
              (cents) if not passed. Used by all rate_types except type PERCENTAGE. PERCENTAGE
              rates use the credit type of associated rates."

          custom_rate: Only set for CUSTOM rate_type. This field is interpreted by custom rate
              processors.

          ending_before: exclusive end date

          is_prorated: Default proration configuration. Only valid for SUBSCRIPTION rate_type.

          price: Default price. For FLAT and SUBSCRIPTION rate_type, this must be >=0. For
              PERCENTAGE rate_type, this is a decimal fraction, e.g. use 0.1 for 10%; this
              must be >=0 and <=1.

          pricing_group_values: Optional. List of pricing group key value pairs which will be used to calculate
              the price.

          quantity: Default quantity. For SUBSCRIPTION rate_type, this must be >=0.

          tiers: Only set for TIERED rate_type.

          use_list_prices: Only set for PERCENTAGE rate_type. Defaults to false. If true, rate is computed
              using list prices rather than the standard rates for this product on the
              contract.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contract-pricing/rate-cards/addRate",
            body=await async_maybe_transform(
                {
                    "entitled": entitled,
                    "product_id": product_id,
                    "rate_card_id": rate_card_id,
                    "rate_type": rate_type,
                    "starting_at": starting_at,
                    "credit_type_id": credit_type_id,
                    "custom_rate": custom_rate,
                    "ending_before": ending_before,
                    "is_prorated": is_prorated,
                    "price": price,
                    "pricing_group_values": pricing_group_values,
                    "quantity": quantity,
                    "tiers": tiers,
                    "use_list_prices": use_list_prices,
                },
                rate_add_params.RateAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateAddResponse,
        )

    async def add_many(
        self,
        *,
        rate_card_id: str | NotGiven = NOT_GIVEN,
        rates: Iterable[rate_add_many_params.Rate] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RateAddManyResponse:
        """
        Add new rates

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contract-pricing/rate-cards/addRates",
            body=await async_maybe_transform(
                {
                    "rate_card_id": rate_card_id,
                    "rates": rates,
                },
                rate_add_many_params.RateAddManyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RateAddManyResponse,
        )


class RatesResourceWithRawResponse:
    def __init__(self, rates: RatesResource) -> None:
        self._rates = rates

        self.list = to_raw_response_wrapper(
            rates.list,
        )
        self.add = to_raw_response_wrapper(
            rates.add,
        )
        self.add_many = to_raw_response_wrapper(
            rates.add_many,
        )


class AsyncRatesResourceWithRawResponse:
    def __init__(self, rates: AsyncRatesResource) -> None:
        self._rates = rates

        self.list = async_to_raw_response_wrapper(
            rates.list,
        )
        self.add = async_to_raw_response_wrapper(
            rates.add,
        )
        self.add_many = async_to_raw_response_wrapper(
            rates.add_many,
        )


class RatesResourceWithStreamingResponse:
    def __init__(self, rates: RatesResource) -> None:
        self._rates = rates

        self.list = to_streamed_response_wrapper(
            rates.list,
        )
        self.add = to_streamed_response_wrapper(
            rates.add,
        )
        self.add_many = to_streamed_response_wrapper(
            rates.add_many,
        )


class AsyncRatesResourceWithStreamingResponse:
    def __init__(self, rates: AsyncRatesResource) -> None:
        self._rates = rates

        self.list = async_to_streamed_response_wrapper(
            rates.list,
        )
        self.add = async_to_streamed_response_wrapper(
            rates.add,
        )
        self.add_many = async_to_streamed_response_wrapper(
            rates.add_many,
        )
