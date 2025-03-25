# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from datetime import datetime

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ...types.v2 import (
    contract_edit_params,
    contract_list_params,
    contract_retrieve_params,
    contract_edit_commit_params,
    contract_edit_credit_params,
    contract_get_edit_history_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.contract_edit_response import ContractEditResponse
from ...types.v2.contract_list_response import ContractListResponse
from ...types.v2.contract_retrieve_response import ContractRetrieveResponse
from ...types.v2.contract_edit_commit_response import ContractEditCommitResponse
from ...types.v2.contract_edit_credit_response import ContractEditCreditResponse
from ...types.v2.contract_get_edit_history_response import ContractGetEditHistoryResponse

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return ContractsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        contract_id: str,
        customer_id: str,
        as_of_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_balance: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveResponse:
        """Get a specific contract.

        New clients should use this endpoint rather than the v1
        endpoint.

        Args:
          as_of_date: Optional RFC 3339 timestamp. Return the contract as of this date. Cannot be used
              with include_ledgers parameter.

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

          include_ledgers: Include commit/credit ledgers in the response. Setting this flag may cause the
              query to be slower. Cannot be used with as_of_date parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/contracts/get",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "as_of_date": as_of_date,
                    "include_balance": include_balance,
                    "include_ledgers": include_ledgers,
                },
                contract_retrieve_params.ContractRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_id: str,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_balance: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractListResponse:
        """
        List all contracts for a customer

        Args:
          covering_date: Optional RFC 3339 timestamp. Only include contracts active on the provided date.
              This cannot be provided if starting_at filter is provided.

          include_archived: Include archived contracts in the response.

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the response to be slower.

          include_ledgers: Include commit/credit ledgers in the response. Setting this flag may cause the
              response to be slower.

          starting_at: Optional RFC 3339 timestamp. Only include contracts that started on or after
              this date. This cannot be provided if covering_date filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/contracts/list",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_ledgers": include_ledgers,
                    "starting_at": starting_at,
                },
                contract_list_params.ContractListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractListResponse,
        )

    def edit(
        self,
        *,
        contract_id: str,
        customer_id: str,
        add_commits: Iterable[contract_edit_params.AddCommit] | NotGiven = NOT_GIVEN,
        add_credits: Iterable[contract_edit_params.AddCredit] | NotGiven = NOT_GIVEN,
        add_discounts: Iterable[contract_edit_params.AddDiscount] | NotGiven = NOT_GIVEN,
        add_overrides: Iterable[contract_edit_params.AddOverride] | NotGiven = NOT_GIVEN,
        add_professional_services: Iterable[contract_edit_params.AddProfessionalService] | NotGiven = NOT_GIVEN,
        add_recurring_commits: Iterable[contract_edit_params.AddRecurringCommit] | NotGiven = NOT_GIVEN,
        add_recurring_credits: Iterable[contract_edit_params.AddRecurringCredit] | NotGiven = NOT_GIVEN,
        add_reseller_royalties: Iterable[contract_edit_params.AddResellerRoyalty] | NotGiven = NOT_GIVEN,
        add_scheduled_charges: Iterable[contract_edit_params.AddScheduledCharge] | NotGiven = NOT_GIVEN,
        update_commits: Iterable[contract_edit_params.UpdateCommit] | NotGiven = NOT_GIVEN,
        update_credits: Iterable[contract_edit_params.UpdateCredit] | NotGiven = NOT_GIVEN,
        update_scheduled_charges: Iterable[contract_edit_params.UpdateScheduledCharge] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractEditResponse:
        """Edit a contract.

        Contract editing must be enabled to use this endpoint.

        Args:
          contract_id: ID of the contract being edited

          customer_id: ID of the customer whose contract is being edited

          add_professional_services: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/contracts/edit",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "add_commits": add_commits,
                    "add_credits": add_credits,
                    "add_discounts": add_discounts,
                    "add_overrides": add_overrides,
                    "add_professional_services": add_professional_services,
                    "add_recurring_commits": add_recurring_commits,
                    "add_recurring_credits": add_recurring_credits,
                    "add_reseller_royalties": add_reseller_royalties,
                    "add_scheduled_charges": add_scheduled_charges,
                    "update_commits": update_commits,
                    "update_credits": update_credits,
                    "update_scheduled_charges": update_scheduled_charges,
                },
                contract_edit_params.ContractEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditResponse,
        )

    def edit_commit(
        self,
        *,
        commit_id: str,
        customer_id: str,
        access_schedule: contract_edit_commit_params.AccessSchedule | NotGiven = NOT_GIVEN,
        applicable_product_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        applicable_product_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        invoice_contract_id: str | NotGiven = NOT_GIVEN,
        invoice_schedule: contract_edit_commit_params.InvoiceSchedule | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractEditCommitResponse:
        """Edit a customer or contract commit.

        Contract commits can only be edited using
        this endpoint if contract editing is enabled.

        Args:
          commit_id: ID of the commit to edit

          customer_id: ID of the customer whose commit is being edited

          applicable_product_ids: Which products the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          applicable_product_tags: Which tags the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          invoice_contract_id: ID of contract to use for invoicing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/contracts/commits/edit",
            body=maybe_transform(
                {
                    "commit_id": commit_id,
                    "customer_id": customer_id,
                    "access_schedule": access_schedule,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "invoice_contract_id": invoice_contract_id,
                    "invoice_schedule": invoice_schedule,
                    "product_id": product_id,
                },
                contract_edit_commit_params.ContractEditCommitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditCommitResponse,
        )

    def edit_credit(
        self,
        *,
        credit_id: str,
        customer_id: str,
        access_schedule: contract_edit_credit_params.AccessSchedule | NotGiven = NOT_GIVEN,
        applicable_product_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        applicable_product_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractEditCreditResponse:
        """Edit a customer or contract credit.

        Contract credits can only be edited using
        this endpoint if contract editing is enabled.

        Args:
          credit_id: ID of the credit to edit

          customer_id: ID of the customer whose credit is being edited

          applicable_product_ids: Which products the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          applicable_product_tags: Which tags the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/contracts/credits/edit",
            body=maybe_transform(
                {
                    "credit_id": credit_id,
                    "customer_id": customer_id,
                    "access_schedule": access_schedule,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "product_id": product_id,
                },
                contract_edit_credit_params.ContractEditCreditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditCreditResponse,
        )

    def get_edit_history(
        self,
        *,
        contract_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractGetEditHistoryResponse:
        """
        Get the edit history of a specific contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/contracts/getEditHistory",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                },
                contract_get_edit_history_params.ContractGetEditHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractGetEditHistoryResponse,
        )


class AsyncContractsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncContractsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        contract_id: str,
        customer_id: str,
        as_of_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_balance: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveResponse:
        """Get a specific contract.

        New clients should use this endpoint rather than the v1
        endpoint.

        Args:
          as_of_date: Optional RFC 3339 timestamp. Return the contract as of this date. Cannot be used
              with include_ledgers parameter.

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

          include_ledgers: Include commit/credit ledgers in the response. Setting this flag may cause the
              query to be slower. Cannot be used with as_of_date parameter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/contracts/get",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "as_of_date": as_of_date,
                    "include_balance": include_balance,
                    "include_ledgers": include_ledgers,
                },
                contract_retrieve_params.ContractRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveResponse,
        )

    async def list(
        self,
        *,
        customer_id: str,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_balance: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractListResponse:
        """
        List all contracts for a customer

        Args:
          covering_date: Optional RFC 3339 timestamp. Only include contracts active on the provided date.
              This cannot be provided if starting_at filter is provided.

          include_archived: Include archived contracts in the response.

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the response to be slower.

          include_ledgers: Include commit/credit ledgers in the response. Setting this flag may cause the
              response to be slower.

          starting_at: Optional RFC 3339 timestamp. Only include contracts that started on or after
              this date. This cannot be provided if covering_date filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/contracts/list",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_ledgers": include_ledgers,
                    "starting_at": starting_at,
                },
                contract_list_params.ContractListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractListResponse,
        )

    async def edit(
        self,
        *,
        contract_id: str,
        customer_id: str,
        add_commits: Iterable[contract_edit_params.AddCommit] | NotGiven = NOT_GIVEN,
        add_credits: Iterable[contract_edit_params.AddCredit] | NotGiven = NOT_GIVEN,
        add_discounts: Iterable[contract_edit_params.AddDiscount] | NotGiven = NOT_GIVEN,
        add_overrides: Iterable[contract_edit_params.AddOverride] | NotGiven = NOT_GIVEN,
        add_professional_services: Iterable[contract_edit_params.AddProfessionalService] | NotGiven = NOT_GIVEN,
        add_recurring_commits: Iterable[contract_edit_params.AddRecurringCommit] | NotGiven = NOT_GIVEN,
        add_recurring_credits: Iterable[contract_edit_params.AddRecurringCredit] | NotGiven = NOT_GIVEN,
        add_reseller_royalties: Iterable[contract_edit_params.AddResellerRoyalty] | NotGiven = NOT_GIVEN,
        add_scheduled_charges: Iterable[contract_edit_params.AddScheduledCharge] | NotGiven = NOT_GIVEN,
        update_commits: Iterable[contract_edit_params.UpdateCommit] | NotGiven = NOT_GIVEN,
        update_credits: Iterable[contract_edit_params.UpdateCredit] | NotGiven = NOT_GIVEN,
        update_scheduled_charges: Iterable[contract_edit_params.UpdateScheduledCharge] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractEditResponse:
        """Edit a contract.

        Contract editing must be enabled to use this endpoint.

        Args:
          contract_id: ID of the contract being edited

          customer_id: ID of the customer whose contract is being edited

          add_professional_services: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/contracts/edit",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "add_commits": add_commits,
                    "add_credits": add_credits,
                    "add_discounts": add_discounts,
                    "add_overrides": add_overrides,
                    "add_professional_services": add_professional_services,
                    "add_recurring_commits": add_recurring_commits,
                    "add_recurring_credits": add_recurring_credits,
                    "add_reseller_royalties": add_reseller_royalties,
                    "add_scheduled_charges": add_scheduled_charges,
                    "update_commits": update_commits,
                    "update_credits": update_credits,
                    "update_scheduled_charges": update_scheduled_charges,
                },
                contract_edit_params.ContractEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditResponse,
        )

    async def edit_commit(
        self,
        *,
        commit_id: str,
        customer_id: str,
        access_schedule: contract_edit_commit_params.AccessSchedule | NotGiven = NOT_GIVEN,
        applicable_product_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        applicable_product_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        invoice_contract_id: str | NotGiven = NOT_GIVEN,
        invoice_schedule: contract_edit_commit_params.InvoiceSchedule | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractEditCommitResponse:
        """Edit a customer or contract commit.

        Contract commits can only be edited using
        this endpoint if contract editing is enabled.

        Args:
          commit_id: ID of the commit to edit

          customer_id: ID of the customer whose commit is being edited

          applicable_product_ids: Which products the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          applicable_product_tags: Which tags the commit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the commit applies to all products.

          invoice_contract_id: ID of contract to use for invoicing

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/contracts/commits/edit",
            body=await async_maybe_transform(
                {
                    "commit_id": commit_id,
                    "customer_id": customer_id,
                    "access_schedule": access_schedule,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "invoice_contract_id": invoice_contract_id,
                    "invoice_schedule": invoice_schedule,
                    "product_id": product_id,
                },
                contract_edit_commit_params.ContractEditCommitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditCommitResponse,
        )

    async def edit_credit(
        self,
        *,
        credit_id: str,
        customer_id: str,
        access_schedule: contract_edit_credit_params.AccessSchedule | NotGiven = NOT_GIVEN,
        applicable_product_ids: Optional[List[str]] | NotGiven = NOT_GIVEN,
        applicable_product_tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractEditCreditResponse:
        """Edit a customer or contract credit.

        Contract credits can only be edited using
        this endpoint if contract editing is enabled.

        Args:
          credit_id: ID of the credit to edit

          customer_id: ID of the customer whose credit is being edited

          applicable_product_ids: Which products the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          applicable_product_tags: Which tags the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/contracts/credits/edit",
            body=await async_maybe_transform(
                {
                    "credit_id": credit_id,
                    "customer_id": customer_id,
                    "access_schedule": access_schedule,
                    "applicable_product_ids": applicable_product_ids,
                    "applicable_product_tags": applicable_product_tags,
                    "product_id": product_id,
                },
                contract_edit_credit_params.ContractEditCreditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractEditCreditResponse,
        )

    async def get_edit_history(
        self,
        *,
        contract_id: str,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractGetEditHistoryResponse:
        """
        Get the edit history of a specific contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/contracts/getEditHistory",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                },
                contract_get_edit_history_params.ContractGetEditHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractGetEditHistoryResponse,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            contracts.list,
        )
        self.edit = to_raw_response_wrapper(
            contracts.edit,
        )
        self.edit_commit = to_raw_response_wrapper(
            contracts.edit_commit,
        )
        self.edit_credit = to_raw_response_wrapper(
            contracts.edit_credit,
        )
        self.get_edit_history = to_raw_response_wrapper(
            contracts.get_edit_history,
        )


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = async_to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            contracts.list,
        )
        self.edit = async_to_raw_response_wrapper(
            contracts.edit,
        )
        self.edit_commit = async_to_raw_response_wrapper(
            contracts.edit_commit,
        )
        self.edit_credit = async_to_raw_response_wrapper(
            contracts.edit_credit,
        )
        self.get_edit_history = async_to_raw_response_wrapper(
            contracts.get_edit_history,
        )


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            contracts.list,
        )
        self.edit = to_streamed_response_wrapper(
            contracts.edit,
        )
        self.edit_commit = to_streamed_response_wrapper(
            contracts.edit_commit,
        )
        self.edit_credit = to_streamed_response_wrapper(
            contracts.edit_credit,
        )
        self.get_edit_history = to_streamed_response_wrapper(
            contracts.get_edit_history,
        )


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.retrieve = async_to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            contracts.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            contracts.edit,
        )
        self.edit_commit = async_to_streamed_response_wrapper(
            contracts.edit_commit,
        )
        self.edit_credit = async_to_streamed_response_wrapper(
            contracts.edit_credit,
        )
        self.get_edit_history = async_to_streamed_response_wrapper(
            contracts.get_edit_history,
        )
