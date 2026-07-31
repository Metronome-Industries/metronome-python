# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from metronome import Metronome, AsyncMetronome
from tests.utils import assert_matches_type
from metronome.types.v1 import SettingUpsertAvalaraCredentialsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_upsert_avalara_credentials(self, client: Metronome) -> None:
        setting = client.v1.settings.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
        )
        assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

    @parametrize
    def test_method_upsert_avalara_credentials_with_all_params(self, client: Metronome) -> None:
        setting = client.v1.settings.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
            commit_transactions=True,
        )
        assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

    @parametrize
    def test_raw_response_upsert_avalara_credentials(self, client: Metronome) -> None:
        response = client.v1.settings.with_raw_response.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = response.parse()
        assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

    @parametrize
    def test_streaming_response_upsert_avalara_credentials(self, client: Metronome) -> None:
        with client.v1.settings.with_streaming_response.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = response.parse()
            assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_upsert_avalara_credentials(self, async_client: AsyncMetronome) -> None:
        setting = await async_client.v1.settings.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
        )
        assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

    @parametrize
    async def test_method_upsert_avalara_credentials_with_all_params(self, async_client: AsyncMetronome) -> None:
        setting = await async_client.v1.settings.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
            commit_transactions=True,
        )
        assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

    @parametrize
    async def test_raw_response_upsert_avalara_credentials(self, async_client: AsyncMetronome) -> None:
        response = await async_client.v1.settings.with_raw_response.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        setting = await response.parse()
        assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

    @parametrize
    async def test_streaming_response_upsert_avalara_credentials(self, async_client: AsyncMetronome) -> None:
        async with async_client.v1.settings.with_streaming_response.upsert_avalara_credentials(
            avalara_environment="PRODUCTION",
            avalara_password="my_password_123",
            avalara_username="test@metronome.com",
            delivery_method_ids=["9a906ebb-fbc7-42e8-8e29-53bfd2db3aca"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            setting = await response.parse()
            assert_matches_type(SettingUpsertAvalaraCredentialsResponse, setting, path=["response"])

        assert cast(Any, response.is_closed) is True
