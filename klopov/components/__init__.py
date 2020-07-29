from typing import List

from klopov.components.currency_rates import (
    CURRENCY_RATES_COLLECTIONS,
    currency_rate_router,
)

__all__ = ["COLLECTIONS"]

COLLECTIONS: List[str] = [*CURRENCY_RATES_COLLECTIONS]
