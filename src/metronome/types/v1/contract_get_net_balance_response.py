# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ContractGetNetBalanceResponse", "Data"]


class Data(BaseModel):
    balance: float
    """
    The combined net balance that the customer has access to use at this moment
    across all pertinent commits and credits.
    """

    credit_type_id: str
    """This ID identifies the credit type for the balance.

    The credit type can be fiat or a custom pricing unit. Quantity-based balances
    return the null credit type UUID.
    """


class ContractGetNetBalanceResponse(BaseModel):
    data: Data
