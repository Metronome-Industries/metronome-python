# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

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
from .commits import (
    CommitsResource,
    AsyncCommitsResource,
    CommitsResourceWithRawResponse,
    AsyncCommitsResourceWithRawResponse,
    CommitsResourceWithStreamingResponse,
    AsyncCommitsResourceWithStreamingResponse,
)
from .credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from .invoices import (
    InvoicesResource,
    AsyncInvoicesResource,
    InvoicesResourceWithRawResponse,
    AsyncInvoicesResourceWithRawResponse,
    InvoicesResourceWithStreamingResponse,
    AsyncInvoicesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
    customer_list_params,
    customer_create_params,
    customer_archive_params,
    customer_set_name_params,
    customer_list_costs_params,
    customer_update_config_params,
    customer_preview_events_params,
    customer_set_ingest_aliases_params,
    customer_list_billable_metrics_params,
    customer_set_billing_configurations_params,
    customer_retrieve_billing_configurations_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from .billing_config import (
    BillingConfigResource,
    AsyncBillingConfigResource,
    BillingConfigResourceWithRawResponse,
    AsyncBillingConfigResourceWithRawResponse,
    BillingConfigResourceWithStreamingResponse,
    AsyncBillingConfigResourceWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from .named_schedules import (
    NamedSchedulesResource,
    AsyncNamedSchedulesResource,
    NamedSchedulesResourceWithRawResponse,
    AsyncNamedSchedulesResourceWithRawResponse,
    NamedSchedulesResourceWithStreamingResponse,
    AsyncNamedSchedulesResourceWithStreamingResponse,
)
from ....types.v1.customer_detail import CustomerDetail
from ....types.v1.customer_create_response import CustomerCreateResponse
from ....types.v1.customer_archive_response import CustomerArchiveResponse
from ....types.v1.customer_retrieve_response import CustomerRetrieveResponse
from ....types.v1.customer_set_name_response import CustomerSetNameResponse
from ....types.v1.customer_list_costs_response import CustomerListCostsResponse
from ....types.v1.customer_preview_events_response import CustomerPreviewEventsResponse
from ....types.v1.customer_list_billable_metrics_response import CustomerListBillableMetricsResponse
from ....types.v1.customer_set_billing_configurations_response import CustomerSetBillingConfigurationsResponse
from ....types.v1.customer_retrieve_billing_configurations_response import CustomerRetrieveBillingConfigurationsResponse

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
    def commits(self) -> CommitsResource:
        return CommitsResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResource:
        return NamedSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return CustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return CustomersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        billing_config: customer_create_params.BillingConfig | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        customer_billing_provider_configurations: Iterable[customer_create_params.CustomerBillingProviderConfiguration]
        | Omit = omit,
        customer_revenue_system_configurations: Iterable[customer_create_params.CustomerRevenueSystemConfiguration]
        | Omit = omit,
        external_id: str | Omit = omit,
        ingest_aliases: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerCreateResponse:
        """
        Create a new customer in Metronome and optionally the billing configuration
        (recommended) which dictates where invoices for the customer will be sent or
        where payment will be collected.

        ### Use this endpoint to:

        Execute your customer provisioning workflows for either PLG motions, where
        customers originate in your platform, or SLG motions, where customers originate
        in your sales system.

        ### Key response fields:

        This end-point returns the `customer_id` created by the request. This id can be
        used to fetch relevant billing configurations and create contracts.

        ### Example workflow:

        - Generally, Metronome recommends first creating the customer in the downstream
          payment / ERP system when payment method is collected and then creating the
          customer in Metronome using the response (i.e. `customer_id`) from the
          downstream system. If you do not create a billing configuration on customer
          creation, you can add it later.
        - Once a customer is created, you can then create a contract for the customer.
          In the contract creation process, you will need to add the customer billing
          configuration to the contract to ensure Metronome invoices the customer
          correctly. This is because a customer can have multiple configurations.
        - As part of the customer creation process, set the ingest alias for the
          customer which will ensure usage is accurately mapped to the customer. Ingest
          aliases can be added or changed after the creation process as well.

        ### Usage guidelines:

        For details on different billing configurations for different systems, review
        the `/setCustomerBillingConfiguration` end-point.

        Args:
          name: This will be truncated to 160 characters if the provided name is longer.

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          external_id: (deprecated, use ingest_aliases instead) an alias that can be used to refer to
              this customer in usage events

          ingest_aliases: Aliases that can be used to refer to this customer in usage events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customers",
            body=maybe_transform(
                {
                    "name": name,
                    "billing_config": billing_config,
                    "custom_fields": custom_fields,
                    "customer_billing_provider_configurations": customer_billing_provider_configurations,
                    "customer_revenue_system_configurations": customer_revenue_system_configurations,
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
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerRetrieveResponse:
        """Get detailed information for a specific customer by their Metronome ID.

        Returns
        customer profile data including name, creation date, ingest aliases,
        configuration settings, and custom fields. Use this endpoint to fetch complete
        customer details for billing operations or account management.

        Note: If searching for a customer billing configuration, use the
        `/getCustomerBillingConfigurations` endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._get(
            f"/v1/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ingest_alias: str | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        only_archived: bool | Omit = omit,
        salesforce_account_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CustomerDetail]:
        """Gets a paginated list of all customers in your Metronome account.

        Use this
        endpoint to browse your customer base, implement customer search functionality,
        or sync customer data with external systems. Returns customer details including
        IDs, names, and configuration settings. Supports filtering and pagination
        parameters for efficient data retrieval.

        Args:
          customer_ids: Filter the customer list by customer_id. Up to 100 ids can be provided.

          ingest_alias: Filter the customer list by ingest_alias

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          only_archived: Filter the customer list to only return archived customers. By default, only
              active customers are returned.

          salesforce_account_ids: Filter the customer list by salesforce_account_id. Up to 100 ids can be
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customers",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerArchiveResponse:
        """Use this endpoint to archive a customer while preserving auditability.

        Archiving
        a customer will automatically archive all contracts as of the current date and
        void all corresponding invoices. Use this endpoint if a customer is onboarded by
        mistake.

        ### Usage guidelines:

        - Once a customer is archived, it cannot be unarchived.
        - Archived customers can still be viewed through the API or the UI for audit
          purposes.
        - Ingest aliases remain idempotent for archived customers. In order to reuse an
          ingest alias, first remove the ingest alias from the customer prior to
          archiving.
        - Any notifications associated with the customer will no longer be triggered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customers/archive",
            body=maybe_transform({"id": id}, customer_archive_params.CustomerArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerArchiveResponse,
        )

    def list_billable_metrics(
        self,
        *,
        customer_id: str,
        include_archived: bool | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        on_current_plan: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CustomerListBillableMetricsResponse]:
        """Get all billable metrics available for a specific customer.

        Supports pagination
        and filtering by current plan status or archived metrics. Use this endpoint to
        see which metrics are being tracked for billing calculations for a given
        customer.

        Args:
          include_archived: If true, the list of returned metrics will include archived metrics

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
            f"/v1/customers/{customer_id}/billable-metrics",
            page=SyncCursorPage[CustomerListBillableMetricsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_archived": include_archived,
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
        *,
        customer_id: str,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CustomerListCostsResponse]:
        """
        Fetch daily pending costs for the specified customer, broken down by credit type
        and line items. Note: this is not supported for customers whose plan includes a
        UNIQUE-type billable metric. This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

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
            f"/v1/customers/{customer_id}/costs",
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

    def preview_events(
        self,
        *,
        customer_id: str,
        events: Iterable[customer_preview_events_params.Event],
        mode: Literal["replace", "merge"] | Omit = omit,
        skip_zero_qty_line_items: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerPreviewEventsResponse:
        """Preview how a set of events will affect a customer's invoices.

        Generates draft
        invoices for a customer using their current contract configuration and the
        provided events. This is useful for testing how new events will affect the
        customer's invoices before they are actually processed. Customers on contracts
        with SQL billable metrics are not supported.

        Args:
          events: Array of usage events to include in the preview calculation. Must contain at
              least one event in `merge` mode.

          mode: Controls how the provided events are combined with existing usage data. Use
              `replace` to calculate the preview as if these are the only events for the
              customer, ignoring all historical usage. Use `merge` to combine these events
              with the customer's existing usage. Defaults to `replace`.

          skip_zero_qty_line_items: When `true`, line items with zero quantity are excluded from the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/v1/customers/{customer_id}/previewEvents",
            body=maybe_transform(
                {
                    "events": events,
                    "mode": mode,
                    "skip_zero_qty_line_items": skip_zero_qty_line_items,
                },
                customer_preview_events_params.CustomerPreviewEventsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerPreviewEventsResponse,
        )

    def retrieve_billing_configurations(
        self,
        *,
        customer_id: str,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerRetrieveBillingConfigurationsResponse:
        """Returns all billing configurations previously set for the customer.

        Use during
        the contract provisioning process to fetch the
        `billing_provider_configuration_id` needed to set the contract billing
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/getCustomerBillingProviderConfigurations",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "include_archived": include_archived,
                },
                customer_retrieve_billing_configurations_params.CustomerRetrieveBillingConfigurationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrieveBillingConfigurationsResponse,
        )

    def set_billing_configurations(
        self,
        *,
        data: Iterable[customer_set_billing_configurations_params.Data],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerSetBillingConfigurationsResponse:
        """Create a billing configuration for a customer.

        Once created, these
        configurations are available to associate to a contract and dictates which
        downstream system to collect payment in or send the invoice to. You can create
        multiple configurations per customer. The configuration formats are distinct for
        each downstream provider.

        ### Use this endpoint to:

        - Add the initial configuration to an existing customer. Once created, the
          billing configuration can then be associated to the customer's contract.
        - Add a new configuration to an existing customer. This might be used as part of
          an upgrade or downgrade workflow where the customer was previously billed
          through system A (e.g. Stripe) but will now be billed through system B (e.g.
          AWS). Once created, the new configuration can then be associated to the
          customer's contract.
        - Multiple configurations can be added per destination. For example, you can
          create two Stripe billing configurations for a Metronome customer that each
          have a distinct `collection_method`.

        ### Delivery method options:

        - `direct_to_billing_provider`: Use when Metronome should send invoices directly
          to the billing provider's API (e.g., Stripe, NetSuite). This is the most
          common method for automated billing workflows.
        - `tackle`: Use specifically for AWS Marketplace transactions that require
          Tackle's co-selling platform for partner attribution and commission tracking.
        - `aws_sqs`: Use when you want invoice data delivered to an AWS SQS queue for
          custom processing before sending to your billing system.
        - `aws_sns`: Use when you want invoice notifications published to an AWS SNS
          topic for event-driven billing workflows.

        ### Key response fields:

        The id for the customer billing configuration. This id can be used to associate
        the billing configuration to a contract.

        ### Usage guidelines:

        Must use the `delivery_method_id` if you have multiple Stripe accounts connected
        to Metronome.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/setCustomerBillingProviderConfigurations",
            body=maybe_transform(
                {"data": data}, customer_set_billing_configurations_params.CustomerSetBillingConfigurationsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetBillingConfigurationsResponse,
        )

    def set_ingest_aliases(
        self,
        *,
        customer_id: str,
        ingest_aliases: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets the ingest aliases for a customer.

        Use this endpoint to associate a
        Metronome customer with an internal ID for easier tracking between systems.
        Ingest aliases can be used in the `customer_id` field when sending usage events
        to Metronome.

        ### Usage guidelines:

        - This call is idempotent and fully replaces the set of ingest aliases for the
          given customer.
        - Switching an ingest alias from one customer to another will associate all
          corresponding usage to the new customer.
        - Use multiple ingest aliases to model child organizations within a single
          Metronome customer.

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
            f"/v1/customers/{customer_id}/setIngestAliases",
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
        *,
        customer_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerSetNameResponse:
        """Updates the display name for a customer record.

        Use this to correct customer
        names, update business names after rebranding, or maintain accurate customer
        information for invoicing and reporting. Returns the updated customer object
        with the new name applied immediately across all billing documents and
        interfaces.

        Args:
          name: The new name for the customer. This will be truncated to 160 characters if the
              provided name is longer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return self._post(
            f"/v1/customers/{customer_id}/setName",
            body=maybe_transform({"name": name}, customer_set_name_params.CustomerSetNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetNameResponse,
        )

    def update_config(
        self,
        *,
        customer_id: str,
        leave_stripe_invoices_in_draft: Optional[bool] | Omit = omit,
        salesforce_account_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update configuration settings for a specific customer, such as external system
        integrations (e.g., Salesforce account ID) and other customer-specific billing
        parameters. Use this endpoint to modify customer configurations without
        affecting core customer data like name or ingest aliases.

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
            f"/v1/customers/{customer_id}/updateConfig",
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
    def commits(self) -> AsyncCommitsResource:
        return AsyncCommitsResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResource:
        return AsyncNamedSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncCustomersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        billing_config: customer_create_params.BillingConfig | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        customer_billing_provider_configurations: Iterable[customer_create_params.CustomerBillingProviderConfiguration]
        | Omit = omit,
        customer_revenue_system_configurations: Iterable[customer_create_params.CustomerRevenueSystemConfiguration]
        | Omit = omit,
        external_id: str | Omit = omit,
        ingest_aliases: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerCreateResponse:
        """
        Create a new customer in Metronome and optionally the billing configuration
        (recommended) which dictates where invoices for the customer will be sent or
        where payment will be collected.

        ### Use this endpoint to:

        Execute your customer provisioning workflows for either PLG motions, where
        customers originate in your platform, or SLG motions, where customers originate
        in your sales system.

        ### Key response fields:

        This end-point returns the `customer_id` created by the request. This id can be
        used to fetch relevant billing configurations and create contracts.

        ### Example workflow:

        - Generally, Metronome recommends first creating the customer in the downstream
          payment / ERP system when payment method is collected and then creating the
          customer in Metronome using the response (i.e. `customer_id`) from the
          downstream system. If you do not create a billing configuration on customer
          creation, you can add it later.
        - Once a customer is created, you can then create a contract for the customer.
          In the contract creation process, you will need to add the customer billing
          configuration to the contract to ensure Metronome invoices the customer
          correctly. This is because a customer can have multiple configurations.
        - As part of the customer creation process, set the ingest alias for the
          customer which will ensure usage is accurately mapped to the customer. Ingest
          aliases can be added or changed after the creation process as well.

        ### Usage guidelines:

        For details on different billing configurations for different systems, review
        the `/setCustomerBillingConfiguration` end-point.

        Args:
          name: This will be truncated to 160 characters if the provided name is longer.

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          external_id: (deprecated, use ingest_aliases instead) an alias that can be used to refer to
              this customer in usage events

          ingest_aliases: Aliases that can be used to refer to this customer in usage events

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "billing_config": billing_config,
                    "custom_fields": custom_fields,
                    "customer_billing_provider_configurations": customer_billing_provider_configurations,
                    "customer_revenue_system_configurations": customer_revenue_system_configurations,
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
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerRetrieveResponse:
        """Get detailed information for a specific customer by their Metronome ID.

        Returns
        customer profile data including name, creation date, ingest aliases,
        configuration settings, and custom fields. Use this endpoint to fetch complete
        customer details for billing operations or account management.

        Note: If searching for a customer billing configuration, use the
        `/getCustomerBillingConfigurations` endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._get(
            f"/v1/customers/{customer_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrieveResponse,
        )

    def list(
        self,
        *,
        customer_ids: SequenceNotStr[str] | Omit = omit,
        ingest_alias: str | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        only_archived: bool | Omit = omit,
        salesforce_account_ids: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerDetail, AsyncCursorPage[CustomerDetail]]:
        """Gets a paginated list of all customers in your Metronome account.

        Use this
        endpoint to browse your customer base, implement customer search functionality,
        or sync customer data with external systems. Returns customer details including
        IDs, names, and configuration settings. Supports filtering and pagination
        parameters for efficient data retrieval.

        Args:
          customer_ids: Filter the customer list by customer_id. Up to 100 ids can be provided.

          ingest_alias: Filter the customer list by ingest_alias

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          only_archived: Filter the customer list to only return archived customers. By default, only
              active customers are returned.

          salesforce_account_ids: Filter the customer list by salesforce_account_id. Up to 100 ids can be
              provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customers",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerArchiveResponse:
        """Use this endpoint to archive a customer while preserving auditability.

        Archiving
        a customer will automatically archive all contracts as of the current date and
        void all corresponding invoices. Use this endpoint if a customer is onboarded by
        mistake.

        ### Usage guidelines:

        - Once a customer is archived, it cannot be unarchived.
        - Archived customers can still be viewed through the API or the UI for audit
          purposes.
        - Ingest aliases remain idempotent for archived customers. In order to reuse an
          ingest alias, first remove the ingest alias from the customer prior to
          archiving.
        - Any notifications associated with the customer will no longer be triggered.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customers/archive",
            body=await async_maybe_transform({"id": id}, customer_archive_params.CustomerArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerArchiveResponse,
        )

    def list_billable_metrics(
        self,
        *,
        customer_id: str,
        include_archived: bool | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        on_current_plan: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerListBillableMetricsResponse, AsyncCursorPage[CustomerListBillableMetricsResponse]]:
        """Get all billable metrics available for a specific customer.

        Supports pagination
        and filtering by current plan status or archived metrics. Use this endpoint to
        see which metrics are being tracked for billing calculations for a given
        customer.

        Args:
          include_archived: If true, the list of returned metrics will include archived metrics

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
            f"/v1/customers/{customer_id}/billable-metrics",
            page=AsyncCursorPage[CustomerListBillableMetricsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_archived": include_archived,
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
        *,
        customer_id: str,
        ending_before: Union[str, datetime],
        starting_on: Union[str, datetime],
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomerListCostsResponse, AsyncCursorPage[CustomerListCostsResponse]]:
        """
        Fetch daily pending costs for the specified customer, broken down by credit type
        and line items. Note: this is not supported for customers whose plan includes a
        UNIQUE-type billable metric. This is a Plans (deprecated) endpoint. New clients
        should implement using Contracts.

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
            f"/v1/customers/{customer_id}/costs",
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

    async def preview_events(
        self,
        *,
        customer_id: str,
        events: Iterable[customer_preview_events_params.Event],
        mode: Literal["replace", "merge"] | Omit = omit,
        skip_zero_qty_line_items: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerPreviewEventsResponse:
        """Preview how a set of events will affect a customer's invoices.

        Generates draft
        invoices for a customer using their current contract configuration and the
        provided events. This is useful for testing how new events will affect the
        customer's invoices before they are actually processed. Customers on contracts
        with SQL billable metrics are not supported.

        Args:
          events: Array of usage events to include in the preview calculation. Must contain at
              least one event in `merge` mode.

          mode: Controls how the provided events are combined with existing usage data. Use
              `replace` to calculate the preview as if these are the only events for the
              customer, ignoring all historical usage. Use `merge` to combine these events
              with the customer's existing usage. Defaults to `replace`.

          skip_zero_qty_line_items: When `true`, line items with zero quantity are excluded from the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/v1/customers/{customer_id}/previewEvents",
            body=await async_maybe_transform(
                {
                    "events": events,
                    "mode": mode,
                    "skip_zero_qty_line_items": skip_zero_qty_line_items,
                },
                customer_preview_events_params.CustomerPreviewEventsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerPreviewEventsResponse,
        )

    async def retrieve_billing_configurations(
        self,
        *,
        customer_id: str,
        include_archived: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerRetrieveBillingConfigurationsResponse:
        """Returns all billing configurations previously set for the customer.

        Use during
        the contract provisioning process to fetch the
        `billing_provider_configuration_id` needed to set the contract billing
        configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/getCustomerBillingProviderConfigurations",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "include_archived": include_archived,
                },
                customer_retrieve_billing_configurations_params.CustomerRetrieveBillingConfigurationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerRetrieveBillingConfigurationsResponse,
        )

    async def set_billing_configurations(
        self,
        *,
        data: Iterable[customer_set_billing_configurations_params.Data],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerSetBillingConfigurationsResponse:
        """Create a billing configuration for a customer.

        Once created, these
        configurations are available to associate to a contract and dictates which
        downstream system to collect payment in or send the invoice to. You can create
        multiple configurations per customer. The configuration formats are distinct for
        each downstream provider.

        ### Use this endpoint to:

        - Add the initial configuration to an existing customer. Once created, the
          billing configuration can then be associated to the customer's contract.
        - Add a new configuration to an existing customer. This might be used as part of
          an upgrade or downgrade workflow where the customer was previously billed
          through system A (e.g. Stripe) but will now be billed through system B (e.g.
          AWS). Once created, the new configuration can then be associated to the
          customer's contract.
        - Multiple configurations can be added per destination. For example, you can
          create two Stripe billing configurations for a Metronome customer that each
          have a distinct `collection_method`.

        ### Delivery method options:

        - `direct_to_billing_provider`: Use when Metronome should send invoices directly
          to the billing provider's API (e.g., Stripe, NetSuite). This is the most
          common method for automated billing workflows.
        - `tackle`: Use specifically for AWS Marketplace transactions that require
          Tackle's co-selling platform for partner attribution and commission tracking.
        - `aws_sqs`: Use when you want invoice data delivered to an AWS SQS queue for
          custom processing before sending to your billing system.
        - `aws_sns`: Use when you want invoice notifications published to an AWS SNS
          topic for event-driven billing workflows.

        ### Key response fields:

        The id for the customer billing configuration. This id can be used to associate
        the billing configuration to a contract.

        ### Usage guidelines:

        Must use the `delivery_method_id` if you have multiple Stripe accounts connected
        to Metronome.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/setCustomerBillingProviderConfigurations",
            body=await async_maybe_transform(
                {"data": data}, customer_set_billing_configurations_params.CustomerSetBillingConfigurationsParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetBillingConfigurationsResponse,
        )

    async def set_ingest_aliases(
        self,
        *,
        customer_id: str,
        ingest_aliases: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets the ingest aliases for a customer.

        Use this endpoint to associate a
        Metronome customer with an internal ID for easier tracking between systems.
        Ingest aliases can be used in the `customer_id` field when sending usage events
        to Metronome.

        ### Usage guidelines:

        - This call is idempotent and fully replaces the set of ingest aliases for the
          given customer.
        - Switching an ingest alias from one customer to another will associate all
          corresponding usage to the new customer.
        - Use multiple ingest aliases to model child organizations within a single
          Metronome customer.

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
            f"/v1/customers/{customer_id}/setIngestAliases",
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
        *,
        customer_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomerSetNameResponse:
        """Updates the display name for a customer record.

        Use this to correct customer
        names, update business names after rebranding, or maintain accurate customer
        information for invoicing and reporting. Returns the updated customer object
        with the new name applied immediately across all billing documents and
        interfaces.

        Args:
          name: The new name for the customer. This will be truncated to 160 characters if the
              provided name is longer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        return await self._post(
            f"/v1/customers/{customer_id}/setName",
            body=await async_maybe_transform({"name": name}, customer_set_name_params.CustomerSetNameParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomerSetNameResponse,
        )

    async def update_config(
        self,
        *,
        customer_id: str,
        leave_stripe_invoices_in_draft: Optional[bool] | Omit = omit,
        salesforce_account_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Update configuration settings for a specific customer, such as external system
        integrations (e.g., Salesforce account ID) and other customer-specific billing
        parameters. Use this endpoint to modify customer configurations without
        affecting core customer data like name or ingest aliases.

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
            f"/v1/customers/{customer_id}/updateConfig",
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
        self.preview_events = to_raw_response_wrapper(
            customers.preview_events,
        )
        self.retrieve_billing_configurations = to_raw_response_wrapper(
            customers.retrieve_billing_configurations,
        )
        self.set_billing_configurations = to_raw_response_wrapper(
            customers.set_billing_configurations,
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

    @cached_property
    def commits(self) -> CommitsResourceWithRawResponse:
        return CommitsResourceWithRawResponse(self._customers.commits)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._customers.credits)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResourceWithRawResponse:
        return NamedSchedulesResourceWithRawResponse(self._customers.named_schedules)


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
        self.preview_events = async_to_raw_response_wrapper(
            customers.preview_events,
        )
        self.retrieve_billing_configurations = async_to_raw_response_wrapper(
            customers.retrieve_billing_configurations,
        )
        self.set_billing_configurations = async_to_raw_response_wrapper(
            customers.set_billing_configurations,
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

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithRawResponse:
        return AsyncCommitsResourceWithRawResponse(self._customers.commits)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._customers.credits)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResourceWithRawResponse:
        return AsyncNamedSchedulesResourceWithRawResponse(self._customers.named_schedules)


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
        self.preview_events = to_streamed_response_wrapper(
            customers.preview_events,
        )
        self.retrieve_billing_configurations = to_streamed_response_wrapper(
            customers.retrieve_billing_configurations,
        )
        self.set_billing_configurations = to_streamed_response_wrapper(
            customers.set_billing_configurations,
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

    @cached_property
    def commits(self) -> CommitsResourceWithStreamingResponse:
        return CommitsResourceWithStreamingResponse(self._customers.commits)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._customers.credits)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResourceWithStreamingResponse:
        return NamedSchedulesResourceWithStreamingResponse(self._customers.named_schedules)


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
        self.preview_events = async_to_streamed_response_wrapper(
            customers.preview_events,
        )
        self.retrieve_billing_configurations = async_to_streamed_response_wrapper(
            customers.retrieve_billing_configurations,
        )
        self.set_billing_configurations = async_to_streamed_response_wrapper(
            customers.set_billing_configurations,
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

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithStreamingResponse:
        return AsyncCommitsResourceWithStreamingResponse(self._customers.commits)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._customers.credits)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResourceWithStreamingResponse:
        return AsyncNamedSchedulesResourceWithStreamingResponse(self._customers.named_schedules)
