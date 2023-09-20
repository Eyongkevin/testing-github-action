from django.test import TestCase
from apps.resources import models

# Create your tests here.


class TestTagModel(TestCase):  # Test<model-name>Model
    """Test the Tag model"""

    def setUp(self) -> None:
        self.tag_name = "Python"
        self.tag = models.Tag(name=self.tag_name)

    def test_create_tag(self):
        # Here I check if the object created is of the instance Tag
        self.assertIsInstance(self.tag, models.Tag)

    def test_dunder_str(self):
        # cast the object to a string and check the result
        self.assertEqual(str(self.tag), self.tag_name)


class TestCategoryModel(TestCase):  # Test<model-name>Model
    """Test the Cat model"""

    def setUp(self) -> None:
        self.cat_name = "Programming Language"
        self.cat = models.Category(cat=self.cat_name)

    def test_create_category(self):
        # Here I check if the object created is of the instance Cat
        self.assertIsInstance(self.cat, models.Category)

    def test_dunder_str(self):
        # cast the object to a string and check the result
        self.assertEqual(str(self.cat), self.cat_name)

    def test_verbose_name_plural(self):
        expected_verbose_name_plural = "Categories"

        self.assertEqual(
            self.cat._meta.verbose_name_plural,
            expected_verbose_name_plural,
        )
