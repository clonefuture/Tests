import unittest
from unittest.mock import patch
from bookkeeping import *


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        print("Вызван метод ==> SetUp")

    def tearDown(self) -> None:
        print("Вызван метод ==> tearDown")

    def test_check_document_existance(self):
        test_cases = [
            {
                'input_num': '2207 876234',
                'exp_res': True
            },
            {
                'input_num': 'asdf',
                'exp_res': False
            }
        ]

        for test_case in test_cases:
            result = check_document_existance(test_case['input_num'])
            self.assertEqual(test_case['exp_res'], result)

    @patch('builtins.input')
    def test_get_doc_owner_name1(self, mocked_input):
        mocked_input.return_value = '112'

        result = get_doc_owner_name()
        self.assertEqual(result, None)

    @patch('builtins.input')
    def test_get_doc_owner_name(self, mocked_input):
        mocked_input.return_value = '11-2'

        result = get_doc_owner_name()
        self.assertEqual(result, 'Геннадий Покемонов')

    def test_get_all_doc_owners_names(self):
        users_list = []
        for docs in documents:
            users_list.append(docs['name'])
        exp_result = set(users_list)
        result = get_all_doc_owners_names()
        self.assertEqual(exp_result, result)

    @patch('builtins.input')
    def test_add_new_shelf(self, mocked_input):
        for shelf in directories.keys():
            mocked_input.return_value = shelf

            result = add_new_shelf()
            self.assertFalse(result[1], False)

    @patch('builtins.input')
    def test_add_new_shelf1(self, mocked_input):
        mocked_input.return_value = 'f5'

        result = add_new_shelf()
        self.assertEqual(result, ('f5', True))

    @patch('builtins.input')
    def test_delete_doc(self, mocked_input):
        for each_doc in documents:
            mocked_input.return_value = each_doc['number']

            delete_doc()
            result = False
            for docs in documents:
                if docs['number'] == mocked_input.return_value:
                    return True
                return False
            self.assertFalse(result, False)

    @patch('builtins.input')
    def test_get_doc_shelf1(self, mocked_input):
        mocked_input.return_value = '10006'

        result = get_doc_shelf()
        self.assertEqual(result, '2')

    @patch('builtins.input')
    def test_get_doc_shelf2(self, mocked_input):
        mocked_input.return_value = '100'

        result = get_doc_shelf()
        self.assertEqual(result, None)

    @patch('builtins.input')
    def test_add_new_doc(self, mocked_input):
        mocked_input.side_effect = ('911', "driver's license", 'Joe Murphy', 's')

        result = add_new_doc()
        exp = [i for i, j in directories.items() if j == ['911']][0]
        self.assertEqual(result, exp)


if __name__ == "__main__":
    unittest.main()
