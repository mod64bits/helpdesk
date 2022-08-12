from django.test import TestCase
from .models import User


class UsersURLTest(TestCase):
    def setUp(self):
        User.objects.create_user("marcio", "marcio@gmail.com", "Mikita*2719")
        User.objects.create_user("miguel", "miguel@gmail.com", "Mikita*2719")

    def test_get_created_user(self):
        user_marcio = User.objects.get(username="marcio")
        user_miguel = User.objects.get(username="miguel")

        self.assertEqual(User.get_full_name(user_miguel), "miguel")
        self.assertEqual(User.get_full_name(user_marcio), "marcio")
