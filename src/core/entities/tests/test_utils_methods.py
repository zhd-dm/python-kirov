import copy

import unittest


from core.entities.config.utils import _invalid_conf


ENTITY_CONF_VALID_MOCK = {
    'method': 'crm.deal.list',
    'params': { 'select': ['*', 'UF_*'] },
    'delivered_fields': [ 'id', 'name' ]
}


class TestEntitiesUtils(unittest.TestCase):
    def setUp(self):
        pass



    # @unittest.skip
    def test_invalid_conf(self):
        test_dict = copy.deepcopy(ENTITY_CONF_VALID_MOCK)
        result = _invalid_conf(test_dict)
        self.assertEqual(result, False)
    # @unittest.skip
    def test_invalid_conf2(self):
        test_dict = copy.deepcopy(ENTITY_CONF_VALID_MOCK)
        test_dict['params'] = None
        result = _invalid_conf(test_dict)
        self.assertEqual(result, True)
    # @unittest.skip
    def test_invalid_conf3(self):
        test_dict = copy.deepcopy(ENTITY_CONF_VALID_MOCK)
        test_dict['delivered_fields'] = None
        result = _invalid_conf(test_dict)
        self.assertEqual(result, True)




    def tearDown(self):
        pass