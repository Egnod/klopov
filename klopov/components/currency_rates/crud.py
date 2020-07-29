from typing import List, Type

from klopov.core.database.crud import BaseMongoCRUD


class CurrencyRateCRUD(BaseMongoCRUD):
    collection = "currency_rates"


class CurrencyRateProviderCRUD(BaseMongoCRUD):
    collection = "currency_rates_providers"


CRUDS: List[Type[BaseMongoCRUD]] = [CurrencyRateProviderCRUD, CurrencyRateCRUD]
