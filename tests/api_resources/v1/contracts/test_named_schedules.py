# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome._utils import parse_datetime
from metronome.types.v1.contracts import (
    NamedScheduleRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNamedSchedules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Metronome) -> None:
        named_schedule = client.v1.contracts.named_schedules.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
        )
        assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Metronome) -> None:
        named_schedule = client.v1.contracts.named_schedules.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            covering_date=parse_datetime("2022-02-15T00:00:00Z"),
        )
        assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Metronome) -> None:
        response = client.v1.contracts.named_schedules.with_raw_response.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_schedule = response.parse()
        assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Metronome) -> None:
        with client.v1.contracts.named_schedules.with_streaming_response.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_schedule = response.parse()
            assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Metronome) -> None:
        named_schedule = client.v1.contracts.named_schedules.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
        )
        assert named_schedule is None

    @parametrize
    def test_method_update_with_all_params(self, client: Metronome) -> None:
        named_schedule = client.v1.contracts.named_schedules.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
            ending_before=parse_datetime("2022-02-15T00:00:00Z"),
        )
        assert named_schedule is None

    @parametrize
    def test_raw_response_update(self, client: Metronome) -> None:
        response = client.v1.contracts.named_schedules.with_raw_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_schedule = response.parse()
        assert named_schedule is None

    @parametrize
    def test_streaming_response_update(self, client: Metronome) -> None:
        with client.v1.contracts.named_schedules.with_streaming_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_schedule = response.parse()
            assert named_schedule is None

        assert cast(Any, response.is_closed) is True


class TestAsyncNamedSchedules:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMetronome) -> None:
        named_schedule = await async_client.v1.contracts.named_schedules.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
        )
        assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMetronome) -> None:
        named_schedule = await async_client.v1.contracts.named_schedules.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            covering_date=parse_datetime("2022-02-15T00:00:00Z"),
        )
        assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.named_schedules.with_raw_response.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_schedule = await response.parse()
        assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.named_schedules.with_streaming_response.retrieve(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_schedule = await response.parse()
            assert_matches_type(NamedScheduleRetrieveResponse, named_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncMetronome) -> None:
        named_schedule = await async_client.v1.contracts.named_schedules.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
        )
        assert named_schedule is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMetronome) -> None:
        named_schedule = await async_client.v1.contracts.named_schedules.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
            ending_before=parse_datetime("2022-02-15T00:00:00Z"),
        )
        assert named_schedule is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.contracts.named_schedules.with_raw_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_schedule = await response.parse()
        assert named_schedule is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.contracts.named_schedules.with_streaming_response.update(
            rate_card_id="d7abd0cd-4ae9-4db7-8676-e986a4ebd8dc",
            schedule_name="my-schedule",
            starting_at=parse_datetime("2022-02-01T00:00:00Z"),
            value={"my_key": "my_value"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_schedule = await response.parse()
            assert named_schedule is None

        assert cast(Any, response.is_closed) is True
