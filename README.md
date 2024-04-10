# TestECommerceWebsite Test Suite

The `TestECommerceWebsite` test suite is designed to automate the testing of an eCommerce website, covering various aspects from user authentication to the checkout process.

## Usage

To use the test suite, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Clone the repository containing the test suite to your local machine.
3. Navigate to the directory containing the test suite.
4. Run the following command to execute the test suite:

    ```bash
    python3 -m unittest test_ecommerce_website.py
    ```

## Functionality

The `TestECommerceWebsite` class contains the following test cases:

1. **Website Response Test**: Verifies if the website is responding correctly.

2. **Login Test**: Tests successful and failed user login scenarios.
    - **Home**:
      - Verify login form display
    - **Login**:
      - Verify successful login
      - Verify failed login with incorrect credentials

3. **Product Search Test**: Tests the functionality of searching for products on the website.
    - **Home**:
      - Verify search bar display
    - **Products**:
      - Verify search results display
      - Verify filtering options

4. **Add to Cart Test**: Tests the functionality of adding products to the shopping cart.
    - **Products**:
      - Verify product list display
    - **Product Details**:
      - Verify product details display
      - Verify add to cart button functionality

5. **Checkout Process Test**: Tests the entire checkout process, including adding items to the cart, entering shipping information, making payment, and placing the order.
    - **Cart**:
      - Verify cart display
      - Verify cart contents
    - **Checkout**:
      - Verify checkout form display
    - **Shipping**:
      - Verify shipping form display
    - **Payment**:
      - Verify payment form display
    - **Place Order**:
      - Verify order confirmation display

6. **Product Details Page Test**: Tests the functionality of accessing and verifying product details on the product details page.
    - **Products**:
      - Verify product list display
    - **Product Details**:
      - Verify product details display
      - Verify product information accuracy
