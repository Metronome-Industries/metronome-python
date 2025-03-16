# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TypeVar, Generic, Optional, List

from typing_extensions import override

import re
from typing_extensions import TypedDict, Literal, Annotated, Protocol, runtime_checkable

from httpx import URL, Response
from pydantic import Field as FieldInfo

from ._models import BaseModel
from ._utils import PropertyInfo, is_mapping
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage, PageInfo

__all__ = ["SyncCursorPage", "AsyncCursorPage"]

_T = TypeVar('_T')

class SyncCursorPage(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    next_page: Optional[str] = None
    """Cursor to fetch the next page"""
    data: List[_T]
    """Items of the page"""

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page = self.next_page
        if not next_page:
          return None

        return PageInfo(params={"next_page": next_page})

class AsyncCursorPage(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    next_page: Optional[str] = None
    """Cursor to fetch the next page"""
    data: List[_T]
    """Items of the page"""

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page = self.next_page
        if not next_page:
          return None

        return PageInfo(params={"next_page": next_page})