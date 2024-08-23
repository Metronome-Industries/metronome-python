# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal

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
from ...types.customers import commit_list_params, commit_create_params, commit_update_end_date_params
from ...types.customers.commit_list_response import CommitListResponse
from ...types.customers.commit_create_response import CommitCreateResponse
from ...types.customers.commit_update_end_date_response import CommitUpdateEndDateResponse

__all__ = ["CommitsResource", "AsyncCommitsResource"]


class CommitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommitsResourceWithRawResponse:
        return CommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommitsResourceWithStreamingResponse:
        return CommitsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        access_schedule: commit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        type: Literal["PREPAID", "POSTPAID"],
        applicable_contract_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_tags: List[str] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        invoice_contract_id: str | NotGiven = NOT_GIVEN,
        invoice_schedule: commit_create_params.InvoiceSchedule | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitCreateResponse:
        """
        Create a new commit at the customer level.

        Args:
          access_schedule: Schedule for distributing the commit to the customer. For "POSTPAID" commits
              only one schedule item is allowed and amount must match invoice_schedule total.

          priority: If multiple credits or commits are applicable, the one with the lower priority
              will apply first.

          applicable_contract_ids: Which contract the commit applies to. If not provided, the commit applies to all
              contracts.

          applicable_product_ids: Which products the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          applicable_product_tags: Which tags the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          description: Used only in UI/API. It is not exposed to end customers.

          invoice_contract_id: The contract that this commit will be billed on. This is required for "POSTPAID"
              commits and for "PREPAID" commits unless there is no invoice schedule above
              (i.e., the commit is 'free').

          invoice_schedule: Required for "POSTPAID" commits: the true up invoice will be generated at this
              time and only one schedule item is allowed; the total must match
              accesss_schedule amount. Optional for "PREPAID" commits: if not provided, this
              will be a "complimentary" commit with no invoice.

          name: displayed on invoices

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/customerCommits/create",
            body=maybe_transform(
                {
                    "access_schedule": access_schedule,
                    "customer_id": customer_id,
                    "priority": priority,
                    "product_id": product_id,
                    "type": type,
                    "applicable_contract_ids": applicable_contract_ids,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "custom_fields": custom_fields,
                    "description": description,
                    "invoice_contract_id": invoice_contract_id,
                    "invoice_schedule": invoice_schedule,
                    "name": name,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                },
                commit_create_params.CommitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitCreateResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        commit_id: str | NotGiven = NOT_GIVEN,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_contract_commits: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitListResponse:
        """
        List commits.

        Args:
          covering_date: Include only commits that have access schedules that "cover" the provided date

          effective_before: Include only commits that have any access before the provided date (exclusive)

          include_archived: Include commits from archived contracts.

          include_contract_commits: Include commits on the contract level.

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          next_page: The next page token from a previous response.

          starting_at: Include only commits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/customerCommits/list",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "commit_id": commit_id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_contract_commits": include_contract_commits,
                    "include_ledgers": include_ledgers,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                commit_list_params.CommitListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitListResponse,
        )

    def update_end_date(
        self,
        *,
        commit_id: str,
        customer_id: str,
        access_ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoices_ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitUpdateEndDateResponse:
        """
        Update the end date of a PREPAID commit

        Args:
          commit_id: ID of the commit to update. Only supports "PREPAID" commits.

          customer_id: ID of the customer whose commit is to be updated

          access_ending_before: RFC 3339 timestamp indicating when access to the commit will end and it will no
              longer be possible to draw it down (exclusive). If not provided, the access will
              not be updated.

          invoices_ending_before: RFC 3339 timestamp indicating when the commit will stop being invoiced
              (exclusive). If not provided, the invoice schedule will not be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/customerCommits/updateEndDate",
            body=maybe_transform(
                {
                    "commit_id": commit_id,
                    "customer_id": customer_id,
                    "access_ending_before": access_ending_before,
                    "invoices_ending_before": invoices_ending_before,
                },
                commit_update_end_date_params.CommitUpdateEndDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitUpdateEndDateResponse,
        )


class AsyncCommitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommitsResourceWithRawResponse:
        return AsyncCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommitsResourceWithStreamingResponse:
        return AsyncCommitsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        access_schedule: commit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        type: Literal["PREPAID", "POSTPAID"],
        applicable_contract_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_ids: List[str] | NotGiven = NOT_GIVEN,
        applicable_product_tags: List[str] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        invoice_contract_id: str | NotGiven = NOT_GIVEN,
        invoice_schedule: commit_create_params.InvoiceSchedule | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitCreateResponse:
        """
        Create a new commit at the customer level.

        Args:
          access_schedule: Schedule for distributing the commit to the customer. For "POSTPAID" commits
              only one schedule item is allowed and amount must match invoice_schedule total.

          priority: If multiple credits or commits are applicable, the one with the lower priority
              will apply first.

          applicable_contract_ids: Which contract the commit applies to. If not provided, the commit applies to all
              contracts.

          applicable_product_ids: Which products the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          applicable_product_tags: Which tags the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          description: Used only in UI/API. It is not exposed to end customers.

          invoice_contract_id: The contract that this commit will be billed on. This is required for "POSTPAID"
              commits and for "PREPAID" commits unless there is no invoice schedule above
              (i.e., the commit is 'free').

          invoice_schedule: Required for "POSTPAID" commits: the true up invoice will be generated at this
              time and only one schedule item is allowed; the total must match
              accesss_schedule amount. Optional for "PREPAID" commits: if not provided, this
              will be a "complimentary" commit with no invoice.

          name: displayed on invoices

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/customerCommits/create",
            body=await async_maybe_transform(
                {
                    "access_schedule": access_schedule,
                    "customer_id": customer_id,
                    "priority": priority,
                    "product_id": product_id,
                    "type": type,
                    "applicable_contract_ids": applicable_contract_ids,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "custom_fields": custom_fields,
                    "description": description,
                    "invoice_contract_id": invoice_contract_id,
                    "invoice_schedule": invoice_schedule,
                    "name": name,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                },
                commit_create_params.CommitCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitCreateResponse,
        )

    async def list(
        self,
        *,
        customer_id: str,
        commit_id: str | NotGiven = NOT_GIVEN,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_contract_commits: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitListResponse:
        """
        List commits.

        Args:
          covering_date: Include only commits that have access schedules that "cover" the provided date

          effective_before: Include only commits that have any access before the provided date (exclusive)

          include_archived: Include commits from archived contracts.

          include_contract_commits: Include commits on the contract level.

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          next_page: The next page token from a previous response.

          starting_at: Include only commits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/customerCommits/list",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "commit_id": commit_id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_contract_commits": include_contract_commits,
                    "include_ledgers": include_ledgers,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                commit_list_params.CommitListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitListResponse,
        )

    async def update_end_date(
        self,
        *,
        commit_id: str,
        customer_id: str,
        access_ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoices_ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitUpdateEndDateResponse:
        """
        Update the end date of a PREPAID commit

        Args:
          commit_id: ID of the commit to update. Only supports "PREPAID" commits.

          customer_id: ID of the customer whose commit is to be updated

          access_ending_before: RFC 3339 timestamp indicating when access to the commit will end and it will no
              longer be possible to draw it down (exclusive). If not provided, the access will
              not be updated.

          invoices_ending_before: RFC 3339 timestamp indicating when the commit will stop being invoiced
              (exclusive). If not provided, the invoice schedule will not be updated.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/customerCommits/updateEndDate",
            body=await async_maybe_transform(
                {
                    "commit_id": commit_id,
                    "customer_id": customer_id,
                    "access_ending_before": access_ending_before,
                    "invoices_ending_before": invoices_ending_before,
                },
                commit_update_end_date_params.CommitUpdateEndDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommitUpdateEndDateResponse,
        )


class CommitsResourceWithRawResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.create = to_raw_response_wrapper(
            commits.create,
        )
        self.list = to_raw_response_wrapper(
            commits.list,
        )
        self.update_end_date = to_raw_response_wrapper(
            commits.update_end_date,
        )


class AsyncCommitsResourceWithRawResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.create = async_to_raw_response_wrapper(
            commits.create,
        )
        self.list = async_to_raw_response_wrapper(
            commits.list,
        )
        self.update_end_date = async_to_raw_response_wrapper(
            commits.update_end_date,
        )


class CommitsResourceWithStreamingResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.create = to_streamed_response_wrapper(
            commits.create,
        )
        self.list = to_streamed_response_wrapper(
            commits.list,
        )
        self.update_end_date = to_streamed_response_wrapper(
            commits.update_end_date,
        )


class AsyncCommitsResourceWithStreamingResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.create = async_to_streamed_response_wrapper(
            commits.create,
        )
        self.list = async_to_streamed_response_wrapper(
            commits.list,
        )
        self.update_end_date = async_to_streamed_response_wrapper(
            commits.update_end_date,
        )
