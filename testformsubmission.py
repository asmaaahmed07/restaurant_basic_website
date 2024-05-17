from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import unittest

class TestFormSubmission(unittest.TestCase):
    def setUp(self):
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening a window)
        chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resources in Docker container

        # Initialize Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(executable_path='/usr/local/bin/chromedriver'), options=chrome_options)
    
    def test_form_submission(self):
        # Navigate to the web application
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        # Fill out the form
        self.driver.find_element(By.ID, "input-field-id").send_keys("Test Input")
        self.driver.find_element(By.ID, "submit-button-id").click()

        # Verify that the form submission was successful
        success_message = self.driver.find_element(By.ID, "success-message-id")
        self.assertIsNotNone(success_message)
    
    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
