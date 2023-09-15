import unittest
import os
from questions.sql_questions import get_test_ids_by_status, get_min_max_date_for_test_id_and_status

def get_db_absolute_path():
    current_directory = os.path.dirname(__file__)
    return os.path.join(current_directory, 'databases/mytestdatabase.sqlite')

class TestDatabaseQueries(unittest.TestCase):
    def setUp(self):
        # Calculate the absolute path to the test database file
        self.db_absolute_path = get_db_absolute_path()

    def test_get_distinct_test_ids_with_status_false(self):
        result = get_test_ids_by_status(self.db_absolute_path, False)
        for test_id_tuple in result:
            self.assertIsInstance(test_id_tuple, tuple)
            self.assertEqual(len(test_id_tuple), 1)
            self.assertIsInstance(test_id_tuple[0], int)
        self.assertIsInstance(result, list)

    def test_get_min_max_dates_for_test_id_1(self):
        result = get_min_max_date_for_test_id_and_status(self.db_absolute_path, 1, True)

        for date_range_tuple in result:
            self.assertIsInstance(date_range_tuple, tuple)
            self.assertEqual(len(date_range_tuple), 2)  
            print(date_range_tuple)
            self.assertIsInstance(date_range_tuple[0], str)
            self.assertIsInstance(date_range_tuple[1], str)  

if __name__ == '__main__':
    unittest.main()
