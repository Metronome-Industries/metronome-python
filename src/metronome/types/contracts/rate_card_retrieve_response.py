# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List, Dict

from datetime import datetime

from ..shared.credit_type_data import CreditTypeData

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RateCardRetrieveResponse", "Data", "DataAlias", "DataCreditTypeConversion"]

class DataAlias(BaseModel):
    name: str

    ending_before: Optional[datetime] = None

    starting_at: Optional[datetime] = None

class DataCreditTypeConversion(BaseModel):
    custom_credit_type: CreditTypeData

    fiat_per_custom_credit: str

class Data(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    name: str

    aliases: Optional[List[DataAlias]] = None

    credit_type_conversions: Optional[List[DataCreditTypeConversion]] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    fiat_credit_type: Optional[CreditTypeData] = None

class RateCardRetrieveResponse(BaseModel):
    data: Data