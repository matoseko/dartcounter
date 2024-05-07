from django.test import TestCase
from django.contrib.auth.models import User
from dartscounter.viewer.models import create_user

class CreateUserTestCase(TestCase):
    def test_create_user(self):
        # Arrange
        username = "testuser"
        email = "test@example.com"
        password = "testpassword"

        # Act
        user = create_user(username, email, password)

        # Assert
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))