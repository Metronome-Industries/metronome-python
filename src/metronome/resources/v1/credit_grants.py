# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    credit_grant_edit_params,
    credit_grant_list_params,
    credit_grant_void_params,
    credit_grant_create_params,
    credit_grant_list_entries_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage, SyncCursorPageWithoutLimit, AsyncCursorPageWithoutLimit
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.credit_grant_edit_response import CreditGrantEditResponse
from ...types.v1.credit_grant_list_response import CreditGrantListResponse
from ...types.v1.credit_grant_void_response import CreditGrantVoidResponse
from ...types.v1.credit_grant_create_response import CreditGrantCreateResponse
from ...types.v1.credit_grant_list_entries_response import CreditGrantListEntriesResponse

__all__ = ["CreditGrantsResource", "AsyncCreditGrantsResource"]


class CreditGrantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return CreditGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return CreditGrantsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        expires_at: Union[str, datetime],
        grant_amount: credit_grant_create_params.GrantAmount,
        name: str,
        paid_amount: credit_grant_create_params.PaidAmount,
        priority: float,
        credit_grant_type: str | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        effective_at: Union[str, datetime] | Omit = omit,
        invoice_date: Union[str, datetime] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        rollover_settings: credit_grant_create_params.RolloverSettings | Omit = omit,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantCreateResponse:
        """Create a new credit grant.

        This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

        Args:
          customer_id: the Metronome ID of the customer

          expires_at: The credit grant will only apply to usage or charges dated before this timestamp

          grant_amount: the amount of credits granted

          name: the name of the credit grant as it will appear on invoices

          paid_amount: the amount paid for this credit grant

          custom_fields: Custom fields to attach to the credit grant.

          effective_at: The credit grant will only apply to usage or charges dated on or after this
              timestamp

          invoice_date: The date to issue an invoice for the paid_amount.

          product_ids: The product(s) which these credits will be applied to. (If unspecified, the
              credits will be applied to charges for all products.). The array ordering
              specified here will be used to determine the order in which credits will be
              applied to invoice line items

          rollover_settings: Configure a rollover for this credit grant so if it expires it rolls over a
              configured amount to a new credit grant. This feature is currently opt-in only.
              Contact Metronome to be added to the beta.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/credits/createGrant",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "expires_at": expires_at,
                    "grant_amount": grant_amount,
                    "name": name,
                    "paid_amount": paid_amount,
                    "priority": priority,
                    "credit_grant_type": credit_grant_type,
                    "custom_fields": custom_fields,
                    "effective_at": effective_at,
                    "invoice_date": invoice_date,
                    "product_ids": product_ids,
                    "reason": reason,
                    "rollover_settings": rollover_settings,
                    "uniqueness_key": uniqueness_key,
                },
                credit_grant_create_params.CreditGrantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantCreateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        credit_grant_ids: SequenceNotStr[str] | Omit = omit,
        credit_type_ids: SequenceNotStr[str] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        not_expiring_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CreditGrantListResponse]:
        """List credit grants.

        This list does not included voided grants. This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          credit_grant_ids: An array of credit grant IDs. If this is specified, neither credit_type_ids nor
              customer_ids may be specified.

          credit_type_ids: An array of credit type IDs. This must not be specified if credit_grant_ids is
              specified.

          customer_ids: An array of Metronome customer IDs. This must not be specified if
              credit_grant_ids is specified.

          effective_before: Only return credit grants that are effective before this timestamp (exclusive).

          not_expiring_before: Only return credit grants that expire at or after this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/credits/listGrants",
            page=SyncCursorPage[CreditGrantListResponse],
            body=maybe_transform(
                {
                    "credit_grant_ids": credit_grant_ids,
                    "credit_type_ids": credit_type_ids,
                    "customer_ids": customer_ids,
                    "effective_before": effective_before,
                    "not_expiring_before": not_expiring_before,
                },
                credit_grant_list_params.CreditGrantListParams,
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
                    credit_grant_list_params.CreditGrantListParams,
                ),
            ),
            model=CreditGrantListResponse,
            method="post",
        )

    def edit(
        self,
        *,
        id: str,
        credit_grant_type: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantEditResponse:
        """Edit an existing credit grant.

        This is a Plans (deprecated) endpoint. New
        clients should implement using Contracts.

        Args:
          id: the ID of the credit grant

          credit_grant_type: the updated credit grant type

          expires_at: the updated expiration date for the credit grant

          name: the updated name for the credit grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/credits/editGrant",
            body=maybe_transform(
                {
                    "id": id,
                    "credit_grant_type": credit_grant_type,
                    "expires_at": expires_at,
                    "name": name,
                },
                credit_grant_edit_params.CreditGrantEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantEditResponse,
        )

    def list_entries(
        self,
        *,
        next_page: str | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        credit_type_ids: SequenceNotStr[str] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPageWithoutLimit[CreditGrantListEntriesResponse]:
        """Fetches a list of credit ledger entries.

        Returns lists of ledgers per customer.
        Ledger entries are returned in chronological order. Ledger entries associated
        with voided credit grants are not included. This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

          sort: Ledgers sort order by date, asc or desc. Defaults to asc.

          credit_type_ids: A list of Metronome credit type IDs to fetch ledger entries for. If absent,
              ledger entries for all credit types will be returned.

          customer_ids: A list of Metronome customer IDs to fetch ledger entries for. If absent, ledger
              entries for all customers will be returned.

          ending_before: If supplied, ledger entries will only be returned with an effective_at before
              this time. This timestamp must not be in the future. If no timestamp is
              supplied, all entries up to the start of the customer's next billing period will
              be returned.

          starting_on: If supplied, only ledger entries effective at or after this time will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/credits/listEntries",
            page=SyncCursorPageWithoutLimit[CreditGrantListEntriesResponse],
            body=maybe_transform(
                {
                    "credit_type_ids": credit_type_ids,
                    "customer_ids": customer_ids,
                    "ending_before": ending_before,
                    "starting_on": starting_on,
                },
                credit_grant_list_entries_params.CreditGrantListEntriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "next_page": next_page,
                        "sort": sort,
                    },
                    credit_grant_list_entries_params.CreditGrantListEntriesParams,
                ),
            ),
            model=CreditGrantListEntriesResponse,
            method="post",
        )

    def void(
        self,
        *,
        id: str,
        release_uniqueness_key: bool | Omit = omit,
        void_credit_purchase_invoice: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantVoidResponse:
        """Void a credit grant.

        This is a Plans (deprecated) endpoint. New clients should
        implement using Contracts.

        Args:
          release_uniqueness_key: If true, resets the uniqueness key on this grant so it can be re-used

          void_credit_purchase_invoice: If true, void the purchase invoice associated with the grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/credits/voidGrant",
            body=maybe_transform(
                {
                    "id": id,
                    "release_uniqueness_key": release_uniqueness_key,
                    "void_credit_purchase_invoice": void_credit_purchase_invoice,
                },
                credit_grant_void_params.CreditGrantVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantVoidResponse,
        )


class AsyncCreditGrantsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditGrantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditGrantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncCreditGrantsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        expires_at: Union[str, datetime],
        grant_amount: credit_grant_create_params.GrantAmount,
        name: str,
        paid_amount: credit_grant_create_params.PaidAmount,
        priority: float,
        credit_grant_type: str | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        effective_at: Union[str, datetime] | Omit = omit,
        invoice_date: Union[str, datetime] | Omit = omit,
        product_ids: SequenceNotStr[str] | Omit = omit,
        reason: str | Omit = omit,
        rollover_settings: credit_grant_create_params.RolloverSettings | Omit = omit,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantCreateResponse:
        """Create a new credit grant.

        This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

        Args:
          customer_id: the Metronome ID of the customer

          expires_at: The credit grant will only apply to usage or charges dated before this timestamp

          grant_amount: the amount of credits granted

          name: the name of the credit grant as it will appear on invoices

          paid_amount: the amount paid for this credit grant

          custom_fields: Custom fields to attach to the credit grant.

          effective_at: The credit grant will only apply to usage or charges dated on or after this
              timestamp

          invoice_date: The date to issue an invoice for the paid_amount.

          product_ids: The product(s) which these credits will be applied to. (If unspecified, the
              credits will be applied to charges for all products.). The array ordering
              specified here will be used to determine the order in which credits will be
              applied to invoice line items

          rollover_settings: Configure a rollover for this credit grant so if it expires it rolls over a
              configured amount to a new credit grant. This feature is currently opt-in only.
              Contact Metronome to be added to the beta.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/credits/createGrant",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "expires_at": expires_at,
                    "grant_amount": grant_amount,
                    "name": name,
                    "paid_amount": paid_amount,
                    "priority": priority,
                    "credit_grant_type": credit_grant_type,
                    "custom_fields": custom_fields,
                    "effective_at": effective_at,
                    "invoice_date": invoice_date,
                    "product_ids": product_ids,
                    "reason": reason,
                    "rollover_settings": rollover_settings,
                    "uniqueness_key": uniqueness_key,
                },
                credit_grant_create_params.CreditGrantCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantCreateResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        credit_grant_ids: SequenceNotStr[str] | Omit = omit,
        credit_type_ids: SequenceNotStr[str] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        not_expiring_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CreditGrantListResponse, AsyncCursorPage[CreditGrantListResponse]]:
        """List credit grants.

        This list does not included voided grants. This is a Plans
        (deprecated) endpoint. New clients should implement using Contracts.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          credit_grant_ids: An array of credit grant IDs. If this is specified, neither credit_type_ids nor
              customer_ids may be specified.

          credit_type_ids: An array of credit type IDs. This must not be specified if credit_grant_ids is
              specified.

          customer_ids: An array of Metronome customer IDs. This must not be specified if
              credit_grant_ids is specified.

          effective_before: Only return credit grants that are effective before this timestamp (exclusive).

          not_expiring_before: Only return credit grants that expire at or after this timestamp.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/credits/listGrants",
            page=AsyncCursorPage[CreditGrantListResponse],
            body=maybe_transform(
                {
                    "credit_grant_ids": credit_grant_ids,
                    "credit_type_ids": credit_type_ids,
                    "customer_ids": customer_ids,
                    "effective_before": effective_before,
                    "not_expiring_before": not_expiring_before,
                },
                credit_grant_list_params.CreditGrantListParams,
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
                    credit_grant_list_params.CreditGrantListParams,
                ),
            ),
            model=CreditGrantListResponse,
            method="post",
        )

    async def edit(
        self,
        *,
        id: str,
        credit_grant_type: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantEditResponse:
        """Edit an existing credit grant.

        This is a Plans (deprecated) endpoint. New
        clients should implement using Contracts.

        Args:
          id: the ID of the credit grant

          credit_grant_type: the updated credit grant type

          expires_at: the updated expiration date for the credit grant

          name: the updated name for the credit grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/credits/editGrant",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "credit_grant_type": credit_grant_type,
                    "expires_at": expires_at,
                    "name": name,
                },
                credit_grant_edit_params.CreditGrantEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantEditResponse,
        )

    def list_entries(
        self,
        *,
        next_page: str | Omit = omit,
        sort: Literal["asc", "desc"] | Omit = omit,
        credit_type_ids: SequenceNotStr[str] | Omit = omit,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CreditGrantListEntriesResponse, AsyncCursorPageWithoutLimit[CreditGrantListEntriesResponse]]:
        """Fetches a list of credit ledger entries.

        Returns lists of ledgers per customer.
        Ledger entries are returned in chronological order. Ledger entries associated
        with voided credit grants are not included. This is a Plans (deprecated)
        endpoint. New clients should implement using Contracts.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

          sort: Ledgers sort order by date, asc or desc. Defaults to asc.

          credit_type_ids: A list of Metronome credit type IDs to fetch ledger entries for. If absent,
              ledger entries for all credit types will be returned.

          customer_ids: A list of Metronome customer IDs to fetch ledger entries for. If absent, ledger
              entries for all customers will be returned.

          ending_before: If supplied, ledger entries will only be returned with an effective_at before
              this time. This timestamp must not be in the future. If no timestamp is
              supplied, all entries up to the start of the customer's next billing period will
              be returned.

          starting_on: If supplied, only ledger entries effective at or after this time will be
              returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/credits/listEntries",
            page=AsyncCursorPageWithoutLimit[CreditGrantListEntriesResponse],
            body=maybe_transform(
                {
                    "credit_type_ids": credit_type_ids,
                    "customer_ids": customer_ids,
                    "ending_before": ending_before,
                    "starting_on": starting_on,
                },
                credit_grant_list_entries_params.CreditGrantListEntriesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "next_page": next_page,
                        "sort": sort,
                    },
                    credit_grant_list_entries_params.CreditGrantListEntriesParams,
                ),
            ),
            model=CreditGrantListEntriesResponse,
            method="post",
        )

    async def void(
        self,
        *,
        id: str,
        release_uniqueness_key: bool | Omit = omit,
        void_credit_purchase_invoice: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditGrantVoidResponse:
        """Void a credit grant.

        This is a Plans (deprecated) endpoint. New clients should
        implement using Contracts.

        Args:
          release_uniqueness_key: If true, resets the uniqueness key on this grant so it can be re-used

          void_credit_purchase_invoice: If true, void the purchase invoice associated with the grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/credits/voidGrant",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "release_uniqueness_key": release_uniqueness_key,
                    "void_credit_purchase_invoice": void_credit_purchase_invoice,
                },
                credit_grant_void_params.CreditGrantVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditGrantVoidResponse,
        )


class CreditGrantsResourceWithRawResponse:
    def __init__(self, credit_grants: CreditGrantsResource) -> None:
        self._credit_grants = credit_grants

        self.create = to_raw_response_wrapper(
            credit_grants.create,
        )
        self.list = to_raw_response_wrapper(
            credit_grants.list,
        )
        self.edit = to_raw_response_wrapper(
            credit_grants.edit,
        )
        self.list_entries = to_raw_response_wrapper(
            credit_grants.list_entries,
        )
        self.void = to_raw_response_wrapper(
            credit_grants.void,
        )


class AsyncCreditGrantsResourceWithRawResponse:
    def __init__(self, credit_grants: AsyncCreditGrantsResource) -> None:
        self._credit_grants = credit_grants

        self.create = async_to_raw_response_wrapper(
            credit_grants.create,
        )
        self.list = async_to_raw_response_wrapper(
            credit_grants.list,
        )
        self.edit = async_to_raw_response_wrapper(
            credit_grants.edit,
        )
        self.list_entries = async_to_raw_response_wrapper(
            credit_grants.list_entries,
        )
        self.void = async_to_raw_response_wrapper(
            credit_grants.void,
        )


class CreditGrantsResourceWithStreamingResponse:
    def __init__(self, credit_grants: CreditGrantsResource) -> None:
        self._credit_grants = credit_grants

        self.create = to_streamed_response_wrapper(
            credit_grants.create,
        )
        self.list = to_streamed_response_wrapper(
            credit_grants.list,
        )
        self.edit = to_streamed_response_wrapper(
            credit_grants.edit,
        )
        self.list_entries = to_streamed_response_wrapper(
            credit_grants.list_entries,
        )
        self.void = to_streamed_response_wrapper(
            credit_grants.void,
        )


class AsyncCreditGrantsResourceWithStreamingResponse:
    def __init__(self, credit_grants: AsyncCreditGrantsResource) -> None:
        self._credit_grants = credit_grants

        self.create = async_to_streamed_response_wrapper(
            credit_grants.create,
        )
        self.list = async_to_streamed_response_wrapper(
            credit_grants.list,
        )
        self.edit = async_to_streamed_response_wrapper(
            credit_grants.edit,
        )
        self.list_entries = async_to_streamed_response_wrapper(
            credit_grants.list_entries,
        )
        self.void = async_to_streamed_response_wrapper(
            credit_grants.void,
        )
