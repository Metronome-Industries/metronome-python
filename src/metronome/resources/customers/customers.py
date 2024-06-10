# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime

import httpx

from .plans import (
    PlansResource,
    AsyncPlansResource,
    PlansResourceWithRawResponse,
    AsyncPlansResourceWithRawResponse,
    PlansResourceWithStreamingResponse,
    AsyncPlansResourceWithStreamingResponse,
)
from .alerts import (
    AlertsResource,
    AsyncAlertsResource,
    AlertsResourceWithRawResponse,
    AsyncAlertsResourceWithRawResponse,
    AlertsResourceWithStreamingResponse,
    AsyncAlertsResourceWithStreamingResponse,
)
from ...types import (
    customer_list_params,
    customer_create_params,
    customer_archive_params,
    customer_set_name_params,
    customer_list_costs_params,
    customer_update_config_params,
    customer_set_ingest_aliases_params,
    customer_list_billable_metrics_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .billing_config import (
    BillingConfigResource,
    AsyncBillingConfigResource,
    BillingConfigResourceWithRawResponse,
    AsyncBillingConfigResourceWithRawResponse,
    BillingConfigResourceWithStreamingResponse,
    AsyncBillingConfigResourceWithStreamingResponse,
)
from ...types.customer_detail import CustomerDetail
from ...types.customer_create_response import CustomerCreateResponse
from ...types.customer_archive_response import CustomerArchiveResponse
from ...types.customer_retrieve_response import CustomerRetrieveResponse
from ...types.customer_set_name_response import CustomerSetNameResponse
from ...types.customer_list_costs_response import CustomerListCostsResponse
from ...types.customer_list_billable_metrics_response import CustomerListBillableMetricsResponse

__all__ = ["CustomersResource", "AsyncCustomersResource"]


class CustomersResource(SyncAPIResource):
    @cached_property
    def alerts(self) -> AlertsResource:
        return AlertsResource(self._client)

    @cached_property
    def plans(self) -> PlansResource:
        return PlansResource(self._client)

    @cached_property
    def invoices(self) -> InvoicesResource:
        return InvoicesResource(self._client)

    @cached_property
    def billing_config(self) -> BillingConfigResource:
        return BillingConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        billing_config: customer_create_params.BillingConfig | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ingest_aliases: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerCreateResponse:
        """
        Create a new customer

        Args:
          external_id: (deprecated, use ingest_aliases instead) the first ID (Metronome ID or ingest
              alias) that can be used in usage events

          ingest_aliases: Aliases that can be used to refer to this customer in usage events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/customers",
            body=maybe_transform(
                {
                    "name": name,
                    "billing_config": billing_config,
                    "custom_fields": custom_fields,
                    "external_id": external_id,
                    "ingest_aliases": ingest_aliases,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreateResponse,
        )

    def retrieve(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerRetrieveResponse:
        """
        Get a customer by Metronome ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get(
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        ingest_alias: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        only_archived: bool | NotGiven = NOT_GIVEN,
        salesforce_account_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[CustomerDetail]:
        """
        List all customers.

        Args:
          customer_ids: Filter the customer list by customer_id. Up to 100 ids can be provided.

          ingest_alias: Filter the customer list by ingest_alias

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          only_archived: Filter the customer list by only archived customers.

          salesforce_account_ids: Filter the customer list by salesforce_account_id. Up to 100 ids can be
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/customers",
            page=SyncCursorPage[CustomerDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_ids": customer_ids,
                        "ingest_alias": ingest_alias,
                        "limit": limit,
                        "next_page": next_page,
                        "only_archived": only_archived,
                        "salesforce_account_ids": salesforce_account_ids,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=CustomerDetail,
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
    ) -> CustomerArchiveResponse:
        """
        Archive a customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/customers/archive",
            body=maybe_transform({"id": id}, customer_archive_params.CustomerArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerArchiveResponse,
        )

    def list_billable_metrics(
        self,
        customer_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        on_current_plan: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[CustomerListBillableMetricsResponse]:
        """
        List all billable metrics.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          on_current_plan: If true, the list of metrics will be filtered to just ones that are on the
              customer's current plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/billable-metrics",
            page=SyncCursorPage[CustomerListBillableMetricsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                        "on_current_plan": on_current_plan,
                    },
                    customer_list_billable_metrics_params.CustomerListBillableMetricsParams,
                ),
            ),
            model=CustomerListBillableMetricsResponse,
        )

    def list_costs(
        self,
        customer_id: str,
        *,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[CustomerListCostsResponse]:
        """
        Fetch daily pending costs for the specified customer, broken down by credit type
        and line items. Note: this is not supported for customers whose plan includes a
        UNIQUE-type billable metric.

        Args:
          ending_before: RFC 3339 timestamp (exclusive)

          starting_on: RFC 3339 timestamp (inclusive)

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
            f"/customers/{customer_id}/costs",
            page=SyncCursorPage[CustomerListCostsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "starting_on": starting_on,
                        "limit": limit,
                        "next_page": next_page,
                    },
                    customer_list_costs_params.CustomerListCostsParams,
                ),
            ),
            model=CustomerListCostsResponse,
        )

    def set_ingest_aliases(
        self,
        customer_id: str,
        *,
        ingest_aliases: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets the ingest aliases for a customer.

        Ingest aliases can be used in the
        `customer_id` field when sending usage events to Metronome. This call is
        idempotent. It fully replaces the set of ingest aliases for the given customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/customers/{customer_id}/setIngestAliases",
            body=maybe_transform(
                {"ingest_aliases": ingest_aliases}, customer_set_ingest_aliases_params.CustomerSetIngestAliasesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_name(
        self,
        customer_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSetNameResponse:
        """
        Updates the specified customer's name.

        Args:
          name: The new name for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/customers/{customer_id}/setName",
            body=maybe_transform({"name": name}, customer_set_name_params.CustomerSetNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetNameResponse,
        )

    def update_config(
        self,
        customer_id: str,
        *,
        leave_stripe_invoices_in_draft: Optional[bool] | NotGiven = NOT_GIVEN,
        salesforce_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates the specified customer's config.

        Args:
          leave_stripe_invoices_in_draft: Leave in draft or set to auto-advance on invoices sent to Stripe. Falls back to
              the client-level config if unset, which defaults to true if unset.

          salesforce_account_id: The Salesforce account ID for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/customers/{customer_id}/updateConfig",
            body=maybe_transform(
                {
                    "leave_stripe_invoices_in_draft": leave_stripe_invoices_in_draft,
                    "salesforce_account_id": salesforce_account_id,
                },
                customer_update_config_params.CustomerUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCustomersResource(AsyncAPIResource):
    @cached_property
    def alerts(self) -> AsyncAlertsResource:
        return AsyncAlertsResource(self._client)

    @cached_property
    def plans(self) -> AsyncPlansResource:
        return AsyncPlansResource(self._client)

    @cached_property
    def invoices(self) -> AsyncInvoicesResource:
        return AsyncInvoicesResource(self._client)

    @cached_property
    def billing_config(self) -> AsyncBillingConfigResource:
        return AsyncBillingConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        billing_config: customer_create_params.BillingConfig | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        external_id: str | NotGiven = NOT_GIVEN,
        ingest_aliases: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerCreateResponse:
        """
        Create a new customer

        Args:
          external_id: (deprecated, use ingest_aliases instead) the first ID (Metronome ID or ingest
              alias) that can be used in usage events

          ingest_aliases: Aliases that can be used to refer to this customer in usage events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/customers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "billing_config": billing_config,
                    "custom_fields": custom_fields,
                    "external_id": external_id,
                    "ingest_aliases": ingest_aliases,
                },
                customer_create_params.CustomerCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerCreateResponse,
        )

    async def retrieve(
        self,
        customer_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerRetrieveResponse:
        """
        Get a customer by Metronome ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._get(
            f"/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        ingest_alias: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        only_archived: bool | NotGiven = NOT_GIVEN,
        salesforce_account_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomerDetail, AsyncCursorPage[CustomerDetail]]:
        """
        List all customers.

        Args:
          customer_ids: Filter the customer list by customer_id. Up to 100 ids can be provided.

          ingest_alias: Filter the customer list by ingest_alias

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          only_archived: Filter the customer list by only archived customers.

          salesforce_account_ids: Filter the customer list by salesforce_account_id. Up to 100 ids can be
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/customers",
            page=AsyncCursorPage[CustomerDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "customer_ids": customer_ids,
                        "ingest_alias": ingest_alias,
                        "limit": limit,
                        "next_page": next_page,
                        "only_archived": only_archived,
                        "salesforce_account_ids": salesforce_account_ids,
                    },
                    customer_list_params.CustomerListParams,
                ),
            ),
            model=CustomerDetail,
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
    ) -> CustomerArchiveResponse:
        """
        Archive a customer

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/customers/archive",
            body=await async_maybe_transform({"id": id}, customer_archive_params.CustomerArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerArchiveResponse,
        )

    def list_billable_metrics(
        self,
        customer_id: str,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        on_current_plan: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomerListBillableMetricsResponse, AsyncCursorPage[CustomerListBillableMetricsResponse]]:
        """
        List all billable metrics.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          on_current_plan: If true, the list of metrics will be filtered to just ones that are on the
              customer's current plan

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get_api_list(
            f"/customers/{customer_id}/billable-metrics",
            page=AsyncCursorPage[CustomerListBillableMetricsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                        "on_current_plan": on_current_plan,
                    },
                    customer_list_billable_metrics_params.CustomerListBillableMetricsParams,
                ),
            ),
            model=CustomerListBillableMetricsResponse,
        )

    def list_costs(
        self,
        customer_id: str,
        *,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomerListCostsResponse, AsyncCursorPage[CustomerListCostsResponse]]:
        """
        Fetch daily pending costs for the specified customer, broken down by credit type
        and line items. Note: this is not supported for customers whose plan includes a
        UNIQUE-type billable metric.

        Args:
          ending_before: RFC 3339 timestamp (exclusive)

          starting_on: RFC 3339 timestamp (inclusive)

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
            f"/customers/{customer_id}/costs",
            page=AsyncCursorPage[CustomerListCostsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "starting_on": starting_on,
                        "limit": limit,
                        "next_page": next_page,
                    },
                    customer_list_costs_params.CustomerListCostsParams,
                ),
            ),
            model=CustomerListCostsResponse,
        )

    async def set_ingest_aliases(
        self,
        customer_id: str,
        *,
        ingest_aliases: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets the ingest aliases for a customer.

        Ingest aliases can be used in the
        `customer_id` field when sending usage events to Metronome. This call is
        idempotent. It fully replaces the set of ingest aliases for the given customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/customers/{customer_id}/setIngestAliases",
            body=await async_maybe_transform(
                {"ingest_aliases": ingest_aliases}, customer_set_ingest_aliases_params.CustomerSetIngestAliasesParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_name(
        self,
        customer_id: str,
        *,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomerSetNameResponse:
        """
        Updates the specified customer's name.

        Args:
          name: The new name for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/customers/{customer_id}/setName",
            body=await async_maybe_transform({"name": name}, customer_set_name_params.CustomerSetNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetNameResponse,
        )

    async def update_config(
        self,
        customer_id: str,
        *,
        leave_stripe_invoices_in_draft: Optional[bool] | NotGiven = NOT_GIVEN,
        salesforce_account_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates the specified customer's config.

        Args:
          leave_stripe_invoices_in_draft: Leave in draft or set to auto-advance on invoices sent to Stripe. Falls back to
              the client-level config if unset, which defaults to true if unset.

          salesforce_account_id: The Salesforce account ID for the customer

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/customers/{customer_id}/updateConfig",
            body=await async_maybe_transform(
                {
                    "leave_stripe_invoices_in_draft": leave_stripe_invoices_in_draft,
                    "salesforce_account_id": salesforce_account_id,
                },
                customer_update_config_params.CustomerUpdateConfigParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CustomersResourceWithRawResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = to_raw_response_wrapper(
            customers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            customers.list,
        )
        self.archive = to_raw_response_wrapper(
            customers.archive,
        )
        self.list_billable_metrics = to_raw_response_wrapper(
            customers.list_billable_metrics,
        )
        self.list_costs = to_raw_response_wrapper(
            customers.list_costs,
        )
        self.set_ingest_aliases = to_raw_response_wrapper(
            customers.set_ingest_aliases,
        )
        self.set_name = to_raw_response_wrapper(
            customers.set_name,
        )
        self.update_config = to_raw_response_wrapper(
            customers.update_config,
        )

    @cached_property
    def alerts(self) -> AlertsResourceWithRawResponse:
        return AlertsResourceWithRawResponse(self._customers.alerts)

    @cached_property
    def plans(self) -> PlansResourceWithRawResponse:
        return PlansResourceWithRawResponse(self._customers.plans)

    @cached_property
    def invoices(self) -> InvoicesResourceWithRawResponse:
        return InvoicesResourceWithRawResponse(self._customers.invoices)

    @cached_property
    def billing_config(self) -> BillingConfigResourceWithRawResponse:
        return BillingConfigResourceWithRawResponse(self._customers.billing_config)


class AsyncCustomersResourceWithRawResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_raw_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            customers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            customers.list,
        )
        self.archive = async_to_raw_response_wrapper(
            customers.archive,
        )
        self.list_billable_metrics = async_to_raw_response_wrapper(
            customers.list_billable_metrics,
        )
        self.list_costs = async_to_raw_response_wrapper(
            customers.list_costs,
        )
        self.set_ingest_aliases = async_to_raw_response_wrapper(
            customers.set_ingest_aliases,
        )
        self.set_name = async_to_raw_response_wrapper(
            customers.set_name,
        )
        self.update_config = async_to_raw_response_wrapper(
            customers.update_config,
        )

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithRawResponse:
        return AsyncAlertsResourceWithRawResponse(self._customers.alerts)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithRawResponse:
        return AsyncPlansResourceWithRawResponse(self._customers.plans)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithRawResponse:
        return AsyncInvoicesResourceWithRawResponse(self._customers.invoices)

    @cached_property
    def billing_config(self) -> AsyncBillingConfigResourceWithRawResponse:
        return AsyncBillingConfigResourceWithRawResponse(self._customers.billing_config)


class CustomersResourceWithStreamingResponse:
    def __init__(self, customers: CustomersResource) -> None:
        self._customers = customers

        self.create = to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            customers.list,
        )
        self.archive = to_streamed_response_wrapper(
            customers.archive,
        )
        self.list_billable_metrics = to_streamed_response_wrapper(
            customers.list_billable_metrics,
        )
        self.list_costs = to_streamed_response_wrapper(
            customers.list_costs,
        )
        self.set_ingest_aliases = to_streamed_response_wrapper(
            customers.set_ingest_aliases,
        )
        self.set_name = to_streamed_response_wrapper(
            customers.set_name,
        )
        self.update_config = to_streamed_response_wrapper(
            customers.update_config,
        )

    @cached_property
    def alerts(self) -> AlertsResourceWithStreamingResponse:
        return AlertsResourceWithStreamingResponse(self._customers.alerts)

    @cached_property
    def plans(self) -> PlansResourceWithStreamingResponse:
        return PlansResourceWithStreamingResponse(self._customers.plans)

    @cached_property
    def invoices(self) -> InvoicesResourceWithStreamingResponse:
        return InvoicesResourceWithStreamingResponse(self._customers.invoices)

    @cached_property
    def billing_config(self) -> BillingConfigResourceWithStreamingResponse:
        return BillingConfigResourceWithStreamingResponse(self._customers.billing_config)


class AsyncCustomersResourceWithStreamingResponse:
    def __init__(self, customers: AsyncCustomersResource) -> None:
        self._customers = customers

        self.create = async_to_streamed_response_wrapper(
            customers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            customers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            customers.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            customers.archive,
        )
        self.list_billable_metrics = async_to_streamed_response_wrapper(
            customers.list_billable_metrics,
        )
        self.list_costs = async_to_streamed_response_wrapper(
            customers.list_costs,
        )
        self.set_ingest_aliases = async_to_streamed_response_wrapper(
            customers.set_ingest_aliases,
        )
        self.set_name = async_to_streamed_response_wrapper(
            customers.set_name,
        )
        self.update_config = async_to_streamed_response_wrapper(
            customers.update_config,
        )

    @cached_property
    def alerts(self) -> AsyncAlertsResourceWithStreamingResponse:
        return AsyncAlertsResourceWithStreamingResponse(self._customers.alerts)

    @cached_property
    def plans(self) -> AsyncPlansResourceWithStreamingResponse:
        return AsyncPlansResourceWithStreamingResponse(self._customers.plans)

    @cached_property
    def invoices(self) -> AsyncInvoicesResourceWithStreamingResponse:
        return AsyncInvoicesResourceWithStreamingResponse(self._customers.invoices)

    @cached_property
    def billing_config(self) -> AsyncBillingConfigResourceWithStreamingResponse:
        return AsyncBillingConfigResourceWithStreamingResponse(self._customers.billing_config)
