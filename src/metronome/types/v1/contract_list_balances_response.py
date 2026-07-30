# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from ..shared.commit import Commit

from ..shared.credit import Credit

from typing_extensions import TypeAliasType, TypeAlias

__all__ = ["ContractListBalancesResponse"]

ContractListBalancesResponse: TypeAlias = Union[Commit, Credit]