# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.customers import billing_config_create_params
from ...types.customers.billing_config_retrieve_response import BillingConfigRetrieveResponse

__all__ = ["BillingConfigResource", "AsyncBillingConfigResource"]


class BillingConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BillingConfigResourceWithRawResponse:
        return BillingConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingConfigResourceWithStreamingResponse:
        return BillingConfigResourceWithStreamingResponse(self)

    def create(
        self,
        billing_provider_type: Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
        ],
        *,
        customer_id: str,
        billing_provider_customer_id: str,
        aws_product_code: str | NotGiven = NOT_GIVEN,
        aws_region: Literal[
            "af-south-1",
            "ap-east-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "cn-north-1",
            "cn-northwest-1",
            "eu-central-1",
            "eu-north-1",
            "eu-south-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "me-south-1",
            "sa-east-1",
            "us-east-1",
            "us-east-2",
            "us-gov-east-1",
            "us-gov-west-1",
            "us-west-1",
            "us-west-2",
        ]
        | NotGiven = NOT_GIVEN,
        stripe_collection_method: Literal["charge_automatically", "send_invoice"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Set the billing configuration for a given customer.

        Args:
          billing_provider_customer_id: The customer ID in the billing provider's system. For Azure, this is the
              subscription ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not billing_provider_type:
            raise ValueError(
                f"Expected a non-empty value for `billing_provider_type` but received {billing_provider_type!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/customers/{customer_id}/billing-config/{billing_provider_type}",
            body=maybe_transform(
                {
                    "billing_provider_customer_id": billing_provider_customer_id,
                    "aws_product_code": aws_product_code,
                    "aws_region": aws_region,
                    "stripe_collection_method": stripe_collection_method,
                },
                billing_config_create_params.BillingConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        billing_provider_type: Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
        ],
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingConfigRetrieveResponse:
        """
        Fetch the billing configuration for the given customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not billing_provider_type:
            raise ValueError(
                f"Expected a non-empty value for `billing_provider_type` but received {billing_provider_type!r}"
            )
        return self._get(
            f"/customers/{customer_id}/billing-config/{billing_provider_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingConfigRetrieveResponse,
        )

    def delete(
        self,
        billing_provider_type: Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
        ],
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete the billing configuration for a given customer.

        Note: this is unsupported
        for Azure and AWS Marketplace customers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not billing_provider_type:
            raise ValueError(
                f"Expected a non-empty value for `billing_provider_type` but received {billing_provider_type!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/customers/{customer_id}/billing-config/{billing_provider_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBillingConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBillingConfigResourceWithRawResponse:
        return AsyncBillingConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingConfigResourceWithStreamingResponse:
        return AsyncBillingConfigResourceWithStreamingResponse(self)

    async def create(
        self,
        billing_provider_type: Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
        ],
        *,
        customer_id: str,
        billing_provider_customer_id: str,
        aws_product_code: str | NotGiven = NOT_GIVEN,
        aws_region: Literal[
            "af-south-1",
            "ap-east-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "ap-south-1",
            "ap-southeast-1",
            "ap-southeast-2",
            "ca-central-1",
            "cn-north-1",
            "cn-northwest-1",
            "eu-central-1",
            "eu-north-1",
            "eu-south-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "me-south-1",
            "sa-east-1",
            "us-east-1",
            "us-east-2",
            "us-gov-east-1",
            "us-gov-west-1",
            "us-west-1",
            "us-west-2",
        ]
        | NotGiven = NOT_GIVEN,
        stripe_collection_method: Literal["charge_automatically", "send_invoice"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Set the billing configuration for a given customer.

        Args:
          billing_provider_customer_id: The customer ID in the billing provider's system. For Azure, this is the
              subscription ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not billing_provider_type:
            raise ValueError(
                f"Expected a non-empty value for `billing_provider_type` but received {billing_provider_type!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/customers/{customer_id}/billing-config/{billing_provider_type}",
            body=await async_maybe_transform(
                {
                    "billing_provider_customer_id": billing_provider_customer_id,
                    "aws_product_code": aws_product_code,
                    "aws_region": aws_region,
                    "stripe_collection_method": stripe_collection_method,
                },
                billing_config_create_params.BillingConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        billing_provider_type: Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
        ],
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BillingConfigRetrieveResponse:
        """
        Fetch the billing configuration for the given customer.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not billing_provider_type:
            raise ValueError(
                f"Expected a non-empty value for `billing_provider_type` but received {billing_provider_type!r}"
            )
        return await self._get(
            f"/customers/{customer_id}/billing-config/{billing_provider_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BillingConfigRetrieveResponse,
        )

    async def delete(
        self,
        billing_provider_type: Literal[
            "aws_marketplace",
            "stripe",
            "netsuite",
            "custom",
            "azure_marketplace",
            "quickbooks_online",
            "workday",
            "gcp_marketplace",
        ],
        *,
        customer_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Delete the billing configuration for a given customer.

        Note: this is unsupported
        for Azure and AWS Marketplace customers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not customer_id:
            raise ValueError(f"Expected a non-empty value for `customer_id` but received {customer_id!r}")
        if not billing_provider_type:
            raise ValueError(
                f"Expected a non-empty value for `billing_provider_type` but received {billing_provider_type!r}"
            )
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/customers/{customer_id}/billing-config/{billing_provider_type}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BillingConfigResourceWithRawResponse:
    def __init__(self, billing_config: BillingConfigResource) -> None:
        self._billing_config = billing_config

        self.create = to_raw_response_wrapper(
            billing_config.create,
        )
        self.retrieve = to_raw_response_wrapper(
            billing_config.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            billing_config.delete,
        )


class AsyncBillingConfigResourceWithRawResponse:
    def __init__(self, billing_config: AsyncBillingConfigResource) -> None:
        self._billing_config = billing_config

        self.create = async_to_raw_response_wrapper(
            billing_config.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            billing_config.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            billing_config.delete,
        )


class BillingConfigResourceWithStreamingResponse:
    def __init__(self, billing_config: BillingConfigResource) -> None:
        self._billing_config = billing_config

        self.create = to_streamed_response_wrapper(
            billing_config.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            billing_config.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            billing_config.delete,
        )


class AsyncBillingConfigResourceWithStreamingResponse:
    def __init__(self, billing_config: AsyncBillingConfigResource) -> None:
        self._billing_config = billing_config

        self.create = async_to_streamed_response_wrapper(
            billing_config.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            billing_config.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            billing_config.delete,
        )
