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
from ....types.v1.customers import credit_list_params, credit_create_params, credit_update_end_date_params
from ....types.shared.credit import Credit
from ....types.v1.customers.credit_create_response import CreditCreateResponse
from ....types.shared_params.commit_specifier_input import CommitSpecifierInput
from ....types.v1.customers.credit_update_end_date_response import CreditUpdateEndDateResponse

__all__ = ["CreditsResource", "AsyncCreditsResource"]


class CreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return CreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return CreditsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        access_schedule: credit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        applicable_contract_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_tags: SequenceNotStr[str] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        description: str | Omit = omit,
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
    ) -> CreditCreateResponse:
        """
        Creates customer-level credits that provide spending allowances or free credit
        balances for customers across their Metronome usage. Note: In most cases, you
        should add credits directly to customer contracts using the contract/create or
        contract/edit APIs.

        ### Use this endpoint to:

        Use this endpoint when you need to provision credits directly at the customer
        level that can be applied across multiple contracts or scoped to specific
        contracts. Customer-level credits are ideal for:

        - Customer onboarding incentives that apply globally
        - Flexible spending allowances that aren't tied to a single contract
        - Migration scenarios where you need to preserve existing customer balances

        #### Scoping flexibility:

        Customer-level credits can be configured in two ways:

        - Contract-specific: Use the applicable_contract_ids field to limit the credit
          to specific contracts
        - Cross-contract: Leave applicable_contract_ids empty to allow the credit to be
          used across all of the customer's contracts

        #### Product Targeting:

        Credits can be scoped to specific products using `applicable_product_ids` or
        `applicable_product_tags`, or left unrestricted to apply to all products.

        #### Priority considerations:

        When multiple credits are applicable, the one with the lower priority value will
        be consumed first. If there is a tie, contract level commits and credits will be
        applied before customer level commits and credits. Plan your priority scheme
        carefully to ensure credits are applied in the desired order.

        #### Access Schedule Required:

        You must provide an `access_schedule` that defines when and how much credit
        becomes available to the customer over time. This usually is aligned to the
        contract schedule or starts immediately and is set to expire in the future.

        ### Usage Guidelines:

        ⚠️ Preferred Alternative: In most cases, you should add credits directly to
        contracts using the contract/create or contract/edit APIs instead of creating
        customer-level credits. Contract-level credits provide better organization, and
        are easier for finance teams to recognize revenue, and are the recommended
        approach for most use cases.

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

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          description: Used only in UI/API. It is not exposed to end customers.

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
            "/v1/contracts/customerCredits/create",
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
                    "rate_type": rate_type,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "specifiers": specifiers,
                    "uniqueness_key": uniqueness_key,
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
        covering_date: Union[str, datetime] | Omit = omit,
        credit_id: str | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_contract_credits: bool | Omit = omit,
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
    ) -> SyncBodyCursorPage[Credit]:
        """
        Retrieve a detailed list of all credits available to a customer, including
        promotional credits and contract-specific credits. This endpoint provides
        comprehensive visibility into credit balances, access schedules, and usage
        rules, enabling you to build credit management interfaces and track available
        funding.

        ### Use this endpoint to:

        - Display all available credits in customer billing dashboards
        - Show credit balances and expiration dates
        - Track credit usage history with optional ledger details
        - Build credit management and reporting tools
        - Monitor promotional credit utilization • Support customer inquiries about
          available credits

        ### Key response fields:

        An array of Credit objects containing:

        - Credit details: Name, priority, and which applicable products/tags it applies
          to
        - Product ID: The `product_id` of the credit. This is for external mapping into
          your quote-to-cash stack, not the product it applies to.
        - Access schedule: When credits become available and expire
        - Optional ledger entries: Transaction history (if `include_ledgers=true`)
        - Balance information: Current available amount (if `include_balance=true`)
        - Metadata: Custom fields and usage specifiers

        ### Usage guidelines:

        - Pagination: Results limited to 25 commits per page; use next_page for more
        - Date filtering options:
          - `covering_date`: Credits active on a specific date
          - `starting_at`: Credits with access on/after a date
          - `effective_before`: Credits with access before a date (exclusive)
        - Scope options:
          - `include_contract_credits`: Include contract-level credits (not just
            customer-level)
          - `include_archived`: Include archived credits and credits from archived
            contracts
        - Performance considerations:
          - `include_ledgers`: Adds detailed transaction history (slower)
          - `include_balance`: Adds current balance calculation (slower)
        - Optional filtering: Use credit_id to retrieve a specific commit

        Args:
          covering_date: Return only credits that have access schedules that "cover" the provided date

          effective_before: Include only credits that have any access before the provided date (exclusive)

          include_archived: Include archived credits and credits from archived contracts.

          include_balance: Include the balance in the response. Setting this flag may cause the query to be
              slower.

          include_contract_credits: Include credits on the contract level.

          include_ledgers: Include credit ledgers in the response. Setting this flag may cause the query to
              be slower.

          limit: The maximum number of commits to return. Defaults to 25.

          next_page: The next page token from a previous response.

          starting_at: Include only credits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/customerCredits/list",
            page=SyncBodyCursorPage[Credit],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "credit_id": credit_id,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_contract_credits": include_contract_credits,
                    "include_ledgers": include_ledgers,
                    "limit": limit,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                credit_list_params.CreditListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Credit,
            method="post",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditUpdateEndDateResponse:
        """
        Shortens the end date of an existing customer credit to terminate it earlier
        than originally scheduled. Only allows moving end dates forward (earlier), not
        extending them.

        Note: To extend credit end dates or make comprehensive edits, use the 'edit
        credit' endpoint instead.

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
            "/v1/contracts/customerCredits/updateEndDate",
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncCreditsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        access_schedule: credit_create_params.AccessSchedule,
        customer_id: str,
        priority: float,
        product_id: str,
        applicable_contract_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_ids: SequenceNotStr[str] | Omit = omit,
        applicable_product_tags: SequenceNotStr[str] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        description: str | Omit = omit,
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
    ) -> CreditCreateResponse:
        """
        Creates customer-level credits that provide spending allowances or free credit
        balances for customers across their Metronome usage. Note: In most cases, you
        should add credits directly to customer contracts using the contract/create or
        contract/edit APIs.

        ### Use this endpoint to:

        Use this endpoint when you need to provision credits directly at the customer
        level that can be applied across multiple contracts or scoped to specific
        contracts. Customer-level credits are ideal for:

        - Customer onboarding incentives that apply globally
        - Flexible spending allowances that aren't tied to a single contract
        - Migration scenarios where you need to preserve existing customer balances

        #### Scoping flexibility:

        Customer-level credits can be configured in two ways:

        - Contract-specific: Use the applicable_contract_ids field to limit the credit
          to specific contracts
        - Cross-contract: Leave applicable_contract_ids empty to allow the credit to be
          used across all of the customer's contracts

        #### Product Targeting:

        Credits can be scoped to specific products using `applicable_product_ids` or
        `applicable_product_tags`, or left unrestricted to apply to all products.

        #### Priority considerations:

        When multiple credits are applicable, the one with the lower priority value will
        be consumed first. If there is a tie, contract level commits and credits will be
        applied before customer level commits and credits. Plan your priority scheme
        carefully to ensure credits are applied in the desired order.

        #### Access Schedule Required:

        You must provide an `access_schedule` that defines when and how much credit
        becomes available to the customer over time. This usually is aligned to the
        contract schedule or starts immediately and is set to expire in the future.

        ### Usage Guidelines:

        ⚠️ Preferred Alternative: In most cases, you should add credits directly to
        contracts using the contract/create or contract/edit APIs instead of creating
        customer-level credits. Contract-level credits provide better organization, and
        are easier for finance teams to recognize revenue, and are the recommended
        approach for most use cases.

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

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          description: Used only in UI/API. It is not exposed to end customers.

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
            "/v1/contracts/customerCredits/create",
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
                    "rate_type": rate_type,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "specifiers": specifiers,
                    "uniqueness_key": uniqueness_key,
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
        covering_date: Union[str, datetime] | Omit = omit,
        credit_id: str | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_contract_credits: bool | Omit = omit,
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
    ) -> AsyncPaginator[Credit, AsyncBodyCursorPage[Credit]]:
        """
        Retrieve a detailed list of all credits available to a customer, including
        promotional credits and contract-specific credits. This endpoint provides
        comprehensive visibility into credit balances, access schedules, and usage
        rules, enabling you to build credit management interfaces and track available
        funding.

        ### Use this endpoint to:

        - Display all available credits in customer billing dashboards
        - Show credit balances and expiration dates
        - Track credit usage history with optional ledger details
        - Build credit management and reporting tools
        - Monitor promotional credit utilization • Support customer inquiries about
          available credits

        ### Key response fields:

        An array of Credit objects containing:

        - Credit details: Name, priority, and which applicable products/tags it applies
          to
        - Product ID: The `product_id` of the credit. This is for external mapping into
          your quote-to-cash stack, not the product it applies to.
        - Access schedule: When credits become available and expire
        - Optional ledger entries: Transaction history (if `include_ledgers=true`)
        - Balance information: Current available amount (if `include_balance=true`)
        - Metadata: Custom fields and usage specifiers

        ### Usage guidelines:

        - Pagination: Results limited to 25 commits per page; use next_page for more
        - Date filtering options:
          - `covering_date`: Credits active on a specific date
          - `starting_at`: Credits with access on/after a date
          - `effective_before`: Credits with access before a date (exclusive)
        - Scope options:
          - `include_contract_credits`: Include contract-level credits (not just
            customer-level)
          - `include_archived`: Include archived credits and credits from archived
            contracts
        - Performance considerations:
          - `include_ledgers`: Adds detailed transaction history (slower)
          - `include_balance`: Adds current balance calculation (slower)
        - Optional filtering: Use credit_id to retrieve a specific commit

        Args:
          covering_date: Return only credits that have access schedules that "cover" the provided date

          effective_before: Include only credits that have any access before the provided date (exclusive)

          include_archived: Include archived credits and credits from archived contracts.

          include_balance: Include the balance in the response. Setting this flag may cause the query to be
              slower.

          include_contract_credits: Include credits on the contract level.

          include_ledgers: Include credit ledgers in the response. Setting this flag may cause the query to
              be slower.

          limit: The maximum number of commits to return. Defaults to 25.

          next_page: The next page token from a previous response.

          starting_at: Include only credits that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/customerCredits/list",
            page=AsyncBodyCursorPage[Credit],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "credit_id": credit_id,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_contract_credits": include_contract_credits,
                    "include_ledgers": include_ledgers,
                    "limit": limit,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                credit_list_params.CreditListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=Credit,
            method="post",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CreditUpdateEndDateResponse:
        """
        Shortens the end date of an existing customer credit to terminate it earlier
        than originally scheduled. Only allows moving end dates forward (earlier), not
        extending them.

        Note: To extend credit end dates or make comprehensive edits, use the 'edit
        credit' endpoint instead.

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
            "/v1/contracts/customerCredits/updateEndDate",
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
