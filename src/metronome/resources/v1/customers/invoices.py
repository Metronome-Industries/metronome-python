# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
    invoice_list_params,
    invoice_retrieve_params,
    invoice_add_charge_params,
    invoice_list_breakdowns_params,
)
from ....types.v1.customers.invoice import Invoice
from ....types.v1.customers.invoice_retrieve_response import InvoiceRetrieveResponse
from ....types.v1.customers.invoice_add_charge_response import InvoiceAddChargeResponse
from ....types.v1.customers.invoice_list_breakdowns_response import InvoiceListBreakdownsResponse

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

    def retrieve(
        self,
        *,
        customer_id: str,
        invoice_id: str,
        skip_zero_qty_line_items: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceRetrieveResponse:
        """
        Fetch a specific invoice for a given customer.

        Args:
          skip_zero_qty_line_items: If set, all zero quantity line items will be filtered out of the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return self._get(
            f"/v1/customers/{customer_id}/invoices/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"skip_zero_qty_line_items": skip_zero_qty_line_items},
                    invoice_retrieve_params.InvoiceRetrieveParams,
                ),
            ),
            cast_to=InvoiceRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        credit_type_id: str | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        skip_zero_qty_line_items: bool | NotGiven = NOT_GIVEN,
        sort: Literal["date_asc", "date_desc"] | NotGiven = NOT_GIVEN,
        starting_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Invoice]:
        """
        List all invoices for a given customer, optionally filtered by status, date
        range, and/or credit type.

        Args:
          credit_type_id: Only return invoices for the specified credit type

          ending_before: RFC 3339 timestamp (exclusive). Invoices will only be returned for billing
              periods that end before this time.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          skip_zero_qty_line_items: If set, all zero quantity line items will be filtered out of the response

          sort: Invoice sort order by issued_at, e.g. date_asc or date_desc. Defaults to
              date_asc.

          starting_on: RFC 3339 timestamp (inclusive). Invoices will only be returned for billing
              periods that start at or after this time.

          status: Invoice status, e.g. DRAFT, FINALIZED, or VOID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/invoices",
            page=SyncCursorPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "credit_type_id": credit_type_id,
                        "ending_before": ending_before,
                        "limit": limit,
                        "next_page": next_page,
                        "skip_zero_qty_line_items": skip_zero_qty_line_items,
                        "sort": sort,
                        "starting_on": starting_on,
                        "status": status,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    def add_charge(
        self,
        *,
        customer_id: str,
        charge_id: str,
        customer_plan_id: str,
        description: str,
        invoice_start_timestamp: Union[str, datetime],
        price: float,
        quantity: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceAddChargeResponse:
        """
        Add a one time charge to the specified invoice

        Args:
          charge_id: The Metronome ID of the charge to add to the invoice. Note that the charge must
              be on a product that is not on the current plan, and the product must have only
              fixed charges.

          customer_plan_id: The Metronome ID of the customer plan to add the charge to.

          invoice_start_timestamp: The start_timestamp of the invoice to add the charge to.

          price: The price of the charge. This price will match the currency on the invoice, e.g.
              USD cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/v1/customers/{customer_id}/addCharge",
            body=maybe_transform(
                {
                    "charge_id": charge_id,
                    "customer_plan_id": customer_plan_id,
                    "description": description,
                    "invoice_start_timestamp": invoice_start_timestamp,
                    "price": price,
                    "quantity": quantity,
                },
                invoice_add_charge_params.InvoiceAddChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceAddChargeResponse,
        )

    def list_breakdowns(
        self,
        *,
        customer_id: str,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        credit_type_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        skip_zero_qty_line_items: bool | NotGiven = NOT_GIVEN,
        sort: Literal["date_asc", "date_desc"] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        window_size: Literal["HOUR", "DAY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[InvoiceListBreakdownsResponse]:
        """
        List daily or hourly invoice breakdowns for a given customer, optionally
        filtered by status, date range, and/or credit type. Important considerations:

        - If we receive backdated usage after an invoice has been finalized, the
          backdated usage will be included in the response and usage numbers may differ.

        Args:
          ending_before: RFC 3339 timestamp. Breakdowns will only be returned for time windows that end
              on or before this time.

          starting_on: RFC 3339 timestamp. Breakdowns will only be returned for time windows that start
              on or after this time.

          credit_type_id: Only return invoices for the specified credit type

          limit: Max number of results that should be returned. For daily breakdowns, the
              response can return up to 35 days worth of breakdowns. For hourly breakdowns,
              the response can return up to 24 hours. If there are more results, a cursor to
              the next page is returned.

          next_page: Cursor that indicates where the next page of results should start.

          skip_zero_qty_line_items: If set, all zero quantity line items will be filtered out of the response

          sort: Invoice sort order by issued_at, e.g. date_asc or date_desc. Defaults to
              date_asc.

          status: Invoice status, e.g. DRAFT or FINALIZED

          window_size: The granularity of the breakdowns to return. Defaults to day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/invoices/breakdowns",
            page=SyncCursorPage[InvoiceListBreakdownsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "starting_on": starting_on,
                        "credit_type_id": credit_type_id,
                        "limit": limit,
                        "next_page": next_page,
                        "skip_zero_qty_line_items": skip_zero_qty_line_items,
                        "sort": sort,
                        "status": status,
                        "window_size": window_size,
                    },
                    invoice_list_breakdowns_params.InvoiceListBreakdownsParams,
                ),
            ),
            model=InvoiceListBreakdownsResponse,
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

    async def retrieve(
        self,
        *,
        customer_id: str,
        invoice_id: str,
        skip_zero_qty_line_items: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceRetrieveResponse:
        """
        Fetch a specific invoice for a given customer.

        Args:
          skip_zero_qty_line_items: If set, all zero quantity line items will be filtered out of the response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        return await self._get(
            f"/v1/customers/{customer_id}/invoices/{invoice_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"skip_zero_qty_line_items": skip_zero_qty_line_items},
                    invoice_retrieve_params.InvoiceRetrieveParams,
                ),
            ),
            cast_to=InvoiceRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        credit_type_id: str | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        skip_zero_qty_line_items: bool | NotGiven = NOT_GIVEN,
        sort: Literal["date_asc", "date_desc"] | NotGiven = NOT_GIVEN,
        starting_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Invoice, AsyncCursorPage[Invoice]]:
        """
        List all invoices for a given customer, optionally filtered by status, date
        range, and/or credit type.

        Args:
          credit_type_id: Only return invoices for the specified credit type

          ending_before: RFC 3339 timestamp (exclusive). Invoices will only be returned for billing
              periods that end before this time.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          skip_zero_qty_line_items: If set, all zero quantity line items will be filtered out of the response

          sort: Invoice sort order by issued_at, e.g. date_asc or date_desc. Defaults to
              date_asc.

          starting_on: RFC 3339 timestamp (inclusive). Invoices will only be returned for billing
              periods that start at or after this time.

          status: Invoice status, e.g. DRAFT, FINALIZED, or VOID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/invoices",
            page=AsyncCursorPage[Invoice],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "credit_type_id": credit_type_id,
                        "ending_before": ending_before,
                        "limit": limit,
                        "next_page": next_page,
                        "skip_zero_qty_line_items": skip_zero_qty_line_items,
                        "sort": sort,
                        "starting_on": starting_on,
                        "status": status,
                    },
                    invoice_list_params.InvoiceListParams,
                ),
            ),
            model=Invoice,
        )

    async def add_charge(
        self,
        *,
        customer_id: str,
        charge_id: str,
        customer_plan_id: str,
        description: str,
        invoice_start_timestamp: Union[str, datetime],
        price: float,
        quantity: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvoiceAddChargeResponse:
        """
        Add a one time charge to the specified invoice

        Args:
          charge_id: The Metronome ID of the charge to add to the invoice. Note that the charge must
              be on a product that is not on the current plan, and the product must have only
              fixed charges.

          customer_plan_id: The Metronome ID of the customer plan to add the charge to.

          invoice_start_timestamp: The start_timestamp of the invoice to add the charge to.

          price: The price of the charge. This price will match the currency on the invoice, e.g.
              USD cents.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/v1/customers/{customer_id}/addCharge",
            body=await async_maybe_transform(
                {
                    "charge_id": charge_id,
                    "customer_plan_id": customer_plan_id,
                    "description": description,
                    "invoice_start_timestamp": invoice_start_timestamp,
                    "price": price,
                    "quantity": quantity,
                },
                invoice_add_charge_params.InvoiceAddChargeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvoiceAddChargeResponse,
        )

    def list_breakdowns(
        self,
        *,
        customer_id: str,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        credit_type_id: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        skip_zero_qty_line_items: bool | NotGiven = NOT_GIVEN,
        sort: Literal["date_asc", "date_desc"] | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        window_size: Literal["HOUR", "DAY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[InvoiceListBreakdownsResponse, AsyncCursorPage[InvoiceListBreakdownsResponse]]:
        """
        List daily or hourly invoice breakdowns for a given customer, optionally
        filtered by status, date range, and/or credit type. Important considerations:

        - If we receive backdated usage after an invoice has been finalized, the
          backdated usage will be included in the response and usage numbers may differ.

        Args:
          ending_before: RFC 3339 timestamp. Breakdowns will only be returned for time windows that end
              on or before this time.

          starting_on: RFC 3339 timestamp. Breakdowns will only be returned for time windows that start
              on or after this time.

          credit_type_id: Only return invoices for the specified credit type

          limit: Max number of results that should be returned. For daily breakdowns, the
              response can return up to 35 days worth of breakdowns. For hourly breakdowns,
              the response can return up to 24 hours. If there are more results, a cursor to
              the next page is returned.

          next_page: Cursor that indicates where the next page of results should start.

          skip_zero_qty_line_items: If set, all zero quantity line items will be filtered out of the response

          sort: Invoice sort order by issued_at, e.g. date_asc or date_desc. Defaults to
              date_asc.

          status: Invoice status, e.g. DRAFT or FINALIZED

          window_size: The granularity of the breakdowns to return. Defaults to day.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/v1/customers/{customer_id}/invoices/breakdowns",
            page=AsyncCursorPage[InvoiceListBreakdownsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "starting_on": starting_on,
                        "credit_type_id": credit_type_id,
                        "limit": limit,
                        "next_page": next_page,
                        "skip_zero_qty_line_items": skip_zero_qty_line_items,
                        "sort": sort,
                        "status": status,
                        "window_size": window_size,
                    },
                    invoice_list_breakdowns_params.InvoiceListBreakdownsParams,
                ),
            ),
            model=InvoiceListBreakdownsResponse,
        )


class InvoicesResourceWithRawResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.retrieve = to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.list = to_raw_response_wrapper(
            invoices.list,
        )
        self.add_charge = to_raw_response_wrapper(
            invoices.add_charge,
        )
        self.list_breakdowns = to_raw_response_wrapper(
            invoices.list_breakdowns,
        )


class AsyncInvoicesResourceWithRawResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.retrieve = async_to_raw_response_wrapper(
            invoices.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            invoices.list,
        )
        self.add_charge = async_to_raw_response_wrapper(
            invoices.add_charge,
        )
        self.list_breakdowns = async_to_raw_response_wrapper(
            invoices.list_breakdowns,
        )


class InvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: InvoicesResource) -> None:
        self._invoices = invoices

        self.retrieve = to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            invoices.list,
        )
        self.add_charge = to_streamed_response_wrapper(
            invoices.add_charge,
        )
        self.list_breakdowns = to_streamed_response_wrapper(
            invoices.list_breakdowns,
        )


class AsyncInvoicesResourceWithStreamingResponse:
    def __init__(self, invoices: AsyncInvoicesResource) -> None:
        self._invoices = invoices

        self.retrieve = async_to_streamed_response_wrapper(
            invoices.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            invoices.list,
        )
        self.add_charge = async_to_streamed_response_wrapper(
            invoices.add_charge,
        )
        self.list_breakdowns = async_to_streamed_response_wrapper(
            invoices.list_breakdowns,
        )
