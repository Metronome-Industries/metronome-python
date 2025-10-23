# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v2 import (
    notification_edit_params,
    notification_create_params,
    notification_archive_params,
    notification_retrieve_params,
    notification_list_offset_params,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2.notification_edit_response import NotificationEditResponse
from ...types.v2.notification_create_response import NotificationCreateResponse
from ...types.v2.notification_archive_response import NotificationArchiveResponse
from ...types.v2.notification_retrieve_response import NotificationRetrieveResponse
from ...types.v2.notification_list_offset_response import NotificationListOffsetResponse
from ...types.v2.notification_list_system_response import NotificationListSystemResponse
from ...types.v2.lifecycle_event_offset_policy_param import LifecycleEventOffsetPolicyParam
from ...types.v2.lifecycle_event_system_policy_param import LifecycleEventSystemPolicyParam

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        policy: LifecycleEventOffsetPolicyParam,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
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
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCreateResponse,
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
    ) -> NotificationRetrieveResponse:
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
            body=maybe_transform({"id": id}, notification_retrieve_params.NotificationRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationRetrieveResponse,
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
    ) -> NotificationArchiveResponse:
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
            body=maybe_transform({"id": id}, notification_archive_params.NotificationArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationArchiveResponse,
        )

    @overload
    def edit(
        self,
        *,
        policy: LifecycleEventSystemPolicyParam,
        type: Literal["SYSTEM_LIFECYCLE_EVENT"],
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationEditResponse:
        """
        Edit an existing offset lifecycle event notification configuration.

        Args:
          type: Indicates this is a system lifecycle event notification

          is_enabled: Set to true to enable webhook messages for the notification indicated in the
              policy, false to disable. Only supported by system lifecycle events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def edit(
        self,
        *,
        id: str,
        policy: LifecycleEventOffsetPolicyParam,
        type: Literal["OFFSET_LIFECYCLE_EVENT"],
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationEditResponse:
        """
        Edit an existing offset lifecycle event notification configuration.

        Args:
          id: The ID of the notification configuration to edit.

          type: Indicates this is an offset lifecycle event notification

          is_enabled: Set to true to enable webhook messages for the notification indicated in the
              policy, false to disable. Only supported by system lifecycle events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["policy", "type"], ["id", "policy", "type"])
    def edit(
        self,
        *,
        policy: LifecycleEventSystemPolicyParam | LifecycleEventOffsetPolicyParam,
        type: Literal["SYSTEM_LIFECYCLE_EVENT"] | Literal["OFFSET_LIFECYCLE_EVENT"],
        is_enabled: bool | Omit = omit,
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationEditResponse:
        return self._post(
            "/v2/notifications/edit",
            body=maybe_transform(
                {
                    "policy": policy,
                    "type": type,
                    "is_enabled": is_enabled,
                    "id": id,
                },
                notification_edit_params.NotificationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationEditResponse,
        )

    def list_offset(
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
    ) -> NotificationListOffsetResponse:
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
        return self._post(
            "/v2/notifications/offset/list",
            body=maybe_transform(
                {
                    "archive_filter": archive_filter,
                    "cursor": cursor,
                    "limit": limit,
                },
                notification_list_offset_params.NotificationListOffsetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationListOffsetResponse,
        )

    def list_system(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListSystemResponse:
        """List available system lifecycle event types for notifications.

        These are
        read-only event types that can be used when creating offset notifications.
        """
        return self._post(
            "/v2/notifications/system/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationListSystemResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        policy: LifecycleEventOffsetPolicyParam,
        uniqueness_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationCreateResponse:
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
                notification_create_params.NotificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationCreateResponse,
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
    ) -> NotificationRetrieveResponse:
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
            body=await async_maybe_transform({"id": id}, notification_retrieve_params.NotificationRetrieveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationRetrieveResponse,
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
    ) -> NotificationArchiveResponse:
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
            body=await async_maybe_transform({"id": id}, notification_archive_params.NotificationArchiveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationArchiveResponse,
        )

    @overload
    async def edit(
        self,
        *,
        policy: LifecycleEventSystemPolicyParam,
        type: Literal["SYSTEM_LIFECYCLE_EVENT"],
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationEditResponse:
        """
        Edit an existing offset lifecycle event notification configuration.

        Args:
          type: Indicates this is a system lifecycle event notification

          is_enabled: Set to true to enable webhook messages for the notification indicated in the
              policy, false to disable. Only supported by system lifecycle events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def edit(
        self,
        *,
        id: str,
        policy: LifecycleEventOffsetPolicyParam,
        type: Literal["OFFSET_LIFECYCLE_EVENT"],
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationEditResponse:
        """
        Edit an existing offset lifecycle event notification configuration.

        Args:
          id: The ID of the notification configuration to edit.

          type: Indicates this is an offset lifecycle event notification

          is_enabled: Set to true to enable webhook messages for the notification indicated in the
              policy, false to disable. Only supported by system lifecycle events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["policy", "type"], ["id", "policy", "type"])
    async def edit(
        self,
        *,
        policy: LifecycleEventSystemPolicyParam | LifecycleEventOffsetPolicyParam,
        type: Literal["SYSTEM_LIFECYCLE_EVENT"] | Literal["OFFSET_LIFECYCLE_EVENT"],
        is_enabled: bool | Omit = omit,
        id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationEditResponse:
        return await self._post(
            "/v2/notifications/edit",
            body=await async_maybe_transform(
                {
                    "policy": policy,
                    "type": type,
                    "is_enabled": is_enabled,
                    "id": id,
                },
                notification_edit_params.NotificationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationEditResponse,
        )

    async def list_offset(
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
    ) -> NotificationListOffsetResponse:
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
        return await self._post(
            "/v2/notifications/offset/list",
            body=await async_maybe_transform(
                {
                    "archive_filter": archive_filter,
                    "cursor": cursor,
                    "limit": limit,
                },
                notification_list_offset_params.NotificationListOffsetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationListOffsetResponse,
        )

    async def list_system(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListSystemResponse:
        """List available system lifecycle event types for notifications.

        These are
        read-only event types that can be used when creating offset notifications.
        """
        return await self._post(
            "/v2/notifications/system/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationListSystemResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.archive = to_raw_response_wrapper(
            notifications.archive,
        )
        self.edit = to_raw_response_wrapper(
            notifications.edit,
        )
        self.list_offset = to_raw_response_wrapper(
            notifications.list_offset,
        )
        self.list_system = to_raw_response_wrapper(
            notifications.list_system,
        )


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.archive = async_to_raw_response_wrapper(
            notifications.archive,
        )
        self.edit = async_to_raw_response_wrapper(
            notifications.edit,
        )
        self.list_offset = async_to_raw_response_wrapper(
            notifications.list_offset,
        )
        self.list_system = async_to_raw_response_wrapper(
            notifications.list_system,
        )


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.archive = to_streamed_response_wrapper(
            notifications.archive,
        )
        self.edit = to_streamed_response_wrapper(
            notifications.edit,
        )
        self.list_offset = to_streamed_response_wrapper(
            notifications.list_offset,
        )
        self.list_system = to_streamed_response_wrapper(
            notifications.list_system,
        )


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.archive = async_to_streamed_response_wrapper(
            notifications.archive,
        )
        self.edit = async_to_streamed_response_wrapper(
            notifications.edit,
        )
        self.list_offset = async_to_streamed_response_wrapper(
            notifications.list_offset,
        )
        self.list_system = async_to_streamed_response_wrapper(
            notifications.list_system,
        )
