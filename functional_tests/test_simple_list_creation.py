from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_list_for_one_user(self):
        # user goes to homepage to add todo item
        self.browser.get(self.live_server_url)

        # user sees the title 'To-Do' as the page title and header mentiones to-do
        # lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # user decides to add a to do item
        inputbox = self.get_item_input_box()
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
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Enter cashbox data via cashlog form')
        inputbox.send_keys(Keys.ENTER)

        # the page updates again, and now shows both item on the list
        self.wait_for_row_in_list_table(
            '2: Enter cashbox data via cashlog form')
        self.wait_for_row_in_list_table(
            '1: Submit patient payments to finance dept')

        # user wants the site to remember the list, and notes that the site has
        # generated a unique url

        # user visits the unique url to confirm that to do list is still
        # available

        # user quites the todo list for the day
    def test_multiple_users_can_start_lists_at_different_urls(self):

        # user1 starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Submit patient payments to finance dept')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(
            '1: Submit patient payments to finance dept')

        # user1 notices that her list has a unique url
        user1_list_url = self.browser.current_url
        self.assertRegex(user1_list_url, '/lists/.+')

        # now a new usr, user2, comes along to the site

        # we use a new browser session to make sure no information is coming
        # form user1
        self.browser.quit()
        self.browser = webdriver.Chrome(
            "C:\\ChromeDriver\\chromedriver.exe")

        # user2 visits the home page, there is no sign of user1's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Submit patient payments to finance dept', page_text)
        self.assertNotIn('Enter a cashbox data via cashlog form', page_text)

        # user2 starts a new list by entering a new item

        inputbox = self.get_item_input_box()
        inputbox.send_keys('Clean Frontdesk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Clean Frontdesk')

        # user2 gets his own unique URL
        user2_list_url = self.browser.current_url
        self.assertRegex(user2_list_url, '/lists/.+')
        self.assertNotEqual(user2_list_url, user1_list_url)

        # again no trace of user1 list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Submit patient payments to finance dept', page_text)
        self.assertIn('Clean Frontdesk', page_text)
