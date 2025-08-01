# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import gc
import os
import sys
import json
import time
import asyncio
import inspect
import subprocess
import tracemalloc
from typing import Any, Union, cast
from textwrap import dedent
from unittest import mock
from typing_extensions import Literal

import httpx
import pytest
from respx import MockRouter
from pydantic import ValidationError

from metronome import Metronome, AsyncMetronome, APIResponseValidationError
from metronome._types import Omit
from metronome._utils import parse_datetime
from metronome._models import BaseModel, FinalRequestOptions
from metronome._exceptions import APIStatusError, MetronomeError, APITimeoutError, APIResponseValidationError
from metronome._base_client import (
    DEFAULT_TIMEOUT,
    HTTPX_DEFAULT_TIMEOUT,
    BaseClient,
    DefaultHttpxClient,
    DefaultAsyncHttpxClient,
    make_request_options,
)

from .utils import update_env

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
bearer_token = "My Bearer Token"


def _get_params(client: BaseClient[Any, Any]) -> dict[str, str]:
    request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
    url = httpx.URL(request.url)
    return dict(url.params)


def _low_retry_timeout(*_args: Any, **_kwargs: Any) -> float:
    return 0.1


def _get_open_connections(client: Metronome | AsyncMetronome) -> int:
    transport = client._client._transport
    assert isinstance(transport, httpx.HTTPTransport) or isinstance(transport, httpx.AsyncHTTPTransport)

    pool = transport._pool
    return len(pool._requests)


class TestMetronome:
    client = Metronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)

    @pytest.mark.respx(base_url=base_url)
    def test_raw_response(self, respx_mock: MockRouter) -> None:
        respx_mock.post("/foo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = self.client.post("/foo", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)
        assert response.json() == {"foo": "bar"}

    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_for_binary(self, respx_mock: MockRouter) -> None:
        respx_mock.post("/foo").mock(
            return_value=httpx.Response(200, headers={"Content-Type": "application/binary"}, content='{"foo": "bar"}')
        )

        response = self.client.post("/foo", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)
        assert response.json() == {"foo": "bar"}

    def test_copy(self) -> None:
        copied = self.client.copy()
        assert id(copied) != id(self.client)

        copied = self.client.copy(bearer_token="another My Bearer Token")
        assert copied.bearer_token == "another My Bearer Token"
        assert self.client.bearer_token == "My Bearer Token"

    def test_copy_default_options(self) -> None:
        # options that have a default are overridden correctly
        copied = self.client.copy(max_retries=7)
        assert copied.max_retries == 7
        assert self.client.max_retries == 2

        copied2 = copied.copy(max_retries=6)
        assert copied2.max_retries == 6
        assert copied.max_retries == 7

        # timeout
        assert isinstance(self.client.timeout, httpx.Timeout)
        copied = self.client.copy(timeout=None)
        assert copied.timeout is None
        assert isinstance(self.client.timeout, httpx.Timeout)

    def test_copy_default_headers(self) -> None:
        client = Metronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_headers={"X-Foo": "bar"},
        )
        assert client.default_headers["X-Foo"] == "bar"

        # does not override the already given value when not specified
        copied = client.copy()
        assert copied.default_headers["X-Foo"] == "bar"

        # merges already given headers
        copied = client.copy(default_headers={"X-Bar": "stainless"})
        assert copied.default_headers["X-Foo"] == "bar"
        assert copied.default_headers["X-Bar"] == "stainless"

        # uses new values for any already given headers
        copied = client.copy(default_headers={"X-Foo": "stainless"})
        assert copied.default_headers["X-Foo"] == "stainless"

        # set_default_headers

        # completely overrides already set values
        copied = client.copy(set_default_headers={})
        assert copied.default_headers.get("X-Foo") is None

        copied = client.copy(set_default_headers={"X-Bar": "Robert"})
        assert copied.default_headers["X-Bar"] == "Robert"

        with pytest.raises(
            ValueError,
            match="`default_headers` and `set_default_headers` arguments are mutually exclusive",
        ):
            client.copy(set_default_headers={}, default_headers={"X-Foo": "Bar"})

    def test_copy_default_query(self) -> None:
        client = Metronome(
            base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, default_query={"foo": "bar"}
        )
        assert _get_params(client)["foo"] == "bar"

        # does not override the already given value when not specified
        copied = client.copy()
        assert _get_params(copied)["foo"] == "bar"

        # merges already given params
        copied = client.copy(default_query={"bar": "stainless"})
        params = _get_params(copied)
        assert params["foo"] == "bar"
        assert params["bar"] == "stainless"

        # uses new values for any already given headers
        copied = client.copy(default_query={"foo": "stainless"})
        assert _get_params(copied)["foo"] == "stainless"

        # set_default_query

        # completely overrides already set values
        copied = client.copy(set_default_query={})
        assert _get_params(copied) == {}

        copied = client.copy(set_default_query={"bar": "Robert"})
        assert _get_params(copied)["bar"] == "Robert"

        with pytest.raises(
            ValueError,
            # TODO: update
            match="`default_query` and `set_default_query` arguments are mutually exclusive",
        ):
            client.copy(set_default_query={}, default_query={"foo": "Bar"})

    def test_copy_signature(self) -> None:
        # ensure the same parameters that can be passed to the client are defined in the `.copy()` method
        init_signature = inspect.signature(
            # mypy doesn't like that we access the `__init__` property.
            self.client.__init__,  # type: ignore[misc]
        )
        copy_signature = inspect.signature(self.client.copy)
        exclude_params = {"transport", "proxies", "_strict_response_validation"}

        for name in init_signature.parameters.keys():
            if name in exclude_params:
                continue

            copy_param = copy_signature.parameters.get(name)
            assert copy_param is not None, f"copy() signature is missing the {name} param"

    @pytest.mark.skipif(sys.version_info >= (3, 10), reason="fails because of a memory leak that started from 3.12")
    def test_copy_build_request(self) -> None:
        options = FinalRequestOptions(method="get", url="/foo")

        def build_request(options: FinalRequestOptions) -> None:
            client = self.client.copy()
            client._build_request(options)

        # ensure that the machinery is warmed up before tracing starts.
        build_request(options)
        gc.collect()

        tracemalloc.start(1000)

        snapshot_before = tracemalloc.take_snapshot()

        ITERATIONS = 10
        for _ in range(ITERATIONS):
            build_request(options)

        gc.collect()
        snapshot_after = tracemalloc.take_snapshot()

        tracemalloc.stop()

        def add_leak(leaks: list[tracemalloc.StatisticDiff], diff: tracemalloc.StatisticDiff) -> None:
            if diff.count == 0:
                # Avoid false positives by considering only leaks (i.e. allocations that persist).
                return

            if diff.count % ITERATIONS != 0:
                # Avoid false positives by considering only leaks that appear per iteration.
                return

            for frame in diff.traceback:
                if any(
                    frame.filename.endswith(fragment)
                    for fragment in [
                        # to_raw_response_wrapper leaks through the @functools.wraps() decorator.
                        #
                        # removing the decorator fixes the leak for reasons we don't understand.
                        "metronome/_legacy_response.py",
                        "metronome/_response.py",
                        # pydantic.BaseModel.model_dump || pydantic.BaseModel.dict leak memory for some reason.
                        "metronome/_compat.py",
                        # Standard library leaks we don't care about.
                        "/logging/__init__.py",
                    ]
                ):
                    return

            leaks.append(diff)

        leaks: list[tracemalloc.StatisticDiff] = []
        for diff in snapshot_after.compare_to(snapshot_before, "traceback"):
            add_leak(leaks, diff)
        if leaks:
            for leak in leaks:
                print("MEMORY LEAK:", leak)
                for frame in leak.traceback:
                    print(frame)
            raise AssertionError()

    def test_request_timeout(self) -> None:
        request = self.client._build_request(FinalRequestOptions(method="get", url="/foo"))
        timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
        assert timeout == DEFAULT_TIMEOUT

        request = self.client._build_request(
            FinalRequestOptions(method="get", url="/foo", timeout=httpx.Timeout(100.0))
        )
        timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
        assert timeout == httpx.Timeout(100.0)

    def test_client_timeout_option(self) -> None:
        client = Metronome(
            base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, timeout=httpx.Timeout(0)
        )

        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
        assert timeout == httpx.Timeout(0)

    def test_http_client_timeout_option(self) -> None:
        # custom timeout given to the httpx client should be used
        with httpx.Client(timeout=None) as http_client:
            client = Metronome(
                base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, http_client=http_client
            )

            request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
            timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
            assert timeout == httpx.Timeout(None)

        # no timeout given to the httpx client should not use the httpx default
        with httpx.Client() as http_client:
            client = Metronome(
                base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, http_client=http_client
            )

            request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
            timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
            assert timeout == DEFAULT_TIMEOUT

        # explicitly passing the default timeout currently results in it being ignored
        with httpx.Client(timeout=HTTPX_DEFAULT_TIMEOUT) as http_client:
            client = Metronome(
                base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, http_client=http_client
            )

            request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
            timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
            assert timeout == DEFAULT_TIMEOUT  # our default

    async def test_invalid_http_client(self) -> None:
        with pytest.raises(TypeError, match="Invalid `http_client` arg"):
            async with httpx.AsyncClient() as http_client:
                Metronome(
                    base_url=base_url,
                    bearer_token=bearer_token,
                    _strict_response_validation=True,
                    http_client=cast(Any, http_client),
                )

    def test_default_headers_option(self) -> None:
        client = Metronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_headers={"X-Foo": "bar"},
        )
        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        assert request.headers.get("x-foo") == "bar"
        assert request.headers.get("x-stainless-lang") == "python"

        client2 = Metronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_headers={
                "X-Foo": "stainless",
                "X-Stainless-Lang": "my-overriding-header",
            },
        )
        request = client2._build_request(FinalRequestOptions(method="get", url="/foo"))
        assert request.headers.get("x-foo") == "stainless"
        assert request.headers.get("x-stainless-lang") == "my-overriding-header"

    def test_validate_headers(self) -> None:
        client = Metronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        assert request.headers.get("Authorization") == f"Bearer {bearer_token}"

        with pytest.raises(MetronomeError):
            with update_env(**{"METRONOME_BEARER_TOKEN": Omit()}):
                client2 = Metronome(base_url=base_url, bearer_token=None, _strict_response_validation=True)
            _ = client2

    def test_default_query_option(self) -> None:
        client = Metronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_query={"query_param": "bar"},
        )
        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        url = httpx.URL(request.url)
        assert dict(url.params) == {"query_param": "bar"}

        request = client._build_request(
            FinalRequestOptions(
                method="get",
                url="/foo",
                params={"foo": "baz", "query_param": "overridden"},
            )
        )
        url = httpx.URL(request.url)
        assert dict(url.params) == {"foo": "baz", "query_param": "overridden"}

    def test_request_extra_json(self) -> None:
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar"},
                extra_json={"baz": False},
            ),
        )
        data = json.loads(request.content.decode("utf-8"))
        assert data == {"foo": "bar", "baz": False}

        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                extra_json={"baz": False},
            ),
        )
        data = json.loads(request.content.decode("utf-8"))
        assert data == {"baz": False}

        # `extra_json` takes priority over `json_data` when keys clash
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar", "baz": True},
                extra_json={"baz": None},
            ),
        )
        data = json.loads(request.content.decode("utf-8"))
        assert data == {"foo": "bar", "baz": None}

    def test_request_extra_headers(self) -> None:
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(extra_headers={"X-Foo": "Foo"}),
            ),
        )
        assert request.headers.get("X-Foo") == "Foo"

        # `extra_headers` takes priority over `default_headers` when keys clash
        request = self.client.with_options(default_headers={"X-Bar": "true"})._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    extra_headers={"X-Bar": "false"},
                ),
            ),
        )
        assert request.headers.get("X-Bar") == "false"

    def test_request_extra_query(self) -> None:
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    extra_query={"my_query_param": "Foo"},
                ),
            ),
        )
        params = dict(request.url.params)
        assert params == {"my_query_param": "Foo"}

        # if both `query` and `extra_query` are given, they are merged
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    query={"bar": "1"},
                    extra_query={"foo": "2"},
                ),
            ),
        )
        params = dict(request.url.params)
        assert params == {"bar": "1", "foo": "2"}

        # `extra_query` takes priority over `query` when keys clash
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    query={"foo": "1"},
                    extra_query={"foo": "2"},
                ),
            ),
        )
        params = dict(request.url.params)
        assert params == {"foo": "2"}

    def test_multipart_repeating_array(self, client: Metronome) -> None:
        request = client._build_request(
            FinalRequestOptions.construct(
                method="post",
                url="/foo",
                headers={"Content-Type": "multipart/form-data; boundary=6b7ba517decee4a450543ea6ae821c82"},
                json_data={"array": ["foo", "bar"]},
                files=[("foo.txt", b"hello world")],
            )
        )

        assert request.read().split(b"\r\n") == [
            b"--6b7ba517decee4a450543ea6ae821c82",
            b'Content-Disposition: form-data; name="array[]"',
            b"",
            b"foo",
            b"--6b7ba517decee4a450543ea6ae821c82",
            b'Content-Disposition: form-data; name="array[]"',
            b"",
            b"bar",
            b"--6b7ba517decee4a450543ea6ae821c82",
            b'Content-Disposition: form-data; name="foo.txt"; filename="upload"',
            b"Content-Type: application/octet-stream",
            b"",
            b"hello world",
            b"--6b7ba517decee4a450543ea6ae821c82--",
            b"",
        ]

    @pytest.mark.respx(base_url=base_url)
    def test_basic_union_response(self, respx_mock: MockRouter) -> None:
        class Model1(BaseModel):
            name: str

        class Model2(BaseModel):
            foo: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = self.client.get("/foo", cast_to=cast(Any, Union[Model1, Model2]))
        assert isinstance(response, Model2)
        assert response.foo == "bar"

    @pytest.mark.respx(base_url=base_url)
    def test_union_response_different_types(self, respx_mock: MockRouter) -> None:
        """Union of objects with the same field name using a different type"""

        class Model1(BaseModel):
            foo: int

        class Model2(BaseModel):
            foo: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = self.client.get("/foo", cast_to=cast(Any, Union[Model1, Model2]))
        assert isinstance(response, Model2)
        assert response.foo == "bar"

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": 1}))

        response = self.client.get("/foo", cast_to=cast(Any, Union[Model1, Model2]))
        assert isinstance(response, Model1)
        assert response.foo == 1

    @pytest.mark.respx(base_url=base_url)
    def test_non_application_json_content_type_for_json_data(self, respx_mock: MockRouter) -> None:
        """
        Response that sets Content-Type to something other than application/json but returns json data
        """

        class Model(BaseModel):
            foo: int

        respx_mock.get("/foo").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps({"foo": 2}),
                headers={"Content-Type": "application/text"},
            )
        )

        response = self.client.get("/foo", cast_to=Model)
        assert isinstance(response, Model)
        assert response.foo == 2

    def test_base_url_setter(self) -> None:
        client = Metronome(
            base_url="https://example.com/from_init", bearer_token=bearer_token, _strict_response_validation=True
        )
        assert client.base_url == "https://example.com/from_init/"

        client.base_url = "https://example.com/from_setter"  # type: ignore[assignment]

        assert client.base_url == "https://example.com/from_setter/"

    def test_base_url_env(self) -> None:
        with update_env(METRONOME_BASE_URL="http://localhost:5000/from/env"):
            client = Metronome(bearer_token=bearer_token, _strict_response_validation=True)
            assert client.base_url == "http://localhost:5000/from/env/"

    @pytest.mark.parametrize(
        "client",
        [
            Metronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
            ),
            Metronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
                http_client=httpx.Client(),
            ),
        ],
        ids=["standard", "custom http client"],
    )
    def test_base_url_trailing_slash(self, client: Metronome) -> None:
        request = client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar"},
            ),
        )
        assert request.url == "http://localhost:5000/custom/path/foo"

    @pytest.mark.parametrize(
        "client",
        [
            Metronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
            ),
            Metronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
                http_client=httpx.Client(),
            ),
        ],
        ids=["standard", "custom http client"],
    )
    def test_base_url_no_trailing_slash(self, client: Metronome) -> None:
        request = client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar"},
            ),
        )
        assert request.url == "http://localhost:5000/custom/path/foo"

    @pytest.mark.parametrize(
        "client",
        [
            Metronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
            ),
            Metronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
                http_client=httpx.Client(),
            ),
        ],
        ids=["standard", "custom http client"],
    )
    def test_absolute_request_url(self, client: Metronome) -> None:
        request = client._build_request(
            FinalRequestOptions(
                method="post",
                url="https://myapi.com/foo",
                json_data={"foo": "bar"},
            ),
        )
        assert request.url == "https://myapi.com/foo"

    def test_copied_client_does_not_close_http(self) -> None:
        client = Metronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
        assert not client.is_closed()

        copied = client.copy()
        assert copied is not client

        del copied

        assert not client.is_closed()

    def test_client_context_manager(self) -> None:
        client = Metronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
        with client as c2:
            assert c2 is client
            assert not c2.is_closed()
            assert not client.is_closed()
        assert client.is_closed()

    @pytest.mark.respx(base_url=base_url)
    def test_client_response_validation_error(self, respx_mock: MockRouter) -> None:
        class Model(BaseModel):
            foo: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": {"invalid": True}}))

        with pytest.raises(APIResponseValidationError) as exc:
            self.client.get("/foo", cast_to=Model)

        assert isinstance(exc.value.__cause__, ValidationError)

    def test_client_max_retries_validation(self) -> None:
        with pytest.raises(TypeError, match=r"max_retries cannot be None"):
            Metronome(
                base_url=base_url,
                bearer_token=bearer_token,
                _strict_response_validation=True,
                max_retries=cast(Any, None),
            )

    @pytest.mark.respx(base_url=base_url)
    def test_received_text_for_expected_json(self, respx_mock: MockRouter) -> None:
        class Model(BaseModel):
            name: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, text="my-custom-format"))

        strict_client = Metronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)

        with pytest.raises(APIResponseValidationError):
            strict_client.get("/foo", cast_to=Model)

        client = Metronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)

        response = client.get("/foo", cast_to=Model)
        assert isinstance(response, str)  # type: ignore[unreachable]

    @pytest.mark.parametrize(
        "remaining_retries,retry_after,timeout",
        [
            [3, "20", 20],
            [3, "0", 0.5],
            [3, "-10", 0.5],
            [3, "60", 60],
            [3, "61", 0.5],
            [3, "Fri, 29 Sep 2023 16:26:57 GMT", 20],
            [3, "Fri, 29 Sep 2023 16:26:37 GMT", 0.5],
            [3, "Fri, 29 Sep 2023 16:26:27 GMT", 0.5],
            [3, "Fri, 29 Sep 2023 16:27:37 GMT", 60],
            [3, "Fri, 29 Sep 2023 16:27:38 GMT", 0.5],
            [3, "99999999999999999999999999999999999", 0.5],
            [3, "Zun, 29 Sep 2023 16:26:27 GMT", 0.5],
            [3, "", 0.5],
            [2, "", 0.5 * 2.0],
            [1, "", 0.5 * 4.0],
            [-1100, "", 8],  # test large number potentially overflowing
        ],
    )
    @mock.patch("time.time", mock.MagicMock(return_value=1696004797))
    def test_parse_retry_after_header(self, remaining_retries: int, retry_after: str, timeout: float) -> None:
        client = Metronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)

        headers = httpx.Headers({"retry-after": retry_after})
        options = FinalRequestOptions(method="get", url="/foo", max_retries=3)
        calculated = client._calculate_retry_timeout(remaining_retries, options, headers)
        assert calculated == pytest.approx(timeout, 0.5 * 0.875)  # pyright: ignore[reportUnknownMemberType]

    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_retrying_timeout_errors_doesnt_leak(self, respx_mock: MockRouter, client: Metronome) -> None:
        respx_mock.post("/v1/contracts/create").mock(side_effect=httpx.TimeoutException("Test timeout error"))

        with pytest.raises(APITimeoutError):
            client.v1.contracts.with_streaming_response.create(
                customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
                starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            ).__enter__()

        assert _get_open_connections(self.client) == 0

    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_retrying_status_errors_doesnt_leak(self, respx_mock: MockRouter, client: Metronome) -> None:
        respx_mock.post("/v1/contracts/create").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            client.v1.contracts.with_streaming_response.create(
                customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
                starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            ).__enter__()
        assert _get_open_connections(self.client) == 0

    @pytest.mark.parametrize("failures_before_success", [0, 2, 4])
    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.parametrize("failure_mode", ["status", "exception"])
    def test_retries_taken(
        self,
        client: Metronome,
        failures_before_success: int,
        failure_mode: Literal["status", "exception"],
        respx_mock: MockRouter,
    ) -> None:
        client = client.with_options(max_retries=4)

        nb_retries = 0

        def retry_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal nb_retries
            if nb_retries < failures_before_success:
                nb_retries += 1
                if failure_mode == "exception":
                    raise RuntimeError("oops")
                return httpx.Response(500)
            return httpx.Response(200)

        respx_mock.post("/v1/contracts/create").mock(side_effect=retry_handler)

        response = client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d", starting_at=parse_datetime("2020-01-01T00:00:00.000Z")
        )

        assert response.retries_taken == failures_before_success
        assert int(response.http_request.headers.get("x-stainless-retry-count")) == failures_before_success

    @pytest.mark.parametrize("failures_before_success", [0, 2, 4])
    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_omit_retry_count_header(
        self, client: Metronome, failures_before_success: int, respx_mock: MockRouter
    ) -> None:
        client = client.with_options(max_retries=4)

        nb_retries = 0

        def retry_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal nb_retries
            if nb_retries < failures_before_success:
                nb_retries += 1
                return httpx.Response(500)
            return httpx.Response(200)

        respx_mock.post("/v1/contracts/create").mock(side_effect=retry_handler)

        response = client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            extra_headers={"x-stainless-retry-count": Omit()},
        )

        assert len(response.http_request.headers.get_list("x-stainless-retry-count")) == 0

    @pytest.mark.parametrize("failures_before_success", [0, 2, 4])
    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    def test_overwrite_retry_count_header(
        self, client: Metronome, failures_before_success: int, respx_mock: MockRouter
    ) -> None:
        client = client.with_options(max_retries=4)

        nb_retries = 0

        def retry_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal nb_retries
            if nb_retries < failures_before_success:
                nb_retries += 1
                return httpx.Response(500)
            return httpx.Response(200)

        respx_mock.post("/v1/contracts/create").mock(side_effect=retry_handler)

        response = client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            extra_headers={"x-stainless-retry-count": "42"},
        )

        assert response.http_request.headers.get("x-stainless-retry-count") == "42"

    def test_proxy_environment_variables(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # Test that the proxy environment variables are set correctly
        monkeypatch.setenv("HTTPS_PROXY", "https://example.org")

        client = DefaultHttpxClient()

        mounts = tuple(client._mounts.items())
        assert len(mounts) == 1
        assert mounts[0][0].pattern == "https://"

    @pytest.mark.filterwarnings("ignore:.*deprecated.*:DeprecationWarning")
    def test_default_client_creation(self) -> None:
        # Ensure that the client can be initialized without any exceptions
        DefaultHttpxClient(
            verify=True,
            cert=None,
            trust_env=True,
            http1=True,
            http2=False,
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        )

    @pytest.mark.respx(base_url=base_url)
    def test_follow_redirects(self, respx_mock: MockRouter) -> None:
        # Test that the default follow_redirects=True allows following redirects
        respx_mock.post("/redirect").mock(
            return_value=httpx.Response(302, headers={"Location": f"{base_url}/redirected"})
        )
        respx_mock.get("/redirected").mock(return_value=httpx.Response(200, json={"status": "ok"}))

        response = self.client.post("/redirect", body={"key": "value"}, cast_to=httpx.Response)
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    @pytest.mark.respx(base_url=base_url)
    def test_follow_redirects_disabled(self, respx_mock: MockRouter) -> None:
        # Test that follow_redirects=False prevents following redirects
        respx_mock.post("/redirect").mock(
            return_value=httpx.Response(302, headers={"Location": f"{base_url}/redirected"})
        )

        with pytest.raises(APIStatusError) as exc_info:
            self.client.post(
                "/redirect", body={"key": "value"}, options={"follow_redirects": False}, cast_to=httpx.Response
            )

        assert exc_info.value.response.status_code == 302
        assert exc_info.value.response.headers["Location"] == f"{base_url}/redirected"


class TestAsyncMetronome:
    client = AsyncMetronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)

    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.asyncio
    async def test_raw_response(self, respx_mock: MockRouter) -> None:
        respx_mock.post("/foo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = await self.client.post("/foo", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)
        assert response.json() == {"foo": "bar"}

    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.asyncio
    async def test_raw_response_for_binary(self, respx_mock: MockRouter) -> None:
        respx_mock.post("/foo").mock(
            return_value=httpx.Response(200, headers={"Content-Type": "application/binary"}, content='{"foo": "bar"}')
        )

        response = await self.client.post("/foo", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)
        assert response.json() == {"foo": "bar"}

    def test_copy(self) -> None:
        copied = self.client.copy()
        assert id(copied) != id(self.client)

        copied = self.client.copy(bearer_token="another My Bearer Token")
        assert copied.bearer_token == "another My Bearer Token"
        assert self.client.bearer_token == "My Bearer Token"

    def test_copy_default_options(self) -> None:
        # options that have a default are overridden correctly
        copied = self.client.copy(max_retries=7)
        assert copied.max_retries == 7
        assert self.client.max_retries == 2

        copied2 = copied.copy(max_retries=6)
        assert copied2.max_retries == 6
        assert copied.max_retries == 7

        # timeout
        assert isinstance(self.client.timeout, httpx.Timeout)
        copied = self.client.copy(timeout=None)
        assert copied.timeout is None
        assert isinstance(self.client.timeout, httpx.Timeout)

    def test_copy_default_headers(self) -> None:
        client = AsyncMetronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_headers={"X-Foo": "bar"},
        )
        assert client.default_headers["X-Foo"] == "bar"

        # does not override the already given value when not specified
        copied = client.copy()
        assert copied.default_headers["X-Foo"] == "bar"

        # merges already given headers
        copied = client.copy(default_headers={"X-Bar": "stainless"})
        assert copied.default_headers["X-Foo"] == "bar"
        assert copied.default_headers["X-Bar"] == "stainless"

        # uses new values for any already given headers
        copied = client.copy(default_headers={"X-Foo": "stainless"})
        assert copied.default_headers["X-Foo"] == "stainless"

        # set_default_headers

        # completely overrides already set values
        copied = client.copy(set_default_headers={})
        assert copied.default_headers.get("X-Foo") is None

        copied = client.copy(set_default_headers={"X-Bar": "Robert"})
        assert copied.default_headers["X-Bar"] == "Robert"

        with pytest.raises(
            ValueError,
            match="`default_headers` and `set_default_headers` arguments are mutually exclusive",
        ):
            client.copy(set_default_headers={}, default_headers={"X-Foo": "Bar"})

    def test_copy_default_query(self) -> None:
        client = AsyncMetronome(
            base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, default_query={"foo": "bar"}
        )
        assert _get_params(client)["foo"] == "bar"

        # does not override the already given value when not specified
        copied = client.copy()
        assert _get_params(copied)["foo"] == "bar"

        # merges already given params
        copied = client.copy(default_query={"bar": "stainless"})
        params = _get_params(copied)
        assert params["foo"] == "bar"
        assert params["bar"] == "stainless"

        # uses new values for any already given headers
        copied = client.copy(default_query={"foo": "stainless"})
        assert _get_params(copied)["foo"] == "stainless"

        # set_default_query

        # completely overrides already set values
        copied = client.copy(set_default_query={})
        assert _get_params(copied) == {}

        copied = client.copy(set_default_query={"bar": "Robert"})
        assert _get_params(copied)["bar"] == "Robert"

        with pytest.raises(
            ValueError,
            # TODO: update
            match="`default_query` and `set_default_query` arguments are mutually exclusive",
        ):
            client.copy(set_default_query={}, default_query={"foo": "Bar"})

    def test_copy_signature(self) -> None:
        # ensure the same parameters that can be passed to the client are defined in the `.copy()` method
        init_signature = inspect.signature(
            # mypy doesn't like that we access the `__init__` property.
            self.client.__init__,  # type: ignore[misc]
        )
        copy_signature = inspect.signature(self.client.copy)
        exclude_params = {"transport", "proxies", "_strict_response_validation"}

        for name in init_signature.parameters.keys():
            if name in exclude_params:
                continue

            copy_param = copy_signature.parameters.get(name)
            assert copy_param is not None, f"copy() signature is missing the {name} param"

    @pytest.mark.skipif(sys.version_info >= (3, 10), reason="fails because of a memory leak that started from 3.12")
    def test_copy_build_request(self) -> None:
        options = FinalRequestOptions(method="get", url="/foo")

        def build_request(options: FinalRequestOptions) -> None:
            client = self.client.copy()
            client._build_request(options)

        # ensure that the machinery is warmed up before tracing starts.
        build_request(options)
        gc.collect()

        tracemalloc.start(1000)

        snapshot_before = tracemalloc.take_snapshot()

        ITERATIONS = 10
        for _ in range(ITERATIONS):
            build_request(options)

        gc.collect()
        snapshot_after = tracemalloc.take_snapshot()

        tracemalloc.stop()

        def add_leak(leaks: list[tracemalloc.StatisticDiff], diff: tracemalloc.StatisticDiff) -> None:
            if diff.count == 0:
                # Avoid false positives by considering only leaks (i.e. allocations that persist).
                return

            if diff.count % ITERATIONS != 0:
                # Avoid false positives by considering only leaks that appear per iteration.
                return

            for frame in diff.traceback:
                if any(
                    frame.filename.endswith(fragment)
                    for fragment in [
                        # to_raw_response_wrapper leaks through the @functools.wraps() decorator.
                        #
                        # removing the decorator fixes the leak for reasons we don't understand.
                        "metronome/_legacy_response.py",
                        "metronome/_response.py",
                        # pydantic.BaseModel.model_dump || pydantic.BaseModel.dict leak memory for some reason.
                        "metronome/_compat.py",
                        # Standard library leaks we don't care about.
                        "/logging/__init__.py",
                    ]
                ):
                    return

            leaks.append(diff)

        leaks: list[tracemalloc.StatisticDiff] = []
        for diff in snapshot_after.compare_to(snapshot_before, "traceback"):
            add_leak(leaks, diff)
        if leaks:
            for leak in leaks:
                print("MEMORY LEAK:", leak)
                for frame in leak.traceback:
                    print(frame)
            raise AssertionError()

    async def test_request_timeout(self) -> None:
        request = self.client._build_request(FinalRequestOptions(method="get", url="/foo"))
        timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
        assert timeout == DEFAULT_TIMEOUT

        request = self.client._build_request(
            FinalRequestOptions(method="get", url="/foo", timeout=httpx.Timeout(100.0))
        )
        timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
        assert timeout == httpx.Timeout(100.0)

    async def test_client_timeout_option(self) -> None:
        client = AsyncMetronome(
            base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, timeout=httpx.Timeout(0)
        )

        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
        assert timeout == httpx.Timeout(0)

    async def test_http_client_timeout_option(self) -> None:
        # custom timeout given to the httpx client should be used
        async with httpx.AsyncClient(timeout=None) as http_client:
            client = AsyncMetronome(
                base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, http_client=http_client
            )

            request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
            timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
            assert timeout == httpx.Timeout(None)

        # no timeout given to the httpx client should not use the httpx default
        async with httpx.AsyncClient() as http_client:
            client = AsyncMetronome(
                base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, http_client=http_client
            )

            request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
            timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
            assert timeout == DEFAULT_TIMEOUT

        # explicitly passing the default timeout currently results in it being ignored
        async with httpx.AsyncClient(timeout=HTTPX_DEFAULT_TIMEOUT) as http_client:
            client = AsyncMetronome(
                base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True, http_client=http_client
            )

            request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
            timeout = httpx.Timeout(**request.extensions["timeout"])  # type: ignore
            assert timeout == DEFAULT_TIMEOUT  # our default

    def test_invalid_http_client(self) -> None:
        with pytest.raises(TypeError, match="Invalid `http_client` arg"):
            with httpx.Client() as http_client:
                AsyncMetronome(
                    base_url=base_url,
                    bearer_token=bearer_token,
                    _strict_response_validation=True,
                    http_client=cast(Any, http_client),
                )

    def test_default_headers_option(self) -> None:
        client = AsyncMetronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_headers={"X-Foo": "bar"},
        )
        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        assert request.headers.get("x-foo") == "bar"
        assert request.headers.get("x-stainless-lang") == "python"

        client2 = AsyncMetronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_headers={
                "X-Foo": "stainless",
                "X-Stainless-Lang": "my-overriding-header",
            },
        )
        request = client2._build_request(FinalRequestOptions(method="get", url="/foo"))
        assert request.headers.get("x-foo") == "stainless"
        assert request.headers.get("x-stainless-lang") == "my-overriding-header"

    def test_validate_headers(self) -> None:
        client = AsyncMetronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        assert request.headers.get("Authorization") == f"Bearer {bearer_token}"

        with pytest.raises(MetronomeError):
            with update_env(**{"METRONOME_BEARER_TOKEN": Omit()}):
                client2 = AsyncMetronome(base_url=base_url, bearer_token=None, _strict_response_validation=True)
            _ = client2

    def test_default_query_option(self) -> None:
        client = AsyncMetronome(
            base_url=base_url,
            bearer_token=bearer_token,
            _strict_response_validation=True,
            default_query={"query_param": "bar"},
        )
        request = client._build_request(FinalRequestOptions(method="get", url="/foo"))
        url = httpx.URL(request.url)
        assert dict(url.params) == {"query_param": "bar"}

        request = client._build_request(
            FinalRequestOptions(
                method="get",
                url="/foo",
                params={"foo": "baz", "query_param": "overridden"},
            )
        )
        url = httpx.URL(request.url)
        assert dict(url.params) == {"foo": "baz", "query_param": "overridden"}

    def test_request_extra_json(self) -> None:
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar"},
                extra_json={"baz": False},
            ),
        )
        data = json.loads(request.content.decode("utf-8"))
        assert data == {"foo": "bar", "baz": False}

        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                extra_json={"baz": False},
            ),
        )
        data = json.loads(request.content.decode("utf-8"))
        assert data == {"baz": False}

        # `extra_json` takes priority over `json_data` when keys clash
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar", "baz": True},
                extra_json={"baz": None},
            ),
        )
        data = json.loads(request.content.decode("utf-8"))
        assert data == {"foo": "bar", "baz": None}

    def test_request_extra_headers(self) -> None:
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(extra_headers={"X-Foo": "Foo"}),
            ),
        )
        assert request.headers.get("X-Foo") == "Foo"

        # `extra_headers` takes priority over `default_headers` when keys clash
        request = self.client.with_options(default_headers={"X-Bar": "true"})._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    extra_headers={"X-Bar": "false"},
                ),
            ),
        )
        assert request.headers.get("X-Bar") == "false"

    def test_request_extra_query(self) -> None:
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    extra_query={"my_query_param": "Foo"},
                ),
            ),
        )
        params = dict(request.url.params)
        assert params == {"my_query_param": "Foo"}

        # if both `query` and `extra_query` are given, they are merged
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    query={"bar": "1"},
                    extra_query={"foo": "2"},
                ),
            ),
        )
        params = dict(request.url.params)
        assert params == {"bar": "1", "foo": "2"}

        # `extra_query` takes priority over `query` when keys clash
        request = self.client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                **make_request_options(
                    query={"foo": "1"},
                    extra_query={"foo": "2"},
                ),
            ),
        )
        params = dict(request.url.params)
        assert params == {"foo": "2"}

    def test_multipart_repeating_array(self, async_client: AsyncMetronome) -> None:
        request = async_client._build_request(
            FinalRequestOptions.construct(
                method="post",
                url="/foo",
                headers={"Content-Type": "multipart/form-data; boundary=6b7ba517decee4a450543ea6ae821c82"},
                json_data={"array": ["foo", "bar"]},
                files=[("foo.txt", b"hello world")],
            )
        )

        assert request.read().split(b"\r\n") == [
            b"--6b7ba517decee4a450543ea6ae821c82",
            b'Content-Disposition: form-data; name="array[]"',
            b"",
            b"foo",
            b"--6b7ba517decee4a450543ea6ae821c82",
            b'Content-Disposition: form-data; name="array[]"',
            b"",
            b"bar",
            b"--6b7ba517decee4a450543ea6ae821c82",
            b'Content-Disposition: form-data; name="foo.txt"; filename="upload"',
            b"Content-Type: application/octet-stream",
            b"",
            b"hello world",
            b"--6b7ba517decee4a450543ea6ae821c82--",
            b"",
        ]

    @pytest.mark.respx(base_url=base_url)
    async def test_basic_union_response(self, respx_mock: MockRouter) -> None:
        class Model1(BaseModel):
            name: str

        class Model2(BaseModel):
            foo: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = await self.client.get("/foo", cast_to=cast(Any, Union[Model1, Model2]))
        assert isinstance(response, Model2)
        assert response.foo == "bar"

    @pytest.mark.respx(base_url=base_url)
    async def test_union_response_different_types(self, respx_mock: MockRouter) -> None:
        """Union of objects with the same field name using a different type"""

        class Model1(BaseModel):
            foo: int

        class Model2(BaseModel):
            foo: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        response = await self.client.get("/foo", cast_to=cast(Any, Union[Model1, Model2]))
        assert isinstance(response, Model2)
        assert response.foo == "bar"

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": 1}))

        response = await self.client.get("/foo", cast_to=cast(Any, Union[Model1, Model2]))
        assert isinstance(response, Model1)
        assert response.foo == 1

    @pytest.mark.respx(base_url=base_url)
    async def test_non_application_json_content_type_for_json_data(self, respx_mock: MockRouter) -> None:
        """
        Response that sets Content-Type to something other than application/json but returns json data
        """

        class Model(BaseModel):
            foo: int

        respx_mock.get("/foo").mock(
            return_value=httpx.Response(
                200,
                content=json.dumps({"foo": 2}),
                headers={"Content-Type": "application/text"},
            )
        )

        response = await self.client.get("/foo", cast_to=Model)
        assert isinstance(response, Model)
        assert response.foo == 2

    def test_base_url_setter(self) -> None:
        client = AsyncMetronome(
            base_url="https://example.com/from_init", bearer_token=bearer_token, _strict_response_validation=True
        )
        assert client.base_url == "https://example.com/from_init/"

        client.base_url = "https://example.com/from_setter"  # type: ignore[assignment]

        assert client.base_url == "https://example.com/from_setter/"

    def test_base_url_env(self) -> None:
        with update_env(METRONOME_BASE_URL="http://localhost:5000/from/env"):
            client = AsyncMetronome(bearer_token=bearer_token, _strict_response_validation=True)
            assert client.base_url == "http://localhost:5000/from/env/"

    @pytest.mark.parametrize(
        "client",
        [
            AsyncMetronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
            ),
            AsyncMetronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
                http_client=httpx.AsyncClient(),
            ),
        ],
        ids=["standard", "custom http client"],
    )
    def test_base_url_trailing_slash(self, client: AsyncMetronome) -> None:
        request = client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar"},
            ),
        )
        assert request.url == "http://localhost:5000/custom/path/foo"

    @pytest.mark.parametrize(
        "client",
        [
            AsyncMetronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
            ),
            AsyncMetronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
                http_client=httpx.AsyncClient(),
            ),
        ],
        ids=["standard", "custom http client"],
    )
    def test_base_url_no_trailing_slash(self, client: AsyncMetronome) -> None:
        request = client._build_request(
            FinalRequestOptions(
                method="post",
                url="/foo",
                json_data={"foo": "bar"},
            ),
        )
        assert request.url == "http://localhost:5000/custom/path/foo"

    @pytest.mark.parametrize(
        "client",
        [
            AsyncMetronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
            ),
            AsyncMetronome(
                base_url="http://localhost:5000/custom/path/",
                bearer_token=bearer_token,
                _strict_response_validation=True,
                http_client=httpx.AsyncClient(),
            ),
        ],
        ids=["standard", "custom http client"],
    )
    def test_absolute_request_url(self, client: AsyncMetronome) -> None:
        request = client._build_request(
            FinalRequestOptions(
                method="post",
                url="https://myapi.com/foo",
                json_data={"foo": "bar"},
            ),
        )
        assert request.url == "https://myapi.com/foo"

    async def test_copied_client_does_not_close_http(self) -> None:
        client = AsyncMetronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
        assert not client.is_closed()

        copied = client.copy()
        assert copied is not client

        del copied

        await asyncio.sleep(0.2)
        assert not client.is_closed()

    async def test_client_context_manager(self) -> None:
        client = AsyncMetronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)
        async with client as c2:
            assert c2 is client
            assert not c2.is_closed()
            assert not client.is_closed()
        assert client.is_closed()

    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.asyncio
    async def test_client_response_validation_error(self, respx_mock: MockRouter) -> None:
        class Model(BaseModel):
            foo: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, json={"foo": {"invalid": True}}))

        with pytest.raises(APIResponseValidationError) as exc:
            await self.client.get("/foo", cast_to=Model)

        assert isinstance(exc.value.__cause__, ValidationError)

    async def test_client_max_retries_validation(self) -> None:
        with pytest.raises(TypeError, match=r"max_retries cannot be None"):
            AsyncMetronome(
                base_url=base_url,
                bearer_token=bearer_token,
                _strict_response_validation=True,
                max_retries=cast(Any, None),
            )

    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.asyncio
    async def test_received_text_for_expected_json(self, respx_mock: MockRouter) -> None:
        class Model(BaseModel):
            name: str

        respx_mock.get("/foo").mock(return_value=httpx.Response(200, text="my-custom-format"))

        strict_client = AsyncMetronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)

        with pytest.raises(APIResponseValidationError):
            await strict_client.get("/foo", cast_to=Model)

        client = AsyncMetronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=False)

        response = await client.get("/foo", cast_to=Model)
        assert isinstance(response, str)  # type: ignore[unreachable]

    @pytest.mark.parametrize(
        "remaining_retries,retry_after,timeout",
        [
            [3, "20", 20],
            [3, "0", 0.5],
            [3, "-10", 0.5],
            [3, "60", 60],
            [3, "61", 0.5],
            [3, "Fri, 29 Sep 2023 16:26:57 GMT", 20],
            [3, "Fri, 29 Sep 2023 16:26:37 GMT", 0.5],
            [3, "Fri, 29 Sep 2023 16:26:27 GMT", 0.5],
            [3, "Fri, 29 Sep 2023 16:27:37 GMT", 60],
            [3, "Fri, 29 Sep 2023 16:27:38 GMT", 0.5],
            [3, "99999999999999999999999999999999999", 0.5],
            [3, "Zun, 29 Sep 2023 16:26:27 GMT", 0.5],
            [3, "", 0.5],
            [2, "", 0.5 * 2.0],
            [1, "", 0.5 * 4.0],
            [-1100, "", 8],  # test large number potentially overflowing
        ],
    )
    @mock.patch("time.time", mock.MagicMock(return_value=1696004797))
    @pytest.mark.asyncio
    async def test_parse_retry_after_header(self, remaining_retries: int, retry_after: str, timeout: float) -> None:
        client = AsyncMetronome(base_url=base_url, bearer_token=bearer_token, _strict_response_validation=True)

        headers = httpx.Headers({"retry-after": retry_after})
        options = FinalRequestOptions(method="get", url="/foo", max_retries=3)
        calculated = client._calculate_retry_timeout(remaining_retries, options, headers)
        assert calculated == pytest.approx(timeout, 0.5 * 0.875)  # pyright: ignore[reportUnknownMemberType]

    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    async def test_retrying_timeout_errors_doesnt_leak(
        self, respx_mock: MockRouter, async_client: AsyncMetronome
    ) -> None:
        respx_mock.post("/v1/contracts/create").mock(side_effect=httpx.TimeoutException("Test timeout error"))

        with pytest.raises(APITimeoutError):
            await async_client.v1.contracts.with_streaming_response.create(
                customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
                starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            ).__aenter__()

        assert _get_open_connections(self.client) == 0

    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    async def test_retrying_status_errors_doesnt_leak(
        self, respx_mock: MockRouter, async_client: AsyncMetronome
    ) -> None:
        respx_mock.post("/v1/contracts/create").mock(return_value=httpx.Response(500))

        with pytest.raises(APIStatusError):
            await async_client.v1.contracts.with_streaming_response.create(
                customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
                starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            ).__aenter__()
        assert _get_open_connections(self.client) == 0

    @pytest.mark.parametrize("failures_before_success", [0, 2, 4])
    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.asyncio
    @pytest.mark.parametrize("failure_mode", ["status", "exception"])
    async def test_retries_taken(
        self,
        async_client: AsyncMetronome,
        failures_before_success: int,
        failure_mode: Literal["status", "exception"],
        respx_mock: MockRouter,
    ) -> None:
        client = async_client.with_options(max_retries=4)

        nb_retries = 0

        def retry_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal nb_retries
            if nb_retries < failures_before_success:
                nb_retries += 1
                if failure_mode == "exception":
                    raise RuntimeError("oops")
                return httpx.Response(500)
            return httpx.Response(200)

        respx_mock.post("/v1/contracts/create").mock(side_effect=retry_handler)

        response = await client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d", starting_at=parse_datetime("2020-01-01T00:00:00.000Z")
        )

        assert response.retries_taken == failures_before_success
        assert int(response.http_request.headers.get("x-stainless-retry-count")) == failures_before_success

    @pytest.mark.parametrize("failures_before_success", [0, 2, 4])
    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.asyncio
    async def test_omit_retry_count_header(
        self, async_client: AsyncMetronome, failures_before_success: int, respx_mock: MockRouter
    ) -> None:
        client = async_client.with_options(max_retries=4)

        nb_retries = 0

        def retry_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal nb_retries
            if nb_retries < failures_before_success:
                nb_retries += 1
                return httpx.Response(500)
            return httpx.Response(200)

        respx_mock.post("/v1/contracts/create").mock(side_effect=retry_handler)

        response = await client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            extra_headers={"x-stainless-retry-count": Omit()},
        )

        assert len(response.http_request.headers.get_list("x-stainless-retry-count")) == 0

    @pytest.mark.parametrize("failures_before_success", [0, 2, 4])
    @mock.patch("metronome._base_client.BaseClient._calculate_retry_timeout", _low_retry_timeout)
    @pytest.mark.respx(base_url=base_url)
    @pytest.mark.asyncio
    async def test_overwrite_retry_count_header(
        self, async_client: AsyncMetronome, failures_before_success: int, respx_mock: MockRouter
    ) -> None:
        client = async_client.with_options(max_retries=4)

        nb_retries = 0

        def retry_handler(_request: httpx.Request) -> httpx.Response:
            nonlocal nb_retries
            if nb_retries < failures_before_success:
                nb_retries += 1
                return httpx.Response(500)
            return httpx.Response(200)

        respx_mock.post("/v1/contracts/create").mock(side_effect=retry_handler)

        response = await client.v1.contracts.with_raw_response.create(
            customer_id="13117714-3f05-48e5-a6e9-a66093f13b4d",
            starting_at=parse_datetime("2020-01-01T00:00:00.000Z"),
            extra_headers={"x-stainless-retry-count": "42"},
        )

        assert response.http_request.headers.get("x-stainless-retry-count") == "42"

    def test_get_platform(self) -> None:
        # A previous implementation of asyncify could leave threads unterminated when
        # used with nest_asyncio.
        #
        # Since nest_asyncio.apply() is global and cannot be un-applied, this
        # test is run in a separate process to avoid affecting other tests.
        test_code = dedent("""
        import asyncio
        import nest_asyncio
        import threading

        from metronome._utils import asyncify
        from metronome._base_client import get_platform

        async def test_main() -> None:
            result = await asyncify(get_platform)()
            print(result)
            for thread in threading.enumerate():
                print(thread.name)

        nest_asyncio.apply()
        asyncio.run(test_main())
        """)
        with subprocess.Popen(
            [sys.executable, "-c", test_code],
            text=True,
        ) as process:
            timeout = 10  # seconds

            start_time = time.monotonic()
            while True:
                return_code = process.poll()
                if return_code is not None:
                    if return_code != 0:
                        raise AssertionError("calling get_platform using asyncify resulted in a non-zero exit code")

                    # success
                    break

                if time.monotonic() - start_time > timeout:
                    process.kill()
                    raise AssertionError("calling get_platform using asyncify resulted in a hung process")

                time.sleep(0.1)

    async def test_proxy_environment_variables(self, monkeypatch: pytest.MonkeyPatch) -> None:
        # Test that the proxy environment variables are set correctly
        monkeypatch.setenv("HTTPS_PROXY", "https://example.org")

        client = DefaultAsyncHttpxClient()

        mounts = tuple(client._mounts.items())
        assert len(mounts) == 1
        assert mounts[0][0].pattern == "https://"

    @pytest.mark.filterwarnings("ignore:.*deprecated.*:DeprecationWarning")
    async def test_default_client_creation(self) -> None:
        # Ensure that the client can be initialized without any exceptions
        DefaultAsyncHttpxClient(
            verify=True,
            cert=None,
            trust_env=True,
            http1=True,
            http2=False,
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        )

    @pytest.mark.respx(base_url=base_url)
    async def test_follow_redirects(self, respx_mock: MockRouter) -> None:
        # Test that the default follow_redirects=True allows following redirects
        respx_mock.post("/redirect").mock(
            return_value=httpx.Response(302, headers={"Location": f"{base_url}/redirected"})
        )
        respx_mock.get("/redirected").mock(return_value=httpx.Response(200, json={"status": "ok"}))

        response = await self.client.post("/redirect", body={"key": "value"}, cast_to=httpx.Response)
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

    @pytest.mark.respx(base_url=base_url)
    async def test_follow_redirects_disabled(self, respx_mock: MockRouter) -> None:
        # Test that follow_redirects=False prevents following redirects
        respx_mock.post("/redirect").mock(
            return_value=httpx.Response(302, headers={"Location": f"{base_url}/redirected"})
        )

        with pytest.raises(APIStatusError) as exc_info:
            await self.client.post(
                "/redirect", body={"key": "value"}, options={"follow_redirects": False}, cast_to=httpx.Response
            )

        assert exc_info.value.response.status_code == 302
        assert exc_info.value.response.headers["Location"] == f"{base_url}/redirected"
