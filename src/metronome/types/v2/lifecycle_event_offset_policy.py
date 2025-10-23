# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["LifecycleEventOffsetPolicy"]


class LifecycleEventOffsetPolicy(BaseModel):
    offset: str
    """
    ISO-8601 duration string indicating how much time before or after the base event
    this notification should be sent. Positive values indicate notifications after
    the event, negative values indicate notifications before the event. Examples:
    "P1D" (1 day after), "-PT2H" (2 hours before)
    """

    type: str
    """The type of lifecycle event that this offset is based on."""
