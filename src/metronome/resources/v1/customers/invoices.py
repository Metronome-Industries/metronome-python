# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
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
        skip_zero_qty_line_items: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceRetrieveResponse:
        """
        Retrieve detailed information for a specific invoice by its unique identifier.
        This endpoint returns comprehensive invoice data including line items, applied
        credits, totals, and billing period details for both finalized and draft
        invoices.

        ### Use this endpoint to:

        - Display historical invoice details in customer-facing dashboards or billing
          portals.
        - Retrieve current month draft invoices to show customers their month-to-date
          spend.
        - Access finalized invoices for historical billing records and payment
          reconciliation.
        - Validate customer pricing and credit applications for customer support
          queries.

        ### Key response fields:

        Invoice status (DRAFT, FINALIZED, VOID) Billing period start and end dates Total
        amount and amount due after credits Detailed line items broken down by:

        - Customer and contract information
        - Invoice line item type
        - Product/service name and ID
        - Quantity consumed
        - Unit and total price
        - Time period for usage-based charges
        - Applied credits or prepaid commitments

        ### Usage guidelines:

        - Draft invoices update in real-time as usage is reported and may change before
          finalization
        - The response includes both usage-based line items (e.g., API calls, data
          processed) and scheduled charges (e.g., monthly subscriptions, commitment
          fees)
        - Credit and commitment applications are shown as separate line items with
          negative amounts
        - For voided invoices, the response will indicate VOID status but retain all
          original line item details

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
        credit_type_id: str | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        skip_zero_qty_line_items: bool | Omit = omit,
        sort: Literal["date_asc", "date_desc"] | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Invoice]:
        """
        Retrieves a paginated list of invoices for a specific customer, with flexible
        filtering options to narrow results by status, date range, credit type, and
        more. This endpoint provides a comprehensive view of a customer's billing
        history and current charges, supporting both real-time billing dashboards and
        historical reporting needs.

        ### Use this endpoint to:

        - Display historical invoice details in customer-facing dashboards or billing
          portals.
        - Retrieve current month draft invoices to show customers their month-to-date
          spend.
        - Access finalized invoices for historical billing records and payment
          reconciliation.
        - Validate customer pricing and credit applications for customer support
          queries.
        - Generate financial reports by filtering invoices within specific date ranges

        ### Key response fields:

        Array of invoice objects containing:

        - Invoice ID and status (DRAFT, FINALIZED, VOID)
        - Invoice type (USAGE, SCHEDULED)
        - Billing period start and end dates
        - Issue date and due date
        - Total amount, subtotal, and amount due
        - Applied credits summary
        - Contract ID reference
        - External billing provider status (if integrated with Stripe, etc.)
        - Pagination metadata `next_page` cursor

        ### Usage guidelines:

        - The endpoint returns invoice summaries; use the Get Invoice endpoint for
          detailed line items
        - Draft invoices are continuously updated as new usage is reported and will show
          real-time spend
        - Results are ordered by creation date descending by default (newest first)
        - When filtering by date range, the filter applies to the billing period, not
          the issue date
        - For customers with many invoices, implement pagination to ensure all results
          are retrieved External billing provider statuses (like Stripe payment status)
          are included when applicable
        - Voided invoices are included in results by default unless filtered out by
          status

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceAddChargeResponse:
        """Add a one time charge to the specified invoice.

        This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

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
        credit_type_id: str | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        skip_zero_qty_line_items: bool | Omit = omit,
        sort: Literal["date_asc", "date_desc"] | Omit = omit,
        status: str | Omit = omit,
        window_size: Literal["HOUR", "DAY"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[InvoiceListBreakdownsResponse]:
        """
        Retrieve granular time-series breakdowns of invoice data at hourly or daily
        intervals. This endpoint transforms standard invoices into detailed timelines,
        enabling you to track usage patterns, identify consumption spikes, and provide
        customers with transparency into their billing details throughout the billing
        period.

        ### Use this endpoint to:

        - Build usage analytics dashboards showing daily or hourly consumption trends
        - Identify peak usage periods for capacity planning and cost optimization
        - Generate detailed billing reports for finance teams and customer success
        - Troubleshoot billing disputes by examining usage patterns at specific times
        - Power real-time cost monitoring and alerting systems

        ### Key response fields:

        An array of BreakdownInvoice objects, each containing:

        - All standard invoice fields (ID, customer, commit, line items, totals, status)
        - Line items with quantities and costs for that specific period
        - `breakdown_start_timestamp`: Start of the specific time window
        - `breakdown_end_timestamp`: End of the specific time window
        - `next_page`: Pagination cursor for large result sets

        ### Usage guidelines:

        - Time granularity: Set `window_size` to hour or day based on your analysis
          needs
        - Response limits: Daily breakdowns return up to 35 days; hourly breakdowns
          return up to 24 hours per request
        - Date filtering: Use `starting_on` and `ending_before` to focus on specific
          periods
        - Performance: For large date ranges, use pagination to retrieve all data
          efficiently
        - Backdated usage: If usage events arrive after invoice finalization, breakdowns
          will reflect the updated usage
        - Zero quantity filtering: Use `skip_zero_qty_line_items=true` to exclude
          periods with no usage

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

    def retrieve_pdf(
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
    ) -> BinaryAPIResponse:
        """Retrieve a PDF version of a specific invoice by its unique identifier.

        This
        endpoint generates a professionally formatted invoice document suitable for
        sharing with customers, accounting teams, or for record-keeping purposes.

        ### Use this endpoint to:

        - Provide customers with downloadable or emailable copies of their invoices
        - Support accounting and finance teams with official billing documents
        - Maintain accurate records of billing transactions for audits and compliance

        ### Key response details:

        - The response is a binary PDF file representing the full invoice
        - The PDF includes all standard invoice information such as line items, totals,
          billing period, and customer details
        - The document is formatted for clarity and professionalism, suitable for
          official use

        ### Usage guidelines:

        - Ensure the `invoice_id` corresponds to an existing invoice for the specified
          `customer_id`
        - The PDF is generated on-demand; frequent requests for the same invoice may
          impact performance
        - Use appropriate headers to handle the binary response in your application
          (e.g., setting `Content-Type: application/pdf`)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._get(
            f"/v1/customers/{customer_id}/invoices/{invoice_id}/pdf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
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
        skip_zero_qty_line_items: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceRetrieveResponse:
        """
        Retrieve detailed information for a specific invoice by its unique identifier.
        This endpoint returns comprehensive invoice data including line items, applied
        credits, totals, and billing period details for both finalized and draft
        invoices.

        ### Use this endpoint to:

        - Display historical invoice details in customer-facing dashboards or billing
          portals.
        - Retrieve current month draft invoices to show customers their month-to-date
          spend.
        - Access finalized invoices for historical billing records and payment
          reconciliation.
        - Validate customer pricing and credit applications for customer support
          queries.

        ### Key response fields:

        Invoice status (DRAFT, FINALIZED, VOID) Billing period start and end dates Total
        amount and amount due after credits Detailed line items broken down by:

        - Customer and contract information
        - Invoice line item type
        - Product/service name and ID
        - Quantity consumed
        - Unit and total price
        - Time period for usage-based charges
        - Applied credits or prepaid commitments

        ### Usage guidelines:

        - Draft invoices update in real-time as usage is reported and may change before
          finalization
        - The response includes both usage-based line items (e.g., API calls, data
          processed) and scheduled charges (e.g., monthly subscriptions, commitment
          fees)
        - Credit and commitment applications are shown as separate line items with
          negative amounts
        - For voided invoices, the response will indicate VOID status but retain all
          original line item details

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
        credit_type_id: str | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        skip_zero_qty_line_items: bool | Omit = omit,
        sort: Literal["date_asc", "date_desc"] | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Invoice, AsyncCursorPage[Invoice]]:
        """
        Retrieves a paginated list of invoices for a specific customer, with flexible
        filtering options to narrow results by status, date range, credit type, and
        more. This endpoint provides a comprehensive view of a customer's billing
        history and current charges, supporting both real-time billing dashboards and
        historical reporting needs.

        ### Use this endpoint to:

        - Display historical invoice details in customer-facing dashboards or billing
          portals.
        - Retrieve current month draft invoices to show customers their month-to-date
          spend.
        - Access finalized invoices for historical billing records and payment
          reconciliation.
        - Validate customer pricing and credit applications for customer support
          queries.
        - Generate financial reports by filtering invoices within specific date ranges

        ### Key response fields:

        Array of invoice objects containing:

        - Invoice ID and status (DRAFT, FINALIZED, VOID)
        - Invoice type (USAGE, SCHEDULED)
        - Billing period start and end dates
        - Issue date and due date
        - Total amount, subtotal, and amount due
        - Applied credits summary
        - Contract ID reference
        - External billing provider status (if integrated with Stripe, etc.)
        - Pagination metadata `next_page` cursor

        ### Usage guidelines:

        - The endpoint returns invoice summaries; use the Get Invoice endpoint for
          detailed line items
        - Draft invoices are continuously updated as new usage is reported and will show
          real-time spend
        - Results are ordered by creation date descending by default (newest first)
        - When filtering by date range, the filter applies to the billing period, not
          the issue date
        - For customers with many invoices, implement pagination to ensure all results
          are retrieved External billing provider statuses (like Stripe payment status)
          are included when applicable
        - Voided invoices are included in results by default unless filtered out by
          status

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvoiceAddChargeResponse:
        """Add a one time charge to the specified invoice.

        This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

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
        credit_type_id: str | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        skip_zero_qty_line_items: bool | Omit = omit,
        sort: Literal["date_asc", "date_desc"] | Omit = omit,
        status: str | Omit = omit,
        window_size: Literal["HOUR", "DAY"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InvoiceListBreakdownsResponse, AsyncCursorPage[InvoiceListBreakdownsResponse]]:
        """
        Retrieve granular time-series breakdowns of invoice data at hourly or daily
        intervals. This endpoint transforms standard invoices into detailed timelines,
        enabling you to track usage patterns, identify consumption spikes, and provide
        customers with transparency into their billing details throughout the billing
        period.

        ### Use this endpoint to:

        - Build usage analytics dashboards showing daily or hourly consumption trends
        - Identify peak usage periods for capacity planning and cost optimization
        - Generate detailed billing reports for finance teams and customer success
        - Troubleshoot billing disputes by examining usage patterns at specific times
        - Power real-time cost monitoring and alerting systems

        ### Key response fields:

        An array of BreakdownInvoice objects, each containing:

        - All standard invoice fields (ID, customer, commit, line items, totals, status)
        - Line items with quantities and costs for that specific period
        - `breakdown_start_timestamp`: Start of the specific time window
        - `breakdown_end_timestamp`: End of the specific time window
        - `next_page`: Pagination cursor for large result sets

        ### Usage guidelines:

        - Time granularity: Set `window_size` to hour or day based on your analysis
          needs
        - Response limits: Daily breakdowns return up to 35 days; hourly breakdowns
          return up to 24 hours per request
        - Date filtering: Use `starting_on` and `ending_before` to focus on specific
          periods
        - Performance: For large date ranges, use pagination to retrieve all data
          efficiently
        - Backdated usage: If usage events arrive after invoice finalization, breakdowns
          will reflect the updated usage
        - Zero quantity filtering: Use `skip_zero_qty_line_items=true` to exclude
          periods with no usage

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

    async def retrieve_pdf(
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
    ) -> AsyncBinaryAPIResponse:
        """Retrieve a PDF version of a specific invoice by its unique identifier.

        This
        endpoint generates a professionally formatted invoice document suitable for
        sharing with customers, accounting teams, or for record-keeping purposes.

        ### Use this endpoint to:

        - Provide customers with downloadable or emailable copies of their invoices
        - Support accounting and finance teams with official billing documents
        - Maintain accurate records of billing transactions for audits and compliance

        ### Key response details:

        - The response is a binary PDF file representing the full invoice
        - The PDF includes all standard invoice information such as line items, totals,
          billing period, and customer details
        - The document is formatted for clarity and professionalism, suitable for
          official use

        ### Usage guidelines:

        - Ensure the `invoice_id` corresponds to an existing invoice for the specified
          `customer_id`
        - The PDF is generated on-demand; frequent requests for the same invoice may
          impact performance
        - Use appropriate headers to handle the binary response in your application
          (e.g., setting `Content-Type: application/pdf`)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not invoice_id:
            raise ValueError(f"Expected a non-empty value for `invoice_id` but received {invoice_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._get(
            f"/v1/customers/{customer_id}/invoices/{invoice_id}/pdf",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
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
        self.retrieve_pdf = to_custom_raw_response_wrapper(
            invoices.retrieve_pdf,
            BinaryAPIResponse,
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
        self.retrieve_pdf = async_to_custom_raw_response_wrapper(
            invoices.retrieve_pdf,
            AsyncBinaryAPIResponse,
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
        self.retrieve_pdf = to_custom_streamed_response_wrapper(
            invoices.retrieve_pdf,
            StreamedBinaryAPIResponse,
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
        self.retrieve_pdf = async_to_custom_streamed_response_wrapper(
            invoices.retrieve_pdf,
            AsyncStreamedBinaryAPIResponse,
        )
