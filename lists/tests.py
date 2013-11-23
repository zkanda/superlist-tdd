from django.test import TestCase


class SimpleTest(TestCase):

    def test_basic_addition(self):
        "Basic Addition"
        self.assertEqual(1+1, 3)
