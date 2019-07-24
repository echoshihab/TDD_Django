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

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

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

        # user hits enter, the page updates and the page lists "submit patient
        # payments to finance dept"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table(
            '1: Submit patient payments to finance dept')

        # user uses the text box to add another ites - "Enter cashbox data via
        # cashlog form"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Enter cashbox data via cashlog form')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # the page updates again, and now shows both item on the list
        self.check_for_row_in_list_table(
            '1: Submit patient payments to finance dept')
        self.check_for_row_in_list_table(
            '2: Enter cashbox data via cashlog form')

        # user wants the site to remember the list, and notes that the site has
        # generated a unique url
        self.fail('Finish the test')
        # user visits the unique url to confirm that to do list is still
        # available

        # user quites the todo list for the day


if __name__ == '__main__':
    unittest.main(warnings='ignore')
