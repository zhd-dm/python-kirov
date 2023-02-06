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

TEST_MATRIX_MOCK = [
    [1, 2, 3], ['a', 'b', 'c'], [(), True, None],
    [12.423, 'test', False], [{}, -100], [[[], {1: {}}], None, 5],
    ['s', 'int', 'str'], [-2, '', ''], [[{}], None]
]

TEST_STR_DICT_MOCK = "{'a': 1, 'b': True, 'c': None}"