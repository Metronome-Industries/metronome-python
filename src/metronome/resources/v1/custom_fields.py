# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import (
    custom_field_add_key_params,
    custom_field_list_keys_params,
    custom_field_remove_key_params,
    custom_field_set_values_params,
    custom_field_delete_values_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPageWithoutLimit, AsyncCursorPageWithoutLimit
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.custom_field_list_keys_response import CustomFieldListKeysResponse

__all__ = ["CustomFieldsResource", "AsyncCustomFieldsResource"]


class CustomFieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return CustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return CustomFieldsResourceWithStreamingResponse(self)

    def add_key(
        self,
        *,
        enforce_uniqueness: bool,
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates a new custom field key for a given entity (e.g.

        billable metric,
        contract, alert).

        Custom fields are properties that you can add to Metronome objects to store
        metadata like foreign keys or other descriptors. This metadata can get
        transferred to or accessed by other systems to contextualize Metronome data and
        power business processes. For example, to service workflows like revenue
        recognition, reconciliation, and invoicing, custom fields help Metronome know
        the relationship between entities in the platform and third-party systems.

        ### Use this endpoint to:

        - Create a new custom field key for Customer objects in Metronome. You can then
          use the Set Custom Field Values endpoint to set the value of this key for a
          specific customer.
        - Specify whether the key should enforce uniqueness. If the key is set to
          enforce uniqueness and you attempt to set a custom field value for the key
          that already exists, it will fail.

        ### Usage guidelines:

        - Custom fields set on commits, credits, and contracts can be used to scope
          alert evaluation. For example, you can create a spend threshold alert that
          only considers spend associated with contracts with custom field key
          `contract_type` and value `paygo`
        - Custom fields set on products can be used in the Stripe integration to set
          metadata on invoices.
        - Custom fields for customers, contracts, invoices, products, commits, scheduled
          charges, and subscriptions are passed down to the invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/customFields/addKey",
            body=maybe_transform(
                {
                    "enforce_uniqueness": enforce_uniqueness,
                    "entity": entity,
                    "key": key,
                },
                custom_field_add_key_params.CustomFieldAddKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_values(
        self,
        *,
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        entity_id: str,
        keys: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove specific custom field values from a Metronome entity instance by
        specifying the field keys to delete. Use this endpoint to clean up unwanted
        custom field data while preserving other fields on the same entity. Requires the
        entity type, entity ID, and array of keys to remove.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/customFields/deleteValues",
            body=maybe_transform(
                {
                    "entity": entity,
                    "entity_id": entity_id,
                    "keys": keys,
                },
                custom_field_delete_values_params.CustomFieldDeleteValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_keys(
        self,
        *,
        next_page: str | Omit = omit,
        entities: List[
            Literal[
                "alert",
                "billable_metric",
                "charge",
                "commit",
                "contract_credit",
                "contract_product",
                "contract",
                "credit_grant",
                "customer_plan",
                "customer",
                "discount",
                "invoice",
                "plan",
                "professional_service",
                "product",
                "rate_card",
                "scheduled_charge",
                "subscription",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPageWithoutLimit[CustomFieldListKeysResponse]:
        """
        Retrieve all your active custom field keys, with optional filtering by entity
        type (customer, contract, product, etc.). Use this endpoint to discover what
        custom field keys are available before setting values on entities or to audit
        your custom field configuration across different entity types.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

          entities: Optional list of entity types to return keys for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customFields/listKeys",
            page=SyncCursorPageWithoutLimit[CustomFieldListKeysResponse],
            body=maybe_transform({"entities": entities}, custom_field_list_keys_params.CustomFieldListKeysParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_page": next_page}, custom_field_list_keys_params.CustomFieldListKeysParams
                ),
            ),
            model=CustomFieldListKeysResponse,
            method="post",
        )

    def remove_key(
        self,
        *,
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a custom field key from the allowlist for a specific entity type,
        preventing future use of that key across all instances of the entity. Existing
        values for this key on entity instances will no longer be accessible once the
        key is removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/customFields/removeKey",
            body=maybe_transform(
                {
                    "entity": entity,
                    "key": key,
                },
                custom_field_remove_key_params.CustomFieldRemoveKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def set_values(
        self,
        *,
        custom_fields: Dict[str, str],
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets custom field values on a specific Metronome entity instance.

        Overwrites
        existing values for matching keys while preserving other fields. All updates are
        transactional—either all values are set or none are. Custom field values are
        limited to 200 characters each.

        Args:
          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/customFields/setValues",
            body=maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "entity": entity,
                    "entity_id": entity_id,
                },
                custom_field_set_values_params.CustomFieldSetValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCustomFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncCustomFieldsResourceWithStreamingResponse(self)

    async def add_key(
        self,
        *,
        enforce_uniqueness: bool,
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Creates a new custom field key for a given entity (e.g.

        billable metric,
        contract, alert).

        Custom fields are properties that you can add to Metronome objects to store
        metadata like foreign keys or other descriptors. This metadata can get
        transferred to or accessed by other systems to contextualize Metronome data and
        power business processes. For example, to service workflows like revenue
        recognition, reconciliation, and invoicing, custom fields help Metronome know
        the relationship between entities in the platform and third-party systems.

        ### Use this endpoint to:

        - Create a new custom field key for Customer objects in Metronome. You can then
          use the Set Custom Field Values endpoint to set the value of this key for a
          specific customer.
        - Specify whether the key should enforce uniqueness. If the key is set to
          enforce uniqueness and you attempt to set a custom field value for the key
          that already exists, it will fail.

        ### Usage guidelines:

        - Custom fields set on commits, credits, and contracts can be used to scope
          alert evaluation. For example, you can create a spend threshold alert that
          only considers spend associated with contracts with custom field key
          `contract_type` and value `paygo`
        - Custom fields set on products can be used in the Stripe integration to set
          metadata on invoices.
        - Custom fields for customers, contracts, invoices, products, commits, scheduled
          charges, and subscriptions are passed down to the invoice.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/customFields/addKey",
            body=await async_maybe_transform(
                {
                    "enforce_uniqueness": enforce_uniqueness,
                    "entity": entity,
                    "key": key,
                },
                custom_field_add_key_params.CustomFieldAddKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_values(
        self,
        *,
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        entity_id: str,
        keys: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove specific custom field values from a Metronome entity instance by
        specifying the field keys to delete. Use this endpoint to clean up unwanted
        custom field data while preserving other fields on the same entity. Requires the
        entity type, entity ID, and array of keys to remove.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/customFields/deleteValues",
            body=await async_maybe_transform(
                {
                    "entity": entity,
                    "entity_id": entity_id,
                    "keys": keys,
                },
                custom_field_delete_values_params.CustomFieldDeleteValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_keys(
        self,
        *,
        next_page: str | Omit = omit,
        entities: List[
            Literal[
                "alert",
                "billable_metric",
                "charge",
                "commit",
                "contract_credit",
                "contract_product",
                "contract",
                "credit_grant",
                "customer_plan",
                "customer",
                "discount",
                "invoice",
                "plan",
                "professional_service",
                "product",
                "rate_card",
                "scheduled_charge",
                "subscription",
            ]
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CustomFieldListKeysResponse, AsyncCursorPageWithoutLimit[CustomFieldListKeysResponse]]:
        """
        Retrieve all your active custom field keys, with optional filtering by entity
        type (customer, contract, product, etc.). Use this endpoint to discover what
        custom field keys are available before setting values on entities or to audit
        your custom field configuration across different entity types.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

          entities: Optional list of entity types to return keys for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/customFields/listKeys",
            page=AsyncCursorPageWithoutLimit[CustomFieldListKeysResponse],
            body=maybe_transform({"entities": entities}, custom_field_list_keys_params.CustomFieldListKeysParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"next_page": next_page}, custom_field_list_keys_params.CustomFieldListKeysParams
                ),
            ),
            model=CustomFieldListKeysResponse,
            method="post",
        )

    async def remove_key(
        self,
        *,
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        key: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a custom field key from the allowlist for a specific entity type,
        preventing future use of that key across all instances of the entity. Existing
        values for this key on entity instances will no longer be accessible once the
        key is removed.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/customFields/removeKey",
            body=await async_maybe_transform(
                {
                    "entity": entity,
                    "key": key,
                },
                custom_field_remove_key_params.CustomFieldRemoveKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def set_values(
        self,
        *,
        custom_fields: Dict[str, str],
        entity: Literal[
            "alert",
            "billable_metric",
            "charge",
            "commit",
            "contract_credit",
            "contract_product",
            "contract",
            "credit_grant",
            "customer_plan",
            "customer",
            "discount",
            "invoice",
            "plan",
            "professional_service",
            "product",
            "rate_card",
            "scheduled_charge",
            "subscription",
        ],
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Sets custom field values on a specific Metronome entity instance.

        Overwrites
        existing values for matching keys while preserving other fields. All updates are
        transactional—either all values are set or none are. Custom field values are
        limited to 200 characters each.

        Args:
          custom_fields: Custom fields to be added eg. { "key1": "value1", "key2": "value2" }

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/customFields/setValues",
            body=await async_maybe_transform(
                {
                    "custom_fields": custom_fields,
                    "entity": entity,
                    "entity_id": entity_id,
                },
                custom_field_set_values_params.CustomFieldSetValuesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.add_key = to_raw_response_wrapper(
            custom_fields.add_key,
        )
        self.delete_values = to_raw_response_wrapper(
            custom_fields.delete_values,
        )
        self.list_keys = to_raw_response_wrapper(
            custom_fields.list_keys,
        )
        self.remove_key = to_raw_response_wrapper(
            custom_fields.remove_key,
        )
        self.set_values = to_raw_response_wrapper(
            custom_fields.set_values,
        )


class AsyncCustomFieldsResourceWithRawResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.add_key = async_to_raw_response_wrapper(
            custom_fields.add_key,
        )
        self.delete_values = async_to_raw_response_wrapper(
            custom_fields.delete_values,
        )
        self.list_keys = async_to_raw_response_wrapper(
            custom_fields.list_keys,
        )
        self.remove_key = async_to_raw_response_wrapper(
            custom_fields.remove_key,
        )
        self.set_values = async_to_raw_response_wrapper(
            custom_fields.set_values,
        )


class CustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: CustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.add_key = to_streamed_response_wrapper(
            custom_fields.add_key,
        )
        self.delete_values = to_streamed_response_wrapper(
            custom_fields.delete_values,
        )
        self.list_keys = to_streamed_response_wrapper(
            custom_fields.list_keys,
        )
        self.remove_key = to_streamed_response_wrapper(
            custom_fields.remove_key,
        )
        self.set_values = to_streamed_response_wrapper(
            custom_fields.set_values,
        )


class AsyncCustomFieldsResourceWithStreamingResponse:
    def __init__(self, custom_fields: AsyncCustomFieldsResource) -> None:
        self._custom_fields = custom_fields

        self.add_key = async_to_streamed_response_wrapper(
            custom_fields.add_key,
        )
        self.delete_values = async_to_streamed_response_wrapper(
            custom_fields.delete_values,
        )
        self.list_keys = async_to_streamed_response_wrapper(
            custom_fields.list_keys,
        )
        self.remove_key = async_to_streamed_response_wrapper(
            custom_fields.remove_key,
        )
        self.set_values = async_to_streamed_response_wrapper(
            custom_fields.set_values,
        )
