# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from datetime import datetime

import httpx

from ..types import (
    credit_grant_edit_params,
    credit_grant_list_params,
    credit_grant_void_params,
    credit_grant_create_params,
    credit_grant_list_entries_params,
    credit_grant_list_credit_types_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)
from ..types.credit_grant_edit_response import CreditGrantEditResponse
from ..types.credit_grant_list_response import CreditGrantListResponse
from ..types.credit_grant_void_response import CreditGrantVoidResponse
from ..types.credit_grant_create_response import CreditGrantCreateResponse
from ..types.credit_grant_list_entries_response import CreditGrantListEntriesResponse
from ..types.credit_grant_list_credit_types_response import CreditGrantListCreditTypesResponse

__all__ = ["CreditGrantsResource", "AsyncCreditGrantsResource"]


class CreditGrantsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditGrantsResourceWithRawResponse:
        return CreditGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditGrantsResourceWithStreamingResponse:
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
        credit_grant_type: str | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoice_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        product_ids: List[str] | NotGiven = NOT_GIVEN,
        reason: str | NotGiven = NOT_GIVEN,
        rollover_settings: credit_grant_create_params.RolloverSettings | NotGiven = NOT_GIVEN,
        uniqueness_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantCreateResponse:
        """
        Create a new credit grant

        Args:
          customer_id: the Metronome ID of the customer

          expires_at: The credit grant will only apply to billing periods that end before this
              timestamp.

          grant_amount: the amount of credits granted

          name: the name of the credit grant as it will appear on invoices

          paid_amount: the amount paid for this credit grant

          custom_fields: Custom fields to attach to the credit grant.

          effective_at: The credit grant will only apply to billing periods that end at or after this
              timestamp.

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
            "/credits/createGrant",
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
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        credit_grant_ids: List[str] | NotGiven = NOT_GIVEN,
        credit_type_ids: List[str] | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_expiring_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantListResponse:
        """List credit grants.

        This list does not included voided grants.

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
        return self._post(
            "/credits/listGrants",
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
            cast_to=CreditGrantListResponse,
        )

    def edit(
        self,
        *,
        id: str,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantEditResponse:
        """
        Edit an existing credit grant

        Args:
          id: the ID of the credit grant

          expires_at: the updated expiration date for the credit grant

          name: the updated name for the credit grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/credits/editGrant",
            body=maybe_transform(
                {
                    "id": id,
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

    def list_credit_types(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantListCreditTypesResponse:
        """
        List all pricing units (known in the API by the legacy term "credit types").

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/credit-types/list",
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
                    credit_grant_list_credit_types_params.CreditGrantListCreditTypesParams,
                ),
            ),
            cast_to=CreditGrantListCreditTypesResponse,
        )

    def list_entries(
        self,
        *,
        next_page: str | NotGiven = NOT_GIVEN,
        credit_type_ids: List[str] | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        starting_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantListEntriesResponse:
        """Fetches a list of credit ledger entries.

        Returns lists of ledgers per customer.
        Ledger entries are returned in reverse chronological order. Ledger entries
        associated with voided credit grants are not included.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

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
        return self._post(
            "/credits/listEntries",
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
                    {"next_page": next_page}, credit_grant_list_entries_params.CreditGrantListEntriesParams
                ),
            ),
            cast_to=CreditGrantListEntriesResponse,
        )

    def void(
        self,
        *,
        id: str,
        void_credit_purchase_invoice: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantVoidResponse:
        """
        Void a credit grant

        Args:
          void_credit_purchase_invoice: If true, void the purchase invoice associated with the grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/credits/voidGrant",
            body=maybe_transform(
                {
                    "id": id,
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
        return AsyncCreditGrantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditGrantsResourceWithStreamingResponse:
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
        credit_grant_type: str | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        effective_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        invoice_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        product_ids: List[str] | NotGiven = NOT_GIVEN,
        reason: str | NotGiven = NOT_GIVEN,
        rollover_settings: credit_grant_create_params.RolloverSettings | NotGiven = NOT_GIVEN,
        uniqueness_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantCreateResponse:
        """
        Create a new credit grant

        Args:
          customer_id: the Metronome ID of the customer

          expires_at: The credit grant will only apply to billing periods that end before this
              timestamp.

          grant_amount: the amount of credits granted

          name: the name of the credit grant as it will appear on invoices

          paid_amount: the amount paid for this credit grant

          custom_fields: Custom fields to attach to the credit grant.

          effective_at: The credit grant will only apply to billing periods that end at or after this
              timestamp.

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
            "/credits/createGrant",
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

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        credit_grant_ids: List[str] | NotGiven = NOT_GIVEN,
        credit_type_ids: List[str] | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        not_expiring_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantListResponse:
        """List credit grants.

        This list does not included voided grants.

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
        return await self._post(
            "/credits/listGrants",
            body=await async_maybe_transform(
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
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                    },
                    credit_grant_list_params.CreditGrantListParams,
                ),
            ),
            cast_to=CreditGrantListResponse,
        )

    async def edit(
        self,
        *,
        id: str,
        expires_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantEditResponse:
        """
        Edit an existing credit grant

        Args:
          id: the ID of the credit grant

          expires_at: the updated expiration date for the credit grant

          name: the updated name for the credit grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/credits/editGrant",
            body=await async_maybe_transform(
                {
                    "id": id,
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

    async def list_credit_types(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantListCreditTypesResponse:
        """
        List all pricing units (known in the API by the legacy term "credit types").

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/credit-types/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next_page": next_page,
                    },
                    credit_grant_list_credit_types_params.CreditGrantListCreditTypesParams,
                ),
            ),
            cast_to=CreditGrantListCreditTypesResponse,
        )

    async def list_entries(
        self,
        *,
        next_page: str | NotGiven = NOT_GIVEN,
        credit_type_ids: List[str] | NotGiven = NOT_GIVEN,
        customer_ids: List[str] | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        starting_on: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantListEntriesResponse:
        """Fetches a list of credit ledger entries.

        Returns lists of ledgers per customer.
        Ledger entries are returned in reverse chronological order. Ledger entries
        associated with voided credit grants are not included.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

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
        return await self._post(
            "/credits/listEntries",
            body=await async_maybe_transform(
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
                query=await async_maybe_transform(
                    {"next_page": next_page}, credit_grant_list_entries_params.CreditGrantListEntriesParams
                ),
            ),
            cast_to=CreditGrantListEntriesResponse,
        )

    async def void(
        self,
        *,
        id: str,
        void_credit_purchase_invoice: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditGrantVoidResponse:
        """
        Void a credit grant

        Args:
          void_credit_purchase_invoice: If true, void the purchase invoice associated with the grant

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/credits/voidGrant",
            body=await async_maybe_transform(
                {
                    "id": id,
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
        self.list_credit_types = to_raw_response_wrapper(
            credit_grants.list_credit_types,
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
        self.list_credit_types = async_to_raw_response_wrapper(
            credit_grants.list_credit_types,
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
        self.list_credit_types = to_streamed_response_wrapper(
            credit_grants.list_credit_types,
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
        self.list_credit_types = async_to_streamed_response_wrapper(
            credit_grants.list_credit_types,
        )
        self.list_entries = async_to_streamed_response_wrapper(
            credit_grants.list_entries,
        )
        self.void = async_to_streamed_response_wrapper(
            credit_grants.void,
        )
