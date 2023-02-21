from typing import Union, Dict, List

from fast_bitrix24 import BitrixAsync


from core.entity_configs.entity_config import EntityConfig
from core.connectors.bx_connector import BXConnector
from utils.mapping import print_info


class BXApi:

    async def _get_bx_data(self, req_obj: EntityConfig) -> Union[List, Dict]:
        webhook = BXConnector().webhook
        bx = BitrixAsync(webhook, False)
        method = f'{req_obj.parent_name}.{req_obj.entity_name}.{req_obj.type_method}' if req_obj.parent_name else f'{req_obj.entity_name}.{req_obj.type_method}'
        print_info(f'Method name -> {method}')

        return await bx.get_all(
            method,
            params = req_obj.params
        )