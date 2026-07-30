# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional, Dict

__all__ = ["Customer"]

class Customer(BaseModel):
    id: str
    """the Metronome ID of the customer"""

    external_id: str
    """
    (deprecated, use ingest_aliases instead) the first ID (Metronome or ingest
    alias) that can be used in usage events
    """

    ingest_aliases: List[str]
    """
    aliases for this customer that can be used instead of the Metronome customer ID
    in usage events
    """

    name: str

    custom_fields: Optional[Dict[str, str]] = None
    """Custom fields to be added eg. { "key1": "value1", "key2": "value2" }"""