# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.customers import credit_list_params, credit_create_params, credit_update_end_date_params
from ...types.customers.credit_list_response import CreditListResponse
from ...types.customers.credit_create_response import CreditCreateResponse
from ...types.customers.credit_update_end_date_response import CreditUpdateEndDateResponse

__all__ = ["CreditsResource", "AsyncCreditsResource"]


class CreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        access_schedule: credit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        applicable_contract_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_tags: List[str] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCreateResponse:
        """
        Create a new credit at the customer level.

        Args:
          access_schedule: Schedule for distributing the credit to the customer.

          priority: If multiple credits or commits are applicable, the one with the lower priority
              will apply first.

          applicable_contract_ids: Which contract the credit applies to. If not provided, the credit applies to all
              contracts.

          applicable_product_ids: Which products the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          applicable_product_tags: Which tags the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          description: Used only in UI/API. It is not exposed to end customers.

          name: displayed on invoices

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/customerCredits/create",
            body=maybe_transform(
                {
                    "access_schedule": access_schedule,
                    "customer_id": customer_id,
                    "priority": priority,
                    "product_id": product_id,
                    "applicable_contract_ids": applicable_contract_ids,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "custom_fields": custom_fields,
                    "description": description,
                    "name": name,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                },
                credit_create_params.CreditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCreateResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        credit_id: str | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_contract_credits: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditListResponse:
        """
        List credits.

        Args:
          covering_date: Return only credits that have access schedules that "cover" the provided date

          effective_before: Include only credits that have any access before the provided date (exclusive)

          include_archived: Include credits from archived contracts.

          include_contract_credits: Include credits on the contract level.

          include_ledgers: Include credit ledgers in the response. Setting this flag may cause the query to
              be slower.

          next_page: The next page token from a previous response.

          starting_at: Include only credits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/customerCredits/list",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "credit_id": credit_id,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_contract_credits": include_contract_credits,
                    "include_ledgers": include_ledgers,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                credit_list_params.CreditListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditListResponse,
        )

    def update_end_date(
        self,
        *,
        access_ending_before: Union[str, datetime],
        credit_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditUpdateEndDateResponse:
        """
        Update the end date of a credit

        Args:
          access_ending_before: RFC 3339 timestamp indicating when access to the credit will end and it will no
              longer be possible to draw it down (exclusive).

          credit_id: ID of the commit to update

          customer_id: ID of the customer whose credit is to be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/customerCredits/updateEndDate",
            body=maybe_transform(
                {
                    "access_ending_before": access_ending_before,
                    "credit_id": credit_id,
                    "customer_id": customer_id,
                },
                credit_update_end_date_params.CreditUpdateEndDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditUpdateEndDateResponse,
        )


class AsyncCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        access_schedule: credit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        applicable_contract_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_tags: List[str] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditCreateResponse:
        """
        Create a new credit at the customer level.

        Args:
          access_schedule: Schedule for distributing the credit to the customer.

          priority: If multiple credits or commits are applicable, the one with the lower priority
              will apply first.

          applicable_contract_ids: Which contract the credit applies to. If not provided, the credit applies to all
              contracts.

          applicable_product_ids: Which products the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          applicable_product_tags: Which tags the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          description: Used only in UI/API. It is not exposed to end customers.

          name: displayed on invoices

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/customerCredits/create",
            body=await async_maybe_transform(
                {
                    "access_schedule": access_schedule,
                    "customer_id": customer_id,
                    "priority": priority,
                    "product_id": product_id,
                    "applicable_contract_ids": applicable_contract_ids,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "custom_fields": custom_fields,
                    "description": description,
                    "name": name,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                },
                credit_create_params.CreditCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditCreateResponse,
        )

    async def list(
        self,
        *,
        customer_id: str,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        credit_id: str | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_contract_credits: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditListResponse:
        """
        List credits.

        Args:
          covering_date: Return only credits that have access schedules that "cover" the provided date

          effective_before: Include only credits that have any access before the provided date (exclusive)

          include_archived: Include credits from archived contracts.

          include_contract_credits: Include credits on the contract level.

          include_ledgers: Include credit ledgers in the response. Setting this flag may cause the query to
              be slower.

          next_page: The next page token from a previous response.

          starting_at: Include only credits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/customerCredits/list",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "credit_id": credit_id,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_contract_credits": include_contract_credits,
                    "include_ledgers": include_ledgers,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                credit_list_params.CreditListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditListResponse,
        )

    async def update_end_date(
        self,
        *,
        access_ending_before: Union[str, datetime],
        credit_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditUpdateEndDateResponse:
        """
        Update the end date of a credit

        Args:
          access_ending_before: RFC 3339 timestamp indicating when access to the credit will end and it will no
              longer be possible to draw it down (exclusive).

          credit_id: ID of the commit to update

          customer_id: ID of the customer whose credit is to be updated

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/customerCredits/updateEndDate",
            body=await async_maybe_transform(
                {
                    "access_ending_before": access_ending_before,
                    "credit_id": credit_id,
                    "customer_id": customer_id,
                },
                credit_update_end_date_params.CreditUpdateEndDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditUpdateEndDateResponse,
        )


class CreditsResourceWithRawResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.create = to_raw_response_wrapper(
            credits.create,
        )
        self.list = to_raw_response_wrapper(
            credits.list,
        )
        self.update_end_date = to_raw_response_wrapper(
            credits.update_end_date,
        )


class AsyncCreditsResourceWithRawResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.create = async_to_raw_response_wrapper(
            credits.create,
        )
        self.list = async_to_raw_response_wrapper(
            credits.list,
        )
        self.update_end_date = async_to_raw_response_wrapper(
            credits.update_end_date,
        )


class CreditsResourceWithStreamingResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.create = to_streamed_response_wrapper(
            credits.create,
        )
        self.list = to_streamed_response_wrapper(
            credits.list,
        )
        self.update_end_date = to_streamed_response_wrapper(
            credits.update_end_date,
        )


class AsyncCreditsResourceWithStreamingResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.create = async_to_streamed_response_wrapper(
            credits.create,
        )
        self.list = async_to_streamed_response_wrapper(
            credits.list,
        )
        self.update_end_date = async_to_streamed_response_wrapper(
            credits.update_end_date,
        )
