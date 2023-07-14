# This is a sample Python script.
import unittest
from search_strain_by_name.search_strain_by_name import lambda_handler as _search_strain_by_name

class LamdaTest(unittest.TestCase):
    def test_search_strain_by_name_status(self):
        print(f"searching strains")
        event = {'queryStringParameters':{'query': 'ort'}}
        result = _search_strain_by_name(event, None)
        self.assertEqual(result['statusCode'], 200)
    def test_search_strain_by_name_count(self):
        print(f"searching strains")
        event = {'queryStringParameters':{'query': 'ort'}}
        result = _search_strain_by_name(event, None)
        self.assertEqual(len(result['body']), 2)
    # search_string = request_data['query']
# Press the green button in the gutter to run the script.

    # request_data = event['queryStringParameters']
    # search_string = request_data['query']
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
