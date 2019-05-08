from selenium import webdriver

# XY sets up the browser and loads the to-do list app
browser = webdriver.Firefox()
browser.get("http://localhost:8000")

# He checks that the page title is correct
assert "To-Do" in browser.title

# He adds a to-do list item: "book karaoke room"

# XY notes that pressing enter updates the page with the item:
# "1. book karaoke room"

# The text box below allows another item to be added
# so XY adds another: "invite friends to karaoke"

# The page is updated with both items.

# XY checks that the site has a custom URL for the list.

# XY checks that the custom URL holds the correct list.

# OK, time to do other stuff.
browser.quit()


