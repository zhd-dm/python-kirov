# import asyncio
# from typing import Dict, List

# # Local imports
# from utils import Utils, get_data, print_error
# from tables import BaseTable
# from fields.base_entity_config import BaseConfig
# from fields.crm_deal_list_fields import CRM_DEAL_LIST_CONFIG

# utils = Utils()
# engine = utils.engine

# async def main():
#     try:
#         print()
#         entity = BaseConfig(CRM_DEAL_LIST_CONFIG)
#         deals: List[Dict[str, any]] = await get_data(entity)
#         deal_table = BaseTable(engine)
#         deal_table._drop_and_create()
#         for deal in deals:
#             deal_table._add_data(deal)


#     except Exception as error:
#         print_error(error)

#     finally:
#         engine.pool.dispose()

# asyncio.run(main())