# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..._base_client import make_request_options
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Add a key to the allow list for a given entity.

        There is a 100 character limit
        on custom field keys.

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
        keys: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes one or more custom fields on an instance of a Metronome entity.

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
        next_page: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomFieldListKeysResponse:
        """
        List all active custom field keys, optionally filtered by entity type.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

          entities: Optional list of entity types to return keys for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customFields/listKeys",
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
            cast_to=CustomFieldListKeysResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Remove a key from the allow list for a given entity.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets one or more custom fields on an instance of a Metronome entity.

        If a
        key/value pair passed in this request matches one already set on the entity, its
        value will be overwritten. Any key/value pairs that exist on the entity that do
        not match those passed in this request will remain untouched. This endpoint is
        transactional and will update all key/value pairs or no key/value pairs. Partial
        updates are not supported. There is a 200 character limit on custom field
        values.

        Args:
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Add a key to the allow list for a given entity.

        There is a 100 character limit
        on custom field keys.

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
        keys: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes one or more custom fields on an instance of a Metronome entity.

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

    async def list_keys(
        self,
        *,
        next_page: str | NotGiven = NOT_GIVEN,
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
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomFieldListKeysResponse:
        """
        List all active custom field keys, optionally filtered by entity type.

        Args:
          next_page: Cursor that indicates where the next page of results should start.

          entities: Optional list of entity types to return keys for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customFields/listKeys",
            body=await async_maybe_transform(
                {"entities": entities}, custom_field_list_keys_params.CustomFieldListKeysParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"next_page": next_page}, custom_field_list_keys_params.CustomFieldListKeysParams
                ),
            ),
            cast_to=CustomFieldListKeysResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Remove a key from the allow list for a given entity.

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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Sets one or more custom fields on an instance of a Metronome entity.

        If a
        key/value pair passed in this request matches one already set on the entity, its
        value will be overwritten. Any key/value pairs that exist on the entity that do
        not match those passed in this request will remain untouched. This endpoint is
        transactional and will update all key/value pairs or no key/value pairs. Partial
        updates are not supported. There is a 200 character limit on custom field
        values.

        Args:
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
