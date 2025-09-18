# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ...types.v1 import dashboard_get_embeddable_url_params
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v1.dashboard_get_embeddable_url_response import DashboardGetEmbeddableURLResponse

__all__ = ["DashboardsResource", "AsyncDashboardsResource"]


class DashboardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DashboardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return DashboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DashboardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return DashboardsResourceWithStreamingResponse(self)

    def get_embeddable_url(
        self,
        *,
        customer_id: str,
        dashboard: Literal["invoices", "usage", "credits", "commits_and_credits"],
        bm_group_key_overrides: Iterable[dashboard_get_embeddable_url_params.BmGroupKeyOverride] | Omit = omit,
        color_overrides: Iterable[dashboard_get_embeddable_url_params.ColorOverride] | Omit = omit,
        dashboard_options: Iterable[dashboard_get_embeddable_url_params.DashboardOption] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetEmbeddableURLResponse:
        """
        Generate secure, embeddable dashboard URLs that allow you to seamlessly
        integrate Metronome's billing visualizations directly into your application.
        This endpoint creates authenticated iframe-ready URLs for customer-specific
        dashboards, providing a white-labeled billing experience without building custom
        UI.

        ### Use this endpoint to:

        - Embed billing dashboards directly in your customer portal or admin interface
        - Provide self-service access to invoices, usage data, and credit balances
        - Build white-labeled billing experiences with minimal development effort

        ### Key response fields:

        - A secure, time-limited URL that can be embedded in an iframe
        - The URL includes authentication tokens and configuration parameters
        - URLs are customer-specific and respect your security settings

        ### Usage guidelines:

        - Dashboard types: Choose from `invoices`, `usage`, or `commits_and_credits`
        - Customization options:
          - `dashboard_options`: Configure whether you want invoices to show zero usage
            line items
          - `color_overrides`: Match your brand's color palette
          - `bm_group_key_overrides`: Customize how dimensions are displayed (for the
            usage embeddable dashboard)
        - Iframe implementation: Embed the returned URL directly in an iframe element
        - Responsive design: Dashboards automatically adapt to container dimensions

        Args:
          dashboard: The type of dashboard to retrieve.

          bm_group_key_overrides: Optional list of billable metric group key overrides

          color_overrides: Optional list of colors to override

          dashboard_options: Optional dashboard specific options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/dashboards/getEmbeddableUrl",
            body=maybe_transform(
                {
                    "customer_id": customer_id,
                    "dashboard": dashboard,
                    "bm_group_key_overrides": bm_group_key_overrides,
                    "color_overrides": color_overrides,
                    "dashboard_options": dashboard_options,
                },
                dashboard_get_embeddable_url_params.DashboardGetEmbeddableURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardGetEmbeddableURLResponse,
        )


class AsyncDashboardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDashboardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDashboardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDashboardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Metronome-Industries/metronome-python#with_streaming_response
        """
        return AsyncDashboardsResourceWithStreamingResponse(self)

    async def get_embeddable_url(
        self,
        *,
        customer_id: str,
        dashboard: Literal["invoices", "usage", "credits", "commits_and_credits"],
        bm_group_key_overrides: Iterable[dashboard_get_embeddable_url_params.BmGroupKeyOverride] | Omit = omit,
        color_overrides: Iterable[dashboard_get_embeddable_url_params.ColorOverride] | Omit = omit,
        dashboard_options: Iterable[dashboard_get_embeddable_url_params.DashboardOption] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DashboardGetEmbeddableURLResponse:
        """
        Generate secure, embeddable dashboard URLs that allow you to seamlessly
        integrate Metronome's billing visualizations directly into your application.
        This endpoint creates authenticated iframe-ready URLs for customer-specific
        dashboards, providing a white-labeled billing experience without building custom
        UI.

        ### Use this endpoint to:

        - Embed billing dashboards directly in your customer portal or admin interface
        - Provide self-service access to invoices, usage data, and credit balances
        - Build white-labeled billing experiences with minimal development effort

        ### Key response fields:

        - A secure, time-limited URL that can be embedded in an iframe
        - The URL includes authentication tokens and configuration parameters
        - URLs are customer-specific and respect your security settings

        ### Usage guidelines:

        - Dashboard types: Choose from `invoices`, `usage`, or `commits_and_credits`
        - Customization options:
          - `dashboard_options`: Configure whether you want invoices to show zero usage
            line items
          - `color_overrides`: Match your brand's color palette
          - `bm_group_key_overrides`: Customize how dimensions are displayed (for the
            usage embeddable dashboard)
        - Iframe implementation: Embed the returned URL directly in an iframe element
        - Responsive design: Dashboards automatically adapt to container dimensions

        Args:
          dashboard: The type of dashboard to retrieve.

          bm_group_key_overrides: Optional list of billable metric group key overrides

          color_overrides: Optional list of colors to override

          dashboard_options: Optional dashboard specific options

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/dashboards/getEmbeddableUrl",
            body=await async_maybe_transform(
                {
                    "customer_id": customer_id,
                    "dashboard": dashboard,
                    "bm_group_key_overrides": bm_group_key_overrides,
                    "color_overrides": color_overrides,
                    "dashboard_options": dashboard_options,
                },
                dashboard_get_embeddable_url_params.DashboardGetEmbeddableURLParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DashboardGetEmbeddableURLResponse,
        )


class DashboardsResourceWithRawResponse:
    def __init__(self, dashboards: DashboardsResource) -> None:
        self._dashboards = dashboards

        self.get_embeddable_url = to_raw_response_wrapper(
            dashboards.get_embeddable_url,
        )


class AsyncDashboardsResourceWithRawResponse:
    def __init__(self, dashboards: AsyncDashboardsResource) -> None:
        self._dashboards = dashboards

        self.get_embeddable_url = async_to_raw_response_wrapper(
            dashboards.get_embeddable_url,
        )


class DashboardsResourceWithStreamingResponse:
    def __init__(self, dashboards: DashboardsResource) -> None:
        self._dashboards = dashboards

        self.get_embeddable_url = to_streamed_response_wrapper(
            dashboards.get_embeddable_url,
        )


class AsyncDashboardsResourceWithStreamingResponse:
    def __init__(self, dashboards: AsyncDashboardsResource) -> None:
        self._dashboards = dashboards

        self.get_embeddable_url = async_to_streamed_response_wrapper(
            dashboards.get_embeddable_url,
        )
