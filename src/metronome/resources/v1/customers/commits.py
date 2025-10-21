# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncBodyCursorPage, AsyncBodyCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1.customers import commit_list_params, commit_create_params, commit_update_end_date_params
from ....types.shared.commit import Commit
from ....types.v1.customers.commit_create_response import CommitCreateResponse
from ....types.shared_params.commit_specifier_input import CommitSpecifierInput
from ....types.v1.customers.commit_update_end_date_response import CommitUpdateEndDateResponse

__all__ = ["CommitsResource", "AsyncCommitsResource"]


class CommitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return CommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return CommitsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        access_schedule: commit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        type: Literal["PREPAID", "POSTPAID"],
        applicable_contract_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_tags: SequenceNotStr[str] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        description: str | Omit = omit,
        invoice_contract_id: str | Omit = omit,
        invoice_schedule: commit_create_params.InvoiceSchedule | Omit = omit,
        name: str | Omit = omit,
        netsuite_sales_order_id: str | Omit = omit,
        rate_type: Literal["COMMIT_RATE", "LIST_RATE"] | Omit = omit,
        salesforce_opportunity_id: str | Omit = omit,
        specifiers: Iterable[CommitSpecifierInput] | Omit = omit,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitCreateResponse:
        """
        Creates customer-level commits that establish spending commitments for customers
        across their Metronome usage. Commits represent contracted spending obligations
        that can be either prepaid (paid upfront) or postpaid (billed later).

        Note: In most cases, you should add commitments directly to customer contracts
        using the contract/create or contract/edit APIs.

        ### Use this endpoint to:

        Use this endpoint when you need to establish customer-level spending commitments
        that can be applied across multiple contracts or scoped to specific contracts.
        Customer-level commits are ideal for:

        - Enterprise-wide minimum spending agreements that span multiple contracts
        - Multi-contract volume commitments with shared spending pools
        - Cross-contract discount tiers based on aggregate usage

        #### Commit type Requirements:

        - You must specify either "prepaid" or "postpaid" as the commit type:
        - Prepaid commits: Customer pays upfront; invoice_schedule is optional (if
          omitted, creates a commit without an invoice)
        - Postpaid commits: Customer pays when the commitment expires (the end of the
          access_schedule); invoice_schedule is required and must match access_schedule
          totals.

        #### Billing configuration:

        - invoice_contract_id is required for postpaid commits and for prepaid commits
          with billing (only optional for free prepaid commits) unless do_not_invoice is
          set to true
        - For postpaid commits: access_schedule and invoice_schedule must have matching
          amounts
        - For postpaid commits: only one schedule item is allowed in both schedules.

        #### Scoping flexibility:

        Customer-level commits can be configured in a few ways:

        - Contract-specific: Use the `applicable_contract_ids` field to limit the commit
          to specific contracts
        - Cross-contract: Leave `applicable_contract_ids` empty to allow the commit to
          be used across all of the customer's contracts

        #### Product targeting:

        Commits can be scoped to specific products using applicable_product_ids,
        applicable_product_tags, or specifiers, or left unrestricted to apply to all
        products.

        #### Priority considerations:

        When multiple commits are applicable, the one with the lower priority value will
        be consumed first. If there is a tie, contract level commits and credits will be
        applied before customer level commits and credits. Plan your priority scheme
        carefully to ensure commits are applied in the desired order.

        ### Usage guidelines:

        ⚠️ Preferred Alternative: In most cases, you should add commits directly to
        contracts using the create contract or edit contract APIs instead of creating
        customer-level commits. Contract-level commits provide better organization and
        are the recommended approach for standard use cases.

        Args:
          access_schedule: Schedule for distributing the commit to the customer. For "POSTPAID" commits
              only one schedule item is allowed and amount must match invoice_schedule total.

          priority: If multiple credits or commits are applicable, the one with the lower priority
              will apply first.

          product_id: ID of the fixed product associated with the commit. This is required because
              products are used to invoice the commit amount.

          applicable_contract_ids: Which contract the commit applies to. If not provided, the commit applies to all
              contracts.

          applicable_product_ids: Which products the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          applicable_product_tags: Which tags the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          description: Used only in UI/API. It is not exposed to end customers.

          invoice_contract_id: The contract that this commit will be billed on. This is required for "POSTPAID"
              commits and for "PREPAID" commits unless there is no invoice schedule above
              (i.e., the commit is 'free'), or if do_not_invoice is set to true.

          invoice_schedule: Required for "POSTPAID" commits: the true up invoice will be generated at this
              time and only one schedule item is allowed; the total must match
              accesss_schedule amount. Optional for "PREPAID" commits: if not provided, this
              will be a "complimentary" commit with no invoice.

          name: displayed on invoices

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          specifiers: List of filters that determine what kind of customer usage draws down a commit
              or credit. A customer's usage needs to meet the condition of at least one of the
              specifiers to contribute to a commit's or credit's drawdown. This field cannot
              be used together with `applicable_product_ids` or `applicable_product_tags`.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a commit or credit
              is made with a uniqueness key that was previously used to create a commit or
              credit, a new record will not be created and the request will fail with a 409
              error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contracts/customerCommits/create",
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
                    "rate_type": rate_type,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "specifiers": specifiers,
                    "uniqueness_key": uniqueness_key,
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
        commit_id: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_contract_commits: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncBodyCursorPage[Commit]:
        """
        Retrieve all commit agreements for a customer, including both prepaid and
        postpaid commitments. This endpoint provides comprehensive visibility into
        contractual spending obligations, enabling you to track commitment utilization
        and manage customer contracts effectively.

        ### Use this endpoint to:

        - Display commitment balances and utilization in customer dashboards
        - Track prepaid commitment drawdown and remaining balances
        - Monitor postpaid commitment progress toward minimum thresholds
        - Build commitment tracking and forecasting tools
        - Show commitment history with optional ledger details
        - Manage rollover balances between contract periods

        ### Key response fields:

        An array of Commit objects containing:

        - Commit type: PREPAID (pay upfront) or POSTPAID (pay at true-up)
        - Rate type: COMMIT_RATE (discounted) or LIST_RATE (standard pricing)
        - Access schedule: When commitment funds become available
        - Invoice schedule: When the customer is billed
        - Product targeting: Which product(s) usage is eligible to draw from this commit
        - Optional ledger entries: Transaction history (if `include_ledgers=true`)
        - Balance information: Current available amount (if `include_balance=true`)
        - Rollover settings: Fraction of unused amount that carries forward

        ### Usage guidelines:

        - Pagination: Results limited to 25 commits per page; use 'next_page' for more
        - Date filtering options:
          - `covering_date`: Commits active on a specific date
          - `starting_at`: Commits with access on/after a date
          - `effective_before`: Commits with access before a date (exclusive)
        - Scope options:
          - `include_contract_commits`: Include contract-level commits (not just
            customer-level)
          - `include_archived`: Include archived commits and commits from archived
            contracts
        - Performance considerations:
          - include_ledgers: Adds detailed transaction history (slower)
          - include_balance: Adds current balance calculation (slower)
        - Optional filtering: Use commit_id to retrieve a specific commit

        Args:
          covering_date: Include only commits that have access schedules that "cover" the provided date

          effective_before: Include only commits that have any access before the provided date (exclusive)

          include_archived: Include archived commits and commits from archived contracts.

          include_balance: Include the balance in the response. Setting this flag may cause the query to be
              slower.

          include_contract_commits: Include commits on the contract level.

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          limit: The maximum number of commits to return. Defaults to 25.

          next_page: The next page token from a previous response.

          starting_at: Include only commits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/customerCommits/list",
            page=SyncBodyCursorPage[Commit],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "commit_id": commit_id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_contract_commits": include_contract_commits,
                    "include_ledgers": include_ledgers,
                    "limit": limit,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                commit_list_params.CommitListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Commit,
            method="post",
        )

    def update_end_date(
        self,
        *,
        commit_id: str,
        customer_id: str,
        access_ending_before: Union[str, datetime] | Omit = omit,
        invoices_ending_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitUpdateEndDateResponse:
        """
        Shortens the end date of a prepaid commit to terminate it earlier than
        originally scheduled. Use this endpoint when you need to cancel or reduce the
        duration of an existing prepaid commit. Only works with prepaid commit types and
        can only move the end date forward (earlier), not extend it.

        ### Usage guidelines:

        To extend commit end dates or make other comprehensive edits, use the 'edit
        commit' endpoint instead.

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
            "/v1/contracts/customerCommits/updateEndDate",
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncCommitsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        access_schedule: commit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        type: Literal["PREPAID", "POSTPAID"],
        applicable_contract_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_tags: SequenceNotStr[str] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        description: str | Omit = omit,
        invoice_contract_id: str | Omit = omit,
        invoice_schedule: commit_create_params.InvoiceSchedule | Omit = omit,
        name: str | Omit = omit,
        netsuite_sales_order_id: str | Omit = omit,
        rate_type: Literal["COMMIT_RATE", "LIST_RATE"] | Omit = omit,
        salesforce_opportunity_id: str | Omit = omit,
        specifiers: Iterable[CommitSpecifierInput] | Omit = omit,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitCreateResponse:
        """
        Creates customer-level commits that establish spending commitments for customers
        across their Metronome usage. Commits represent contracted spending obligations
        that can be either prepaid (paid upfront) or postpaid (billed later).

        Note: In most cases, you should add commitments directly to customer contracts
        using the contract/create or contract/edit APIs.

        ### Use this endpoint to:

        Use this endpoint when you need to establish customer-level spending commitments
        that can be applied across multiple contracts or scoped to specific contracts.
        Customer-level commits are ideal for:

        - Enterprise-wide minimum spending agreements that span multiple contracts
        - Multi-contract volume commitments with shared spending pools
        - Cross-contract discount tiers based on aggregate usage

        #### Commit type Requirements:

        - You must specify either "prepaid" or "postpaid" as the commit type:
        - Prepaid commits: Customer pays upfront; invoice_schedule is optional (if
          omitted, creates a commit without an invoice)
        - Postpaid commits: Customer pays when the commitment expires (the end of the
          access_schedule); invoice_schedule is required and must match access_schedule
          totals.

        #### Billing configuration:

        - invoice_contract_id is required for postpaid commits and for prepaid commits
          with billing (only optional for free prepaid commits) unless do_not_invoice is
          set to true
        - For postpaid commits: access_schedule and invoice_schedule must have matching
          amounts
        - For postpaid commits: only one schedule item is allowed in both schedules.

        #### Scoping flexibility:

        Customer-level commits can be configured in a few ways:

        - Contract-specific: Use the `applicable_contract_ids` field to limit the commit
          to specific contracts
        - Cross-contract: Leave `applicable_contract_ids` empty to allow the commit to
          be used across all of the customer's contracts

        #### Product targeting:

        Commits can be scoped to specific products using applicable_product_ids,
        applicable_product_tags, or specifiers, or left unrestricted to apply to all
        products.

        #### Priority considerations:

        When multiple commits are applicable, the one with the lower priority value will
        be consumed first. If there is a tie, contract level commits and credits will be
        applied before customer level commits and credits. Plan your priority scheme
        carefully to ensure commits are applied in the desired order.

        ### Usage guidelines:

        ⚠️ Preferred Alternative: In most cases, you should add commits directly to
        contracts using the create contract or edit contract APIs instead of creating
        customer-level commits. Contract-level commits provide better organization and
        are the recommended approach for standard use cases.

        Args:
          access_schedule: Schedule for distributing the commit to the customer. For "POSTPAID" commits
              only one schedule item is allowed and amount must match invoice_schedule total.

          priority: If multiple credits or commits are applicable, the one with the lower priority
              will apply first.

          product_id: ID of the fixed product associated with the commit. This is required because
              products are used to invoice the commit amount.

          applicable_contract_ids: Which contract the commit applies to. If not provided, the commit applies to all
              contracts.

          applicable_product_ids: Which products the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          applicable_product_tags: Which tags the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          description: Used only in UI/API. It is not exposed to end customers.

          invoice_contract_id: The contract that this commit will be billed on. This is required for "POSTPAID"
              commits and for "PREPAID" commits unless there is no invoice schedule above
              (i.e., the commit is 'free'), or if do_not_invoice is set to true.

          invoice_schedule: Required for "POSTPAID" commits: the true up invoice will be generated at this
              time and only one schedule item is allowed; the total must match
              accesss_schedule amount. Optional for "PREPAID" commits: if not provided, this
              will be a "complimentary" commit with no invoice.

          name: displayed on invoices

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          specifiers: List of filters that determine what kind of customer usage draws down a commit
              or credit. A customer's usage needs to meet the condition of at least one of the
              specifiers to contribute to a commit's or credit's drawdown. This field cannot
              be used together with `applicable_product_ids` or `applicable_product_tags`.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a commit or credit
              is made with a uniqueness key that was previously used to create a commit or
              credit, a new record will not be created and the request will fail with a 409
              error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contracts/customerCommits/create",
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
                    "rate_type": rate_type,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "specifiers": specifiers,
                    "uniqueness_key": uniqueness_key,
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
        commit_id: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_contract_commits: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Commit, AsyncBodyCursorPage[Commit]]:
        """
        Retrieve all commit agreements for a customer, including both prepaid and
        postpaid commitments. This endpoint provides comprehensive visibility into
        contractual spending obligations, enabling you to track commitment utilization
        and manage customer contracts effectively.

        ### Use this endpoint to:

        - Display commitment balances and utilization in customer dashboards
        - Track prepaid commitment drawdown and remaining balances
        - Monitor postpaid commitment progress toward minimum thresholds
        - Build commitment tracking and forecasting tools
        - Show commitment history with optional ledger details
        - Manage rollover balances between contract periods

        ### Key response fields:

        An array of Commit objects containing:

        - Commit type: PREPAID (pay upfront) or POSTPAID (pay at true-up)
        - Rate type: COMMIT_RATE (discounted) or LIST_RATE (standard pricing)
        - Access schedule: When commitment funds become available
        - Invoice schedule: When the customer is billed
        - Product targeting: Which product(s) usage is eligible to draw from this commit
        - Optional ledger entries: Transaction history (if `include_ledgers=true`)
        - Balance information: Current available amount (if `include_balance=true`)
        - Rollover settings: Fraction of unused amount that carries forward

        ### Usage guidelines:

        - Pagination: Results limited to 25 commits per page; use 'next_page' for more
        - Date filtering options:
          - `covering_date`: Commits active on a specific date
          - `starting_at`: Commits with access on/after a date
          - `effective_before`: Commits with access before a date (exclusive)
        - Scope options:
          - `include_contract_commits`: Include contract-level commits (not just
            customer-level)
          - `include_archived`: Include archived commits and commits from archived
            contracts
        - Performance considerations:
          - include_ledgers: Adds detailed transaction history (slower)
          - include_balance: Adds current balance calculation (slower)
        - Optional filtering: Use commit_id to retrieve a specific commit

        Args:
          covering_date: Include only commits that have access schedules that "cover" the provided date

          effective_before: Include only commits that have any access before the provided date (exclusive)

          include_archived: Include archived commits and commits from archived contracts.

          include_balance: Include the balance in the response. Setting this flag may cause the query to be
              slower.

          include_contract_commits: Include commits on the contract level.

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          limit: The maximum number of commits to return. Defaults to 25.

          next_page: The next page token from a previous response.

          starting_at: Include only commits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/customerCommits/list",
            page=AsyncBodyCursorPage[Commit],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "commit_id": commit_id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_contract_commits": include_contract_commits,
                    "include_ledgers": include_ledgers,
                    "limit": limit,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                commit_list_params.CommitListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Commit,
            method="post",
        )

    async def update_end_date(
        self,
        *,
        commit_id: str,
        customer_id: str,
        access_ending_before: Union[str, datetime] | Omit = omit,
        invoices_ending_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommitUpdateEndDateResponse:
        """
        Shortens the end date of a prepaid commit to terminate it earlier than
        originally scheduled. Use this endpoint when you need to cancel or reduce the
        duration of an existing prepaid commit. Only works with prepaid commit types and
        can only move the end date forward (earlier), not extend it.

        ### Usage guidelines:

        To extend commit end dates or make other comprehensive edits, use the 'edit
        commit' endpoint instead.

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
            "/v1/contracts/customerCommits/updateEndDate",
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
