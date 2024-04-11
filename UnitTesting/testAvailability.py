import unittest
import requests

base_url = "https://us-central1-soa-cloud.cloudfunctions.net/get_availability"

class TestAPI(unittest.TestCase):
    def test_takenAvailability(self):
        params = {
            "time": "13:00",
            "date": "Monday"
        }
        
        response = requests.get(base_url, params=params).json()
        
        self.assertEqual(response['status_code'], 201)      # Assert that the status code is 201, date is occupied and recommended new ones
        self.assertIn('data', response)                     # Assert that it contains a data key
        self.assertIsInstance(response['data'], list)       # Assert that the data is not empty
        
    def test_freeAvailability(self):
        params = {
            "time": "14:00",
            "date": "Monday"
        }
        
        response = requests.get(base_url, params=params).json()
        
        self.assertEqual(response['status_code'], 200)      # Assert that the status code is 200, date is free
        self.assertIn('data', response)                     # Assert that it contains a data key
        self.assertIsInstance(response['data'], list)       # Assert that the data is not empty
        
    def test_outRangeAvailability(self):
        params = {
            "time": "11:35",
            "date": "Sunday"
        }
        
        response = requests.get(base_url, params=params).json()
        
        self.assertEqual(response['status_code'], 462)      # Assert that the status code is 200, date is free
        self.assertIn('message', response)                  # Assert that it contains a message key
        self.assertIsInstance(response['message'], str)     # Assert that the message is a string

if __name__ == '__main__':
    unittest.main()
