from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """
        Start the browser to run tests.
        """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        Close the browser.
        """
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it(self):
        """
        First test for saving a two-item list.
        """
        # XY sets up the browser and loads the to-do list app
        self.browser.get("http://localhost:8000")

        # He checks that the page title is correct
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test.")

        # He adds a to-do list item: "book karaoke room"

        # XY notes that pressing enter updates the page with the item:
        # "1. book karaoke room"

        # The text box below allows another item to be added
        # so XY adds another: "invite friends to karaoke"

        # The page is updated with both items.

        # XY checks that the site has a custom URL for the list.

        # XY checks that the custom URL holds the correct list.

if __name__ == "__main__":
    unittest.main()  # warnings=ignore argument no longer needed
