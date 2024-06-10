# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, MetronomeError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Metronome",
    "AsyncMetronome",
    "Client",
    "AsyncClient",
]


class Metronome(SyncAPIClient):
    alerts: resources.AlertsResource
    plans: resources.PlansResource
    credit_grants: resources.CreditGrantsResource
    customers: resources.CustomersResource
    dashboards: resources.DashboardsResource
    usage: resources.UsageResource
    audit_logs: resources.AuditLogsResource
    custom_fields: resources.CustomFieldsResource
    billable_metrics: resources.BillableMetricsResource
    services: resources.ServicesResource
    with_raw_response: MetronomeWithRawResponse
    with_streaming_response: MetronomeWithStreamedResponse

    # client options
    bearer_token: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous metronome client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `METRONOME_BEARER_TOKEN`
        - `webhook_secret` from `METRONOME_WEBHOOK_SECRET`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("METRONOME_BEARER_TOKEN")
        if bearer_token is None:
            raise MetronomeError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the METRONOME_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if webhook_secret is None:
            webhook_secret = os.environ.get("METRONOME_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("METRONOME_BASE_URL")
        if base_url is None:
            base_url = f"https://api.metronome.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.alerts = resources.AlertsResource(self)
        self.plans = resources.PlansResource(self)
        self.credit_grants = resources.CreditGrantsResource(self)
        self.customers = resources.CustomersResource(self)
        self.dashboards = resources.DashboardsResource(self)
        self.usage = resources.UsageResource(self)
        self.audit_logs = resources.AuditLogsResource(self)
        self.custom_fields = resources.CustomFieldsResource(self)
        self.billable_metrics = resources.BillableMetricsResource(self)
        self.services = resources.ServicesResource(self)
        self.with_raw_response = MetronomeWithRawResponse(self)
        self.with_streaming_response = MetronomeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMetronome(AsyncAPIClient):
    alerts: resources.AsyncAlertsResource
    plans: resources.AsyncPlansResource
    credit_grants: resources.AsyncCreditGrantsResource
    customers: resources.AsyncCustomersResource
    dashboards: resources.AsyncDashboardsResource
    usage: resources.AsyncUsageResource
    audit_logs: resources.AsyncAuditLogsResource
    custom_fields: resources.AsyncCustomFieldsResource
    billable_metrics: resources.AsyncBillableMetricsResource
    services: resources.AsyncServicesResource
    with_raw_response: AsyncMetronomeWithRawResponse
    with_streaming_response: AsyncMetronomeWithStreamedResponse

    # client options
    bearer_token: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async metronome client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `bearer_token` from `METRONOME_BEARER_TOKEN`
        - `webhook_secret` from `METRONOME_WEBHOOK_SECRET`
        """
        if bearer_token is None:
            bearer_token = os.environ.get("METRONOME_BEARER_TOKEN")
        if bearer_token is None:
            raise MetronomeError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the METRONOME_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if webhook_secret is None:
            webhook_secret = os.environ.get("METRONOME_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("METRONOME_BASE_URL")
        if base_url is None:
            base_url = f"https://api.metronome.com/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.alerts = resources.AsyncAlertsResource(self)
        self.plans = resources.AsyncPlansResource(self)
        self.credit_grants = resources.AsyncCreditGrantsResource(self)
        self.customers = resources.AsyncCustomersResource(self)
        self.dashboards = resources.AsyncDashboardsResource(self)
        self.usage = resources.AsyncUsageResource(self)
        self.audit_logs = resources.AsyncAuditLogsResource(self)
        self.custom_fields = resources.AsyncCustomFieldsResource(self)
        self.billable_metrics = resources.AsyncBillableMetricsResource(self)
        self.services = resources.AsyncServicesResource(self)
        self.with_raw_response = AsyncMetronomeWithRawResponse(self)
        self.with_streaming_response = AsyncMetronomeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": f"Bearer {bearer_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MetronomeWithRawResponse:
    def __init__(self, client: Metronome) -> None:
        self.alerts = resources.AlertsResourceWithRawResponse(client.alerts)
        self.plans = resources.PlansResourceWithRawResponse(client.plans)
        self.credit_grants = resources.CreditGrantsResourceWithRawResponse(client.credit_grants)
        self.customers = resources.CustomersResourceWithRawResponse(client.customers)
        self.dashboards = resources.DashboardsResourceWithRawResponse(client.dashboards)
        self.usage = resources.UsageResourceWithRawResponse(client.usage)
        self.audit_logs = resources.AuditLogsResourceWithRawResponse(client.audit_logs)
        self.custom_fields = resources.CustomFieldsResourceWithRawResponse(client.custom_fields)
        self.billable_metrics = resources.BillableMetricsResourceWithRawResponse(client.billable_metrics)
        self.services = resources.ServicesResourceWithRawResponse(client.services)


class AsyncMetronomeWithRawResponse:
    def __init__(self, client: AsyncMetronome) -> None:
        self.alerts = resources.AsyncAlertsResourceWithRawResponse(client.alerts)
        self.plans = resources.AsyncPlansResourceWithRawResponse(client.plans)
        self.credit_grants = resources.AsyncCreditGrantsResourceWithRawResponse(client.credit_grants)
        self.customers = resources.AsyncCustomersResourceWithRawResponse(client.customers)
        self.dashboards = resources.AsyncDashboardsResourceWithRawResponse(client.dashboards)
        self.usage = resources.AsyncUsageResourceWithRawResponse(client.usage)
        self.audit_logs = resources.AsyncAuditLogsResourceWithRawResponse(client.audit_logs)
        self.custom_fields = resources.AsyncCustomFieldsResourceWithRawResponse(client.custom_fields)
        self.billable_metrics = resources.AsyncBillableMetricsResourceWithRawResponse(client.billable_metrics)
        self.services = resources.AsyncServicesResourceWithRawResponse(client.services)


class MetronomeWithStreamedResponse:
    def __init__(self, client: Metronome) -> None:
        self.alerts = resources.AlertsResourceWithStreamingResponse(client.alerts)
        self.plans = resources.PlansResourceWithStreamingResponse(client.plans)
        self.credit_grants = resources.CreditGrantsResourceWithStreamingResponse(client.credit_grants)
        self.customers = resources.CustomersResourceWithStreamingResponse(client.customers)
        self.dashboards = resources.DashboardsResourceWithStreamingResponse(client.dashboards)
        self.usage = resources.UsageResourceWithStreamingResponse(client.usage)
        self.audit_logs = resources.AuditLogsResourceWithStreamingResponse(client.audit_logs)
        self.custom_fields = resources.CustomFieldsResourceWithStreamingResponse(client.custom_fields)
        self.billable_metrics = resources.BillableMetricsResourceWithStreamingResponse(client.billable_metrics)
        self.services = resources.ServicesResourceWithStreamingResponse(client.services)


class AsyncMetronomeWithStreamedResponse:
    def __init__(self, client: AsyncMetronome) -> None:
        self.alerts = resources.AsyncAlertsResourceWithStreamingResponse(client.alerts)
        self.plans = resources.AsyncPlansResourceWithStreamingResponse(client.plans)
        self.credit_grants = resources.AsyncCreditGrantsResourceWithStreamingResponse(client.credit_grants)
        self.customers = resources.AsyncCustomersResourceWithStreamingResponse(client.customers)
        self.dashboards = resources.AsyncDashboardsResourceWithStreamingResponse(client.dashboards)
        self.usage = resources.AsyncUsageResourceWithStreamingResponse(client.usage)
        self.audit_logs = resources.AsyncAuditLogsResourceWithStreamingResponse(client.audit_logs)
        self.custom_fields = resources.AsyncCustomFieldsResourceWithStreamingResponse(client.custom_fields)
        self.billable_metrics = resources.AsyncBillableMetricsResourceWithStreamingResponse(client.billable_metrics)
        self.services = resources.AsyncServicesResourceWithStreamingResponse(client.services)


Client = Metronome

AsyncClient = AsyncMetronome
