from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            "C:\\ChromeDriver\\chromedriver.exe")

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        MAX_WAIT = 10
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_start_list_retrieve_list(self):
        # user goes to homepage to add todo item
        self.browser.get(self.live_server_url)

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
        self.wait_for_row_in_list_table(
            '1: Submit patient payments to finance dept')

        # user uses the text box to add another ites - "Enter cashbox data via
        # cashlog form"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Enter cashbox data via cashlog form')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, and now shows both item on the list
        self.wait_for_row_in_list_table(
            '1: Submit patient payments to finance dept')
        self.wait_for_row_in_list_table(
            '2: Enter cashbox data via cashlog form')

        # user wants the site to remember the list, and notes that the site has
        # generated a unique url
        self.fail('Finish the test')
        # user visits the unique url to confirm that to do list is still
        # available

        # user quites the todo list for the day
