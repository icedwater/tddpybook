from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

        # He notices that the word "To-Do" occurs in the first page header
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # XY sees that there is a text box to enter a to-do item
        inputbox = self.browser.find_element_by_id("new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), "What next?")

        # He adds a to-do list item: "book karaoke room"
        inputbox.send_keys("book karaoke room")
        inputbox.send_keys(Keys.ENTER)

        # XY notes that pressing enter updates the page with the item:
        # "1. book karaoke room"
        table = self.browser.find_element_by_id("to_do_list")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
                any(row.text == "1: book karaoke room" for row in rows),
                "Did not find '1: book karaoke room' in table."
        )

        # The text box below allows another item to be added
        # so XY adds another: "invite friends to karaoke"
        inputbox.send_keys("invite friends to karaoke")
        inputbox.send_keys(keys.ENTER)

        # The page is updated with both items.
        table = self.browser.find_element_by_id("to_do_list")
        rows = table.find_elements_by_tag_name("tr")
        self.assertTrue(
                any(row.text == "2: invite friends to karaoke" for row in rows),
                "Did not find '2: invite friends to karaoke' in table."
        )

        # XY checks that the site has a custom URL for the list.
        self.fail("Test will fail here!")

        # XY checks that the custom URL holds the correct list.

if __name__ == "__main__":
    unittest.main()  # warnings=ignore argument no longer needed
