import unittest
import requests

base_url = "https://us-central1-soa-cloud.cloudfunctions.net/get_emotions"

class TestAPI(unittest.TestCase):
    def test_goodFeedback(self):
        params = {
            "text": "Food was perfect!"
        }
        
        response = requests.get(base_url, params=params).json()
        
        self.assertEqual(response['status_code'], 200)      # Assert that the status code is 201
        self.assertIn('data', response)                     # Assert that it contains a data key
        
        try:                                                # Assert response corresponds to int value
            int(response['data'])
        except (TypeError, ValueError):
            self.fail("Value associated with 'data' key is not castable to int")        
        
    def test_midFeedback(self):
        params = {
            "text": "Food was okay, not great not bad"
        }
        
        response = requests.get(base_url, params=params).json()
        
        self.assertEqual(response['status_code'], 200)      # Assert that the status code is 200
        self.assertIn('data', response)                     # Assert that it contains a data key
        
        try:                                                # Assert response corresponds to int value
            int(response['data'])
        except (TypeError, ValueError):
            self.fail("Value associated with 'data' key is not castable to int")    
        
    def test_badFeedback(self):
        params = {
            "text": "Food was horrible!"
        }
        
        response = requests.get(base_url, params=params).json()
        
        self.assertEqual(response['status_code'], 200)      # Assert that the status code is 200
        self.assertIn('data', response)                     # Assert that it contains a data key
        
        try:                                                # Assert response corresponds to int value
            int(response['data'])
        except (TypeError, ValueError):
            self.fail("Value associated with 'data' key is not castable to int")    

if __name__ == '__main__':
    unittest.main()
