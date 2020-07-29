from typing import List

from klopov.components.currency_rates.crud import CRUDS

COLLECTIONS: List[str] = [crud_cls.collection for crud_cls in CRUDS]
