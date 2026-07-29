# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncBodyCursorPageCursorField, AsyncBodyCursorPageCursorField
from ...._base_client import AsyncPaginator, make_request_options
from ....types.v2.notifications import (
    offset_edit_params,
    offset_list_params,
    offset_create_params,
    offset_archive_params,
    offset_retrieve_params,
)
from ....types.v2.notifications.offset_edit_response import OffsetEditResponse
from ....types.v2.notifications.offset_create_response import OffsetCreateResponse
from ....types.v2.notifications.offset_archive_response import OffsetArchiveResponse
from ....types.v2.notifications.offset_retrieve_response import OffsetRetrieveResponse
from ....types.v2.lifecycle_event_offset_notification_config import LifecycleEventOffsetNotificationConfig

__all__ = ["OffsetResource", "AsyncOffsetResource"]


class OffsetResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OffsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return OffsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OffsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return OffsetResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        policy: offset_create_params.Policy,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetCreateResponse:
        """Create an offset lifecycle event notification configuration.

        The lifecycle event
        type is inferred from the policy.type field.

        Args:
          name: The name for this offset notification configuration.

          policy: The offset lifecycle event policy that defines when and how this notification
              should be triggered. The lifecycle event type is inferred from the policy.type
              field.

          uniqueness_key: Optional uniqueness key to prevent duplicate notification configurations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/notifications/create",
            body=maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "uniqueness_key": uniqueness_key,
                },
                offset_create_params.OffsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetRetrieveResponse:
        """
        Retrieve a specific offset lifecycle event notification configuration by ID.

        Args:
          id: The ID of the notification configuration to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/notifications/get",
            body=maybe_transform({"id": id}, offset_retrieve_params.OffsetRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetRetrieveResponse,
        )

    def list(
        self,
        *,
        archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"] | Omit = omit,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig]:
        """List offset lifecycle event notification configurations.

        These are user-created
        notifications that trigger at a specified time offset relative to lifecycle
        events. Returns a maximum of 400 results per request.

        Args:
          archive_filter: Filter options for the notification configurations. If not provided, defaults to
              NOT_ARCHIVED.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/notifications/offset/list",
            page=SyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig],
            body=maybe_transform(
                {
                    "archive_filter": archive_filter,
                    "cursor": cursor,
                    "limit": limit,
                },
                offset_list_params.OffsetListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LifecycleEventOffsetNotificationConfig,
            method="post",
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
    ) -> OffsetArchiveResponse:
        """Archive an offset lifecycle event notification configuration.

        Archived
        notifications are not processed.

        Args:
          id: The ID of the offset lifecycle event notification configuration to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/notifications/archive",
            body=maybe_transform({"id": id}, offset_archive_params.OffsetArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetArchiveResponse,
        )

    def edit(
        self,
        *,
        policy: offset_edit_params.Policy,
        id: str | Omit = omit,
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetEditResponse:
        """
        Edit an existing offset lifecycle event notification configuration.

        Args:
          policy: Updated policy configuration. The policy.type must match the existing lifecycle
              event type.

          id: The ID of the notification configuration to edit. Not provided when updating the
              configuration for system events

          is_enabled: Set to true to enable webhook messages for the notification indicated in the
              policy, false to disable. Only supported by system lifecycle events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/notifications/edit",
            body=maybe_transform(
                {
                    "policy": policy,
                    "id": id,
                    "is_enabled": is_enabled,
                },
                offset_edit_params.OffsetEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetEditResponse,
        )


class AsyncOffsetResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOffsetResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOffsetResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOffsetResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncOffsetResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        policy: offset_create_params.Policy,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetCreateResponse:
        """Create an offset lifecycle event notification configuration.

        The lifecycle event
        type is inferred from the policy.type field.

        Args:
          name: The name for this offset notification configuration.

          policy: The offset lifecycle event policy that defines when and how this notification
              should be triggered. The lifecycle event type is inferred from the policy.type
              field.

          uniqueness_key: Optional uniqueness key to prevent duplicate notification configurations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/notifications/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "policy": policy,
                    "uniqueness_key": uniqueness_key,
                },
                offset_create_params.OffsetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetRetrieveResponse:
        """
        Retrieve a specific offset lifecycle event notification configuration by ID.

        Args:
          id: The ID of the notification configuration to retrieve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/notifications/get",
            body=await async_maybe_transform({"id": id}, offset_retrieve_params.OffsetRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetRetrieveResponse,
        )

    def list(
        self,
        *,
        archive_filter: Literal["ARCHIVED", "NOT_ARCHIVED", "ALL"] | Omit = omit,
        cursor: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        LifecycleEventOffsetNotificationConfig, AsyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig]
    ]:
        """List offset lifecycle event notification configurations.

        These are user-created
        notifications that trigger at a specified time offset relative to lifecycle
        events. Returns a maximum of 400 results per request.

        Args:
          archive_filter: Filter options for the notification configurations. If not provided, defaults to
              NOT_ARCHIVED.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/notifications/offset/list",
            page=AsyncBodyCursorPageCursorField[LifecycleEventOffsetNotificationConfig],
            body=maybe_transform(
                {
                    "archive_filter": archive_filter,
                    "cursor": cursor,
                    "limit": limit,
                },
                offset_list_params.OffsetListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=LifecycleEventOffsetNotificationConfig,
            method="post",
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
    ) -> OffsetArchiveResponse:
        """Archive an offset lifecycle event notification configuration.

        Archived
        notifications are not processed.

        Args:
          id: The ID of the offset lifecycle event notification configuration to archive.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/notifications/archive",
            body=await async_maybe_transform({"id": id}, offset_archive_params.OffsetArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetArchiveResponse,
        )

    async def edit(
        self,
        *,
        policy: offset_edit_params.Policy,
        id: str | Omit = omit,
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OffsetEditResponse:
        """
        Edit an existing offset lifecycle event notification configuration.

        Args:
          policy: Updated policy configuration. The policy.type must match the existing lifecycle
              event type.

          id: The ID of the notification configuration to edit. Not provided when updating the
              configuration for system events

          is_enabled: Set to true to enable webhook messages for the notification indicated in the
              policy, false to disable. Only supported by system lifecycle events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/notifications/edit",
            body=await async_maybe_transform(
                {
                    "policy": policy,
                    "id": id,
                    "is_enabled": is_enabled,
                },
                offset_edit_params.OffsetEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OffsetEditResponse,
        )


class OffsetResourceWithRawResponse:
    def __init__(self, offset: OffsetResource) -> None:
        self._offset = offset

        self.create = to_raw_response_wrapper(
            offset.create,
        )
        self.retrieve = to_raw_response_wrapper(
            offset.retrieve,
        )
        self.list = to_raw_response_wrapper(
            offset.list,
        )
        self.archive = to_raw_response_wrapper(
            offset.archive,
        )
        self.edit = to_raw_response_wrapper(
            offset.edit,
        )


class AsyncOffsetResourceWithRawResponse:
    def __init__(self, offset: AsyncOffsetResource) -> None:
        self._offset = offset

        self.create = async_to_raw_response_wrapper(
            offset.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            offset.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            offset.list,
        )
        self.archive = async_to_raw_response_wrapper(
            offset.archive,
        )
        self.edit = async_to_raw_response_wrapper(
            offset.edit,
        )


class OffsetResourceWithStreamingResponse:
    def __init__(self, offset: OffsetResource) -> None:
        self._offset = offset

        self.create = to_streamed_response_wrapper(
            offset.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            offset.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            offset.list,
        )
        self.archive = to_streamed_response_wrapper(
            offset.archive,
        )
        self.edit = to_streamed_response_wrapper(
            offset.edit,
        )


class AsyncOffsetResourceWithStreamingResponse:
    def __init__(self, offset: AsyncOffsetResource) -> None:
        self._offset = offset

        self.create = async_to_streamed_response_wrapper(
            offset.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            offset.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            offset.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            offset.archive,
        )
        self.edit = async_to_streamed_response_wrapper(
            offset.edit,
        )
