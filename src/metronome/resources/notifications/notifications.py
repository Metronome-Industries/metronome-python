# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .offset import (
    OffsetResource,
    AsyncOffsetResource,
    OffsetResourceWithRawResponse,
    AsyncOffsetResourceWithRawResponse,
    OffsetResourceWithStreamingResponse,
    AsyncOffsetResourceWithStreamingResponse,
)
from .system import (
    SystemResource,
    AsyncSystemResource,
    SystemResourceWithRawResponse,
    AsyncSystemResourceWithRawResponse,
    SystemResourceWithStreamingResponse,
    AsyncSystemResourceWithStreamingResponse,
)
from ...types import (
    notification_create_params,
    notification_update_params,
    notification_archive_params,
    notification_retrieve_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.notification_create_response import NotificationCreateResponse
from ...types.notification_update_response import NotificationUpdateResponse
from ...types.notification_archive_response import NotificationArchiveResponse
from ...types.notification_retrieve_response import NotificationRetrieveResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def offset(self) -> OffsetResource:
        return OffsetResource(self._client)

    @cached_property
    def system(self) -> SystemResource:
        return SystemResource(self._client)

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
        policy: notification_create_params.Policy,
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

    def update(
        self,
        *,
        policy: notification_update_params.Policy,
        id: str | Omit = omit,
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationUpdateResponse:
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
                notification_update_params.NotificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdateResponse,
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


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def offset(self) -> AsyncOffsetResource:
        return AsyncOffsetResource(self._client)

    @cached_property
    def system(self) -> AsyncSystemResource:
        return AsyncSystemResource(self._client)

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
        policy: notification_create_params.Policy,
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

    async def update(
        self,
        *,
        policy: notification_update_params.Policy,
        id: str | Omit = omit,
        is_enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationUpdateResponse:
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
                notification_update_params.NotificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdateResponse,
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


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.update = to_raw_response_wrapper(
            notifications.update,
        )
        self.archive = to_raw_response_wrapper(
            notifications.archive,
        )

    @cached_property
    def offset(self) -> OffsetResourceWithRawResponse:
        return OffsetResourceWithRawResponse(self._notifications.offset)

    @cached_property
    def system(self) -> SystemResourceWithRawResponse:
        return SystemResourceWithRawResponse(self._notifications.system)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_raw_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            notifications.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            notifications.update,
        )
        self.archive = async_to_raw_response_wrapper(
            notifications.archive,
        )

    @cached_property
    def offset(self) -> AsyncOffsetResourceWithRawResponse:
        return AsyncOffsetResourceWithRawResponse(self._notifications.offset)

    @cached_property
    def system(self) -> AsyncSystemResourceWithRawResponse:
        return AsyncSystemResourceWithRawResponse(self._notifications.system)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.create = to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            notifications.update,
        )
        self.archive = to_streamed_response_wrapper(
            notifications.archive,
        )

    @cached_property
    def offset(self) -> OffsetResourceWithStreamingResponse:
        return OffsetResourceWithStreamingResponse(self._notifications.offset)

    @cached_property
    def system(self) -> SystemResourceWithStreamingResponse:
        return SystemResourceWithStreamingResponse(self._notifications.system)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.create = async_to_streamed_response_wrapper(
            notifications.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            notifications.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            notifications.update,
        )
        self.archive = async_to_streamed_response_wrapper(
            notifications.archive,
        )

    @cached_property
    def offset(self) -> AsyncOffsetResourceWithStreamingResponse:
        return AsyncOffsetResourceWithStreamingResponse(self._notifications.offset)

    @cached_property
    def system(self) -> AsyncSystemResourceWithStreamingResponse:
        return AsyncSystemResourceWithStreamingResponse(self._notifications.system)
