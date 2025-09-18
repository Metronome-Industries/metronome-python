# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import invoice_void_params, invoice_regenerate_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.invoice_void_response import InvoiceVoidResponse
from ...types.v1.invoice_regenerate_response import InvoiceRegenerateResponse

__all__ = ["InvoicesResource", "AsyncInvoicesResource"]


class InvoicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return InvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return InvoicesResourceWithStreamingResponse(self)

    def regenerate(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceRegenerateResponse:
        """
        This endpoint regenerates a voided invoice and recalculates the invoice based on
        up-to-date rates, available balances, and other fees regardless of the billing
        period.

        ### Use this endpoint to:

        Recalculate an invoice with updated rate terms, available balance, and fees to
        correct billing disputes or discrepancies

        ### Key response fields:

        The regenerated invoice id, which is distinct from the previously voided
        invoice.

        ### Usage guidelines:

        If an invoice is attached to a contract with a billing provider on it, the
        regenerated invoice will be distributed based on the configuration.

        Args:
          id: The invoice id to regenerate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/invoices/regenerate",
            body=maybe_transform({"id": id}, invoice_regenerate_params.InvoiceRegenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceRegenerateResponse,
        )

    def void(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceVoidResponse:
        """
        Permanently cancels an invoice by setting its status to voided, preventing
        collection and removing it from customer billing. Use this to correct billing
        errors, cancel incorrect charges, or handle disputed invoices that should not be
        collected. Returns the voided invoice ID with the status change applied
        immediately to stop any payment processing.

        Args:
          id: The invoice id to void

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/invoices/void",
            body=maybe_transform({"id": id}, invoice_void_params.InvoiceVoidParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceVoidResponse,
        )


class AsyncInvoicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvoicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvoicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvoicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncInvoicesResourceWithStreamingResponse(self)

    async def regenerate(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceRegenerateResponse:
        """
        This endpoint regenerates a voided invoice and recalculates the invoice based on
        up-to-date rates, available balances, and other fees regardless of the billing
        period.

        ### Use this endpoint to:

        Recalculate an invoice with updated rate terms, available balance, and fees to
        correct billing disputes or discrepancies

        ### Key response fields:

        The regenerated invoice id, which is distinct from the previously voided
        invoice.

        ### Usage guidelines:

        If an invoice is attached to a contract with a billing provider on it, the
        regenerated invoice will be distributed based on the configuration.

        Args:
          id: The invoice id to regenerate

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/invoices/regenerate",
            body=await async_maybe_transform({"id": id}, invoice_regenerate_params.InvoiceRegenerateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceRegenerateResponse,
        )

    async def void(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceVoidResponse:
        """
        Permanently cancels an invoice by setting its status to voided, preventing
        collection and removing it from customer billing. Use this to correct billing
        errors, cancel incorrect charges, or handle disputed invoices that should not be
        collected. Returns the voided invoice ID with the status change applied
        immediately to stop any payment processing.

        Args:
          id: The invoice id to void

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/invoices/void",
            body=await async_maybe_transform({"id": id}, invoice_void_params.InvoiceVoidParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceVoidResponse,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.regenerate = to_raw_response_wrapper(
            invoices.regenerate,
        )
        self.void = to_raw_response_wrapper(
            invoices.void,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.regenerate = async_to_raw_response_wrapper(
            invoices.regenerate,
        )
        self.void = async_to_raw_response_wrapper(
            invoices.void,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.regenerate = to_streamed_response_wrapper(
            invoices.regenerate,
        )
        self.void = to_streamed_response_wrapper(
            invoices.void,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.regenerate = async_to_streamed_response_wrapper(
            invoices.regenerate,
        )
        self.void = async_to_streamed_response_wrapper(
            invoices.void,
        )
