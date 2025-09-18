# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ....._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v1.contracts.rate_cards import product_order_set_params, product_order_update_params
from .....types.v1.contracts.rate_cards.product_order_set_response import ProductOrderSetResponse
from .....types.v1.contracts.rate_cards.product_order_update_response import ProductOrderUpdateResponse

__all__ = ["ProductOrdersResource", "AsyncProductOrdersResource"]


class ProductOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return ProductOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return ProductOrdersResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        product_moves: Iterable[product_order_update_params.ProductMove],
        rate_card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductOrderUpdateResponse:
        """
        The ordering of products on a rate card determines the order in which the
        products will appear on customers' invoices. Use this endpoint to set the order
        of specific products on the rate card by moving them relative to their current
        location.

        Args:
          rate_card_id: ID of the rate card to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/rate-cards/moveRateCardProducts",
            body=maybe_transform(
                {
                    "product_moves": product_moves,
                    "rate_card_id": rate_card_id,
                },
                product_order_update_params.ProductOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductOrderUpdateResponse,
        )

    def set(
        self,
        *,
        product_order: SequenceNotStr[str],
        rate_card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductOrderSetResponse:
        """
        The ordering of products on a rate card determines the order in which the
        products will appear on customers' invoices. Use this endpoint to set the order
        of products on the rate card.

        Args:
          rate_card_id: ID of the rate card to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/rate-cards/setRateCardProductsOrder",
            body=maybe_transform(
                {
                    "product_order": product_order,
                    "rate_card_id": rate_card_id,
                },
                product_order_set_params.ProductOrderSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductOrderSetResponse,
        )


class AsyncProductOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncProductOrdersResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        product_moves: Iterable[product_order_update_params.ProductMove],
        rate_card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductOrderUpdateResponse:
        """
        The ordering of products on a rate card determines the order in which the
        products will appear on customers' invoices. Use this endpoint to set the order
        of specific products on the rate card by moving them relative to their current
        location.

        Args:
          rate_card_id: ID of the rate card to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/rate-cards/moveRateCardProducts",
            body=await async_maybe_transform(
                {
                    "product_moves": product_moves,
                    "rate_card_id": rate_card_id,
                },
                product_order_update_params.ProductOrderUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductOrderUpdateResponse,
        )

    async def set(
        self,
        *,
        product_order: SequenceNotStr[str],
        rate_card_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductOrderSetResponse:
        """
        The ordering of products on a rate card determines the order in which the
        products will appear on customers' invoices. Use this endpoint to set the order
        of products on the rate card.

        Args:
          rate_card_id: ID of the rate card to update

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/rate-cards/setRateCardProductsOrder",
            body=await async_maybe_transform(
                {
                    "product_order": product_order,
                    "rate_card_id": rate_card_id,
                },
                product_order_set_params.ProductOrderSetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductOrderSetResponse,
        )


class ProductOrdersResourceWithRawResponse:
    def __init__(self, product_orders: ProductOrdersResource) -> None:
        self._product_orders = product_orders

        self.update = to_raw_response_wrapper(
            product_orders.update,
        )
        self.set = to_raw_response_wrapper(
            product_orders.set,
        )


class AsyncProductOrdersResourceWithRawResponse:
    def __init__(self, product_orders: AsyncProductOrdersResource) -> None:
        self._product_orders = product_orders

        self.update = async_to_raw_response_wrapper(
            product_orders.update,
        )
        self.set = async_to_raw_response_wrapper(
            product_orders.set,
        )


class ProductOrdersResourceWithStreamingResponse:
    def __init__(self, product_orders: ProductOrdersResource) -> None:
        self._product_orders = product_orders

        self.update = to_streamed_response_wrapper(
            product_orders.update,
        )
        self.set = to_streamed_response_wrapper(
            product_orders.set,
        )


class AsyncProductOrdersResourceWithStreamingResponse:
    def __init__(self, product_orders: AsyncProductOrdersResource) -> None:
        self._product_orders = product_orders

        self.update = async_to_streamed_response_wrapper(
            product_orders.update,
        )
        self.set = async_to_streamed_response_wrapper(
            product_orders.set,
        )
