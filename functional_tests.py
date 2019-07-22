from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            "C:\\ChromeDriver\\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def test_start_list_retrieve_list(self):
        # user goes to homepage to add todo item
        self.browser.get('http://localhost:8000')

        # user sees the title 'To-Do' as the page title and header mentiones to-do
        # lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test')

        # user decides to add a to do item

        # user types 'submit patient payments to finance dept"

        # user hits ente, the page updates and the page lists "submit patient
        # payments to finance dept"

        # user uses the text box to add another ites - "enter cashlog data via
        # cashlog form"

        # the page updates again, and now shows both item on the list

        # user wants the site to remember the list, and notes that the site has
        # generated a unique url

        # user visits the unique url to confirm that to do list is still
        # available

        # user quites the todo list for the day

if __name__ == '__main__':
    unittest.main(warnings='ignore')
