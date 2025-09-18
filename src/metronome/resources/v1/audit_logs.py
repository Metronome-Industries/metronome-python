# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from ...types.v1 import audit_log_list_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.v1.audit_log_list_response import AuditLogListResponse

__all__ = ["AuditLogsResource", "AsyncAuditLogsResource"]


class AuditLogsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        ending_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: str | Omit = omit,
        sort: Literal["date_asc", "date_desc"] | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AuditLogListResponse]:
        """
        Get a comprehensive audit trail of all operations performed in your Metronome
        account, whether initiated through the API, web interface, or automated
        processes. This endpoint provides detailed logs of who did what and when,
        enabling compliance reporting, security monitoring, and operational
        troubleshooting across all interaction channels.

        ### Use this endpoint to:

        - Monitor all account activity for security and compliance purposes
        - Track configuration changes regardless of source (API, UI, or system)
        - Investigate issues by reviewing historical operations

        ### Key response fields:

        An array of AuditLog objects containing:

        - id: Unique identifier for the audit log entry
        - timestamp: When the action occurred (RFC 3339 format)
        - actor: Information about who performed the action
        - request: Details including request ID, IP address, and user agent
        - `resource_type`: The type of resource affected (e.g., customer, contract,
          invoice)
        - `resource_id`: The specific resource identifier
        - `action`: The operation performed
        - `next_page`: Cursor for continuous log retrieval

        ### Usage guidelines:

        - Continuous retrieval: The next_page token enables uninterrupted log
          streaming—save it between requests to ensure no logs are missed
        - Empty responses: An empty data array means no new logs yet; continue polling
          with the same next_page token
        - Date filtering:
          - `starting_on`: Earliest logs to return (inclusive)
          - `ending_before`: Latest logs to return (exclusive)
          - Cannot be used with `next_page`
        - Resource filtering: Must specify both `resource_type` and `resource_id`
          together
        - Sort order: Default is `date_asc`; use `date_desc` for newest first

        Args:
          ending_before: RFC 3339 timestamp (exclusive). Cannot be used with 'next_page'.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          resource_id: Optional parameter that can be used to filter which audit logs are returned. If
              you specify resource_id, you must also specify resource_type.

          resource_type: Optional parameter that can be used to filter which audit logs are returned. If
              you specify resource_type, you must also specify resource_id.

          sort: Sort order by timestamp, e.g. date_asc or date_desc. Defaults to date_asc.

          starting_on: RFC 3339 timestamp of the earliest audit log to return. Cannot be used with
              'next_page'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/auditLogs",
            page=SyncCursorPage[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "next_page": next_page,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "sort": sort,
                        "starting_on": starting_on,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AsyncAuditLogsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncAuditLogsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        ending_before: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        next_page: str | Omit = omit,
        resource_id: str | Omit = omit,
        resource_type: str | Omit = omit,
        sort: Literal["date_asc", "date_desc"] | Omit = omit,
        starting_on: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditLogListResponse, AsyncCursorPage[AuditLogListResponse]]:
        """
        Get a comprehensive audit trail of all operations performed in your Metronome
        account, whether initiated through the API, web interface, or automated
        processes. This endpoint provides detailed logs of who did what and when,
        enabling compliance reporting, security monitoring, and operational
        troubleshooting across all interaction channels.

        ### Use this endpoint to:

        - Monitor all account activity for security and compliance purposes
        - Track configuration changes regardless of source (API, UI, or system)
        - Investigate issues by reviewing historical operations

        ### Key response fields:

        An array of AuditLog objects containing:

        - id: Unique identifier for the audit log entry
        - timestamp: When the action occurred (RFC 3339 format)
        - actor: Information about who performed the action
        - request: Details including request ID, IP address, and user agent
        - `resource_type`: The type of resource affected (e.g., customer, contract,
          invoice)
        - `resource_id`: The specific resource identifier
        - `action`: The operation performed
        - `next_page`: Cursor for continuous log retrieval

        ### Usage guidelines:

        - Continuous retrieval: The next_page token enables uninterrupted log
          streaming—save it between requests to ensure no logs are missed
        - Empty responses: An empty data array means no new logs yet; continue polling
          with the same next_page token
        - Date filtering:
          - `starting_on`: Earliest logs to return (inclusive)
          - `ending_before`: Latest logs to return (exclusive)
          - Cannot be used with `next_page`
        - Resource filtering: Must specify both `resource_type` and `resource_id`
          together
        - Sort order: Default is `date_asc`; use `date_desc` for newest first

        Args:
          ending_before: RFC 3339 timestamp (exclusive). Cannot be used with 'next_page'.

          limit: Max number of results that should be returned

          next_page: Cursor that indicates where the next page of results should start.

          resource_id: Optional parameter that can be used to filter which audit logs are returned. If
              you specify resource_id, you must also specify resource_type.

          resource_type: Optional parameter that can be used to filter which audit logs are returned. If
              you specify resource_type, you must also specify resource_id.

          sort: Sort order by timestamp, e.g. date_asc or date_desc. Defaults to date_asc.

          starting_on: RFC 3339 timestamp of the earliest audit log to return. Cannot be used with
              'next_page'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/auditLogs",
            page=AsyncCursorPage[AuditLogListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "limit": limit,
                        "next_page": next_page,
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "sort": sort,
                        "starting_on": starting_on,
                    },
                    audit_log_list_params.AuditLogListParams,
                ),
            ),
            model=AuditLogListResponse,
        )


class AuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_raw_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithRawResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_raw_response_wrapper(
            audit_logs.list,
        )


class AuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = to_streamed_response_wrapper(
            audit_logs.list,
        )


class AsyncAuditLogsResourceWithStreamingResponse:
    def __init__(self, audit_logs: AsyncAuditLogsResource) -> None:
        self._audit_logs = audit_logs

        self.list = async_to_streamed_response_wrapper(
            audit_logs.list,
        )
