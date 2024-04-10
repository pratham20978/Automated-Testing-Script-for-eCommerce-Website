# Automated Testing Script for eCommerce Website

## What is it?

This Python script is designed to automate the testing process for an eCommerce website. It includes test cases for essential functionalities such as user login, product search, and retrieving product details. By automating these tests, it ensures the reliability and functionality of critical features of the eCommerce platform.

## How it Works

The automated testing script works by sending HTTP requests to the eCommerce website's API endpoints and validating the responses. Here's an overview of the process:

1. **Setup**: The script initializes the base URL of the eCommerce website.

2. **Login Process Testing**: The script sends a POST request with login credentials to the `/login` endpoint and checks if the login is successful by verifying the response status code and the presence of a session ID.

3. **Product Search Testing**: It sends a GET request with a search query to the `/search` endpoint and verifies the response status code to ensure successful product search functionality.

4. **Product Details Testing**: The script sends a GET request with a product ID to the `/products` endpoint and checks if the response status code is valid. It then extracts and verifies the product details such as name, description, and price from the response.

5. **Test Reporting**: After running the tests, the script generates a test report in CSV format (`test_report.csv`). This report contains details of each test case and its outcome (passed or failed).

## Use

The script serves as a valuable tool for quality assurance (QA) engineers and developers working on the eCommerce website. It allows for efficient and thorough testing of various aspects of the website, helping to identify and address any issues or bugs in the system. Additionally, it aids in maintaining the overall quality and performance of the eCommerce platform, thereby enhancing user experience and satisfaction.

## How to Use

1. **Clone the Repository**: Begin by cloning this repository to your local machine using the following command:

    ```bash
    git clone https://github.com/your_username/automated-testing-script.git
    ```

2. **Install Dependencies**: Navigate to the project directory and install the required dependencies by running:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure**: Open the script file (`test_script.py`) and update the `base_url` variable with the URL of your eCommerce website.

4. **Run the Tests**: Execute the script to run the automated tests by running:

    ```bash
    python test_script.py
    ```

5. **View Test Results**: After running the tests, the script will generate a test report in CSV format (`test_report.csv`). You can view the test results in this file to identify any failures or errors.

6. **Interpret Results**: Analyze the test results to determine the success or failure of each test case. Failed tests indicate potential issues or bugs that need to be addressed.

7. **Iterate and Improve**: Use the test results to iterate on the codebase, addressing any identified issues or bugs. Repeat the testing process to ensure the continued reliability and functionality of the eCommerce website.

## Contribution

Contributions are welcome! If you encounter any bugs, issues, or have suggestions for improvements, please feel free to open an issue or submit a pull request.

