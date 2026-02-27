# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    package_list_params,
    package_create_params,
    package_archive_params,
    package_retrieve_params,
    package_list_contracts_on_package_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.package_list_response import PackageListResponse
from ...types.v1.package_create_response import PackageCreateResponse
from ...types.v1.package_archive_response import PackageArchiveResponse
from ...types.v1.package_retrieve_response import PackageRetrieveResponse
from ...types.shared_params.spend_threshold_configuration import SpendThresholdConfiguration
from ...types.v1.package_list_contracts_on_package_response import PackageListContractsOnPackageResponse
from ...types.shared_params.prepaid_balance_threshold_configuration import PrepaidBalanceThresholdConfiguration

__all__ = ["PackagesResource", "AsyncPackagesResource"]


class PackagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PackagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return PackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PackagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return PackagesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        aliases: Iterable[package_create_params.Alias] | Omit = omit,
        billing_anchor_date: Literal["contract_start_date", "first_billing_period"] | Omit = omit,
        billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]
        | Omit = omit,
        commits: Iterable[package_create_params.Commit] | Omit = omit,
        contract_name: str | Omit = omit,
        credits: Iterable[package_create_params.Credit] | Omit = omit,
        delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"] | Omit = omit,
        duration: package_create_params.Duration | Omit = omit,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        overrides: Iterable[package_create_params.Override] | Omit = omit,
        prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfiguration | Omit = omit,
        rate_card_alias: str | Omit = omit,
        rate_card_id: str | Omit = omit,
        recurring_commits: Iterable[package_create_params.RecurringCommit] | Omit = omit,
        recurring_credits: Iterable[package_create_params.RecurringCredit] | Omit = omit,
        scheduled_charges: Iterable[package_create_params.ScheduledCharge] | Omit = omit,
        scheduled_charges_on_usage_invoices: Literal["ALL"] | Omit = omit,
        spend_threshold_configuration: SpendThresholdConfiguration | Omit = omit,
        subscriptions: Iterable[package_create_params.Subscription] | Omit = omit,
        uniqueness_key: str | Omit = omit,
        usage_statement_schedule: package_create_params.UsageStatementSchedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PackageCreateResponse:
        """
        Create a package that defines a set of reusable, time-relative contract terms
        that can be used across cohorts of customers. Packages provide an abstraction
        layer on top of rate cards to provide an easy way to provision customers with
        standard pricing.

        ### **Use this endpoint to:**

        - Model standard pay-as-you-go pricing packages that can be easily reused across
          customers
        - Define standardized contract terms and discounting for sales-led motions
        - Set aliases for the package to facilitate easy package transition. Aliases are
          human-readable names that you can use in the place of the id of the package
          when provisioning a customer’s contract. By using an alias, you can easily
          create a contract and provision a customer by choosing the “Starter Plan”
          package, without storing the package ID in your internal systems. This is
          helpful when launching terms for a package, as you can create a new package
          with the “Starter Plan” alias scheduled to be assigned without updating your
          provisioning code.

        ### Key input fields:

        - `starting_at_offset`: Starting date relative to contract start. Generates the
          `starting_at` date when a contract is provisioned using a package.
        - `duration`: Duration starting from `starting_at_offset`. Generates the
          `ending_before` date when a contract is provisioned using a package.
        - `date_offset`: Date relative to contract start. Used for point-in-time dates
          without a duration.
        - `aliases`: Human-readable name to use when provisioning contracts with a
          package.

        ### Usage guidelines:

        - Use packages for standard self-serve use cases where customers have consistent
          terms. For customers with negotiated custom contract terms, use the
          `createContract` endpoint for maximum flexibility.
        - Billing provider configuration can be set when creating a package by using
          `billing_provider` and `delivery_method`. To provision a customer successfully
          with a package, the customer must have one and only one billing provider
          configuration that matches the billing provider configuration set on the
          package.
        - A package alias can only be used by one package at a time. If you create a new
          package with an alias that is already in use by another package, the original
          package’s alias schedule will be updated. The alias will reference the package
          to which it was most recently assigned.
        - Terms can only be specified using times relative to the contract start date.
          Supported granularities are: `days`, `weeks`, `months`, `years`
        - Packages cannot be edited once created. Use the rate card to easily add new
          rates across all of your customers or make direct edits to a contract after
          provisioning with a package. Edited contracts will still be associated with
          the package used during provisioning.

        Args:
          aliases: Reference this alias when creating a contract. If the same alias is assigned to
              multiple packages, it will reference the package to which it was most recently
              assigned. It is not exposed to end customers.

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          rate_card_alias: Selects the rate card linked to the specified alias as of the contract's start
              date.

          scheduled_charges_on_usage_invoices: Determines which scheduled and commit charges to consolidate onto the Contract's
              usage invoice. The charge's `timestamp` must match the usage invoice's
              `ending_before` date for consolidation to occur. This field cannot be modified
              after a Contract has been created. If this field is omitted, charges will appear
              on a separate invoice from usage charges.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/packages/create",
            body=maybe_transform(
                {
                    "name": name,
                    "aliases": aliases,
                    "billing_anchor_date": billing_anchor_date,
                    "billing_provider": billing_provider,
                    "commits": commits,
                    "contract_name": contract_name,
                    "credits": credits,
                    "delivery_method": delivery_method,
                    "duration": duration,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "net_payment_terms_days": net_payment_terms_days,
                    "overrides": overrides,
                    "prepaid_balance_threshold_configuration": prepaid_balance_threshold_configuration,
                    "rate_card_alias": rate_card_alias,
                    "rate_card_id": rate_card_id,
                    "recurring_commits": recurring_commits,
                    "recurring_credits": recurring_credits,
                    "scheduled_charges": scheduled_charges,
                    "scheduled_charges_on_usage_invoices": scheduled_charges_on_usage_invoices,
                    "spend_threshold_configuration": spend_threshold_configuration,
                    "subscriptions": subscriptions,
                    "uniqueness_key": uniqueness_key,
                    "usage_statement_schedule": usage_statement_schedule,
                },
                package_create_params.PackageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PackageCreateResponse,
        )

    def retrieve(
        self,
        *,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PackageRetrieveResponse:
        """
        Gets the details for a specific package, including name, aliases, duration, and
        terms. Use this endpoint to understand a package’s alias schedule, or display a
        specific package’s details to end customers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/packages/get",
            body=maybe_transform({"package_id": package_id}, package_retrieve_params.PackageRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PackageRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PackageListResponse]:
        """Lists all packages with details including name, aliases, duration, and terms.

        To
        view contracts on a specific package, use the `listContractsOnPackage` endpoint.

        Args:
          limit: The maximum number of packages to return. Defaults to 10.

          next_page: Cursor that indicates where the next page of results should start.

          archive_filter: Filter packages by archived status. Defaults to NOT_ARCHIVED.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/packages/list",
            page=SyncCursorPage[PackageListResponse],
            body=maybe_transform({"archive_filter": archive_filter}, package_list_params.PackageListParams),
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
                    package_list_params.PackageListParams,
                ),
            ),
            model=PackageListResponse,
            method="post",
        )

    def archive(
        self,
        *,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PackageArchiveResponse:
        """Archive a package.

        Archived packages cannot be used to create new contracts.
        However, existing contracts associated with the package will continue to
        function as normal. Once you archive a package, you can still retrieve it in the
        UI and API, but you cannot unarchive it.

        Args:
          package_id: ID of the package to archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/packages/archive",
            body=maybe_transform({"package_id": package_id}, package_archive_params.PackageArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PackageArchiveResponse,
        )

    def list_contracts_on_package(
        self,
        *,
        package_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[PackageListContractsOnPackageResponse]:
        """
        For a given package, returns all contract IDs and customer IDs associated with
        the package over a specific time period.

        ### Use this endpoint to:

        - Understand which customers are provisioned on a package at any given time for
          internal cohort management
        - Manage customer migrations to a new package. For example, to migrate all
          active customers to a new package, call this endpoint, end contracts, and
          provision customers on a new package.

        ### **Usage guidelines:**

        Use the **`starting_at`**, **`covering_date`**,
        and **`include_archived`** parameters to filter the list of returned contracts.
        For example, to list only currently active contracts,
        pass **`covering_date`** equal to the current time.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          covering_date: Optional RFC 3339 timestamp. Only include contracts active on the provided date.
              This cannot be provided if starting_at filter is provided.

          include_archived: Default false. Determines whether to include archived contracts in the results

          starting_at: Optional RFC 3339 timestamp. Only include contracts that started on or after
              this date. This cannot be provided if covering_date filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/packages/listContractsOnPackage",
            page=SyncCursorPage[PackageListContractsOnPackageResponse],
            body=maybe_transform(
                {
                    "package_id": package_id,
                    "covering_date": covering_date,
                    "include_archived": include_archived,
                    "starting_at": starting_at,
                },
                package_list_contracts_on_package_params.PackageListContractsOnPackageParams,
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
                    package_list_contracts_on_package_params.PackageListContractsOnPackageParams,
                ),
            ),
            model=PackageListContractsOnPackageResponse,
            method="post",
        )


class AsyncPackagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPackagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPackagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPackagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncPackagesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        aliases: Iterable[package_create_params.Alias] | Omit = omit,
        billing_anchor_date: Literal["contract_start_date", "first_billing_period"] | Omit = omit,
        billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]
        | Omit = omit,
        commits: Iterable[package_create_params.Commit] | Omit = omit,
        contract_name: str | Omit = omit,
        credits: Iterable[package_create_params.Credit] | Omit = omit,
        delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"] | Omit = omit,
        duration: package_create_params.Duration | Omit = omit,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        overrides: Iterable[package_create_params.Override] | Omit = omit,
        prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfiguration | Omit = omit,
        rate_card_alias: str | Omit = omit,
        rate_card_id: str | Omit = omit,
        recurring_commits: Iterable[package_create_params.RecurringCommit] | Omit = omit,
        recurring_credits: Iterable[package_create_params.RecurringCredit] | Omit = omit,
        scheduled_charges: Iterable[package_create_params.ScheduledCharge] | Omit = omit,
        scheduled_charges_on_usage_invoices: Literal["ALL"] | Omit = omit,
        spend_threshold_configuration: SpendThresholdConfiguration | Omit = omit,
        subscriptions: Iterable[package_create_params.Subscription] | Omit = omit,
        uniqueness_key: str | Omit = omit,
        usage_statement_schedule: package_create_params.UsageStatementSchedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PackageCreateResponse:
        """
        Create a package that defines a set of reusable, time-relative contract terms
        that can be used across cohorts of customers. Packages provide an abstraction
        layer on top of rate cards to provide an easy way to provision customers with
        standard pricing.

        ### **Use this endpoint to:**

        - Model standard pay-as-you-go pricing packages that can be easily reused across
          customers
        - Define standardized contract terms and discounting for sales-led motions
        - Set aliases for the package to facilitate easy package transition. Aliases are
          human-readable names that you can use in the place of the id of the package
          when provisioning a customer’s contract. By using an alias, you can easily
          create a contract and provision a customer by choosing the “Starter Plan”
          package, without storing the package ID in your internal systems. This is
          helpful when launching terms for a package, as you can create a new package
          with the “Starter Plan” alias scheduled to be assigned without updating your
          provisioning code.

        ### Key input fields:

        - `starting_at_offset`: Starting date relative to contract start. Generates the
          `starting_at` date when a contract is provisioned using a package.
        - `duration`: Duration starting from `starting_at_offset`. Generates the
          `ending_before` date when a contract is provisioned using a package.
        - `date_offset`: Date relative to contract start. Used for point-in-time dates
          without a duration.
        - `aliases`: Human-readable name to use when provisioning contracts with a
          package.

        ### Usage guidelines:

        - Use packages for standard self-serve use cases where customers have consistent
          terms. For customers with negotiated custom contract terms, use the
          `createContract` endpoint for maximum flexibility.
        - Billing provider configuration can be set when creating a package by using
          `billing_provider` and `delivery_method`. To provision a customer successfully
          with a package, the customer must have one and only one billing provider
          configuration that matches the billing provider configuration set on the
          package.
        - A package alias can only be used by one package at a time. If you create a new
          package with an alias that is already in use by another package, the original
          package’s alias schedule will be updated. The alias will reference the package
          to which it was most recently assigned.
        - Terms can only be specified using times relative to the contract start date.
          Supported granularities are: `days`, `weeks`, `months`, `years`
        - Packages cannot be edited once created. Use the rate card to easily add new
          rates across all of your customers or make direct edits to a contract after
          provisioning with a package. Edited contracts will still be associated with
          the package used during provisioning.

        Args:
          aliases: Reference this alias when creating a contract. If the same alias is assigned to
              multiple packages, it will reference the package to which it was most recently
              assigned. It is not exposed to end customers.

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          rate_card_alias: Selects the rate card linked to the specified alias as of the contract's start
              date.

          scheduled_charges_on_usage_invoices: Determines which scheduled and commit charges to consolidate onto the Contract's
              usage invoice. The charge's `timestamp` must match the usage invoice's
              `ending_before` date for consolidation to occur. This field cannot be modified
              after a Contract has been created. If this field is omitted, charges will appear
              on a separate invoice from usage charges.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/packages/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "aliases": aliases,
                    "billing_anchor_date": billing_anchor_date,
                    "billing_provider": billing_provider,
                    "commits": commits,
                    "contract_name": contract_name,
                    "credits": credits,
                    "delivery_method": delivery_method,
                    "duration": duration,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "net_payment_terms_days": net_payment_terms_days,
                    "overrides": overrides,
                    "prepaid_balance_threshold_configuration": prepaid_balance_threshold_configuration,
                    "rate_card_alias": rate_card_alias,
                    "rate_card_id": rate_card_id,
                    "recurring_commits": recurring_commits,
                    "recurring_credits": recurring_credits,
                    "scheduled_charges": scheduled_charges,
                    "scheduled_charges_on_usage_invoices": scheduled_charges_on_usage_invoices,
                    "spend_threshold_configuration": spend_threshold_configuration,
                    "subscriptions": subscriptions,
                    "uniqueness_key": uniqueness_key,
                    "usage_statement_schedule": usage_statement_schedule,
                },
                package_create_params.PackageCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PackageCreateResponse,
        )

    async def retrieve(
        self,
        *,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PackageRetrieveResponse:
        """
        Gets the details for a specific package, including name, aliases, duration, and
        terms. Use this endpoint to understand a package’s alias schedule, or display a
        specific package’s details to end customers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/packages/get",
            body=await async_maybe_transform({"package_id": package_id}, package_retrieve_params.PackageRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PackageRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PackageListResponse, AsyncCursorPage[PackageListResponse]]:
        """Lists all packages with details including name, aliases, duration, and terms.

        To
        view contracts on a specific package, use the `listContractsOnPackage` endpoint.

        Args:
          limit: The maximum number of packages to return. Defaults to 10.

          next_page: Cursor that indicates where the next page of results should start.

          archive_filter: Filter packages by archived status. Defaults to NOT_ARCHIVED.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/packages/list",
            page=AsyncCursorPage[PackageListResponse],
            body=maybe_transform({"archive_filter": archive_filter}, package_list_params.PackageListParams),
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
                    package_list_params.PackageListParams,
                ),
            ),
            model=PackageListResponse,
            method="post",
        )

    async def archive(
        self,
        *,
        package_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PackageArchiveResponse:
        """Archive a package.

        Archived packages cannot be used to create new contracts.
        However, existing contracts associated with the package will continue to
        function as normal. Once you archive a package, you can still retrieve it in the
        UI and API, but you cannot unarchive it.

        Args:
          package_id: ID of the package to archive

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/packages/archive",
            body=await async_maybe_transform({"package_id": package_id}, package_archive_params.PackageArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PackageArchiveResponse,
        )

    def list_contracts_on_package(
        self,
        *,
        package_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PackageListContractsOnPackageResponse, AsyncCursorPage[PackageListContractsOnPackageResponse]]:
        """
        For a given package, returns all contract IDs and customer IDs associated with
        the package over a specific time period.

        ### Use this endpoint to:

        - Understand which customers are provisioned on a package at any given time for
          internal cohort management
        - Manage customer migrations to a new package. For example, to migrate all
          active customers to a new package, call this endpoint, end contracts, and
          provision customers on a new package.

        ### **Usage guidelines:**

        Use the **`starting_at`**, **`covering_date`**,
        and **`include_archived`** parameters to filter the list of returned contracts.
        For example, to list only currently active contracts,
        pass **`covering_date`** equal to the current time.

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          covering_date: Optional RFC 3339 timestamp. Only include contracts active on the provided date.
              This cannot be provided if starting_at filter is provided.

          include_archived: Default false. Determines whether to include archived contracts in the results

          starting_at: Optional RFC 3339 timestamp. Only include contracts that started on or after
              this date. This cannot be provided if covering_date filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/packages/listContractsOnPackage",
            page=AsyncCursorPage[PackageListContractsOnPackageResponse],
            body=maybe_transform(
                {
                    "package_id": package_id,
                    "covering_date": covering_date,
                    "include_archived": include_archived,
                    "starting_at": starting_at,
                },
                package_list_contracts_on_package_params.PackageListContractsOnPackageParams,
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
                    package_list_contracts_on_package_params.PackageListContractsOnPackageParams,
                ),
            ),
            model=PackageListContractsOnPackageResponse,
            method="post",
        )


class PackagesResourceWithRawResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.create = to_raw_response_wrapper(
            packages.create,
        )
        self.retrieve = to_raw_response_wrapper(
            packages.retrieve,
        )
        self.list = to_raw_response_wrapper(
            packages.list,
        )
        self.archive = to_raw_response_wrapper(
            packages.archive,
        )
        self.list_contracts_on_package = to_raw_response_wrapper(
            packages.list_contracts_on_package,
        )


class AsyncPackagesResourceWithRawResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.create = async_to_raw_response_wrapper(
            packages.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            packages.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            packages.list,
        )
        self.archive = async_to_raw_response_wrapper(
            packages.archive,
        )
        self.list_contracts_on_package = async_to_raw_response_wrapper(
            packages.list_contracts_on_package,
        )


class PackagesResourceWithStreamingResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.create = to_streamed_response_wrapper(
            packages.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            packages.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            packages.list,
        )
        self.archive = to_streamed_response_wrapper(
            packages.archive,
        )
        self.list_contracts_on_package = to_streamed_response_wrapper(
            packages.list_contracts_on_package,
        )


class AsyncPackagesResourceWithStreamingResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.create = async_to_streamed_response_wrapper(
            packages.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            packages.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            packages.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            packages.archive,
        )
        self.list_contracts_on_package = async_to_streamed_response_wrapper(
            packages.list_contracts_on_package,
        )
