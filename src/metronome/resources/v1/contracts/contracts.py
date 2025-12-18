# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Union, Iterable, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import (
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
    contract_create_historical_invoices_params,
    contract_schedule_pro_services_invoice_params,
    contract_retrieve_subscription_quantity_history_params,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncBodyCursorPage, AsyncBodyCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from .named_schedules import (
    NamedSchedulesResource,
    AsyncNamedSchedulesResource,
    NamedSchedulesResourceWithRawResponse,
    AsyncNamedSchedulesResourceWithRawResponse,
    NamedSchedulesResourceWithStreamingResponse,
    AsyncNamedSchedulesResourceWithStreamingResponse,
)
from .rate_cards.rate_cards import (
    RateCardsResource,
    AsyncRateCardsResource,
    RateCardsResourceWithRawResponse,
    AsyncRateCardsResourceWithRawResponse,
    RateCardsResourceWithStreamingResponse,
    AsyncRateCardsResourceWithStreamingResponse,
)
from ....types.v1.contract_list_response import ContractListResponse
from ....types.v1.contract_amend_response import ContractAmendResponse
from ....types.v1.contract_create_response import ContractCreateResponse
from ....types.v1.contract_archive_response import ContractArchiveResponse
from ....types.v1.contract_retrieve_response import ContractRetrieveResponse
from ....types.shared_params.base_usage_filter import BaseUsageFilter
from ....types.v1.contract_list_balances_response import ContractListBalancesResponse
from ....types.v1.contract_update_end_date_response import ContractUpdateEndDateResponse
from ....types.shared_params.spend_threshold_configuration import SpendThresholdConfiguration
from ....types.v1.contract_retrieve_rate_schedule_response import ContractRetrieveRateScheduleResponse
from ....types.v1.contract_create_historical_invoices_response import ContractCreateHistoricalInvoicesResponse
from ....types.v1.contract_schedule_pro_services_invoice_response import ContractScheduleProServicesInvoiceResponse
from ....types.shared_params.prepaid_balance_threshold_configuration import PrepaidBalanceThresholdConfiguration
from ....types.v1.contract_retrieve_subscription_quantity_history_response import (
    ContractRetrieveSubscriptionQuantityHistoryResponse,
)

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

    def create(
        self,
        *,
        customer_id: str,
        starting_at: Union[str, datetime],
        billing_provider_configuration: contract_create_params.BillingProviderConfiguration | Omit = omit,
        commits: Iterable[contract_create_params.Commit] | Omit = omit,
        credits: Iterable[contract_create_params.Credit] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        discounts: Iterable[contract_create_params.Discount] | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        hierarchy_configuration: contract_create_params.HierarchyConfiguration | Omit = omit,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | Omit = omit,
        name: str | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        netsuite_sales_order_id: str | Omit = omit,
        overrides: Iterable[contract_create_params.Override] | Omit = omit,
        prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfiguration | Omit = omit,
        priority: float | Omit = omit,
        professional_services: Iterable[contract_create_params.ProfessionalService] | Omit = omit,
        rate_card_alias: str | Omit = omit,
        rate_card_id: str | Omit = omit,
        recurring_commits: Iterable[contract_create_params.RecurringCommit] | Omit = omit,
        recurring_credits: Iterable[contract_create_params.RecurringCredit] | Omit = omit,
        reseller_royalties: Iterable[contract_create_params.ResellerRoyalty] | Omit = omit,
        revenue_system_configuration: contract_create_params.RevenueSystemConfiguration | Omit = omit,
        salesforce_opportunity_id: str | Omit = omit,
        scheduled_charges: Iterable[contract_create_params.ScheduledCharge] | Omit = omit,
        scheduled_charges_on_usage_invoices: Literal["ALL"] | Omit = omit,
        spend_threshold_configuration: SpendThresholdConfiguration | Omit = omit,
        subscriptions: Iterable[contract_create_params.Subscription] | Omit = omit,
        total_contract_value: float | Omit = omit,
        transition: contract_create_params.Transition | Omit = omit,
        uniqueness_key: str | Omit = omit,
        usage_filter: BaseUsageFilter | Omit = omit,
        usage_statement_schedule: contract_create_params.UsageStatementSchedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateResponse:
        """
        Contracts define a customer's products, pricing, discounts, access duration, and
        billing configuration. Contracts serve as the central billing agreement for both
        PLG and Enterprise customers, you can automatically customers access to your
        products and services directly from your product or CRM.

        ### Use this endpoint to:

        - PLG onboarding: Automatically provision new self-serve customers with
          contracts when they sign up.
        - Enterprise sales: Push negotiated contracts from Salesforce with custom
          pricing and commitments
        - Promotional pricing: Implement time-limited discounts and free trials through
          overrides

        ### Key components:

        #### Contract Term and Billing Schedule

        - Set contract duration using `starting_at` and `ending_before` fields. PLG
          contracts typically use perpetual agreements (no end date), while Enterprise
          contracts have fixed end dates which can be edited over time in the case of
          co-term upsells.

        #### Rate Card

        If you are offering usage based pricing, you can set a rate card for the
        contract to reference through `rate_card_id` or `rate_card_alias`. The rate card
        is a store of all of your usage based products and their centralized pricing.
        Any new products or price changes on the rate card can be set to automatically
        propagate to all associated contracts - this ensures consistent pricing and
        product launches flow to contracts without manual updates and migrations. The
        `usage_statement_schedule` determines the cadence on which Metronome will
        finalize a usage invoice for the customer. This defaults to monthly on the 1st,
        with options for custom dates, quarterly, or annual cadences. Note: Most usage
        based billing companies align usage statements to be evaluated aligned to the
        first of the month. Read more about
        [Rate Cards](https://docs.metronome.com/pricing-packaging/create-manage-rate-cards/).

        #### Overrides and discounts

        Customize pricing on the contract through time-bounded overrides that can target
        specific products, product families, or complex usage scenarios. Overrides
        enable two key capabilities:

        - Discounts: Apply percentage discounts, fixed rate reductions, or
          quantity-based pricing tiers
        - Entitlements: Provide special pricing or access to specific products for
          negotiated deals

        Read more about
        [Contract Overrides](https://docs.metronome.com/manage-product-access/add-contract-override/).

        #### Commits and Credits

        Using commits, configure prepaid or postpaid spending commitments where
        customers promise to spend a certain amount over the contract period paid in
        advance or in arrears. Use credits to provide free spending allowances. Under
        the hood these are the same mechanisms, however, credits are typically offered
        for free (SLA or promotional) or as a part of an allotment associated with a
        Subscription.

        In Metronome, you can set commits and credits to only be applicable for a subset
        of usage. Use `applicable_product_ids` or `applicable_product_tags` to create
        product or product-family specific commits or credits, or you can build complex
        boolean logic specifiers to target usage based on pricing and presentation group
        values using `override_specifiers`.

        These objects can also also be configured to have a recurrence schedule to
        easily model customer packaging which includes recurring monthly or quarterly
        allotments.

        Commits support rollover settings (`rollover_fraction`) to transfer unused
        balances between contract periods, either entirely or as a percentage.

        Read more about
        [Credits and Commits](https://docs.metronome.com/pricing-packaging/apply-credits-commits/).

        #### Subscriptions

        You can add a fixed recurring charge to a contract, like monthly licenses or
        seat-based fees, using the subscription charge. Subscription charges are defined
        on your rate card and you can select which subscription is applicable to add to
        each contract. When you add a subscription to a contract you need to:

        - Define whether the subscription is paid for in-advance or in-arrears
          (`collection_schedule`)
        - Define the proration behavior (`proration`)
        - Specify an initial quantity (`initial_quantity`)
        - Define which subscription rate on the rate card should be used
          (`subscription_rate`)

        Read more about
        [Subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/).

        #### Scheduled Charges

        Set up one-time, recurring, or entirely custom charges that occur on specific
        dates, separate from usage-based billing or commitments. These can be used to
        model non-recurring platform charges or professional services.

        #### Threshold Billing

        Metronome allows you to configure automatic billing triggers when customers
        reach spending thresholds to prevent fraud and manage risk. You can use
        `spend_threshold_configuration` to trigger an invoice to cover current charges
        whenever the threshold is reached or you can ensure the customer maintains a
        minimum prepaid balance using the `prepaid_balance_configuration`.

        Read more about
        [Spend Threshold](https://docs.metronome.com/manage-product-access/spend-thresholds/)
        and
        [Prepaid Balance Thresholds](https://docs.metronome.com/manage-product-access/prepaid-balance-thresholds/).

        ### Usage guidelines:

        - You can always
          [Edit Contracts](https://docs.metronome.com/manage-product-access/edit-contract/)
          after it has been created, using the `editContract` endpoint. Metronome keeps
          track of all edits, both in the audit log and over the `getEditHistory`
          endpoint.
        - Customers in Metronome can have multiple concurrent contracts at one time. Use
          `usage_filters` to route the correct usage to each contract.
          [Read more about usage filters](https://docs.metronome.com/manage-product-access/provision-customer/#create-a-usage-filter).

        Args:
          starting_at: inclusive contract start time

          billing_provider_configuration: The billing provider configuration associated with a contract. Provide either an
              ID or the provider and delivery method.

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          discounts: This field's availability is dependent on your client's configuration.

          ending_before: exclusive contract end time

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          priority: Priority of the contract.

          professional_services: This field's availability is dependent on your client's configuration.

          rate_card_alias: Selects the rate card linked to the specified alias as of the contract's start
              date.

          reseller_royalties: This field's availability is dependent on your client's configuration.

          revenue_system_configuration: The revenue system configuration associated with a contract. Provide either an
              ID or the provider and delivery method.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          scheduled_charges_on_usage_invoices: Determines which scheduled and commit charges to consolidate onto the Contract's
              usage invoice. The charge's `timestamp` must match the usage invoice's
              `ending_before` date for consolidation to occur. This field cannot be modified
              after a Contract has been created. If this field is omitted, charges will appear
              on a separate invoice from usage charges.

          subscriptions: Optional list of
              [subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/)
              to add to the contract.

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
            "/v1/contracts/create",
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
                    "hierarchy_configuration": hierarchy_configuration,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "name": name,
                    "net_payment_terms_days": net_payment_terms_days,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "overrides": overrides,
                    "prepaid_balance_threshold_configuration": prepaid_balance_threshold_configuration,
                    "priority": priority,
                    "professional_services": professional_services,
                    "rate_card_alias": rate_card_alias,
                    "rate_card_id": rate_card_id,
                    "recurring_commits": recurring_commits,
                    "recurring_credits": recurring_credits,
                    "reseller_royalties": reseller_royalties,
                    "revenue_system_configuration": revenue_system_configuration,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "scheduled_charges": scheduled_charges,
                    "scheduled_charges_on_usage_invoices": scheduled_charges_on_usage_invoices,
                    "spend_threshold_configuration": spend_threshold_configuration,
                    "subscriptions": subscriptions,
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
        include_balance: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """This is the v1 endpoint to get a contract.

        New clients should implement using
        the v2 endpoint.

        Args:
          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contracts/get",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
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
        covering_date: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractListResponse:
        """
        Retrieves all contracts for a specific customer, including pricing, terms,
        credits, and commitments. Use this to view a customer's contract history and
        current agreements for billing management. Returns contract details with
        optional ledgers and balance information.

        ⚠️ Note: This is the legacy v1 endpoint - new integrations should use the v2
        endpoint for enhanced features.

        Args:
          covering_date: Optional RFC 3339 timestamp. If provided, the response will include only
              contracts effective on the provided date. This cannot be provided if the
              starting_at filter is provided.

          include_archived: Include archived contracts in the response

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

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
            "/v1/contracts/list",
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

    def add_manual_balance_entry(
        self,
        *,
        id: str,
        amount: float,
        customer_id: str,
        reason: str,
        segment_id: str,
        contract_id: str | Omit = omit,
        per_group_amounts: Dict[str, float] | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Manually adjust the available balance on a commit or credit.

        This entry is
        appended to the commit ledger as a new event. Optionally include a description
        that provides the reasoning for the entry.

        ### Use this endpoint to:

        - Address incorrect usage burn-down caused by malformed usage or invalid config
        - Decrease available balance to account for outages where usage may have not
          been tracked or sent to Metronome
        - Issue credits to customers in the form of increased balance on existing commit
          or credit

        ### Usage guidelines:

        Manual ledger entries can be extremely useful for resolving discrepancies in
        Metronome. However, most corrections to inaccurate billings can be modified
        upstream of the commit, whether that is via contract editing, rate editing, or
        other actions that cause an invoice to be recalculated.

        Args:
          id: ID of the balance (commit or credit) to update.

          amount: Amount to add to the segment. A negative number will draw down from the balance.

          customer_id: ID of the customer whose balance is to be updated.

          reason: Reason for the manual adjustment. This will be displayed in the ledger.

          segment_id: ID of the segment to update.

          contract_id: ID of the contract to update. Leave blank to update a customer level balance.

          per_group_amounts: If using individually configured commits/credits attached to seat managed
              subscriptions, the amount to add for each seat. Must sum to total amount.

          timestamp: RFC 3339 timestamp indicating when the manual adjustment takes place. If not
              provided, it will default to the start of the segment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/contracts/addManualBalanceLedgerEntry",
            body=maybe_transform(
                {
                    "id": id,
                    "amount": amount,
                    "customer_id": customer_id,
                    "reason": reason,
                    "segment_id": segment_id,
                    "contract_id": contract_id,
                    "per_group_amounts": per_group_amounts,
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
        commits: Iterable[contract_amend_params.Commit] | Omit = omit,
        credits: Iterable[contract_amend_params.Credit] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        discounts: Iterable[contract_amend_params.Discount] | Omit = omit,
        netsuite_sales_order_id: str | Omit = omit,
        overrides: Iterable[contract_amend_params.Override] | Omit = omit,
        professional_services: Iterable[contract_amend_params.ProfessionalService] | Omit = omit,
        reseller_royalties: Iterable[contract_amend_params.ResellerRoyalty] | Omit = omit,
        salesforce_opportunity_id: str | Omit = omit,
        scheduled_charges: Iterable[contract_amend_params.ScheduledCharge] | Omit = omit,
        total_contract_value: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractAmendResponse:
        """Amendments will be replaced by Contract editing.

        New clients should implement
        using the `editContract` endpoint. Read more about the migration to contract
        editing [here](/guides/implement-metronome/migrate-amendments-to-edits/) and
        reach out to your Metronome representative for more details. Once contract
        editing is enabled, access to this endpoint will be removed.

        Args:
          contract_id: ID of the contract to amend

          customer_id: ID of the customer whose contract is to be amended

          starting_at: inclusive start time for the amendment

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

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
            "/v1/contracts/amend",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractArchiveResponse:
        """Permanently end and archive a contract along with all its terms.

        Any draft
        invoices will be canceled, and all upcoming scheduled invoices will be
        voided–also all finalized invoices can optionally be voided. Use this in the
        event a contract was incorrectly created and needed to be removed from a
        customer.

        #### Impact on commits and credits:

        When archiving a contract, all associated commits and credits are also archived.
        For prepaid commits with active segments, Metronome automatically generates
        expiration ledger entries to close out any remaining balances, ensuring accurate
        accounting of unused prepaid amounts. These ledger entries will appear in the
        commit's transaction history with type `PREPAID_COMMIT_EXPIRATION`.

        #### Archived contract visibility:

        Archived contracts remain accessible for historical reporting and audit
        purposes. They can be retrieved using the `ListContracts` endpoint by setting
        the `include_archived` parameter to `true` or in the Metronome UI when the "Show
        archived" option is enabled.

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
            "/v1/contracts/archive",
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

    def create_historical_invoices(
        self,
        *,
        invoices: Iterable[contract_create_historical_invoices_params.Invoice],
        preview: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateHistoricalInvoicesResponse:
        """
        Create historical usage invoices for past billing periods on specific contracts.
        Use this endpoint to generate retroactive invoices with custom usage line items,
        quantities, and date ranges. Supports preview mode to validate invoice data
        before creation. Ideal for billing migrations or correcting past billing
        periods.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contracts/createHistoricalInvoices",
            body=maybe_transform(
                {
                    "invoices": invoices,
                    "preview": preview,
                },
                contract_create_historical_invoices_params.ContractCreateHistoricalInvoicesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateHistoricalInvoicesResponse,
        )

    def list_balances(
        self,
        *,
        customer_id: str,
        id: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        exclude_zero_balances: bool | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_contract_balances: bool | Omit = omit,
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
    ) -> SyncBodyCursorPage[ContractListBalancesResponse]:
        """
        Retrieve a comprehensive view of all available balances (commits and credits)
        for a customer. This endpoint provides real-time visibility into prepaid funds,
        postpaid commitments, promotional credits, and other balance types that can
        offset usage charges, helping you build transparent billing experiences.

        ### Use this endpoint to:

        - Display current available balances in customer dashboards
        - Verify available funds before approving high-usage operations
        - Generate balance reports for finance teams
        - Filter balances by contract or date ranges

        ### Key response fields:

        An array of balance objects (all credits and commits) containing:

        - Balance details: Current available amount for each commit or credit
        - Metadata: Product associations, priorities, applicable date ranges
        - Optional ledger entries: Detailed transaction history (if
          `include_ledgers=true`)
        - Balance calculations: Including pending transactions and future-dated entries
        - Custom fields: Any additional metadata attached to balances

        ### Usage guidelines:

        - Date filtering: Use `effective_before` to include only balances with access
          before a specific date (exclusive)
        - Set `include_balance=true` for calculated balance amounts on each commit or
          credit
        - Set `include_ledgers=true` for full transaction history
        - Set `include_contract_balances = true` to see contract level balances
        - Balance logic: Reflects currently accessible amounts, excluding expired/future
          segments
        - Manual adjustments: Includes all manual ledger entries, even future-dated ones

        Args:
          covering_date: Return only balances that have access schedules that "cover" the provided date

          effective_before: Include only balances that have any access before the provided date (exclusive)

          exclude_zero_balances: Exclude balances with zero amounts from the response.

          include_archived: Include archived credits and credits from archived contracts.

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

          include_contract_balances: Include balances on the contract level.

          include_ledgers: Include ledgers in the response. Setting this flag may cause the query to be
              slower.

          limit: The maximum number of commits to return. Defaults to 25.

          next_page: The next page token from a previous response.

          starting_at: Include only balances that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/customerBalances/list",
            page=SyncBodyCursorPage[ContractListBalancesResponse],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "id": id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "exclude_zero_balances": exclude_zero_balances,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_contract_balances": include_contract_balances,
                    "include_ledgers": include_ledgers,
                    "limit": limit,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                contract_list_balances_params.ContractListBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(
                Any, ContractListBalancesResponse
            ),  # Union types cannot be passed in as arguments in the type system
            method="post",
        )

    def retrieve_rate_schedule(
        self,
        *,
        contract_id: str,
        customer_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        at: Union[str, datetime] | Omit = omit,
        selectors: Iterable[contract_retrieve_rate_schedule_params.Selector] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveRateScheduleResponse:
        """
        For a specific customer and contract, get the rates at a specific point in time.
        This endpoint takes the contract's rate card into consideration, including
        scheduled changes. It also takes into account overrides on the contract.

        For example, if you want to show your customer a summary of the prices they are
        paying, inclusive of any negotiated discounts or promotions, use this endpoint.
        This endpoint only returns rates that are entitled.

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
            "/v1/contracts/getContractRateSchedule",
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

    def retrieve_subscription_quantity_history(
        self,
        *,
        contract_id: str,
        customer_id: str,
        subscription_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveSubscriptionQuantityHistoryResponse:
        """
        Get the history of subscription quantities and prices over time for a given
        `subscription_id`. This endpoint can be used to power an in-product experience
        where you show a customer their historical changes to seat count. Future changes
        are not included in this endpoint - use the `getContract` endpoint to view the
        future scheduled changes to a subscription's quantity.

        Subscriptions are used to model fixed recurring fees as well as seat-based
        recurring fees. To model changes to the number of seats in Metronome, you can
        increment or decrement the quantity on a subscription at any point in the past
        or future.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contracts/getSubscriptionQuantityHistory",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "subscription_id": subscription_id,
                },
                contract_retrieve_subscription_quantity_history_params.ContractRetrieveSubscriptionQuantityHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveSubscriptionQuantityHistoryResponse,
        )

    def schedule_pro_services_invoice(
        self,
        *,
        contract_id: str,
        customer_id: str,
        issued_at: Union[str, datetime],
        line_items: Iterable[contract_schedule_pro_services_invoice_params.LineItem],
        netsuite_invoice_header_end: Union[str, datetime] | Omit = omit,
        netsuite_invoice_header_start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractScheduleProServicesInvoiceResponse:
        """
        Create a new scheduled invoice for Professional Services terms on a contract.
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
            "/v1/contracts/scheduleProServicesInvoice",
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
        group_values: SequenceNotStr[str],
        starting_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If a customer has multiple contracts with overlapping rates, the usage filter
        routes usage to the appropriate contract based on a predefined group key.

        As an example, imagine you have a customer associated with two projects. Each
        project is associated with its own contract. You can create a usage filter with
        group key `project_id` on each contract, and route usage for `project_1` to the
        first contract and `project_2` to the second contract.

        ### Use this endpoint to:

        - Support enterprise contracting scenarios where multiple contracts are
          associated to the same customer with the same rates.
        - Update the usage filter associated with the contract over time.

        ### Usage guidelines:

        To use usage filters, the `group_key` must be defined on the billable metrics
        underlying the rate card on the contracts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/contracts/setUsageFilter",
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
        allow_ending_before_finalized_invoice: bool | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUpdateEndDateResponse:
        """Update or add an end date to a contract.

        Ending a contract early will impact
        draft usage statements, truncate any terms, and remove upcoming scheduled
        invoices. Moving the date into the future will only extend the contract length.
        Terms and scheduled invoices are not extended. In-advance subscriptions will not
        be extended. Use this if a contract's end date has changed or if a perpetual
        contract ends.

        Args:
          contract_id: ID of the contract to update

          customer_id: ID of the customer whose contract is to be updated

          allow_ending_before_finalized_invoice: If true, allows setting the contract end date earlier than the end_timestamp of
              existing finalized invoices. Finalized invoices will be unchanged; if you want
              to incorporate the new end date, you can void and regenerate finalized usage
              invoices. Defaults to true.

          ending_before: RFC 3339 timestamp indicating when the contract will end (exclusive). If not
              provided, the contract will be updated to be open-ended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contracts/updateEndDate",
            body=maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "allow_ending_before_finalized_invoice": allow_ending_before_finalized_invoice,
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

    async def create(
        self,
        *,
        customer_id: str,
        starting_at: Union[str, datetime],
        billing_provider_configuration: contract_create_params.BillingProviderConfiguration | Omit = omit,
        commits: Iterable[contract_create_params.Commit] | Omit = omit,
        credits: Iterable[contract_create_params.Credit] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        discounts: Iterable[contract_create_params.Discount] | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        hierarchy_configuration: contract_create_params.HierarchyConfiguration | Omit = omit,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | Omit = omit,
        name: str | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        netsuite_sales_order_id: str | Omit = omit,
        overrides: Iterable[contract_create_params.Override] | Omit = omit,
        prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfiguration | Omit = omit,
        priority: float | Omit = omit,
        professional_services: Iterable[contract_create_params.ProfessionalService] | Omit = omit,
        rate_card_alias: str | Omit = omit,
        rate_card_id: str | Omit = omit,
        recurring_commits: Iterable[contract_create_params.RecurringCommit] | Omit = omit,
        recurring_credits: Iterable[contract_create_params.RecurringCredit] | Omit = omit,
        reseller_royalties: Iterable[contract_create_params.ResellerRoyalty] | Omit = omit,
        revenue_system_configuration: contract_create_params.RevenueSystemConfiguration | Omit = omit,
        salesforce_opportunity_id: str | Omit = omit,
        scheduled_charges: Iterable[contract_create_params.ScheduledCharge] | Omit = omit,
        scheduled_charges_on_usage_invoices: Literal["ALL"] | Omit = omit,
        spend_threshold_configuration: SpendThresholdConfiguration | Omit = omit,
        subscriptions: Iterable[contract_create_params.Subscription] | Omit = omit,
        total_contract_value: float | Omit = omit,
        transition: contract_create_params.Transition | Omit = omit,
        uniqueness_key: str | Omit = omit,
        usage_filter: BaseUsageFilter | Omit = omit,
        usage_statement_schedule: contract_create_params.UsageStatementSchedule | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateResponse:
        """
        Contracts define a customer's products, pricing, discounts, access duration, and
        billing configuration. Contracts serve as the central billing agreement for both
        PLG and Enterprise customers, you can automatically customers access to your
        products and services directly from your product or CRM.

        ### Use this endpoint to:

        - PLG onboarding: Automatically provision new self-serve customers with
          contracts when they sign up.
        - Enterprise sales: Push negotiated contracts from Salesforce with custom
          pricing and commitments
        - Promotional pricing: Implement time-limited discounts and free trials through
          overrides

        ### Key components:

        #### Contract Term and Billing Schedule

        - Set contract duration using `starting_at` and `ending_before` fields. PLG
          contracts typically use perpetual agreements (no end date), while Enterprise
          contracts have fixed end dates which can be edited over time in the case of
          co-term upsells.

        #### Rate Card

        If you are offering usage based pricing, you can set a rate card for the
        contract to reference through `rate_card_id` or `rate_card_alias`. The rate card
        is a store of all of your usage based products and their centralized pricing.
        Any new products or price changes on the rate card can be set to automatically
        propagate to all associated contracts - this ensures consistent pricing and
        product launches flow to contracts without manual updates and migrations. The
        `usage_statement_schedule` determines the cadence on which Metronome will
        finalize a usage invoice for the customer. This defaults to monthly on the 1st,
        with options for custom dates, quarterly, or annual cadences. Note: Most usage
        based billing companies align usage statements to be evaluated aligned to the
        first of the month. Read more about
        [Rate Cards](https://docs.metronome.com/pricing-packaging/create-manage-rate-cards/).

        #### Overrides and discounts

        Customize pricing on the contract through time-bounded overrides that can target
        specific products, product families, or complex usage scenarios. Overrides
        enable two key capabilities:

        - Discounts: Apply percentage discounts, fixed rate reductions, or
          quantity-based pricing tiers
        - Entitlements: Provide special pricing or access to specific products for
          negotiated deals

        Read more about
        [Contract Overrides](https://docs.metronome.com/manage-product-access/add-contract-override/).

        #### Commits and Credits

        Using commits, configure prepaid or postpaid spending commitments where
        customers promise to spend a certain amount over the contract period paid in
        advance or in arrears. Use credits to provide free spending allowances. Under
        the hood these are the same mechanisms, however, credits are typically offered
        for free (SLA or promotional) or as a part of an allotment associated with a
        Subscription.

        In Metronome, you can set commits and credits to only be applicable for a subset
        of usage. Use `applicable_product_ids` or `applicable_product_tags` to create
        product or product-family specific commits or credits, or you can build complex
        boolean logic specifiers to target usage based on pricing and presentation group
        values using `override_specifiers`.

        These objects can also also be configured to have a recurrence schedule to
        easily model customer packaging which includes recurring monthly or quarterly
        allotments.

        Commits support rollover settings (`rollover_fraction`) to transfer unused
        balances between contract periods, either entirely or as a percentage.

        Read more about
        [Credits and Commits](https://docs.metronome.com/pricing-packaging/apply-credits-commits/).

        #### Subscriptions

        You can add a fixed recurring charge to a contract, like monthly licenses or
        seat-based fees, using the subscription charge. Subscription charges are defined
        on your rate card and you can select which subscription is applicable to add to
        each contract. When you add a subscription to a contract you need to:

        - Define whether the subscription is paid for in-advance or in-arrears
          (`collection_schedule`)
        - Define the proration behavior (`proration`)
        - Specify an initial quantity (`initial_quantity`)
        - Define which subscription rate on the rate card should be used
          (`subscription_rate`)

        Read more about
        [Subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/).

        #### Scheduled Charges

        Set up one-time, recurring, or entirely custom charges that occur on specific
        dates, separate from usage-based billing or commitments. These can be used to
        model non-recurring platform charges or professional services.

        #### Threshold Billing

        Metronome allows you to configure automatic billing triggers when customers
        reach spending thresholds to prevent fraud and manage risk. You can use
        `spend_threshold_configuration` to trigger an invoice to cover current charges
        whenever the threshold is reached or you can ensure the customer maintains a
        minimum prepaid balance using the `prepaid_balance_configuration`.

        Read more about
        [Spend Threshold](https://docs.metronome.com/manage-product-access/spend-thresholds/)
        and
        [Prepaid Balance Thresholds](https://docs.metronome.com/manage-product-access/prepaid-balance-thresholds/).

        ### Usage guidelines:

        - You can always
          [Edit Contracts](https://docs.metronome.com/manage-product-access/edit-contract/)
          after it has been created, using the `editContract` endpoint. Metronome keeps
          track of all edits, both in the audit log and over the `getEditHistory`
          endpoint.
        - Customers in Metronome can have multiple concurrent contracts at one time. Use
          `usage_filters` to route the correct usage to each contract.
          [Read more about usage filters](https://docs.metronome.com/manage-product-access/provision-customer/#create-a-usage-filter).

        Args:
          starting_at: inclusive contract start time

          billing_provider_configuration: The billing provider configuration associated with a contract. Provide either an
              ID or the provider and delivery method.

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          discounts: This field's availability is dependent on your client's configuration.

          ending_before: exclusive contract end time

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          netsuite_sales_order_id: This field's availability is dependent on your client's configuration.

          priority: Priority of the contract.

          professional_services: This field's availability is dependent on your client's configuration.

          rate_card_alias: Selects the rate card linked to the specified alias as of the contract's start
              date.

          reseller_royalties: This field's availability is dependent on your client's configuration.

          revenue_system_configuration: The revenue system configuration associated with a contract. Provide either an
              ID or the provider and delivery method.

          salesforce_opportunity_id: This field's availability is dependent on your client's configuration.

          scheduled_charges_on_usage_invoices: Determines which scheduled and commit charges to consolidate onto the Contract's
              usage invoice. The charge's `timestamp` must match the usage invoice's
              `ending_before` date for consolidation to occur. This field cannot be modified
              after a Contract has been created. If this field is omitted, charges will appear
              on a separate invoice from usage charges.

          subscriptions: Optional list of
              [subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/)
              to add to the contract.

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
            "/v1/contracts/create",
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
                    "hierarchy_configuration": hierarchy_configuration,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "name": name,
                    "net_payment_terms_days": net_payment_terms_days,
                    "netsuite_sales_order_id": netsuite_sales_order_id,
                    "overrides": overrides,
                    "prepaid_balance_threshold_configuration": prepaid_balance_threshold_configuration,
                    "priority": priority,
                    "professional_services": professional_services,
                    "rate_card_alias": rate_card_alias,
                    "rate_card_id": rate_card_id,
                    "recurring_commits": recurring_commits,
                    "recurring_credits": recurring_credits,
                    "reseller_royalties": reseller_royalties,
                    "revenue_system_configuration": revenue_system_configuration,
                    "salesforce_opportunity_id": salesforce_opportunity_id,
                    "scheduled_charges": scheduled_charges,
                    "scheduled_charges_on_usage_invoices": scheduled_charges_on_usage_invoices,
                    "spend_threshold_configuration": spend_threshold_configuration,
                    "subscriptions": subscriptions,
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
        include_balance: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """This is the v1 endpoint to get a contract.

        New clients should implement using
        the v2 endpoint.

        Args:
          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

          include_ledgers: Include commit ledgers in the response. Setting this flag may cause the query to
              be slower.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contracts/get",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
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
        covering_date: Union[str, datetime] | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        starting_at: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractListResponse:
        """
        Retrieves all contracts for a specific customer, including pricing, terms,
        credits, and commitments. Use this to view a customer's contract history and
        current agreements for billing management. Returns contract details with
        optional ledgers and balance information.

        ⚠️ Note: This is the legacy v1 endpoint - new integrations should use the v2
        endpoint for enhanced features.

        Args:
          covering_date: Optional RFC 3339 timestamp. If provided, the response will include only
              contracts effective on the provided date. This cannot be provided if the
              starting_at filter is provided.

          include_archived: Include archived contracts in the response

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

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
            "/v1/contracts/list",
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

    async def add_manual_balance_entry(
        self,
        *,
        id: str,
        amount: float,
        customer_id: str,
        reason: str,
        segment_id: str,
        contract_id: str | Omit = omit,
        per_group_amounts: Dict[str, float] | Omit = omit,
        timestamp: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Manually adjust the available balance on a commit or credit.

        This entry is
        appended to the commit ledger as a new event. Optionally include a description
        that provides the reasoning for the entry.

        ### Use this endpoint to:

        - Address incorrect usage burn-down caused by malformed usage or invalid config
        - Decrease available balance to account for outages where usage may have not
          been tracked or sent to Metronome
        - Issue credits to customers in the form of increased balance on existing commit
          or credit

        ### Usage guidelines:

        Manual ledger entries can be extremely useful for resolving discrepancies in
        Metronome. However, most corrections to inaccurate billings can be modified
        upstream of the commit, whether that is via contract editing, rate editing, or
        other actions that cause an invoice to be recalculated.

        Args:
          id: ID of the balance (commit or credit) to update.

          amount: Amount to add to the segment. A negative number will draw down from the balance.

          customer_id: ID of the customer whose balance is to be updated.

          reason: Reason for the manual adjustment. This will be displayed in the ledger.

          segment_id: ID of the segment to update.

          contract_id: ID of the contract to update. Leave blank to update a customer level balance.

          per_group_amounts: If using individually configured commits/credits attached to seat managed
              subscriptions, the amount to add for each seat. Must sum to total amount.

          timestamp: RFC 3339 timestamp indicating when the manual adjustment takes place. If not
              provided, it will default to the start of the segment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/contracts/addManualBalanceLedgerEntry",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "amount": amount,
                    "customer_id": customer_id,
                    "reason": reason,
                    "segment_id": segment_id,
                    "contract_id": contract_id,
                    "per_group_amounts": per_group_amounts,
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
        commits: Iterable[contract_amend_params.Commit] | Omit = omit,
        credits: Iterable[contract_amend_params.Credit] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        discounts: Iterable[contract_amend_params.Discount] | Omit = omit,
        netsuite_sales_order_id: str | Omit = omit,
        overrides: Iterable[contract_amend_params.Override] | Omit = omit,
        professional_services: Iterable[contract_amend_params.ProfessionalService] | Omit = omit,
        reseller_royalties: Iterable[contract_amend_params.ResellerRoyalty] | Omit = omit,
        salesforce_opportunity_id: str | Omit = omit,
        scheduled_charges: Iterable[contract_amend_params.ScheduledCharge] | Omit = omit,
        total_contract_value: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractAmendResponse:
        """Amendments will be replaced by Contract editing.

        New clients should implement
        using the `editContract` endpoint. Read more about the migration to contract
        editing [here](/guides/implement-metronome/migrate-amendments-to-edits/) and
        reach out to your Metronome representative for more details. Once contract
        editing is enabled, access to this endpoint will be removed.

        Args:
          contract_id: ID of the contract to amend

          customer_id: ID of the customer whose contract is to be amended

          starting_at: inclusive start time for the amendment

          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

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
            "/v1/contracts/amend",
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractArchiveResponse:
        """Permanently end and archive a contract along with all its terms.

        Any draft
        invoices will be canceled, and all upcoming scheduled invoices will be
        voided–also all finalized invoices can optionally be voided. Use this in the
        event a contract was incorrectly created and needed to be removed from a
        customer.

        #### Impact on commits and credits:

        When archiving a contract, all associated commits and credits are also archived.
        For prepaid commits with active segments, Metronome automatically generates
        expiration ledger entries to close out any remaining balances, ensuring accurate
        accounting of unused prepaid amounts. These ledger entries will appear in the
        commit's transaction history with type `PREPAID_COMMIT_EXPIRATION`.

        #### Archived contract visibility:

        Archived contracts remain accessible for historical reporting and audit
        purposes. They can be retrieved using the `ListContracts` endpoint by setting
        the `include_archived` parameter to `true` or in the Metronome UI when the "Show
        archived" option is enabled.

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
            "/v1/contracts/archive",
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

    async def create_historical_invoices(
        self,
        *,
        invoices: Iterable[contract_create_historical_invoices_params.Invoice],
        preview: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractCreateHistoricalInvoicesResponse:
        """
        Create historical usage invoices for past billing periods on specific contracts.
        Use this endpoint to generate retroactive invoices with custom usage line items,
        quantities, and date ranges. Supports preview mode to validate invoice data
        before creation. Ideal for billing migrations or correcting past billing
        periods.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contracts/createHistoricalInvoices",
            body=await async_maybe_transform(
                {
                    "invoices": invoices,
                    "preview": preview,
                },
                contract_create_historical_invoices_params.ContractCreateHistoricalInvoicesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractCreateHistoricalInvoicesResponse,
        )

    def list_balances(
        self,
        *,
        customer_id: str,
        id: str | Omit = omit,
        covering_date: Union[str, datetime] | Omit = omit,
        effective_before: Union[str, datetime] | Omit = omit,
        exclude_zero_balances: bool | Omit = omit,
        include_archived: bool | Omit = omit,
        include_balance: bool | Omit = omit,
        include_contract_balances: bool | Omit = omit,
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
    ) -> AsyncPaginator[ContractListBalancesResponse, AsyncBodyCursorPage[ContractListBalancesResponse]]:
        """
        Retrieve a comprehensive view of all available balances (commits and credits)
        for a customer. This endpoint provides real-time visibility into prepaid funds,
        postpaid commitments, promotional credits, and other balance types that can
        offset usage charges, helping you build transparent billing experiences.

        ### Use this endpoint to:

        - Display current available balances in customer dashboards
        - Verify available funds before approving high-usage operations
        - Generate balance reports for finance teams
        - Filter balances by contract or date ranges

        ### Key response fields:

        An array of balance objects (all credits and commits) containing:

        - Balance details: Current available amount for each commit or credit
        - Metadata: Product associations, priorities, applicable date ranges
        - Optional ledger entries: Detailed transaction history (if
          `include_ledgers=true`)
        - Balance calculations: Including pending transactions and future-dated entries
        - Custom fields: Any additional metadata attached to balances

        ### Usage guidelines:

        - Date filtering: Use `effective_before` to include only balances with access
          before a specific date (exclusive)
        - Set `include_balance=true` for calculated balance amounts on each commit or
          credit
        - Set `include_ledgers=true` for full transaction history
        - Set `include_contract_balances = true` to see contract level balances
        - Balance logic: Reflects currently accessible amounts, excluding expired/future
          segments
        - Manual adjustments: Includes all manual ledger entries, even future-dated ones

        Args:
          covering_date: Return only balances that have access schedules that "cover" the provided date

          effective_before: Include only balances that have any access before the provided date (exclusive)

          exclude_zero_balances: Exclude balances with zero amounts from the response.

          include_archived: Include archived credits and credits from archived contracts.

          include_balance: Include the balance of credits and commits in the response. Setting this flag
              may cause the query to be slower.

          include_contract_balances: Include balances on the contract level.

          include_ledgers: Include ledgers in the response. Setting this flag may cause the query to be
              slower.

          limit: The maximum number of commits to return. Defaults to 25.

          next_page: The next page token from a previous response.

          starting_at: Include only balances that have any access on or after the provided date

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contracts/customerBalances/list",
            page=AsyncBodyCursorPage[ContractListBalancesResponse],
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "id": id,
                    "covering_date": covering_date,
                    "effective_before": effective_before,
                    "exclude_zero_balances": exclude_zero_balances,
                    "include_archived": include_archived,
                    "include_balance": include_balance,
                    "include_contract_balances": include_contract_balances,
                    "include_ledgers": include_ledgers,
                    "limit": limit,
                    "next_page": next_page,
                    "starting_at": starting_at,
                },
                contract_list_balances_params.ContractListBalancesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=cast(
                Any, ContractListBalancesResponse
            ),  # Union types cannot be passed in as arguments in the type system
            method="post",
        )

    async def retrieve_rate_schedule(
        self,
        *,
        contract_id: str,
        customer_id: str,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        at: Union[str, datetime] | Omit = omit,
        selectors: Iterable[contract_retrieve_rate_schedule_params.Selector] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveRateScheduleResponse:
        """
        For a specific customer and contract, get the rates at a specific point in time.
        This endpoint takes the contract's rate card into consideration, including
        scheduled changes. It also takes into account overrides on the contract.

        For example, if you want to show your customer a summary of the prices they are
        paying, inclusive of any negotiated discounts or promotions, use this endpoint.
        This endpoint only returns rates that are entitled.

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
            "/v1/contracts/getContractRateSchedule",
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

    async def retrieve_subscription_quantity_history(
        self,
        *,
        contract_id: str,
        customer_id: str,
        subscription_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveSubscriptionQuantityHistoryResponse:
        """
        Get the history of subscription quantities and prices over time for a given
        `subscription_id`. This endpoint can be used to power an in-product experience
        where you show a customer their historical changes to seat count. Future changes
        are not included in this endpoint - use the `getContract` endpoint to view the
        future scheduled changes to a subscription's quantity.

        Subscriptions are used to model fixed recurring fees as well as seat-based
        recurring fees. To model changes to the number of seats in Metronome, you can
        increment or decrement the quantity on a subscription at any point in the past
        or future.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contracts/getSubscriptionQuantityHistory",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "subscription_id": subscription_id,
                },
                contract_retrieve_subscription_quantity_history_params.ContractRetrieveSubscriptionQuantityHistoryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractRetrieveSubscriptionQuantityHistoryResponse,
        )

    async def schedule_pro_services_invoice(
        self,
        *,
        contract_id: str,
        customer_id: str,
        issued_at: Union[str, datetime],
        line_items: Iterable[contract_schedule_pro_services_invoice_params.LineItem],
        netsuite_invoice_header_end: Union[str, datetime] | Omit = omit,
        netsuite_invoice_header_start: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractScheduleProServicesInvoiceResponse:
        """
        Create a new scheduled invoice for Professional Services terms on a contract.
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
            "/v1/contracts/scheduleProServicesInvoice",
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
        group_values: SequenceNotStr[str],
        starting_at: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        If a customer has multiple contracts with overlapping rates, the usage filter
        routes usage to the appropriate contract based on a predefined group key.

        As an example, imagine you have a customer associated with two projects. Each
        project is associated with its own contract. You can create a usage filter with
        group key `project_id` on each contract, and route usage for `project_1` to the
        first contract and `project_2` to the second contract.

        ### Use this endpoint to:

        - Support enterprise contracting scenarios where multiple contracts are
          associated to the same customer with the same rates.
        - Update the usage filter associated with the contract over time.

        ### Usage guidelines:

        To use usage filters, the `group_key` must be defined on the billable metrics
        underlying the rate card on the contracts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/contracts/setUsageFilter",
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
        allow_ending_before_finalized_invoice: bool | Omit = omit,
        ending_before: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractUpdateEndDateResponse:
        """Update or add an end date to a contract.

        Ending a contract early will impact
        draft usage statements, truncate any terms, and remove upcoming scheduled
        invoices. Moving the date into the future will only extend the contract length.
        Terms and scheduled invoices are not extended. In-advance subscriptions will not
        be extended. Use this if a contract's end date has changed or if a perpetual
        contract ends.

        Args:
          contract_id: ID of the contract to update

          customer_id: ID of the customer whose contract is to be updated

          allow_ending_before_finalized_invoice: If true, allows setting the contract end date earlier than the end_timestamp of
              existing finalized invoices. Finalized invoices will be unchanged; if you want
              to incorporate the new end date, you can void and regenerate finalized usage
              invoices. Defaults to true.

          ending_before: RFC 3339 timestamp indicating when the contract will end (exclusive). If not
              provided, the contract will be updated to be open-ended.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contracts/updateEndDate",
            body=await async_maybe_transform(
                {
                    "contract_id": contract_id,
                    "customer_id": customer_id,
                    "allow_ending_before_finalized_invoice": allow_ending_before_finalized_invoice,
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
        self.create_historical_invoices = to_raw_response_wrapper(
            contracts.create_historical_invoices,
        )
        self.list_balances = to_raw_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = to_raw_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.retrieve_subscription_quantity_history = to_raw_response_wrapper(
            contracts.retrieve_subscription_quantity_history,
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
        self.create_historical_invoices = async_to_raw_response_wrapper(
            contracts.create_historical_invoices,
        )
        self.list_balances = async_to_raw_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = async_to_raw_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.retrieve_subscription_quantity_history = async_to_raw_response_wrapper(
            contracts.retrieve_subscription_quantity_history,
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
        self.create_historical_invoices = to_streamed_response_wrapper(
            contracts.create_historical_invoices,
        )
        self.list_balances = to_streamed_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = to_streamed_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.retrieve_subscription_quantity_history = to_streamed_response_wrapper(
            contracts.retrieve_subscription_quantity_history,
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
        self.create_historical_invoices = async_to_streamed_response_wrapper(
            contracts.create_historical_invoices,
        )
        self.list_balances = async_to_streamed_response_wrapper(
            contracts.list_balances,
        )
        self.retrieve_rate_schedule = async_to_streamed_response_wrapper(
            contracts.retrieve_rate_schedule,
        )
        self.retrieve_subscription_quantity_history = async_to_streamed_response_wrapper(
            contracts.retrieve_subscription_quantity_history,
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
