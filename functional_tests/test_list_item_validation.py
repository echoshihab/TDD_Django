from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # user goes to hom page and accidentally tries to submit an empty
        # list item. User hits enter on the empty input box

        # the home page refrheshes and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # perversely, she now decides to submit a second blank list item

        # she receives a similar warning on the list page

        # and she can correct it by filling some text in

        self.fail('write me!')
