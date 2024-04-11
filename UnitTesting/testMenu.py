import unittest
import requests

base_url = "https://us-central1-soa-cloud.cloudfunctions.net/get_menu"

class TestAPI(unittest.TestCase):
    def test_fullMenu(self):
        
        response = requests.get(base_url).json()
        data = response['data']
        
        self.assertEqual(response['status_code'], 200)      # Assert that the status code is 200
        
        self.assertIn('data', response)                     # Assert that it contains a data key
        self.assertIsInstance(data, list)                   # Assert that the data is not empty
        
        self.assertIn('dish', data[0])                      # Assert that data contains a dish key
        self.assertIsNotNone(data[0]['dish'])               # Assert that dish is not empty
        
        self.assertIn('drink', data[0])                     # Assert that data contains a drink key
        self.assertIsNotNone(data[0]['drink'])              # Assert that drink is not empty
        
        self.assertIn('dessert', data[0])                   # Assert that data contains a dessert key
        self.assertIsNotNone(data[0]['dessert'])            # Assert that dessert is not empty

if __name__ == '__main__':
    unittest.main()
