# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, MetronomeError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import v1, v2
    from .resources.v1.v1 import V1Resource, AsyncV1Resource
    from .resources.v2.v2 import V2Resource, AsyncV2Resource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "Metronome",
    "AsyncMetronome",
    "Client",
    "AsyncClient",
]


class Metronome(SyncAPIClient):
    # client options
    bearer_token: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Metronome client instance.

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
            base_url = f"https://api.metronome.com"

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

    @cached_property
    def v2(self) -> V2Resource:
        from .resources.v2 import V2Resource

        return V2Resource(self)

    @cached_property
    def v1(self) -> V1Resource:
        from .resources.v1 import V1Resource

        return V1Resource(self)

    @cached_property
    def with_raw_response(self) -> MetronomeWithRawResponse:
        return MetronomeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetronomeWithStreamedResponse:
        return MetronomeWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
    # client options
    bearer_token: str
    webhook_secret: str | None

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncMetronome client instance.

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
            base_url = f"https://api.metronome.com"

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

    @cached_property
    def v2(self) -> AsyncV2Resource:
        from .resources.v2 import AsyncV2Resource

        return AsyncV2Resource(self)

    @cached_property
    def v1(self) -> AsyncV1Resource:
        from .resources.v1 import AsyncV1Resource

        return AsyncV1Resource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMetronomeWithRawResponse:
        return AsyncMetronomeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetronomeWithStreamedResponse:
        return AsyncMetronomeWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
    _client: Metronome

    def __init__(self, client: Metronome) -> None:
        self._client = client

    @cached_property
    def v2(self) -> v2.V2ResourceWithRawResponse:
        from .resources.v2 import V2ResourceWithRawResponse

        return V2ResourceWithRawResponse(self._client.v2)

    @cached_property
    def v1(self) -> v1.V1ResourceWithRawResponse:
        from .resources.v1 import V1ResourceWithRawResponse

        return V1ResourceWithRawResponse(self._client.v1)


class AsyncMetronomeWithRawResponse:
    _client: AsyncMetronome

    def __init__(self, client: AsyncMetronome) -> None:
        self._client = client

    @cached_property
    def v2(self) -> v2.AsyncV2ResourceWithRawResponse:
        from .resources.v2 import AsyncV2ResourceWithRawResponse

        return AsyncV2ResourceWithRawResponse(self._client.v2)

    @cached_property
    def v1(self) -> v1.AsyncV1ResourceWithRawResponse:
        from .resources.v1 import AsyncV1ResourceWithRawResponse

        return AsyncV1ResourceWithRawResponse(self._client.v1)


class MetronomeWithStreamedResponse:
    _client: Metronome

    def __init__(self, client: Metronome) -> None:
        self._client = client

    @cached_property
    def v2(self) -> v2.V2ResourceWithStreamingResponse:
        from .resources.v2 import V2ResourceWithStreamingResponse

        return V2ResourceWithStreamingResponse(self._client.v2)

    @cached_property
    def v1(self) -> v1.V1ResourceWithStreamingResponse:
        from .resources.v1 import V1ResourceWithStreamingResponse

        return V1ResourceWithStreamingResponse(self._client.v1)


class AsyncMetronomeWithStreamedResponse:
    _client: AsyncMetronome

    def __init__(self, client: AsyncMetronome) -> None:
        self._client = client

    @cached_property
    def v2(self) -> v2.AsyncV2ResourceWithStreamingResponse:
        from .resources.v2 import AsyncV2ResourceWithStreamingResponse

        return AsyncV2ResourceWithStreamingResponse(self._client.v2)

    @cached_property
    def v1(self) -> v1.AsyncV1ResourceWithStreamingResponse:
        from .resources.v1 import AsyncV1ResourceWithStreamingResponse

        return AsyncV1ResourceWithStreamingResponse(self._client.v1)


Client = Metronome

AsyncClient = AsyncMetronome
