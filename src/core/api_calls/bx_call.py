from typing import Union, List, Dict


from fast_bitrix24 import BitrixAsync

from utils.mapping import print_info
from connectors.db_connector import DBConnector
from core.entities.config.types import T_ENTITY_METHOD, T_ENTITY_PARAMS


class BxCall:
    """
    Класс для вызовов и получения данных из BX24

    Параметры:
    `method: T_ENTITY_METHOD` -> Метод, на который отправляется запрос
    `params: T_ENTITY_PARAMS` -> Объект параметров запроса
    """

    def __init__(self, method: T_ENTITY_METHOD, params: T_ENTITY_PARAMS):
        self.__method = method
        self.__params = params

    async def _get_bx_data(self) -> Union[List, Dict]:
        webhook = DBConnector().webhook
        bx = BitrixAsync(webhook, False)
        print_info(f'Method name -> {self.__method}')

        return await bx.get_all(
            self.__method,
            params = self.__params
        )