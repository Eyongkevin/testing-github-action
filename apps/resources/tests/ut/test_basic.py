from django.test import TestCase

# Create your tests here.


# Test Case
class TestBasicCalculation(TestCase):
    # unit test
    def test_basic_sum(self):
        # arrange
        x = 1
        y = 4

        # act
        result = x + y

        # assert
        assert result == 5  # self.assertEqual(result, 5)
