# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

from ..types import package_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.package_create_response import PackageCreateResponse
from ..types.shared_params.spend_threshold_configuration import SpendThresholdConfiguration
from ..types.shared_params.prepaid_balance_threshold_configuration import PrepaidBalanceThresholdConfiguration

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
        billing_anchor_date: Literal["contract_start_date", "first_billing_period"] | Omit = omit,
        billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]
        | Omit = omit,
        commits: Iterable[package_create_params.Commit] | Omit = omit,
        contract_name: str | Omit = omit,
        credits: Iterable[package_create_params.Credit] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"] | Omit = omit,
        duration: package_create_params.Duration | Omit = omit,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        overrides: Iterable[package_create_params.Override] | Omit = omit,
        prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfiguration | Omit = omit,
        priority: float | Omit = omit,
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
        """Create a new package

        Args:
          custom_fields: Custom fields to be added eg.

        { "key1": "value1", "key2": "value2" }

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          priority: Priority of the generated contract.

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
                    "billing_anchor_date": billing_anchor_date,
                    "billing_provider": billing_provider,
                    "commits": commits,
                    "contract_name": contract_name,
                    "credits": credits,
                    "custom_fields": custom_fields,
                    "delivery_method": delivery_method,
                    "duration": duration,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "net_payment_terms_days": net_payment_terms_days,
                    "overrides": overrides,
                    "prepaid_balance_threshold_configuration": prepaid_balance_threshold_configuration,
                    "priority": priority,
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
        billing_anchor_date: Literal["contract_start_date", "first_billing_period"] | Omit = omit,
        billing_provider: Literal["aws_marketplace", "azure_marketplace", "gcp_marketplace", "stripe", "netsuite"]
        | Omit = omit,
        commits: Iterable[package_create_params.Commit] | Omit = omit,
        contract_name: str | Omit = omit,
        credits: Iterable[package_create_params.Credit] | Omit = omit,
        custom_fields: Dict[str, str] | Omit = omit,
        delivery_method: Literal["direct_to_billing_provider", "aws_sqs", "tackle", "aws_sns"] | Omit = omit,
        duration: package_create_params.Duration | Omit = omit,
        multiplier_override_prioritization: Literal["LOWEST_MULTIPLIER", "EXPLICIT"] | Omit = omit,
        net_payment_terms_days: float | Omit = omit,
        overrides: Iterable[package_create_params.Override] | Omit = omit,
        prepaid_balance_threshold_configuration: PrepaidBalanceThresholdConfiguration | Omit = omit,
        priority: float | Omit = omit,
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
        """Create a new package

        Args:
          custom_fields: Custom fields to be added eg.

        { "key1": "value1", "key2": "value2" }

          multiplier_override_prioritization: Defaults to LOWEST_MULTIPLIER, which applies the greatest discount to list
              prices automatically. EXPLICIT prioritization requires specifying priorities for
              each multiplier; the one with the lowest priority value will be prioritized
              first. If tiered overrides are used, prioritization must be explicit.

          priority: Priority of the generated contract.

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
                    "billing_anchor_date": billing_anchor_date,
                    "billing_provider": billing_provider,
                    "commits": commits,
                    "contract_name": contract_name,
                    "credits": credits,
                    "custom_fields": custom_fields,
                    "delivery_method": delivery_method,
                    "duration": duration,
                    "multiplier_override_prioritization": multiplier_override_prioritization,
                    "net_payment_terms_days": net_payment_terms_days,
                    "overrides": overrides,
                    "prepaid_balance_threshold_configuration": prepaid_balance_threshold_configuration,
                    "priority": priority,
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


class PackagesResourceWithRawResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.create = to_raw_response_wrapper(
            packages.create,
        )


class AsyncPackagesResourceWithRawResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.create = async_to_raw_response_wrapper(
            packages.create,
        )


class PackagesResourceWithStreamingResponse:
    def __init__(self, packages: PackagesResource) -> None:
        self._packages = packages

        self.create = to_streamed_response_wrapper(
            packages.create,
        )


class AsyncPackagesResourceWithStreamingResponse:
    def __init__(self, packages: AsyncPackagesResource) -> None:
        self._packages = packages

        self.create = async_to_streamed_response_wrapper(
            packages.create,
        )
