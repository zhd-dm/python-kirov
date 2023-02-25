from typing import Union, Dict, List

from fast_bitrix24 import BitrixAsync


from core.entity_configs.entity_config import EntityConfig
from features.bitrix.bx_connector import BXConnector
from features.print.print import Print


class BXApi:

    async def _get_bx_data(self, req_obj: EntityConfig) -> Union[List, Dict]:
        webhook = BXConnector().webhook
        bx = BitrixAsync(webhook, False)
        method = req_obj.entity_name
        Print().print_info(f'Method name -> {method}')

        return await bx.get_all(
            method,
            params = req_obj.params
        )