# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict, Required, TypeAliasType, TypeAlias

from ..._types import SequenceNotStr

from typing import Union

__all__ = ["CommitHierarchyConfiguration", "ChildAccess", "ChildAccessCommitHierarchyChildAccessAll", "ChildAccessCommitHierarchyChildAccessNone", "ChildAccessCommitHierarchyChildAccessContractIDs"]

class ChildAccessCommitHierarchyChildAccessAll(TypedDict, total=False):
    type: Required[Literal["ALL"]]

class ChildAccessCommitHierarchyChildAccessNone(TypedDict, total=False):
    type: Required[Literal["NONE"]]

class ChildAccessCommitHierarchyChildAccessContractIDs(TypedDict, total=False):
    contract_ids: Required[SequenceNotStr[str]]

    type: Required[Literal["CONTRACT_IDS"]]

ChildAccess: TypeAlias = Union[ChildAccessCommitHierarchyChildAccessAll, ChildAccessCommitHierarchyChildAccessNone, ChildAccessCommitHierarchyChildAccessContractIDs]

class CommitHierarchyConfiguration(TypedDict, total=False):
    child_access: Required[ChildAccess]