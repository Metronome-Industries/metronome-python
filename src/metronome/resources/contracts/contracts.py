# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    contract_list_params,
    contract_amend_params,
    contract_create_params,
    contract_archive_params,
    contract_retrieve_params,
    contract_list_balances_params,
    contract_update_end_date_params,
    contract_set_usage_filter_params,
    contract_retrieve_rate_schedule_params,
    contract_add_manual_balance_entry_params,
    contract_schedule_pro_services_invoice_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .rate_cards import (
    RateCardsResource,
    AsyncRateCardsResource,
    RateCardsResourceWithRawResponse,
    AsyncRateCardsResourceWithRawResponse,
    RateCardsResourceWithStreamingResponse,
    AsyncRateCardsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .named_schedules import (
    NamedSchedulesResource,
    AsyncNamedSchedulesResource,
    NamedSchedulesResourceWithRawResponse,
    AsyncNamedSchedulesResourceWithRawResponse,
    NamedSchedulesResourceWithStreamingResponse,
    AsyncNamedSchedulesResourceWithStreamingResponse,
)
from .rate_cards.rate_cards import RateCardsResource, AsyncRateCardsResource
from ...types.contract_list_response import ContractListResponse
from ...types.contract_amend_response import ContractAmendResponse
from ...types.contract_create_response import ContractCreateResponse
from ...types.contract_archive_response import ContractArchiveResponse
from ...types.contract_retrieve_response import ContractRetrieveResponse
from ...types.contract_list_balances_response import ContractListBalancesResponse
from ...types.shared_params.base_usage_filter import BaseUsageFilter
from ...types.contract_update_end_date_response import ContractUpdateEndDateResponse
from ...types.contract_retrieve_rate_schedule_response import ContractRetrieveRateScheduleResponse
from ...types.contract_schedule_pro_services_invoice_response import ContractScheduleProServicesInvoiceResponse

__all__ = ["ContractsResource", "AsyncContractsResource"]


class ContractsResource(SyncAPIResource):
    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

    @cached_property
    def rate_cards(self) -> RateCardsResource:
        return RateCardsResource(self._client)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResource:
        return NamedSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ContractsResourceWithRawResponse:
        return ContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractsResourceWithStreamingResponse:
        return ContractsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_id: str,
        starting_at: Union[str, datetime],
        billing_provider_configuration: contract_create_params.BillingProviderConfiguration | NotGiven = NOT_GIVEN,
        commits: Iterable[contract_create_params.Commit] | NotGiven = NOT_GIVEN,
        credits: Iterable[contract_create_params.Credit] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        discounts: Iterable[contract_create_params.Discount] | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        net_payment_terms_days: float | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        overrides: Iterable[contract_create_params.Override] | NotGiven = NOT_GIVEN,
        professional_services: Iterable[contract_create_params.ProfessionalService] | NotGiven = NOT_GIVEN,
        rate_card_alias: str | NotGiven = NOT_GIVEN,
        rate_card_id: str | NotGiven = NOT_GIVEN,
        reseller_royalties: Iterable[contract_create_params.ResellerRoyalty] | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        scheduled_charges: Iterable[contract_create_params.ScheduledCharge] | NotGiven = NOT_GIVEN,
        total_contract_value: float | NotGiven = NOT_GIVEN,
        transition: contract_create_params.Transition | NotGiven = NOT_GIVEN,
        uniqueness_key: str | NotGiven = NOT_GIVEN,
        usage_filter: BaseUsageFilter | NotGiven = NOT_GIVEN,
        usage_statement_schedule: contract_create_params.UsageStatementSchedule | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractCreateResponse:
        """
        Create a new contract

        Args:
          starting_at: inclusive contract start time

          billing_provider_configuration: This field's availability is dependent on your client's configuration.

          discounts: This field's availability is dependent on your client's configuration.

          ending_before: exclusive contract end time

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          professional_services: This field's availability is dependent on your client's configuration.

          rate_card_alias: Selects the rate card linked to the specified alias as of the contract's start
              date.

          reseller_royalties: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          total_contract_value: This field's availability is dependent on your client's configuration.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/create",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "starting_at": starting_at,
                    "billing_provider_configuration": billing_provider_configuration,
                    "commits": commits,
                    "credits": credits,
                    "custom_fields": custom_fields,
                    "discounts": discounts,
                    "ending_before": ending_before,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "name": name,
                    "net_payment_terms_days": net_payment_terms_days,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "overrides": overrides,
                    "professional_services": professional_services,
                    "rate_card_alias": rate_card_alias,
                    "rate_card_id": rate_card_id,
                    "reseller_royalties": reseller_royalties,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "scheduled_charges": scheduled_charges,
                    "total_contract_value": total_contract_value,
                    "transition": transition,
                    "uniqueness_key": uniqueness_key,
                    "usage_filter": usage_filter,
                    "usage_statement_schedule": usage_statement_schedule,
                },
                contract_create_params.ContractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateResponse,
        )

    def retrieve(
        self,
        *,
        contract_id: str,
        customer_id: str,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveResponse:
        """
        Get a specific contract

        Args:
          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/get",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
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
          covering_date: Optional RFC 3339 timestamp. If provided, the response will include only
              contracts effective on the provided date. This cannot be provided if the
              starting_at filter is provided.

          include_archived: Include archived contracts in the response

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          starting_at: Optional RFC 3339 timestamp. If provided, the response will include only
              contracts where effective_at is on or after the provided date. This cannot be
              provided if the covering_date filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/list",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "include_archived": include_archived,
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

    def add_manual_balance_entry(
        self,
        *,
        id: str,
        amount: float,
        customer_id: str,
        reason: str,
        segment_id: str,
        contract_id: str | NotGiven = NOT_GIVEN,
        timestamp: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Add a manual balance entry

        Args:
          id: ID of the balance (commit or credit) to update.

          amount: Amount to add to the segment. A negative number will draw down from the balance.

          customer_id: ID of the customer whose balance is to be updated.

          reason: Reason for the manual adjustment. This will be displayed in the ledger.

          segment_id: ID of the segment to update.

          contract_id: ID of the contract to update. Leave blank to update a customer level balance.

          timestamp: RFC 3339 timestamp indicating when the manual adjustment takes place. If not
              provided, it will default to the start of the segment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/contracts/addManualBalanceLedgerEntry",
            body=maybe_transform(
                {
                    "id": id,
                    "amount": amount,
                    "customer_id": customer_id,
                    "reason": reason,
                    "segment_id": segment_id,
                    "contract_id": contract_id,
                    "timestamp": timestamp,
                },
                contract_add_manual_balance_entry_params.ContractAddManualBalanceEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def amend(
        self,
        *,
        contract_id: str,
        customer_id: str,
        starting_at: Union[str, datetime],
        commits: Iterable[contract_amend_params.Commit] | NotGiven = NOT_GIVEN,
        credits: Iterable[contract_amend_params.Credit] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        discounts: Iterable[contract_amend_params.Discount] | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        overrides: Iterable[contract_amend_params.Override] | NotGiven = NOT_GIVEN,
        professional_services: Iterable[contract_amend_params.ProfessionalService] | NotGiven = NOT_GIVEN,
        reseller_royalties: Iterable[contract_amend_params.ResellerRoyalty] | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        scheduled_charges: Iterable[contract_amend_params.ScheduledCharge] | NotGiven = NOT_GIVEN,
        total_contract_value: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractAmendResponse:
        """
        Amend a contract

        Args:
          contract_id: ID of the contract to amend

          customer_id: ID of the customer whose contract is to be amended

          starting_at: inclusive start time for the amendment

          discounts: This field's availability is dependent on your client's configuration.

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          professional_services: This field's availability is dependent on your client's configuration.

          reseller_royalties: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          total_contract_value: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/amend",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "starting_at": starting_at,
                    "commits": commits,
                    "credits": credits,
                    "custom_fields": custom_fields,
                    "discounts": discounts,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "overrides": overrides,
                    "professional_services": professional_services,
                    "reseller_royalties": reseller_royalties,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "scheduled_charges": scheduled_charges,
                    "total_contract_value": total_contract_value,
                },
                contract_amend_params.ContractAmendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractAmendResponse,
        )

    def archive(
        self,
        *,
        contract_id: str,
        customer_id: str,
        void_invoices: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractArchiveResponse:
        """
        Archive a contract

        Args:
          contract_id: ID of the contract to archive

          customer_id: ID of the customer whose contract is to be archived

          void_invoices: If false, the existing finalized invoices will remain after the contract is
              archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/archive",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "void_invoices": void_invoices,
                },
                contract_archive_params.ContractArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractArchiveResponse,
        )

    def list_balances(
        self,
        *,
        customer_id: str,
        id: str | NotGiven = NOT_GIVEN,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_contract_balances: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractListBalancesResponse:
        """
        List balances (commits and credits).

        Args:
          covering_date: Return only balances that have access schedules that "cover" the provided date

          effective_before: Include only balances that have any access before the provided date (exclusive)

          include_archived: Include credits from archived contracts.

          include_contract_balances: Include balances on the contract level.

          include_ledgers: Include ledgers in the response. Setting this flag may cause the query to be
              slower.

          next_page: The next page token from a previous response.

          starting_at: Include only balances that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/customerBalances/list",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "id": id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_contract_balances": include_contract_balances,
                    "include_ledgers": include_ledgers,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                contract_list_balances_params.ContractListBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractListBalancesResponse,
        )

    def retrieve_rate_schedule(
        self,
        *,
        contract_id: str,
        customer_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        selectors: Iterable[contract_retrieve_rate_schedule_params.Selector] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveRateScheduleResponse:
        """
        Get the rate schedule for the rate card on a given contract.

        Args:
          contract_id: ID of the contract to get the rate schedule for.

          customer_id: ID of the customer for whose contract to get the rate schedule for.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          at: optional timestamp which overlaps with the returned rate schedule segments. When
              not specified, the current timestamp will be used.

          selectors: List of rate selectors, rates matching ANY of the selectors will be included in
              the response. Passing no selectors will result in all rates being returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/getContractRateSchedule",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "at": at,
                    "selectors": selectors,
                },
                contract_retrieve_rate_schedule_params.ContractRetrieveRateScheduleParams,
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
                    contract_retrieve_rate_schedule_params.ContractRetrieveRateScheduleParams,
                ),
            ),
            cast_to=ContractRetrieveRateScheduleResponse,
        )

    def schedule_pro_services_invoice(
        self,
        *,
        contract_id: str,
        customer_id: str,
        issued_at: Union[str, datetime],
        line_items: Iterable[contract_schedule_pro_services_invoice_params.LineItem],
        netsuite_invoice_header_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        netsuite_invoice_header_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractScheduleProServicesInvoiceResponse:
        """
        Create a new, scheduled invoice for Professional Services terms on a contract.
        This endpoint's availability is dependent on your client's configuration.

        Args:
          issued_at: The date the invoice is issued

          line_items: Each line requires an amount or both unit_price and quantity.

          netsuite_invoice_header_end: The end date of the invoice header in Netsuite

          netsuite_invoice_header_start: The start date of the invoice header in Netsuite

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/scheduleProServicesInvoice",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "issued_at": issued_at,
                    "line_items": line_items,
                    "netsuite_invoice_header_end": netsuite_invoice_header_end,
                    "netsuite_invoice_header_start": netsuite_invoice_header_start,
                },
                contract_schedule_pro_services_invoice_params.ContractScheduleProServicesInvoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractScheduleProServicesInvoiceResponse,
        )

    def set_usage_filter(
        self,
        *,
        contract_id: str,
        customer_id: str,
        group_key: str,
        group_values: List[str],
        starting_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Set usage filter for a contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/contracts/setUsageFilter",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "group_key": group_key,
                    "group_values": group_values,
                    "starting_at": starting_at,
                },
                contract_set_usage_filter_params.ContractSetUsageFilterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_end_date(
        self,
        *,
        contract_id: str,
        customer_id: str,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractUpdateEndDateResponse:
        """
        Update the end date of a contract

        Args:
          contract_id: ID of the contract to update

          customer_id: ID of the customer whose contract is to be updated

          ending_before: RFC 3339 timestamp indicating when the contract will end (exclusive). If not
              provided, the contract will be updated to be open-ended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/contracts/updateEndDate",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "ending_before": ending_before,
                },
                contract_update_end_date_params.ContractUpdateEndDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractUpdateEndDateResponse,
        )


class AsyncContractsResource(AsyncAPIResource):
    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

    @cached_property
    def rate_cards(self) -> AsyncRateCardsResource:
        return AsyncRateCardsResource(self._client)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResource:
        return AsyncNamedSchedulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncContractsResourceWithRawResponse:
        return AsyncContractsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractsResourceWithStreamingResponse:
        return AsyncContractsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_id: str,
        starting_at: Union[str, datetime],
        billing_provider_configuration: contract_create_params.BillingProviderConfiguration | NotGiven = NOT_GIVEN,
        commits: Iterable[contract_create_params.Commit] | NotGiven = NOT_GIVEN,
        credits: Iterable[contract_create_params.Credit] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        discounts: Iterable[contract_create_params.Discount] | NotGiven = NOT_GIVEN,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        net_payment_terms_days: float | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        overrides: Iterable[contract_create_params.Override] | NotGiven = NOT_GIVEN,
        professional_services: Iterable[contract_create_params.ProfessionalService] | NotGiven = NOT_GIVEN,
        rate_card_alias: str | NotGiven = NOT_GIVEN,
        rate_card_id: str | NotGiven = NOT_GIVEN,
        reseller_royalties: Iterable[contract_create_params.ResellerRoyalty] | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        scheduled_charges: Iterable[contract_create_params.ScheduledCharge] | NotGiven = NOT_GIVEN,
        total_contract_value: float | NotGiven = NOT_GIVEN,
        transition: contract_create_params.Transition | NotGiven = NOT_GIVEN,
        uniqueness_key: str | NotGiven = NOT_GIVEN,
        usage_filter: BaseUsageFilter | NotGiven = NOT_GIVEN,
        usage_statement_schedule: contract_create_params.UsageStatementSchedule | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractCreateResponse:
        """
        Create a new contract

        Args:
          starting_at: inclusive contract start time

          billing_provider_configuration: This field's availability is dependent on your client's configuration.

          discounts: This field's availability is dependent on your client's configuration.

          ending_before: exclusive contract end time

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          professional_services: This field's availability is dependent on your client's configuration.

          rate_card_alias: Selects the rate card linked to the specified alias as of the contract's start
              date.

          reseller_royalties: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          total_contract_value: This field's availability is dependent on your client's configuration.

          uniqueness_key: Prevents the creation of duplicates. If a request to create a record is made
              with a previously used uniqueness key, a new record will not be created and the
              request will fail with a 409 error.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/create",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "starting_at": starting_at,
                    "billing_provider_configuration": billing_provider_configuration,
                    "commits": commits,
                    "credits": credits,
                    "custom_fields": custom_fields,
                    "discounts": discounts,
                    "ending_before": ending_before,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "name": name,
                    "net_payment_terms_days": net_payment_terms_days,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "overrides": overrides,
                    "professional_services": professional_services,
                    "rate_card_alias": rate_card_alias,
                    "rate_card_id": rate_card_id,
                    "reseller_royalties": reseller_royalties,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "scheduled_charges": scheduled_charges,
                    "total_contract_value": total_contract_value,
                    "transition": transition,
                    "uniqueness_key": uniqueness_key,
                    "usage_filter": usage_filter,
                    "usage_statement_schedule": usage_statement_schedule,
                },
                contract_create_params.ContractCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateResponse,
        )

    async def retrieve(
        self,
        *,
        contract_id: str,
        customer_id: str,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveResponse:
        """
        Get a specific contract

        Args:
          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/get",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
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
          covering_date: Optional RFC 3339 timestamp. If provided, the response will include only
              contracts effective on the provided date. This cannot be provided if the
              starting_at filter is provided.

          include_archived: Include archived contracts in the response

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          starting_at: Optional RFC 3339 timestamp. If provided, the response will include only
              contracts where effective_at is on or after the provided date. This cannot be
              provided if the covering_date filter is provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/list",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "covering_date": covering_date,
                    "include_archived": include_archived,
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

    async def add_manual_balance_entry(
        self,
        *,
        id: str,
        amount: float,
        customer_id: str,
        reason: str,
        segment_id: str,
        contract_id: str | NotGiven = NOT_GIVEN,
        timestamp: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Add a manual balance entry

        Args:
          id: ID of the balance (commit or credit) to update.

          amount: Amount to add to the segment. A negative number will draw down from the balance.

          customer_id: ID of the customer whose balance is to be updated.

          reason: Reason for the manual adjustment. This will be displayed in the ledger.

          segment_id: ID of the segment to update.

          contract_id: ID of the contract to update. Leave blank to update a customer level balance.

          timestamp: RFC 3339 timestamp indicating when the manual adjustment takes place. If not
              provided, it will default to the start of the segment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/contracts/addManualBalanceLedgerEntry",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "amount": amount,
                    "customer_id": customer_id,
                    "reason": reason,
                    "segment_id": segment_id,
                    "contract_id": contract_id,
                    "timestamp": timestamp,
                },
                contract_add_manual_balance_entry_params.ContractAddManualBalanceEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def amend(
        self,
        *,
        contract_id: str,
        customer_id: str,
        starting_at: Union[str, datetime],
        commits: Iterable[contract_amend_params.Commit] | NotGiven = NOT_GIVEN,
        credits: Iterable[contract_amend_params.Credit] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        discounts: Iterable[contract_amend_params.Discount] | NotGiven = NOT_GIVEN,
        netsuite_sales_order_id: str | NotGiven = NOT_GIVEN,
        overrides: Iterable[contract_amend_params.Override] | NotGiven = NOT_GIVEN,
        professional_services: Iterable[contract_amend_params.ProfessionalService] | NotGiven = NOT_GIVEN,
        reseller_royalties: Iterable[contract_amend_params.ResellerRoyalty] | NotGiven = NOT_GIVEN,
        salesforce_opportunity_id: str | NotGiven = NOT_GIVEN,
        scheduled_charges: Iterable[contract_amend_params.ScheduledCharge] | NotGiven = NOT_GIVEN,
        total_contract_value: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractAmendResponse:
        """
        Amend a contract

        Args:
          contract_id: ID of the contract to amend

          customer_id: ID of the customer whose contract is to be amended

          starting_at: inclusive start time for the amendment

          discounts: This field's availability is dependent on your client's configuration.

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          professional_services: This field's availability is dependent on your client's configuration.

          reseller_royalties: This field's availability is dependent on your client's configuration.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          total_contract_value: This field's availability is dependent on your client's configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/amend",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "starting_at": starting_at,
                    "commits": commits,
                    "credits": credits,
                    "custom_fields": custom_fields,
                    "discounts": discounts,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "overrides": overrides,
                    "professional_services": professional_services,
                    "reseller_royalties": reseller_royalties,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "scheduled_charges": scheduled_charges,
                    "total_contract_value": total_contract_value,
                },
                contract_amend_params.ContractAmendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractAmendResponse,
        )

    async def archive(
        self,
        *,
        contract_id: str,
        customer_id: str,
        void_invoices: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractArchiveResponse:
        """
        Archive a contract

        Args:
          contract_id: ID of the contract to archive

          customer_id: ID of the customer whose contract is to be archived

          void_invoices: If false, the existing finalized invoices will remain after the contract is
              archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/archive",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "void_invoices": void_invoices,
                },
                contract_archive_params.ContractArchiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractArchiveResponse,
        )

    async def list_balances(
        self,
        *,
        customer_id: str,
        id: str | NotGiven = NOT_GIVEN,
        covering_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        effective_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        include_archived: bool | NotGiven = NOT_GIVEN,
        include_contract_balances: bool | NotGiven = NOT_GIVEN,
        include_ledgers: bool | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        starting_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractListBalancesResponse:
        """
        List balances (commits and credits).

        Args:
          covering_date: Return only balances that have access schedules that "cover" the provided date

          effective_before: Include only balances that have any access before the provided date (exclusive)

          include_archived: Include credits from archived contracts.

          include_contract_balances: Include balances on the contract level.

          include_ledgers: Include ledgers in the response. Setting this flag may cause the query to be
              slower.

          next_page: The next page token from a previous response.

          starting_at: Include only balances that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/customerBalances/list",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "id": id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "include_archived": include_archived,
                    "include_contract_balances": include_contract_balances,
                    "include_ledgers": include_ledgers,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                contract_list_balances_params.ContractListBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractListBalancesResponse,
        )

    async def retrieve_rate_schedule(
        self,
        *,
        contract_id: str,
        customer_id: str,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        selectors: Iterable[contract_retrieve_rate_schedule_params.Selector] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractRetrieveRateScheduleResponse:
        """
        Get the rate schedule for the rate card on a given contract.

        Args:
          contract_id: ID of the contract to get the rate schedule for.

          customer_id: ID of the customer for whose contract to get the rate schedule for.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          at: optional timestamp which overlaps with the returned rate schedule segments. When
              not specified, the current timestamp will be used.

          selectors: List of rate selectors, rates matching ANY of the selectors will be included in
              the response. Passing no selectors will result in all rates being returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/getContractRateSchedule",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "at": at,
                    "selectors": selectors,
                },
                contract_retrieve_rate_schedule_params.ContractRetrieveRateScheduleParams,
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
                    contract_retrieve_rate_schedule_params.ContractRetrieveRateScheduleParams,
                ),
            ),
            cast_to=ContractRetrieveRateScheduleResponse,
        )

    async def schedule_pro_services_invoice(
        self,
        *,
        contract_id: str,
        customer_id: str,
        issued_at: Union[str, datetime],
        line_items: Iterable[contract_schedule_pro_services_invoice_params.LineItem],
        netsuite_invoice_header_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        netsuite_invoice_header_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractScheduleProServicesInvoiceResponse:
        """
        Create a new, scheduled invoice for Professional Services terms on a contract.
        This endpoint's availability is dependent on your client's configuration.

        Args:
          issued_at: The date the invoice is issued

          line_items: Each line requires an amount or both unit_price and quantity.

          netsuite_invoice_header_end: The end date of the invoice header in Netsuite

          netsuite_invoice_header_start: The start date of the invoice header in Netsuite

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/scheduleProServicesInvoice",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "issued_at": issued_at,
                    "line_items": line_items,
                    "netsuite_invoice_header_end": netsuite_invoice_header_end,
                    "netsuite_invoice_header_start": netsuite_invoice_header_start,
                },
                contract_schedule_pro_services_invoice_params.ContractScheduleProServicesInvoiceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractScheduleProServicesInvoiceResponse,
        )

    async def set_usage_filter(
        self,
        *,
        contract_id: str,
        customer_id: str,
        group_key: str,
        group_values: List[str],
        starting_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Set usage filter for a contract

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/contracts/setUsageFilter",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "group_key": group_key,
                    "group_values": group_values,
                    "starting_at": starting_at,
                },
                contract_set_usage_filter_params.ContractSetUsageFilterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_end_date(
        self,
        *,
        contract_id: str,
        customer_id: str,
        ending_before: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ContractUpdateEndDateResponse:
        """
        Update the end date of a contract

        Args:
          contract_id: ID of the contract to update

          customer_id: ID of the customer whose contract is to be updated

          ending_before: RFC 3339 timestamp indicating when the contract will end (exclusive). If not
              provided, the contract will be updated to be open-ended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/contracts/updateEndDate",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "ending_before": ending_before,
                },
                contract_update_end_date_params.ContractUpdateEndDateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractUpdateEndDateResponse,
        )


class ContractsResourceWithRawResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.create = to_raw_response_wrapper(
            contracts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            contracts.list,
        )
        self.add_manual_balance_entry = to_raw_response_wrapper(
            contracts.add_manual_balance_entry,
        )
        self.amend = to_raw_response_wrapper(
            contracts.amend,
        )
        self.archive = to_raw_response_wrapper(
            contracts.archive,
        )
        self.list_balances = to_raw_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = to_raw_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.schedule_pro_services_invoice = to_raw_response_wrapper(
            contracts.schedule_pro_services_invoice,
        )
        self.set_usage_filter = to_raw_response_wrapper(
            contracts.set_usage_filter,
        )
        self.update_end_date = to_raw_response_wrapper(
            contracts.update_end_date,
        )

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._contracts.products)

    @cached_property
    def rate_cards(self) -> RateCardsResourceWithRawResponse:
        return RateCardsResourceWithRawResponse(self._contracts.rate_cards)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResourceWithRawResponse:
        return NamedSchedulesResourceWithRawResponse(self._contracts.named_schedules)


class AsyncContractsResourceWithRawResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.create = async_to_raw_response_wrapper(
            contracts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            contracts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            contracts.list,
        )
        self.add_manual_balance_entry = async_to_raw_response_wrapper(
            contracts.add_manual_balance_entry,
        )
        self.amend = async_to_raw_response_wrapper(
            contracts.amend,
        )
        self.archive = async_to_raw_response_wrapper(
            contracts.archive,
        )
        self.list_balances = async_to_raw_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = async_to_raw_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.schedule_pro_services_invoice = async_to_raw_response_wrapper(
            contracts.schedule_pro_services_invoice,
        )
        self.set_usage_filter = async_to_raw_response_wrapper(
            contracts.set_usage_filter,
        )
        self.update_end_date = async_to_raw_response_wrapper(
            contracts.update_end_date,
        )

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._contracts.products)

    @cached_property
    def rate_cards(self) -> AsyncRateCardsResourceWithRawResponse:
        return AsyncRateCardsResourceWithRawResponse(self._contracts.rate_cards)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResourceWithRawResponse:
        return AsyncNamedSchedulesResourceWithRawResponse(self._contracts.named_schedules)


class ContractsResourceWithStreamingResponse:
    def __init__(self, contracts: ContractsResource) -> None:
        self._contracts = contracts

        self.create = to_streamed_response_wrapper(
            contracts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            contracts.list,
        )
        self.add_manual_balance_entry = to_streamed_response_wrapper(
            contracts.add_manual_balance_entry,
        )
        self.amend = to_streamed_response_wrapper(
            contracts.amend,
        )
        self.archive = to_streamed_response_wrapper(
            contracts.archive,
        )
        self.list_balances = to_streamed_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = to_streamed_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.schedule_pro_services_invoice = to_streamed_response_wrapper(
            contracts.schedule_pro_services_invoice,
        )
        self.set_usage_filter = to_streamed_response_wrapper(
            contracts.set_usage_filter,
        )
        self.update_end_date = to_streamed_response_wrapper(
            contracts.update_end_date,
        )

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._contracts.products)

    @cached_property
    def rate_cards(self) -> RateCardsResourceWithStreamingResponse:
        return RateCardsResourceWithStreamingResponse(self._contracts.rate_cards)

    @cached_property
    def named_schedules(self) -> NamedSchedulesResourceWithStreamingResponse:
        return NamedSchedulesResourceWithStreamingResponse(self._contracts.named_schedules)


class AsyncContractsResourceWithStreamingResponse:
    def __init__(self, contracts: AsyncContractsResource) -> None:
        self._contracts = contracts

        self.create = async_to_streamed_response_wrapper(
            contracts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            contracts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            contracts.list,
        )
        self.add_manual_balance_entry = async_to_streamed_response_wrapper(
            contracts.add_manual_balance_entry,
        )
        self.amend = async_to_streamed_response_wrapper(
            contracts.amend,
        )
        self.archive = async_to_streamed_response_wrapper(
            contracts.archive,
        )
        self.list_balances = async_to_streamed_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = async_to_streamed_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.schedule_pro_services_invoice = async_to_streamed_response_wrapper(
            contracts.schedule_pro_services_invoice,
        )
        self.set_usage_filter = async_to_streamed_response_wrapper(
            contracts.set_usage_filter,
        )
        self.update_end_date = async_to_streamed_response_wrapper(
            contracts.update_end_date,
        )

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._contracts.products)

    @cached_property
    def rate_cards(self) -> AsyncRateCardsResourceWithStreamingResponse:
        return AsyncRateCardsResourceWithStreamingResponse(self._contracts.rate_cards)

    @cached_property
    def named_schedules(self) -> AsyncNamedSchedulesResourceWithStreamingResponse:
        return AsyncNamedSchedulesResourceWithStreamingResponse(self._contracts.named_schedules)
