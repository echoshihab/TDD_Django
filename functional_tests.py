from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user decides to add a to do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # user types 'submit patient payments to finance dept"
        inputbox.send_keys('Submit patient payments to finance dept')

        # user hits ente, the page updates and the page lists "submit patient
        # payments to finance dept"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Submit patient payments to finance dept' for row in rows),
            "New to-do item did not appear in table"
        )

        # user uses the text box to add another ites - "enter cashlog data via
        # cashlog form"
        self.fail('Finish the test')

        # the page updates again, and now shows both item on the list

        # user wants the site to remember the list, and notes that the site has
        # generated a unique url

        # user visits the unique url to confirm that to do list is still
        # available

        # user quites the todo list for the day


if __name__ == '__main__':
    unittest.main(warnings='ignore')
