# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v1.contracts import (
    product_list_params,
    product_create_params,
    product_update_params,
    product_archive_params,
    product_retrieve_params,
)
from ....types.v1.contracts.product_list_response import ProductListResponse
from ....types.v1.contracts.product_create_response import ProductCreateResponse
from ....types.v1.contracts.product_update_response import ProductUpdateResponse
from ....types.v1.contracts.quantity_rounding_param import QuantityRoundingParam
from ....types.v1.contracts.product_archive_response import ProductArchiveResponse
from ....types.v1.contracts.product_retrieve_response import ProductRetrieveResponse
from ....types.v1.contracts.quantity_conversion_param import QuantityConversionParam

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        type: Literal["FIXED", "USAGE", "COMPOSITE", "SUBSCRIPTION", "PROFESSIONAL_SERVICE", "PRO_SERVICE"],
        billable_metric_id: str | NotGiven = NOT_GIVEN,
        composite_product_ids: List[str] | NotGiven = NOT_GIVEN,
        composite_tags: List[str] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        exclude_free_usage: bool | NotGiven = NOT_GIVEN,
        is_refundable: bool | NotGiven = NOT_GIVEN,
        netsuite_internal_item_id: str | NotGiven = NOT_GIVEN,
        netsuite_overage_item_id: str | NotGiven = NOT_GIVEN,
        presentation_group_key: List[str] | NotGiven = NOT_GIVEN,
        pricing_group_key: List[str] | NotGiven = NOT_GIVEN,
        quantity_conversion: Optional[QuantityConversionParam] | NotGiven = NOT_GIVEN,
        quantity_rounding: Optional[QuantityRoundingParam] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductCreateResponse:
        """
        Create a new product

        Args:
          name: displayed on invoices

          billable_metric_id: Required for USAGE products

          composite_product_ids: Required for COMPOSITE products

          composite_tags: Required for COMPOSITE products

          exclude_free_usage: Beta feature only available for composite products. If true, products with $0
              will not be included when computing composite usage. Defaults to false

          is_refundable: This field's availability is dependent on your client's configuration. Defaults
              to true.

          netsuite_internal_item_id: This field's availability is dependent on your client's configuration.

          netsuite_overage_item_id: This field's availability is dependent on your client's configuration.

          presentation_group_key: For USAGE products only. Groups usage line items on invoices. The superset of
              values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          pricing_group_key: For USAGE products only. If set, pricing for this product will be determined for
              each pricing_group_key value, as opposed to the product as a whole. The superset
              of values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          quantity_conversion: Optional. Only valid for USAGE products. If provided, the quantity will be
              converted using the provided conversion factor and operation. For example, if
              the operation is "multiply" and the conversion factor is 100, then the quantity
              will be multiplied by 100. This can be used in cases where data is sent in one
              unit and priced in another. For example, data could be sent in MB and priced in
              GB. In this case, the conversion factor would be 1024 and the operation would be
              "divide".

          quantity_rounding: Optional. Only valid for USAGE products. If provided, the quantity will be
              rounded using the provided rounding method and decimal places. For example, if
              the method is "round up" and the decimal places is 0, then the quantity will be
              rounded up to the nearest integer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/products/create",
            body=maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "billable_metric_id": billable_metric_id,
                    "composite_product_ids": composite_product_ids,
                    "composite_tags": composite_tags,
                    "custom_fields": custom_fields,
                    "exclude_free_usage": exclude_free_usage,
                    "is_refundable": is_refundable,
                    "netsuite_internal_item_id": netsuite_internal_item_id,
                    "netsuite_overage_item_id": netsuite_overage_item_id,
                    "presentation_group_key": presentation_group_key,
                    "pricing_group_key": pricing_group_key,
                    "quantity_conversion": quantity_conversion,
                    "quantity_rounding": quantity_rounding,
                    "tags": tags,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCreateResponse,
        )

    def retrieve(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductRetrieveResponse:
        """
        Get a specific product

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/products/get",
            body=maybe_transform({"id": id}, product_retrieve_params.ProductRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRetrieveResponse,
        )

    def update(
        self,
        *,
        product_id: str,
        starting_at: Union[str, datetime],
        billable_metric_id: str | NotGiven = NOT_GIVEN,
        composite_product_ids: List[str] | NotGiven = NOT_GIVEN,
        composite_tags: List[str] | NotGiven = NOT_GIVEN,
        exclude_free_usage: bool | NotGiven = NOT_GIVEN,
        is_refundable: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        netsuite_internal_item_id: str | NotGiven = NOT_GIVEN,
        netsuite_overage_item_id: str | NotGiven = NOT_GIVEN,
        presentation_group_key: List[str] | NotGiven = NOT_GIVEN,
        pricing_group_key: List[str] | NotGiven = NOT_GIVEN,
        quantity_conversion: Optional[QuantityConversionParam] | NotGiven = NOT_GIVEN,
        quantity_rounding: Optional[QuantityRoundingParam] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductUpdateResponse:
        """
        Update a product

        Args:
          product_id: ID of the product to update

          starting_at: Timestamp representing when the update should go into effect. It must be on an
              hour boundary (e.g. 1:00, not 1:30).

          billable_metric_id: Available for USAGE products only. If not provided, defaults to product's
              current billable metric.

          composite_product_ids: Available for COMPOSITE products only. If not provided, defaults to product's
              current composite_product_ids.

          composite_tags: Available for COMPOSITE products only. If not provided, defaults to product's
              current composite_tags.

          exclude_free_usage: Beta feature only available for composite products. If true, products with $0
              will not be included when computing composite usage. Defaults to false

          is_refundable: Defaults to product's current refundability status. This field's availability is
              dependent on your client's configuration.

          name: displayed on invoices. If not provided, defaults to product's current name.

          netsuite_internal_item_id: If not provided, defaults to product's current netsuite_internal_item_id. This
              field's availability is dependent on your client's configuration.

          netsuite_overage_item_id: Available for USAGE and COMPOSITE products only. If not provided, defaults to
              product's current netsuite_overage_item_id. This field's availability is
              dependent on your client's configuration.

          presentation_group_key: For USAGE products only. Groups usage line items on invoices. The superset of
              values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          pricing_group_key: For USAGE products only. If set, pricing for this product will be determined for
              each pricing_group_key value, as opposed to the product as a whole. The superset
              of values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          quantity_conversion: Optional. Only valid for USAGE products. If provided, the quantity will be
              converted using the provided conversion factor and operation. For example, if
              the operation is "multiply" and the conversion factor is 100, then the quantity
              will be multiplied by 100. This can be used in cases where data is sent in one
              unit and priced in another. For example, data could be sent in MB and priced in
              GB. In this case, the conversion factor would be 1024 and the operation would be
              "divide".

          quantity_rounding: Optional. Only valid for USAGE products. If provided, the quantity will be
              rounded using the provided rounding method and decimal places. For example, if
              the method is "round up" and the decimal places is 0, then the quantity will be
              rounded up to the nearest integer.

          tags: If not provided, defaults to product's current tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/products/update",
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "starting_at": starting_at,
                    "billable_metric_id": billable_metric_id,
                    "composite_product_ids": composite_product_ids,
                    "composite_tags": composite_tags,
                    "exclude_free_usage": exclude_free_usage,
                    "is_refundable": is_refundable,
                    "name": name,
                    "netsuite_internal_item_id": netsuite_internal_item_id,
                    "netsuite_overage_item_id": netsuite_overage_item_id,
                    "presentation_group_key": presentation_group_key,
                    "pricing_group_key": pricing_group_key,
                    "quantity_conversion": quantity_conversion,
                    "quantity_rounding": quantity_rounding,
                    "tags": tags,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[ProductListResponse]:
        """
        List products

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          archive_filter: Filter options for the product list. If not provided, defaults to not archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contract-pricing/products/list",
            page=SyncCursorPage[ProductListResponse],
            body=maybe_transform({"archive_filter": archive_filter}, product_list_params.ProductListParams),
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
                    product_list_params.ProductListParams,
                ),
            ),
            model=ProductListResponse,
            method="post",
        )

    def archive(
        self,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductArchiveResponse:
        """
        Archive a product

        Args:
          product_id: ID of the product to be archived

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/contract-pricing/products/archive",
            body=maybe_transform({"product_id": product_id}, product_archive_params.ProductArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductArchiveResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        type: Literal["FIXED", "USAGE", "COMPOSITE", "SUBSCRIPTION", "PROFESSIONAL_SERVICE", "PRO_SERVICE"],
        billable_metric_id: str | NotGiven = NOT_GIVEN,
        composite_product_ids: List[str] | NotGiven = NOT_GIVEN,
        composite_tags: List[str] | NotGiven = NOT_GIVEN,
        custom_fields: Dict[str, str] | NotGiven = NOT_GIVEN,
        exclude_free_usage: bool | NotGiven = NOT_GIVEN,
        is_refundable: bool | NotGiven = NOT_GIVEN,
        netsuite_internal_item_id: str | NotGiven = NOT_GIVEN,
        netsuite_overage_item_id: str | NotGiven = NOT_GIVEN,
        presentation_group_key: List[str] | NotGiven = NOT_GIVEN,
        pricing_group_key: List[str] | NotGiven = NOT_GIVEN,
        quantity_conversion: Optional[QuantityConversionParam] | NotGiven = NOT_GIVEN,
        quantity_rounding: Optional[QuantityRoundingParam] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductCreateResponse:
        """
        Create a new product

        Args:
          name: displayed on invoices

          billable_metric_id: Required for USAGE products

          composite_product_ids: Required for COMPOSITE products

          composite_tags: Required for COMPOSITE products

          exclude_free_usage: Beta feature only available for composite products. If true, products with $0
              will not be included when computing composite usage. Defaults to false

          is_refundable: This field's availability is dependent on your client's configuration. Defaults
              to true.

          netsuite_internal_item_id: This field's availability is dependent on your client's configuration.

          netsuite_overage_item_id: This field's availability is dependent on your client's configuration.

          presentation_group_key: For USAGE products only. Groups usage line items on invoices. The superset of
              values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          pricing_group_key: For USAGE products only. If set, pricing for this product will be determined for
              each pricing_group_key value, as opposed to the product as a whole. The superset
              of values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          quantity_conversion: Optional. Only valid for USAGE products. If provided, the quantity will be
              converted using the provided conversion factor and operation. For example, if
              the operation is "multiply" and the conversion factor is 100, then the quantity
              will be multiplied by 100. This can be used in cases where data is sent in one
              unit and priced in another. For example, data could be sent in MB and priced in
              GB. In this case, the conversion factor would be 1024 and the operation would be
              "divide".

          quantity_rounding: Optional. Only valid for USAGE products. If provided, the quantity will be
              rounded using the provided rounding method and decimal places. For example, if
              the method is "round up" and the decimal places is 0, then the quantity will be
              rounded up to the nearest integer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/products/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "type": type,
                    "billable_metric_id": billable_metric_id,
                    "composite_product_ids": composite_product_ids,
                    "composite_tags": composite_tags,
                    "custom_fields": custom_fields,
                    "exclude_free_usage": exclude_free_usage,
                    "is_refundable": is_refundable,
                    "netsuite_internal_item_id": netsuite_internal_item_id,
                    "netsuite_overage_item_id": netsuite_overage_item_id,
                    "presentation_group_key": presentation_group_key,
                    "pricing_group_key": pricing_group_key,
                    "quantity_conversion": quantity_conversion,
                    "quantity_rounding": quantity_rounding,
                    "tags": tags,
                },
                product_create_params.ProductCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductCreateResponse,
        )

    async def retrieve(
        self,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductRetrieveResponse:
        """
        Get a specific product

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/products/get",
            body=await async_maybe_transform({"id": id}, product_retrieve_params.ProductRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRetrieveResponse,
        )

    async def update(
        self,
        *,
        product_id: str,
        starting_at: Union[str, datetime],
        billable_metric_id: str | NotGiven = NOT_GIVEN,
        composite_product_ids: List[str] | NotGiven = NOT_GIVEN,
        composite_tags: List[str] | NotGiven = NOT_GIVEN,
        exclude_free_usage: bool | NotGiven = NOT_GIVEN,
        is_refundable: bool | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        netsuite_internal_item_id: str | NotGiven = NOT_GIVEN,
        netsuite_overage_item_id: str | NotGiven = NOT_GIVEN,
        presentation_group_key: List[str] | NotGiven = NOT_GIVEN,
        pricing_group_key: List[str] | NotGiven = NOT_GIVEN,
        quantity_conversion: Optional[QuantityConversionParam] | NotGiven = NOT_GIVEN,
        quantity_rounding: Optional[QuantityRoundingParam] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductUpdateResponse:
        """
        Update a product

        Args:
          product_id: ID of the product to update

          starting_at: Timestamp representing when the update should go into effect. It must be on an
              hour boundary (e.g. 1:00, not 1:30).

          billable_metric_id: Available for USAGE products only. If not provided, defaults to product's
              current billable metric.

          composite_product_ids: Available for COMPOSITE products only. If not provided, defaults to product's
              current composite_product_ids.

          composite_tags: Available for COMPOSITE products only. If not provided, defaults to product's
              current composite_tags.

          exclude_free_usage: Beta feature only available for composite products. If true, products with $0
              will not be included when computing composite usage. Defaults to false

          is_refundable: Defaults to product's current refundability status. This field's availability is
              dependent on your client's configuration.

          name: displayed on invoices. If not provided, defaults to product's current name.

          netsuite_internal_item_id: If not provided, defaults to product's current netsuite_internal_item_id. This
              field's availability is dependent on your client's configuration.

          netsuite_overage_item_id: Available for USAGE and COMPOSITE products only. If not provided, defaults to
              product's current netsuite_overage_item_id. This field's availability is
              dependent on your client's configuration.

          presentation_group_key: For USAGE products only. Groups usage line items on invoices. The superset of
              values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          pricing_group_key: For USAGE products only. If set, pricing for this product will be determined for
              each pricing_group_key value, as opposed to the product as a whole. The superset
              of values in the pricing group key and presentation group key must be set as one
              compound group key on the billable metric.

          quantity_conversion: Optional. Only valid for USAGE products. If provided, the quantity will be
              converted using the provided conversion factor and operation. For example, if
              the operation is "multiply" and the conversion factor is 100, then the quantity
              will be multiplied by 100. This can be used in cases where data is sent in one
              unit and priced in another. For example, data could be sent in MB and priced in
              GB. In this case, the conversion factor would be 1024 and the operation would be
              "divide".

          quantity_rounding: Optional. Only valid for USAGE products. If provided, the quantity will be
              rounded using the provided rounding method and decimal places. For example, if
              the method is "round up" and the decimal places is 0, then the quantity will be
              rounded up to the nearest integer.

          tags: If not provided, defaults to product's current tags

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/products/update",
            body=await async_maybe_transform(
                {
                    "product_id": product_id,
                    "starting_at": starting_at,
                    "billable_metric_id": billable_metric_id,
                    "composite_product_ids": composite_product_ids,
                    "composite_tags": composite_tags,
                    "exclude_free_usage": exclude_free_usage,
                    "is_refundable": is_refundable,
                    "name": name,
                    "netsuite_internal_item_id": netsuite_internal_item_id,
                    "netsuite_overage_item_id": netsuite_overage_item_id,
                    "presentation_group_key": presentation_group_key,
                    "pricing_group_key": pricing_group_key,
                    "quantity_conversion": quantity_conversion,
                    "quantity_rounding": quantity_rounding,
                    "tags": tags,
                },
                product_update_params.ProductUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductUpdateResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        next_page: str | NotGiven = NOT_GIVEN,
        archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ProductListResponse, AsyncCursorPage[ProductListResponse]]:
        """
        List products

        Args:
          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          archive_filter: Filter options for the product list. If not provided, defaults to not archived.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/contract-pricing/products/list",
            page=AsyncCursorPage[ProductListResponse],
            body=maybe_transform({"archive_filter": archive_filter}, product_list_params.ProductListParams),
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
                    product_list_params.ProductListParams,
                ),
            ),
            model=ProductListResponse,
            method="post",
        )

    async def archive(
        self,
        *,
        product_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProductArchiveResponse:
        """
        Archive a product

        Args:
          product_id: ID of the product to be archived

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/contract-pricing/products/archive",
            body=await async_maybe_transform({"product_id": product_id}, product_archive_params.ProductArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductArchiveResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = to_raw_response_wrapper(
            products.update,
        )
        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.archive = to_raw_response_wrapper(
            products.archive,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_raw_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            products.update,
        )
        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.archive = async_to_raw_response_wrapper(
            products.archive,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.create = to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            products.update,
        )
        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.archive = to_streamed_response_wrapper(
            products.archive,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.create = async_to_streamed_response_wrapper(
            products.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            products.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            products.update,
        )
        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            products.archive,
        )
