import copy

import unittest

from utils import key_dict_to_lower, props_list_to_lower, get_dict_by_indexes_of_matrix, find_list_of_matrix
from utils import convert_list_to_dict, convert_str_to_dict_or_list, replace_custom_value

from tests.utils.test_utils_methods_mock import TEST_DICTIONARY_MOCK, TEST_LIST_MOCK, TEST_MATRIX_MOCK, TEST_STR_DICT_MOCK


class TestUtils(unittest.TestCase):
    def setUp(self):
        pass



    @unittest.skip
    def test_key_dict_to_lower_valid(self):
        test_dict = {'KEY1': 'Value1', 'key2': 'Value2'}
        result = key_dict_to_lower(test_dict)
        self.assertEqual(result, {'key1': 'Value1', 'key2': 'Value2'})
    @unittest.skip
    def test_key_dict_to_lower2_valid(self):
        test_dict = {1: None, 2: True}
        result = key_dict_to_lower(test_dict)
        self.assertEqual(result, {1: None, 2: True})

    @unittest.skip
    def test_key_dict_to_lower_invalid(self):
        test_dict = {'KEY1': 'Value1', 'key2': 'Value2'}
        result = key_dict_to_lower(test_dict)
        self.assertNotEqual(result, {'ADA2323': 'AS23D', 'key2': 'Value2'})



    @unittest.skip
    def test_props_list_to_lower_valid(self):
        test_list = ['FIELD', 'test', 'CaTaLoG']
        result = props_list_to_lower(test_list)
        self.assertEqual(result, ['field', 'test', 'catalog'])
    @unittest.skip
    def test_props_list_to_lower2_valid(self):
        test_list = [1, True, None]
        result = props_list_to_lower(test_list)
        self.assertEqual(result, [1, True, None])

    @unittest.skip
    def test_props_list_to_lower_invalid(self):
        test_list = ['FIELD', 'test', 'CaTaLoG']
        result = props_list_to_lower(test_list)
        self.assertNotEqual(result, ['aas', 11, None])




    @unittest.skip
    def test_get_dict_by_indexes_of_matrix_valid(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]]
        result = get_dict_by_indexes_of_matrix(0, 1, test_list)
        self.assertEqual(result, { 'a': 'b', 1: 2, 'd': 2 })
    @unittest.skip
    def test_get_dict_by_indexes_of_matrix2_valid(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]]
        result = get_dict_by_indexes_of_matrix(1, 2, test_list)
        self.assertEqual(result, { 'b': 'c', 2: 3, '2': 0 })

    @unittest.skip
    def test_get_dict_by_indexes_of_matrix_invalid(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]]
        result = get_dict_by_indexes_of_matrix(0, 1, test_list)
        self.assertNotEqual(result, { None: 'b', 1: 2, 'd': 2 })




    @unittest.skip
    def test_find_list_of_matrix_valid(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]]
        result = find_list_of_matrix(0, 'd', test_list)
        self.assertEqual(result, ['d', 2, 0])
    @unittest.skip
    def test_find_list_of_matrix2_valid(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]]
        result = find_list_of_matrix(3, 'd', test_list)
        self.assertEqual(result, None)
    @unittest.skip
    def test_find_list_of_matrix3_valid(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]]
        result = find_list_of_matrix(-1, 'c', test_list)
        self.assertEqual(result, ['a', 'b', 'c'])
    @unittest.skip
    def test_find_list_of_matrix4_valid(self):
        result = find_list_of_matrix(0, {}, TEST_MATRIX_MOCK)
        self.assertEqual(result, [{}, -100])
    @unittest.skip
    def test_find_list_of_matrix5_valid(self):
        result = find_list_of_matrix(-1, None, TEST_MATRIX_MOCK)
        self.assertEqual(result, [(), True, None])

    @unittest.skip
    def test_find_list_of_matrix_invalid(self):
        test_list = [['a', 'b', 'c'], [1, 2, 3], ['d', 2, 0]]
        result = find_list_of_matrix(0, 'd', test_list)
        self.assertNotEqual(result, ['d', 2, 0, 1])




    # @unittest.skip
    def test_convert_list_to_dict_valid(self):
        test_list = ['super', 1, None]
        result = convert_list_to_dict(['a', 'b', 'c'], test_list)
        self.assertEqual(result, { 'a': 'super', 'b': 1, 'c': None })
    # @unittest.skip
    def test_convert_list_to_dict2_valid(self):
        test_keys = [1, {}, None]
        test_list = ['super', 1, None]
        result = convert_list_to_dict(test_keys, test_list)
        self.assertEqual(result, {})
    # @unittest.skip
    def test_convert_list_to_dict3_valid(self):
        test_keys = [1, 's', None, True]
        test_list = ['super', 1, None]
        result = convert_list_to_dict(test_keys, test_list)
        self.assertEqual(result, {})

    # @unittest.skip
    def test_convert_list_to_dict_invalid(self):
        test_list = ['super', 1, None]
        result = convert_list_to_dict(['a', 'b', 'c'], test_list)
        self.assertNotEqual(result, { 'a': 'super', 'b': 1, None: None })




    # @unittest.skip
    def test_convert_str_to_dict_or_list_valid(self):
        test_str = "a, b, c"
        result = convert_str_to_dict_or_list(test_str)
        self.assertEqual(result, ['a', 'b', 'c'])
    # @unittest.skip
    def test_convert_str_to_dict_or_list2_valid(self):
        test_str = TEST_DICTIONARY_MOCK
        result = convert_str_to_dict_or_list(test_str)
        self.assertEqual(result, TEST_DICTIONARY_MOCK)
    # @unittest.skip
    def test_convert_str_to_dict_or_list3_valid(self):
        test_str = TEST_LIST_MOCK
        result = convert_str_to_dict_or_list(test_str)
        self.assertEqual(result, TEST_LIST_MOCK)
    # @unittest.skip
    def test_convert_str_to_dict_or_list4_valid(self):
        test_str = "[string]"
        result = convert_str_to_dict_or_list(test_str)
        self.assertEqual(result, ['string'])
    # @unittest.skip
    def test_convert_str_to_dict_or_list5_valid(self):
        test_str = "string"
        result = convert_str_to_dict_or_list(test_str)
        self.assertEqual(result, 'string')

    # @unittest.skip
    def test_convert_str_to_dict_or_list_invalid(self):
        test_str = "{'a': 1, 'b': {}, 'c': 'str'}"
        result = convert_str_to_dict_or_list(test_str)
        self.assertNotEqual(result, {'a': 132, 'b': {}, 'c': 'str'})



    # @unittest.skip
    def test_replace_custom_value_valid(self):
        result = copy.deepcopy(TEST_DICTIONARY_MOCK)
        replace_custom_value(result, 'custom', ['update'])
        self.assertEqual(result, {
            1: 'str',
            True: False,
            None: None,
            'str': {
                'str': {
                    'str': {
                        'str': {
                            'str': ['update']
                        }
                    }
                },
                'list': [
                    1, 2, None, True, False, 'str', 1.4, ['str']
                ]
            }
        })
    # @unittest.skip
    def test_replace_custom_value2_valid(self):
        result = copy.deepcopy(TEST_DICTIONARY_MOCK)
        replace_custom_value(result, 'custom', ['update'])
        self.assertNotEqual(result, TEST_DICTIONARY_MOCK)





    def tearDown(self):
        pass