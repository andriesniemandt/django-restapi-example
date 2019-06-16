from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # Test creating a new user with an email address is successful
        email = 'test@andries.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # Test the email for a new user to check if it is normalized
        email = 'test@ANDRIES.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        # Test the email for a new user if email invalid
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        # Test creating a new Super User
        user = get_user_model().objects.create_superuser(
            'testemail@test.com',
            'pass1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
