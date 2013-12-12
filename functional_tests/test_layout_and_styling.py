from .base import FunctionalTest


class LayoutAndStyling(FunctionalTest):

    def test_layout_styling(self):
        # Edith goes to the homepage
        self.browser.get(self.server_url)

        # She notices the input box is nicely centered
        inputbox = self.get_item_input_box()
        window_width = self.browser.get_window_size()['width']
        self.browser.implicitly_wait(3)
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            window_width / 2,
            delta=3
        )

        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.get_item_input_box()
        window_width = self.browser.get_window_size()['width']
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            window_width / 2,
            delta=3
        )
