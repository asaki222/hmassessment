import unittest
from unittest.mock import Mock
from questions.python_questions import create_job_status_dict, find_local_maxima, MyDBConnection

class TestFunctions(unittest.TestCase):

    def test_create_job_status_dict(self):
        job = ['id-1', 'id-2', 'id-3', 'id-4']
        status = [0, 1, 0, 0]
        expected_result = {'id-1': 0, 'id-2': 1, 'id-3': 0, 'id-4': 0}
        self.assertEqual(create_job_status_dict(job, status), expected_result)
    
    def test_create_job_status_dict_with_missing_values(self):
        job = ["id-1", "id-2", "id-3", "id-4", "id-5"]
        status = [0, 1, 0, 0]
        expected_result = {'id-1': 0, 'id-2': 1, 'id-3': 0, 'id-4': 0, 'id-5': 'missing'}
        self.assertEqual(create_job_status_dict(job, status), expected_result)

    def test_find_local_maxima(self):
        data = [3, 6, 1, 2, 5, 4, 10, 5, 7, 2, 4]
        expected_result = [(6, 1), (5, 4), (10, 6), (7, 8)]
        self.assertEqual(find_local_maxima(data), expected_result)

    def test_my_db_connection_set_timeout(self):
        mock_rs_connection = Mock()
        
        my_db_conn = MyDBConnection({'username': 'user1', 'password': 'pass1'})
        my_db_conn.rs_connection = mock_rs_connection
        
        mock_rs_connection.set_timeout(20)
        
        mock_rs_connection.set_timeout.assert_called_once_with(20)
    
if __name__ == '__main__':
    unittest.main()
