TEST_DICTIONARY_MOCK = {
    1: 'str',
    True: False,
    None: None,
    'str': {
        'str': {
            'str': {
                'str': {
                    'str': 'custom'
                }
            }
        },
        'list': [
            1, 2, None, True, False, 'str', 1.4, ['str']
        ]
    }
}

TEST_LOWER_DICTIONARY_MOCK = {
    'STR': 'STR',
    'str': 'STR'
}

TEST_GET_KEYS_OF_DICT_BY_CONDITION_MOCK = {
    'key1': 'int',
    'key2': 'str',
    'key3': 'json',
    2: True,
    False: None
}

TEST_LIST_MOCK = [
    1,
    2,
    {
        True: None,
        'str': {
            'str': {
                'str': {
                    'str': {
                        'str': 'custom'
                    }
                }
            },
            'list': [
                1, 2, None, True, False, 'str', 1.4, ['str']
            ]
        }
    },
    ()
]

TEST_MATRIX_NOT_EQUAL_LEN_MOCK = [
    [1, 2, 3], ['a', 'b', 'c'], [(), True, None],
    [12.423, 'test', False], [{}, -100], [[[], {1: {}}], None, 5],
    ['s', 'int', 'str'], [-2, '', ''], [[{}], None]
]

TEXT_MATRIX_EQUAL_LEN_MOCK = [
    [12.423, 'test', False], [[[], {1: {}}], None, 5], [-2, '', '']
]

TEST_STR_DICT_MOCK = "{'a': 1, 'b': True, 'c': None}"
