#!/usr/bin/env python3


#Tasks 2: Automate an eCommerce website based on the above manual task.
#• Make the test cases for automation login
#• Search a product
#• Get the text and price of the product
#• Generate an automated report


import requests
import unittest
import csv

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        # Set up the base URl for the eCommerce website
        self.base_url = "http://example.com"

    def test_succesful_login(self):
        
        login_data = {
            'username': 'test_user',
            'password': 'password'
        }
        response = requests.post(f"{self.base_url}/login", data=login_data)
        self.assertEqual(response.status_code, 200, "Failed to log in user")
        self.assertIn('session_id',response.cookies, "session ID not found in login response")

    def test_search_product(self):
        # Automaitc product search functionality
        
        search_query = "laptop"
        response = requests.get(f"{self.base_url}/search?q={search_query}")
        self.assertEqual(response.status_code, 200, f"failed to search product")

    
    def test_get_product_details(self):
        # Test getting product details including text and price
        product_id = "123444"
        response = requests.get(f"{self.base_url}/products/{product_id}")
        self.assertEqual(response.status_code, 200, f"Failed to get product details for product ID '{product_id}'")

        product_details = response.json()  # Assuming the response contains JSON data
        self.assertIsNotNone(product_details.get('name'),"Product name not found")
        self.assertIsNotNone(product_details.get('description'), "Product description is not found")
        self.assertIsNotNone(product_details.get('price'), "Product price is not found")



if __name__== '__main__':
    # Define the test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLoginProcess)

    # Run the test suite
    runner = unittest.TextTestRunner(verbosity=1)
    test_results = runner.run(suite)


    # write test results to CSV file
    with open('test_report.csv', 'w', newline='') as csvfile:
        fieldnames = ['Test Name', 'Result']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for test_result in test_results.failures + test_results.errors:
            writer.writerow({'Test Name': test_result[0]._testMethodName, 'Result': 'Failed'})
        
        # Calculate the no of succesful tests
        successful_test = test_results.testsRun - len(test_results.failures) -len(test_results.errors)
        for _ in range (successful_test):
            writer.writerow({'Test Name': '', 'Result': 'Passed'})

    
    # Print test results to console
    print("Test run:", test_results.testsRun)
    print("failures:", len(test_results.failures))
    print("Errors:", len(test_results.errors))
    print("Successes:", successful_test)