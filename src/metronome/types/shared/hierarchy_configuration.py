# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "HierarchyConfiguration",
    "ParentHierarchyConfiguration",
    "ParentHierarchyConfigurationChild",
    "ChildHierarchyConfiguration",
    "ChildHierarchyConfigurationParent",
]


class ParentHierarchyConfigurationChild(BaseModel):
    contract_id: str

    customer_id: str


class ParentHierarchyConfiguration(BaseModel):
    children: List[ParentHierarchyConfigurationChild]
    """List of contracts that belong to this parent."""


class ChildHierarchyConfigurationParent(BaseModel):
    contract_id: str

    customer_id: str


class ChildHierarchyConfiguration(BaseModel):
    parent: ChildHierarchyConfigurationParent
    """The single parent contract/customer for this child."""


HierarchyConfiguration: TypeAlias = Union[ParentHierarchyConfiguration, ChildHierarchyConfiguration]
