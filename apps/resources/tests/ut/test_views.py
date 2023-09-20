from django.test import TestCase, Client
from django.urls import reverse
from django.http import HttpResponseRedirect
from apps.user import models as userModel
from apps.resources import models as resourceModels

# Create your tests here.


class TestResourcesView(TestCase):  # Test<view-name>View
    """Test the Resources views"""

    def setUp(self):
        self.client = Client()

    def test_home_page_view_status_code(self):
        response = self.client.get(
            reverse("resources:home-page"),
            HTTP_USER_AGENT="Mozilla/5.0",
        )
        self.assertEqual(response.status_code, 200)

    def test_home_page_view_user_count(self):
        # TODO: CREATE A USER
        userModel.User.objects.create(
            password="test@2023password",
            username="kenz",
            first_name="tony",
            last_name="ralph",
            email="tonyralph@gmail.com",
            bio="Good at anything Python",
            title="Python developer",
        )
        # TODO: Set expected value for the portion of the context
        user_cnt = 1

        # ACT
        response = self.client.get(
            reverse("resources:home-page"),
            HTTP_USER_AGENT="Mozilla/5.0",
        )

        # ASSERT
        self.assertEqual(response.context["user_cnt"], user_cnt)

    def test_home_page_view_resource_count(self):
        # TODO: CREATE A USER
        # TODO: CREATE A TAG
        # TODO: CREATE A CATEGORY
        # TODO: CREATE A RESOURCE
        # TODO: Set expected value for the portion of the context
        res_cnt = 0

        # ACT
        response = self.client.get(
            reverse("resources:home-page"),
            HTTP_USER_AGENT="Mozilla/5.0",
        )

        # ASSERT
        self.assertEqual(response.context["user_cnt"], res_cnt)

    def test_resource_detail_return_login_for_non_authenticated_user(self):
        response = self.client.get(
            reverse("resources:resource-detail", kwargs={"id": 1}),
            HTTP_USER_AGENT="Mozilla/5.0",
        )
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/users/login/?next=/resource/1")

    def test_resource_detail_ok_for_authenticated_user(self):
        # TODO: CREATE A USER
        test_user = userModel.User.objects.create_user(
            password="test@2023password",
            username="kenz",
            first_name="tony",
            last_name="ralph",
            email="tonyralph@gmail.com",
            bio="Good at anything Python",
            title="Python developer",
        )
        test_user.save()

        login = self.client.login(username="kenz", password="test@2023password")
        response = self.client.get(
            reverse("resources:resource-detail", kwargs={"id": 1}),
            HTTP_USER_AGENT="Mozilla/5.0",
        )
        self.assertEqual(response.status_code, 200)
