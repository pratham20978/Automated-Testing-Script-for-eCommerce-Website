#!/usr/bin/env python3


# Tasks 1: Manual Testing Task
# • Write a testcase for an eCommerce website from login to the payment process.
# • You can select any product.



import requests
import unittest

class TestECommerceWebsite(unittest.TestCase):

    # Website response test
    def test_website_response(self):
        #Test website response
        # Assertion: verify if the website is responding correctly
        response = requests.get("http://example.com")
        self.assertEqual(response.status_code, 200, "Failed to get respponse")

# -------------------------------------------------------------------------------
        
        #Test website Authentication

    def test_successful_login(self):
        # Test successful user login
        login_data = {
            'username': 'test_user',
            'password': 'password'
        }
        response = requests.post("http://example.com/login", data=login_data)
        self.assertEqual(response.status_code, 200, "Failed to log in user")

        self.assertIn('session_id', response.cookies, "Session ID not found in logn response")

    def test_failed_login(self):
        # Test failed user login with incorrect credentials
        login_data = {
            'username': 'invalid_user',
            'password': 'invalid_password'
        }
        response = requests.post("http://example.com/login", data=login_data)
        self.assertNotEqual(response.status_code, 200, "User login succeeded with invalid credentials")

    
    def test_succesful_logout(self):

        logout_data={
            'session_id': 'valid_session_id'
        }
        response = requests.post("http://example.com/logout",data=logout_data)
        self.assertEqual(response.status_code,200, "Failed to log out user")

    def test_failed_logout(self):

        logout_data={
            'session_id': 'invalid_session_id'
        }
        response = requests.post("http://example.com/logout", data=logout_data)
        self.assertEqual(response.status_code,200,"User logout succeeded with invalid session ID")


#------------------------------------------------------------------------------
        
    # Test Product Search functionlity
    def test_product_search(self):
        # Test product search functionality
        # Assetions: Verify search results, filters, category navigation
        search_query = "laptop"
        response = requests.get(f"http://amazon.in/search?q={search_query}")
        self.assertEqual(response.status_code, 200, f"fialed to product search with query '{search_query}'")

    # Test add to cart functionality
    def test_add_to_cart(self):
        # Test adding product to the cart
        # Asseting: Verify cart contents, quantities, removal
        product_id = "12345" #Example product ID
        response = requests.post(f"http://www.amazon.com/cart/add/{product_id}")
        self.assertEqual(response.status_code, 200, "failed to add to cart operation")



#-----------------------------------------------------------------------------------

    # Test Checkout process
        
    def test_checkout_process(self):
        # Simulate adding a product to the cart

        # Mock user data
        user_data = {
            'username': 'test_user',
            'password': 'password'
        }

        # Log in 
        login_response = requests.post("http://example.com/login", data= user_data)
        self.assertEqual(login_response.status_code, 200 , "failed for successful login")

        # Get user Sesseion ID or token from login response 
        session_id = login_response.cookies.get('session_id')

        # add item to cart
        cart_response = requests.post("http://example.com/cart", cookies=={'session_id': session_id}, data={'item_id':'123', 'quantity':'1'})
        self.assertEqual(cart_response.status_code, 200, "failed add to cart")

        # Proceed to checkout
        checkout_response = requests.post("http://example.com/checkout", cookies={'session_id':session_id}, data={'address':'123 street'})
        self.assertEqual(checkout_response.status_code, 200, "failed to checkout")

        # Simulate entering shipping info
        shipping_data={'name': 'Pratham Verma', 'address':'92 Govt. colony birlagram', 'city': 'Nagda', 'zipcode': '433501', 'country': 'India'}
        shipping_response = requests.post("http://example.com/checkout/shipping",cookies={'session_id':session_id}, data=shipping_data)
        self.assertEqual(shipping_response.status_code, 200, "failed at shiping")

        # Make payment
        payment_data = {'card_number':'12345678993848','expiraton_data':'12/28', 'cvv':'123'}
        payment_response = requests.post("http://example.com/checkout/payment", cookies={'session_id': session_id}, data=payment_data)
        self.assertEqual(payment_response.status_code, 200, "failed at payment")

        # Simulate placing the order
        place_order_response = requests.post("http://example.com/checkout/place_order", cookies={'session_id': session_id})
        self.assertEqual(place_order_response.status_code, 200, "failed at place order")

        # Verify order confirmation
        self.assertIn('Order confirmed', payment_response.text, "failed to confirm order")


    # Product detail test
    def test_product_details_page(self):
        # Simulate accessing the product details page for a specific product
        product_id = "12345"
        response = requests.get(f"http://example.com/products/{product_id}")

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200, "failed to get product details page access")

        # Assert that the response contains the expected product information
        espected_product_info = {
            'name': 'Product Name',
            'description': 'Product Description',
            'price': "$100",
            'image_url': 'http://example.com/image.jpg',
        }
        product_info = response.json() # Assuming the response contains JSON data

        # Check if the expected product information matches the actual product information
        self.assertEqual(product_info['name'], expected_product_info['name'], "Unexpected product name")
        self.assertEqual(product_info['description'], espected_product_info['description'], "Unexpected product description")
        self.assertEqual(product_info['price'], espected_product_info['price'], "Unexpected product price")
        self.assertEqual(product_info['image_url'], espected_product_info['image_url'], "Unexpected product image URL")




if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)