import copy

import unittest


from core.pg.config.utils import _invalid_conf, _invalid_name, _invalid_primary_key, _invalid_fields, _invalid_enums


TABLE_CONF_VALID_MOCK = {
    'name': 'tablename',
    'primary_key': 'id',
    'fields': {
        'id': 'int',
        'field': 'char',
        'count': 'int',
        'enum_field': 'enum'
    },
    'enums': {
        'enum_field': [ 'str', 2.12, True ]
    }
}


class TestPGUtils(unittest.TestCase):
    def setUp(self):
        pass



    # @unittest.skip
    def test_invalid_conf(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        result = _invalid_conf(test_dict)
        self.assertEqual(result, False)

    # @unittest.skip
    def test_invalid_name(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        test_dict['name'] = None
        result = _invalid_name(test_dict['name'])
        self.assertEqual(result, True)
    # @unittest.skip
    def test_invalid_name2(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        test_dict['name'] = 123
        result = _invalid_name(test_dict['name'])
        self.assertEqual(result, True)

    # @unittest.skip
    def test_invalid_primary_key(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        test_dict['primary_key'] = None
        result = _invalid_primary_key(test_dict['primary_key'])
        self.assertEqual(result, True)
    # @unittest.skip
    def test_invalid_primary_key2(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        test_dict['primary_key'] = ''
        result = _invalid_primary_key(test_dict['primary_key'])
        self.assertEqual(result, False)

    # @unittest.skip
    def test_invalid_fields(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        result = _invalid_fields(test_dict['fields'])
        self.assertEqual(result, False)
    # @unittest.skip
    def test_invalid_fields2(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        test_dict['fields']['id'] = 1
        result = _invalid_fields(test_dict['fields'])
        self.assertEqual(result, True)

    # @unittest.skip
    def test_invalid_enums(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        result = _invalid_enums(test_dict['enums'])
        self.assertEqual(result, False)
    # @unittest.skip
    def test_invalid_enums2(self):
        test_dict = copy.deepcopy(TABLE_CONF_VALID_MOCK)
        test_dict['enums']['id'] = True
        result = _invalid_enums(test_dict['enums'])
        self.assertEqual(result, True)




    def tearDown(self):
        pass