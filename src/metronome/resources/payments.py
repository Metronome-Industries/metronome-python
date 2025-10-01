# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import payment_list_params, payment_attempt_payment_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncBodyCursorPage, AsyncBodyCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.payment_list_response import PaymentListResponse
from ..types.payment_attempt_payment_response import PaymentAttemptPaymentResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        customer_id: str,
        invoice_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        statuses: List[Literal["pending", "requires_intervention", "paid", "canceled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncBodyCursorPage[PaymentListResponse]:
        """
        Fetch all payment attempts for the given invoice.

        Args:
          limit: The maximum number of payments to return. Defaults to 25.

          next_page: The next page token from a previous response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/payments/list",
            page=SyncBodyCursorPage[PaymentListResponse],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "invoice_id": invoice_id,
                    "limit": limit,
                    "next_page": next_page,
                    "statuses": statuses,
                },
                payment_list_params.PaymentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PaymentListResponse,
            method="post",
        )

    def attempt_payment(
        self,
        *,
        customer_id: str,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentAttemptPaymentResponse:
        """
        Trigger a new attempt by canceling any existing attempts for this invoice and
        creating a new Payment. This will trigger another attempt to charge the
        Customer's configured Payment Gateway. Payment can only be attempted if all of
        the following are true:

        - The Metronome Invoice is finalized
        - PLG Invoicing is configured for the Customer
        - You cannot attempt payments for invoices that have already been `paid` or
          `voided`.

        Attempting to payment on an ineligible Invoice or Customer will result in a
        `400` response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/payments/attempt",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "invoice_id": invoice_id,
                },
                payment_attempt_payment_params.PaymentAttemptPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentAttemptPaymentResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        customer_id: str,
        invoice_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        statuses: List[Literal["pending", "requires_intervention", "paid", "canceled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PaymentListResponse, AsyncBodyCursorPage[PaymentListResponse]]:
        """
        Fetch all payment attempts for the given invoice.

        Args:
          limit: The maximum number of payments to return. Defaults to 25.

          next_page: The next page token from a previous response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/payments/list",
            page=AsyncBodyCursorPage[PaymentListResponse],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "invoice_id": invoice_id,
                    "limit": limit,
                    "next_page": next_page,
                    "statuses": statuses,
                },
                payment_list_params.PaymentListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=PaymentListResponse,
            method="post",
        )

    async def attempt_payment(
        self,
        *,
        customer_id: str,
        invoice_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaymentAttemptPaymentResponse:
        """
        Trigger a new attempt by canceling any existing attempts for this invoice and
        creating a new Payment. This will trigger another attempt to charge the
        Customer's configured Payment Gateway. Payment can only be attempted if all of
        the following are true:

        - The Metronome Invoice is finalized
        - PLG Invoicing is configured for the Customer
        - You cannot attempt payments for invoices that have already been `paid` or
          `voided`.

        Attempting to payment on an ineligible Invoice or Customer will result in a
        `400` response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/payments/attempt",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "invoice_id": invoice_id,
                },
                payment_attempt_payment_params.PaymentAttemptPaymentParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentAttemptPaymentResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.list = to_raw_response_wrapper(
            payments.list,
        )
        self.attempt_payment = to_raw_response_wrapper(
            payments.attempt_payment,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.list = async_to_raw_response_wrapper(
            payments.list,
        )
        self.attempt_payment = async_to_raw_response_wrapper(
            payments.attempt_payment,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.list = to_streamed_response_wrapper(
            payments.list,
        )
        self.attempt_payment = to_streamed_response_wrapper(
            payments.attempt_payment,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
        self.attempt_payment = async_to_streamed_response_wrapper(
            payments.attempt_payment,
        )
