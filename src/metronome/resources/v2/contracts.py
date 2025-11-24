# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
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
from ...types.shared_params.commit_specifier_input import CommitSpecifierInput
from ...types.v2.contract_get_edit_history_response import ContractGetEditHistoryResponse
from ...types.shared_params.commit_hierarchy_configuration import CommitHierarchyConfiguration
from ...types.shared_params.spend_threshold_configuration_v2 import SpendThresholdConfigurationV2
from ...types.shared_params.prepaid_balance_threshold_configuration_v2 import PrepaidBalanceThresholdConfigurationV2

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
        as_of_date: Union[str, datetime] | Omit = omit,
        include_balance: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """
        Gets the details for a specific contract, including contract term, rate card
        information, credits and commits, and more.

        ### Use this endpoint to:

        - Check the duration of a customer's current contract
        - Get details on contract terms, including access schedule amounts for
          commitments and credits
        - Understand the state of a contract at a past time. As you can evolve the terms
          of a contract over time through editing, use the `as_of_date` parameter to
          view the full contract configuration as of that point in time.

        ### Usage guidelines:

        - Optionally, use the `include_balance` and `include_ledger` fields to include
          balances and ledgers in the credit and commit responses. Using these fields
          will cause the query to be slower.

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
        For a given customer, lists all of their contracts in chronological order.

        ### Use this endpoint to:

        - Check if a customer is provisioned with any contract, and at which tier
        - Check the duration and terms of a customer's current contract
        - Power a page in your end customer experience that shows the customer's history
          of tiers (e.g. this customer started out on the Pro Plan, then downgraded to
          the Starter plan).

        ### Usage guidelines:

        Use the `starting_at`, `covering_date`, and `include_archived` parameters to
        filter the list of returned contracts. For example, to list only currently
        active contracts, pass `covering_date` equal to the current time.

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
        add_billing_provider_configuration_update: contract_edit_params.AddBillingProviderConfigurationUpdate
        | Omit = omit,
        add_commits: Iterable[contract_edit_params.AddCommit] | Omit = omit,
        add_credits: Iterable[contract_edit_params.AddCredit] | Omit = omit,
        add_discounts: Iterable[contract_edit_params.AddDiscount] | Omit = omit,
        add_overrides: Iterable[contract_edit_params.AddOverride] | Omit = omit,
        add_prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfigurationV2 | Omit = omit,
        add_professional_services: Iterable[contract_edit_params.AddProfessionalService] | Omit = omit,
        add_recurring_commits: Iterable[contract_edit_params.AddRecurringCommit] | Omit = omit,
        add_recurring_credits: Iterable[contract_edit_params.AddRecurringCredit] | Omit = omit,
        add_reseller_royalties: Iterable[contract_edit_params.AddResellerRoyalty] | Omit = omit,
        add_scheduled_charges: Iterable[contract_edit_params.AddScheduledCharge] | Omit = omit,
        add_spend_threshold_configuration: SpendThresholdConfigurationV2 | Omit = omit,
        add_subscriptions: Iterable[contract_edit_params.AddSubscription] | Omit = omit,
        allow_contract_ending_before_finalized_invoice: bool | Omit = omit,
        archive_commits: Iterable[contract_edit_params.ArchiveCommit] | Omit = omit,
        archive_credits: Iterable[contract_edit_params.ArchiveCredit] | Omit = omit,
        archive_scheduled_charges: Iterable[contract_edit_params.ArchiveScheduledCharge] | Omit = omit,
        remove_overrides: Iterable[contract_edit_params.RemoveOverride] | Omit = omit,
        uniqueness_key: str | Omit = omit,
        update_commits: Iterable[contract_edit_params.UpdateCommit] | Omit = omit,
        update_contract_end_date: Union[str, datetime, None] | Omit = omit,
        update_contract_name: Optional[str] | Omit = omit,
        update_credits: Iterable[contract_edit_params.UpdateCredit] | Omit = omit,
        update_prepaid_balance_threshold_configuration: contract_edit_params.UpdatePrepaidBalanceThresholdConfiguration
        | Omit = omit,
        update_recurring_commits: Iterable[contract_edit_params.UpdateRecurringCommit] | Omit = omit,
        update_recurring_credits: Iterable[contract_edit_params.UpdateRecurringCredit] | Omit = omit,
        update_scheduled_charges: Iterable[contract_edit_params.UpdateScheduledCharge] | Omit = omit,
        update_spend_threshold_configuration: contract_edit_params.UpdateSpendThresholdConfiguration | Omit = omit,
        update_subscriptions: Iterable[contract_edit_params.UpdateSubscription] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditResponse:
        """
        The ability to edit a contract helps you react quickly to the needs of your
        customers and your business.

        ### Use this endpoint to:

        - Encode mid-term commitment and discount changes
        - Fix configuration mistakes and easily roll back packaging changes

        ### Key response fields:

        - The `id` of the edit
        - Complete edit details. For example, if you edited the contract to add new
          overrides and credits, you will receive the IDs of those overrides and credits
          in the response.

        ### Usage guidelines:

        - When you edit a contract, any draft invoices update immediately to reflect
          that edit. Finalized invoices remain unchanged - you must void and regenerate
          them in the UI or API to reflect the edit.
        - Contract editing must be enabled to use this endpoint. Reach out to your
          Metronome representative to learn more.

        Args:
          contract_id: ID of the contract being edited

          customer_id: ID of the customer whose contract is being edited

          add_billing_provider_configuration_update: Update the billing provider configuration on the contract. Currently only
              supports adding a billing provider configuration to a contract that does not
              already have one.

          add_professional_services: This field's availability is dependent on your client's configuration.

          add_subscriptions: Optional list of
              [subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/)
              to add to the contract.

          allow_contract_ending_before_finalized_invoice: If true, allows setting the contract end date earlier than the end_timestamp of
              existing finalized invoices. Finalized invoices will be unchanged; if you want
              to incorporate the new end date, you can void and regenerate finalized usage
              invoices. Defaults to true.

          archive_commits: IDs of commits to archive

          archive_credits: IDs of credits to archive

          archive_scheduled_charges: IDs of scheduled charges to archive

          remove_overrides: IDs of overrides to remove

          uniqueness_key: Optional uniqueness key to prevent duplicate contract edits.

          update_contract_end_date: RFC 3339 timestamp indicating when the contract will end (exclusive).

          update_contract_name: Value to update the contract name to. If not provided, the contract name will
              remain unchanged.

          update_recurring_commits: Edits to these recurring commits will only affect commits whose access schedules
              has not started. Expired commits, and commits with an active access schedule
              will remain unchanged.

          update_recurring_credits: Edits to these recurring credits will only affect credits whose access schedules
              has not started. Expired credits, and credits with an active access schedule
              will remain unchanged.

          update_subscriptions: Optional list of subscriptions to update.

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
                    "add_billing_provider_configuration_update": add_billing_provider_configuration_update,
                    "add_commits": add_commits,
                    "add_credits": add_credits,
                    "add_discounts": add_discounts,
                    "add_overrides": add_overrides,
                    "add_prepaid_balance_threshold_configuration": add_prepaid_balance_threshold_configuration,
                    "add_professional_services": add_professional_services,
                    "add_recurring_commits": add_recurring_commits,
                    "add_recurring_credits": add_recurring_credits,
                    "add_reseller_royalties": add_reseller_royalties,
                    "add_scheduled_charges": add_scheduled_charges,
                    "add_spend_threshold_configuration": add_spend_threshold_configuration,
                    "add_subscriptions": add_subscriptions,
                    "allow_contract_ending_before_finalized_invoice": allow_contract_ending_before_finalized_invoice,
                    "archive_commits": archive_commits,
                    "archive_credits": archive_credits,
                    "archive_scheduled_charges": archive_scheduled_charges,
                    "remove_overrides": remove_overrides,
                    "uniqueness_key": uniqueness_key,
                    "update_commits": update_commits,
                    "update_contract_end_date": update_contract_end_date,
                    "update_contract_name": update_contract_name,
                    "update_credits": update_credits,
                    "update_prepaid_balance_threshold_configuration": update_prepaid_balance_threshold_configuration,
                    "update_recurring_commits": update_recurring_commits,
                    "update_recurring_credits": update_recurring_credits,
                    "update_scheduled_charges": update_scheduled_charges,
                    "update_spend_threshold_configuration": update_spend_threshold_configuration,
                    "update_subscriptions": update_subscriptions,
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
        access_schedule: contract_edit_commit_params.AccessSchedule | Omit = omit,
        applicable_product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        applicable_product_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        description: str | Omit = omit,
        hierarchy_configuration: CommitHierarchyConfiguration | Omit = omit,
        invoice_contract_id: str | Omit = omit,
        invoice_schedule: contract_edit_commit_params.InvoiceSchedule | Omit = omit,
        name: str | Omit = omit,
        priority: Optional[float] | Omit = omit,
        product_id: str | Omit = omit,
        rate_type: Literal["LIST_RATE", "COMMIT_RATE"] | Omit = omit,
        specifiers: Optional[Iterable[CommitSpecifierInput]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditCommitResponse:
        """Edit specific details for a contract-level or customer-level commit.

        Use this
        endpoint to modify individual commit access schedules, invoice schedules,
        applicable products, invoicing contracts, or other fields.

        ### Usage guidelines:

        - As with all edits in Metronome, draft invoices will reflect the edit
          immediately, while finalized invoices are untouched unless voided and
          regenerated.
        - If a commit's invoice schedule item is associated with a finalized invoice,
          you cannot remove or update the invoice schedule item.
        - If a commit's invoice schedule item is associated with a voided invoice, you
          cannot remove the invoice schedule item.
        - You cannot remove an commit access schedule segment that was applied to a
          finalized invoice. You can void the invoice beforehand and then remove the
          access schedule segment.

        Args:
          commit_id: ID of the commit to edit

          customer_id: ID of the customer whose commit is being edited

          applicable_product_ids: Which products the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          applicable_product_tags: Which tags the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          description: Updated description for the commit

          hierarchy_configuration: Optional configuration for commit hierarchy access control

          invoice_contract_id: ID of contract to use for invoicing

          name: Updated name for the commit

          priority: If multiple commits are applicable, the one with the lower priority will apply
              first.

          rate_type: If provided, updates the commit to use the specified rate type for current and
              future invoices. Previously finalized invoices will need to be voided and
              regenerated to reflect the rate type change.

          specifiers: List of filters that determine what kind of customer usage draws down a commit
              or credit. A customer's usage needs to meet the condition of at least one of the
              specifiers to contribute to a commit's or credit's drawdown. This field cannot
              be used together with `applicable_product_ids` or `applicable_product_tags`.
              Instead, to target usage by product or product tag, pass those values in the
              body of `specifiers`.

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
                    "description": description,
                    "hierarchy_configuration": hierarchy_configuration,
                    "invoice_contract_id": invoice_contract_id,
                    "invoice_schedule": invoice_schedule,
                    "name": name,
                    "priority": priority,
                    "product_id": product_id,
                    "rate_type": rate_type,
                    "specifiers": specifiers,
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
        access_schedule: contract_edit_credit_params.AccessSchedule | Omit = omit,
        applicable_product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        applicable_product_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        description: str | Omit = omit,
        hierarchy_configuration: CommitHierarchyConfiguration | Omit = omit,
        name: str | Omit = omit,
        priority: Optional[float] | Omit = omit,
        product_id: str | Omit = omit,
        rate_type: Literal["LIST_RATE", "COMMIT_RATE"] | Omit = omit,
        specifiers: Optional[Iterable[CommitSpecifierInput]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditCreditResponse:
        """
        Edit details for a contract-level or customer-level credit.

        ### Use this endpoint to:

        - Extend the duration or the amount of an existing free credit like a trial
        - Modify individual credit access schedules, applicable products, priority, or
          other fields.

        ### Usage guidelines:

        - As with all edits in Metronome, draft invoices will reflect the edit
          immediately, while finalized invoices are untouched unless voided and
          regenerated.
        - You cannot remove an access schedule segment that was applied to a finalized
          invoice. You can void the invoice beforehand and then remove the access
          schedule segment.

        Args:
          credit_id: ID of the credit to edit

          customer_id: ID of the customer whose credit is being edited

          applicable_product_ids: Which products the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          applicable_product_tags: Which tags the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          description: Updated description for the credit

          hierarchy_configuration: Optional configuration for credit hierarchy access control

          name: Updated name for the credit

          priority: If multiple commits are applicable, the one with the lower priority will apply
              first.

          rate_type: If provided, updates the credit to use the specified rate type for current and
              future invoices. Previously finalized invoices will need to be voided and
              regenerated to reflect the rate type change.

          specifiers: List of filters that determine what kind of customer usage draws down a commit
              or credit. A customer's usage needs to meet the condition of at least one of the
              specifiers to contribute to a commit's or credit's drawdown. This field cannot
              be used together with `applicable_product_ids` or `applicable_product_tags`.
              Instead, to target usage by product or product tag, pass those values in the
              body of `specifiers`.

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
                    "description": description,
                    "hierarchy_configuration": hierarchy_configuration,
                    "name": name,
                    "priority": priority,
                    "product_id": product_id,
                    "rate_type": rate_type,
                    "specifiers": specifiers,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractGetEditHistoryResponse:
        """List all the edits made to a contract over time.

        In Metronome, you can edit a
        contract at any point after it's created to fix mistakes or reflect changes in
        terms. Metronome stores a full history of all edits that were ever made to a
        contract, whether through the UI, `editContract` endpoint, or other endpoints
        like `updateContractEndDate`.

        ### Use this endpoint to:

        - Understand what changes were made to a contract, when, and by who

        ### Key response fields:

        - An array of every edit ever made to the contract
        - Details on each individual edit - for example showing that in one edit, a user
          added two discounts and incremented a subscription quantity.

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
        as_of_date: Union[str, datetime] | Omit = omit,
        include_balance: bool | Omit = omit,
        include_ledgers: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractRetrieveResponse:
        """
        Gets the details for a specific contract, including contract term, rate card
        information, credits and commits, and more.

        ### Use this endpoint to:

        - Check the duration of a customer's current contract
        - Get details on contract terms, including access schedule amounts for
          commitments and credits
        - Understand the state of a contract at a past time. As you can evolve the terms
          of a contract over time through editing, use the `as_of_date` parameter to
          view the full contract configuration as of that point in time.

        ### Usage guidelines:

        - Optionally, use the `include_balance` and `include_ledger` fields to include
          balances and ledgers in the credit and commit responses. Using these fields
          will cause the query to be slower.

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
        For a given customer, lists all of their contracts in chronological order.

        ### Use this endpoint to:

        - Check if a customer is provisioned with any contract, and at which tier
        - Check the duration and terms of a customer's current contract
        - Power a page in your end customer experience that shows the customer's history
          of tiers (e.g. this customer started out on the Pro Plan, then downgraded to
          the Starter plan).

        ### Usage guidelines:

        Use the `starting_at`, `covering_date`, and `include_archived` parameters to
        filter the list of returned contracts. For example, to list only currently
        active contracts, pass `covering_date` equal to the current time.

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
        add_billing_provider_configuration_update: contract_edit_params.AddBillingProviderConfigurationUpdate
        | Omit = omit,
        add_commits: Iterable[contract_edit_params.AddCommit] | Omit = omit,
        add_credits: Iterable[contract_edit_params.AddCredit] | Omit = omit,
        add_discounts: Iterable[contract_edit_params.AddDiscount] | Omit = omit,
        add_overrides: Iterable[contract_edit_params.AddOverride] | Omit = omit,
        add_prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfigurationV2 | Omit = omit,
        add_professional_services: Iterable[contract_edit_params.AddProfessionalService] | Omit = omit,
        add_recurring_commits: Iterable[contract_edit_params.AddRecurringCommit] | Omit = omit,
        add_recurring_credits: Iterable[contract_edit_params.AddRecurringCredit] | Omit = omit,
        add_reseller_royalties: Iterable[contract_edit_params.AddResellerRoyalty] | Omit = omit,
        add_scheduled_charges: Iterable[contract_edit_params.AddScheduledCharge] | Omit = omit,
        add_spend_threshold_configuration: SpendThresholdConfigurationV2 | Omit = omit,
        add_subscriptions: Iterable[contract_edit_params.AddSubscription] | Omit = omit,
        allow_contract_ending_before_finalized_invoice: bool | Omit = omit,
        archive_commits: Iterable[contract_edit_params.ArchiveCommit] | Omit = omit,
        archive_credits: Iterable[contract_edit_params.ArchiveCredit] | Omit = omit,
        archive_scheduled_charges: Iterable[contract_edit_params.ArchiveScheduledCharge] | Omit = omit,
        remove_overrides: Iterable[contract_edit_params.RemoveOverride] | Omit = omit,
        uniqueness_key: str | Omit = omit,
        update_commits: Iterable[contract_edit_params.UpdateCommit] | Omit = omit,
        update_contract_end_date: Union[str, datetime, None] | Omit = omit,
        update_contract_name: Optional[str] | Omit = omit,
        update_credits: Iterable[contract_edit_params.UpdateCredit] | Omit = omit,
        update_prepaid_balance_threshold_configuration: contract_edit_params.UpdatePrepaidBalanceThresholdConfiguration
        | Omit = omit,
        update_recurring_commits: Iterable[contract_edit_params.UpdateRecurringCommit] | Omit = omit,
        update_recurring_credits: Iterable[contract_edit_params.UpdateRecurringCredit] | Omit = omit,
        update_scheduled_charges: Iterable[contract_edit_params.UpdateScheduledCharge] | Omit = omit,
        update_spend_threshold_configuration: contract_edit_params.UpdateSpendThresholdConfiguration | Omit = omit,
        update_subscriptions: Iterable[contract_edit_params.UpdateSubscription] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditResponse:
        """
        The ability to edit a contract helps you react quickly to the needs of your
        customers and your business.

        ### Use this endpoint to:

        - Encode mid-term commitment and discount changes
        - Fix configuration mistakes and easily roll back packaging changes

        ### Key response fields:

        - The `id` of the edit
        - Complete edit details. For example, if you edited the contract to add new
          overrides and credits, you will receive the IDs of those overrides and credits
          in the response.

        ### Usage guidelines:

        - When you edit a contract, any draft invoices update immediately to reflect
          that edit. Finalized invoices remain unchanged - you must void and regenerate
          them in the UI or API to reflect the edit.
        - Contract editing must be enabled to use this endpoint. Reach out to your
          Metronome representative to learn more.

        Args:
          contract_id: ID of the contract being edited

          customer_id: ID of the customer whose contract is being edited

          add_billing_provider_configuration_update: Update the billing provider configuration on the contract. Currently only
              supports adding a billing provider configuration to a contract that does not
              already have one.

          add_professional_services: This field's availability is dependent on your client's configuration.

          add_subscriptions: Optional list of
              [subscriptions](https://docs.metronome.com/manage-product-access/create-subscription/)
              to add to the contract.

          allow_contract_ending_before_finalized_invoice: If true, allows setting the contract end date earlier than the end_timestamp of
              existing finalized invoices. Finalized invoices will be unchanged; if you want
              to incorporate the new end date, you can void and regenerate finalized usage
              invoices. Defaults to true.

          archive_commits: IDs of commits to archive

          archive_credits: IDs of credits to archive

          archive_scheduled_charges: IDs of scheduled charges to archive

          remove_overrides: IDs of overrides to remove

          uniqueness_key: Optional uniqueness key to prevent duplicate contract edits.

          update_contract_end_date: RFC 3339 timestamp indicating when the contract will end (exclusive).

          update_contract_name: Value to update the contract name to. If not provided, the contract name will
              remain unchanged.

          update_recurring_commits: Edits to these recurring commits will only affect commits whose access schedules
              has not started. Expired commits, and commits with an active access schedule
              will remain unchanged.

          update_recurring_credits: Edits to these recurring credits will only affect credits whose access schedules
              has not started. Expired credits, and credits with an active access schedule
              will remain unchanged.

          update_subscriptions: Optional list of subscriptions to update.

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
                    "add_billing_provider_configuration_update": add_billing_provider_configuration_update,
                    "add_commits": add_commits,
                    "add_credits": add_credits,
                    "add_discounts": add_discounts,
                    "add_overrides": add_overrides,
                    "add_prepaid_balance_threshold_configuration": add_prepaid_balance_threshold_configuration,
                    "add_professional_services": add_professional_services,
                    "add_recurring_commits": add_recurring_commits,
                    "add_recurring_credits": add_recurring_credits,
                    "add_reseller_royalties": add_reseller_royalties,
                    "add_scheduled_charges": add_scheduled_charges,
                    "add_spend_threshold_configuration": add_spend_threshold_configuration,
                    "add_subscriptions": add_subscriptions,
                    "allow_contract_ending_before_finalized_invoice": allow_contract_ending_before_finalized_invoice,
                    "archive_commits": archive_commits,
                    "archive_credits": archive_credits,
                    "archive_scheduled_charges": archive_scheduled_charges,
                    "remove_overrides": remove_overrides,
                    "uniqueness_key": uniqueness_key,
                    "update_commits": update_commits,
                    "update_contract_end_date": update_contract_end_date,
                    "update_contract_name": update_contract_name,
                    "update_credits": update_credits,
                    "update_prepaid_balance_threshold_configuration": update_prepaid_balance_threshold_configuration,
                    "update_recurring_commits": update_recurring_commits,
                    "update_recurring_credits": update_recurring_credits,
                    "update_scheduled_charges": update_scheduled_charges,
                    "update_spend_threshold_configuration": update_spend_threshold_configuration,
                    "update_subscriptions": update_subscriptions,
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
        access_schedule: contract_edit_commit_params.AccessSchedule | Omit = omit,
        applicable_product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        applicable_product_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        description: str | Omit = omit,
        hierarchy_configuration: CommitHierarchyConfiguration | Omit = omit,
        invoice_contract_id: str | Omit = omit,
        invoice_schedule: contract_edit_commit_params.InvoiceSchedule | Omit = omit,
        name: str | Omit = omit,
        priority: Optional[float] | Omit = omit,
        product_id: str | Omit = omit,
        rate_type: Literal["LIST_RATE", "COMMIT_RATE"] | Omit = omit,
        specifiers: Optional[Iterable[CommitSpecifierInput]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditCommitResponse:
        """Edit specific details for a contract-level or customer-level commit.

        Use this
        endpoint to modify individual commit access schedules, invoice schedules,
        applicable products, invoicing contracts, or other fields.

        ### Usage guidelines:

        - As with all edits in Metronome, draft invoices will reflect the edit
          immediately, while finalized invoices are untouched unless voided and
          regenerated.
        - If a commit's invoice schedule item is associated with a finalized invoice,
          you cannot remove or update the invoice schedule item.
        - If a commit's invoice schedule item is associated with a voided invoice, you
          cannot remove the invoice schedule item.
        - You cannot remove an commit access schedule segment that was applied to a
          finalized invoice. You can void the invoice beforehand and then remove the
          access schedule segment.

        Args:
          commit_id: ID of the commit to edit

          customer_id: ID of the customer whose commit is being edited

          applicable_product_ids: Which products the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          applicable_product_tags: Which tags the commit applies to. If applicable_product_ids,
              applicable_product_tags or specifiers are not provided, the commit applies to
              all products.

          description: Updated description for the commit

          hierarchy_configuration: Optional configuration for commit hierarchy access control

          invoice_contract_id: ID of contract to use for invoicing

          name: Updated name for the commit

          priority: If multiple commits are applicable, the one with the lower priority will apply
              first.

          rate_type: If provided, updates the commit to use the specified rate type for current and
              future invoices. Previously finalized invoices will need to be voided and
              regenerated to reflect the rate type change.

          specifiers: List of filters that determine what kind of customer usage draws down a commit
              or credit. A customer's usage needs to meet the condition of at least one of the
              specifiers to contribute to a commit's or credit's drawdown. This field cannot
              be used together with `applicable_product_ids` or `applicable_product_tags`.
              Instead, to target usage by product or product tag, pass those values in the
              body of `specifiers`.

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
                    "description": description,
                    "hierarchy_configuration": hierarchy_configuration,
                    "invoice_contract_id": invoice_contract_id,
                    "invoice_schedule": invoice_schedule,
                    "name": name,
                    "priority": priority,
                    "product_id": product_id,
                    "rate_type": rate_type,
                    "specifiers": specifiers,
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
        access_schedule: contract_edit_credit_params.AccessSchedule | Omit = omit,
        applicable_product_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        applicable_product_tags: Optional[SequenceNotStr[str]] | Omit = omit,
        description: str | Omit = omit,
        hierarchy_configuration: CommitHierarchyConfiguration | Omit = omit,
        name: str | Omit = omit,
        priority: Optional[float] | Omit = omit,
        product_id: str | Omit = omit,
        rate_type: Literal["LIST_RATE", "COMMIT_RATE"] | Omit = omit,
        specifiers: Optional[Iterable[CommitSpecifierInput]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractEditCreditResponse:
        """
        Edit details for a contract-level or customer-level credit.

        ### Use this endpoint to:

        - Extend the duration or the amount of an existing free credit like a trial
        - Modify individual credit access schedules, applicable products, priority, or
          other fields.

        ### Usage guidelines:

        - As with all edits in Metronome, draft invoices will reflect the edit
          immediately, while finalized invoices are untouched unless voided and
          regenerated.
        - You cannot remove an access schedule segment that was applied to a finalized
          invoice. You can void the invoice beforehand and then remove the access
          schedule segment.

        Args:
          credit_id: ID of the credit to edit

          customer_id: ID of the customer whose credit is being edited

          applicable_product_ids: Which products the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          applicable_product_tags: Which tags the credit applies to. If both applicable_product_ids and
              applicable_product_tags are not provided, the credit applies to all products.

          description: Updated description for the credit

          hierarchy_configuration: Optional configuration for credit hierarchy access control

          name: Updated name for the credit

          priority: If multiple commits are applicable, the one with the lower priority will apply
              first.

          rate_type: If provided, updates the credit to use the specified rate type for current and
              future invoices. Previously finalized invoices will need to be voided and
              regenerated to reflect the rate type change.

          specifiers: List of filters that determine what kind of customer usage draws down a commit
              or credit. A customer's usage needs to meet the condition of at least one of the
              specifiers to contribute to a commit's or credit's drawdown. This field cannot
              be used together with `applicable_product_ids` or `applicable_product_tags`.
              Instead, to target usage by product or product tag, pass those values in the
              body of `specifiers`.

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
                    "description": description,
                    "hierarchy_configuration": hierarchy_configuration,
                    "name": name,
                    "priority": priority,
                    "product_id": product_id,
                    "rate_type": rate_type,
                    "specifiers": specifiers,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractGetEditHistoryResponse:
        """List all the edits made to a contract over time.

        In Metronome, you can edit a
        contract at any point after it's created to fix mistakes or reflect changes in
        terms. Metronome stores a full history of all edits that were ever made to a
        contract, whether through the UI, `editContract` endpoint, or other endpoints
        like `updateContractEndDate`.

        ### Use this endpoint to:

        - Understand what changes were made to a contract, when, and by who

        ### Key response fields:

        - An array of every edit ever made to the contract
        - Details on each individual edit - for example showing that in one edit, a user
          added two discounts and incremented a subscription quantity.

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
