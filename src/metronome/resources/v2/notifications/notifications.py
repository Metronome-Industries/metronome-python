# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

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


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

    @cached_property
    def offset(self) -> OffsetResourceWithRawResponse:
        return OffsetResourceWithRawResponse(self._notifications.offset)

    @cached_property
    def system(self) -> SystemResourceWithRawResponse:
        return SystemResourceWithRawResponse(self._notifications.system)


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

    @cached_property
    def offset(self) -> AsyncOffsetResourceWithRawResponse:
        return AsyncOffsetResourceWithRawResponse(self._notifications.offset)

    @cached_property
    def system(self) -> AsyncSystemResourceWithRawResponse:
        return AsyncSystemResourceWithRawResponse(self._notifications.system)


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

    @cached_property
    def offset(self) -> OffsetResourceWithStreamingResponse:
        return OffsetResourceWithStreamingResponse(self._notifications.offset)

    @cached_property
    def system(self) -> SystemResourceWithStreamingResponse:
        return SystemResourceWithStreamingResponse(self._notifications.system)


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

    @cached_property
    def offset(self) -> AsyncOffsetResourceWithStreamingResponse:
        return AsyncOffsetResourceWithStreamingResponse(self._notifications.offset)

    @cached_property
    def system(self) -> AsyncSystemResourceWithStreamingResponse:
        return AsyncSystemResourceWithStreamingResponse(self._notifications.system)
