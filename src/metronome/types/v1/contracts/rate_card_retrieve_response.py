# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "RateCardRetrieveResponse",
    "Data",
    "DataAlias",
    "DataCreditTypeConversion",
    "DataCreditTypeConversionCustomCreditType",
    "DataFiatCreditType",
]


class DataAlias(BaseModel):
    name: str

    ending_before: Optional[datetime] = None

    starting_at: Optional[datetime] = None


class DataCreditTypeConversionCustomCreditType(BaseModel):
    id: str

    name: str


class DataCreditTypeConversion(BaseModel):
    custom_credit_type: DataCreditTypeConversionCustomCreditType

    fiat_per_custom_credit: str


class DataFiatCreditType(BaseModel):
    id: str

    name: str


class Data(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    name: str

    aliases: Optional[List[DataAlias]] = None

    credit_type_conversions: Optional[List[DataCreditTypeConversion]] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    fiat_credit_type: Optional[DataFiatCreditType] = None


class RateCardRetrieveResponse(BaseModel):
    data: Data
