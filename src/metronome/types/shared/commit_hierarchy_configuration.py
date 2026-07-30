# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, List

from ..._models import BaseModel

from typing_extensions import Literal, TypeAliasType, TypeAlias

__all__ = ["CommitHierarchyConfiguration", "ChildAccess", "ChildAccessCommitHierarchyChildAccessAll", "ChildAccessCommitHierarchyChildAccessNone", "ChildAccessCommitHierarchyChildAccessContractIDs"]

class ChildAccessCommitHierarchyChildAccessAll(BaseModel):
    type: Literal["ALL"]

class ChildAccessCommitHierarchyChildAccessNone(BaseModel):
    type: Literal["NONE"]

class ChildAccessCommitHierarchyChildAccessContractIDs(BaseModel):
    contract_ids: List[str]

    type: Literal["CONTRACT_IDS"]

ChildAccess: TypeAlias = Union[ChildAccessCommitHierarchyChildAccessAll, ChildAccessCommitHierarchyChildAccessNone, ChildAccessCommitHierarchyChildAccessContractIDs]

class CommitHierarchyConfiguration(BaseModel):
    child_access: ChildAccess