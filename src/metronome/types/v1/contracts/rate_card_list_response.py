# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = [
    "RateCardListResponse",
    "Alias",
    "CreditTypeConversion",
    "CreditTypeConversionCustomCreditType",
    "FiatCreditType",
]


class Alias(BaseModel):
    name: str

    ending_before: Optional[datetime] = None

    starting_at: Optional[datetime] = None


class CreditTypeConversionCustomCreditType(BaseModel):
    id: str

    name: str


class CreditTypeConversion(BaseModel):
    custom_credit_type: CreditTypeConversionCustomCreditType

    fiat_per_custom_credit: str


class FiatCreditType(BaseModel):
    id: str

    name: str


class RateCardListResponse(BaseModel):
    id: str

    created_at: datetime

    created_by: str

    name: str

    aliases: Optional[List[Alias]] = None

    credit_type_conversions: Optional[List[CreditTypeConversion]] = None

    custom_fields: Optional[Dict[str, str]] = None

    description: Optional[str] = None

    fiat_credit_type: Optional[FiatCreditType] = None
