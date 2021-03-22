import unittest
from selenium import webdriver


class E2ETests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='E:/gecko/geckodriver.exe')
        self.driver.get('http://localhost:5000')

    def tearDown(self):
        self.driver.quit()

    def test_browser_title_contains_app_name(self):
        self.assertIn('Named Entity Finder', self.driver.title)

    def test_page_heading_is_named_entity_finder(self):
        heading = self._find("heading").text
        self.assertEqual('Named Entity Finder', heading)

    def _find(self, val):
        return self.driver.find_element_by_css_selector(f'[data-test-id="{val}"]')

    def test_has_input_for_text(self):
        input_element = self._find('input-text')
        self.assertIsNotNone(input_element)

    def test_has_a_button_for_submitting_text(self):
        input_element = self._find('submit-button')
        self.assertIsNotNone(input_element)
