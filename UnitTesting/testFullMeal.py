import unittest
import requests

base_url = "https://us-central1-soa-cloud.cloudfunctions.net/get_full_meal"

class TestAPI(unittest.TestCase):
    def test_fullMealDessertInput(self):
            params = {
                "comida": "Churros",
                "tipo": "Dessert"
            }
            
            response = requests.get(base_url, params=params).json()
            data = response['data']
            
            self.assertEqual(response['status_code'], 200)      # Assert that the status code is 200
            self.assertIn('data', response)                     # Assert that it contains a data key
            
            self.assertIn('dish', data)                         # Assert that data contains a dish key
            self.assertIsNotNone(data['dish'])                  # Assert that dish is not null
            
            self.assertIn('drink', data)                        # Assert that data contains a drink key
            self.assertIsNotNone(data['drink'])                 # Assert that drink is not null
            
    def test_fullMealDishInput(self):
            params = {
                "comida": "Beef Tacos",
                "tipo": "Dish"
            }
            
            response = requests.get(base_url, params=params).json()
            data = response['data']
            
            self.assertEqual(response['status_code'], 200)      # Assert that the status code is 200
            self.assertIn('data', response)                     # Assert that it contains a data key
            
            self.assertIn('dessert', data)                      # Assert that data contains a dessert key
            self.assertIsNotNone(data['dessert'])               # Assert that dessert is not null
            
            self.assertIn('drink', data)                        # Assert that data contains a drink key
            self.assertIsNotNone(data['drink'])                 # Assert that drink is not null
            
    def test_fullMealDrinkInput(self):
            params = {
                "comida": "Margarita",
                "tipo": "Drink"
            }
            
            response = requests.get(base_url, params=params).json()
            data = response['data']
            
            self.assertEqual(response['status_code'], 200)      # Assert that the status code is 200
            self.assertIn('data', response)                     # Assert that it contains a data key
            
            self.assertIn('dish', data)                         # Assert that data contains a dish key
            self.assertIsNotNone(data['dish'])                  # Assert that dish is not null
            
            self.assertIn('dessert', data)                      # Assert that data contains a dessert key
            self.assertIsNotNone(data['dessert'])               # Assert that dessert is not null

if __name__ == '__main__':
    unittest.main()