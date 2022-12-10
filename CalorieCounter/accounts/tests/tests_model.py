from django.core.exceptions import ValidationError
from django.test import TestCase

from CalorieCounter.accounts.models import CustomUser


class CustomUserModelTests(TestCase):

    def test_user_save__when_valid_age__expect_correct_result(self):
        user = CustomUser(
            username='user',
            password='1234hello',
            birthday='1999-11-23',
            gender='Male',
            height='189',
            weight=92,
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user)

    def test_user_save__when_invalid_age__expect_error(self):
        user = CustomUser(
            username='user',
            password='1234hello',
            birthday='2010-11-23',
            gender='Male',
            height='189',
            weight=92,
        )

        with self.assertRaises(ValidationError) as ex:
            user.full_clean()
            user.save()

        self.assertIsNotNone(ex.exception)

    def test_user_age_property__when_birthday_already_come__expect_correct_result(self):
        user = CustomUser(
            username='user',
            password='1234hello',
            birthday='2000-02-20',
            gender='Male',
            height='189',
            weight=92,
        )

        user.full_clean()
        user.save()

        self.assertEquals(user.age, 22)

    def test_user_age_property__when_birthday_not_come_yet__expect_correct_result(self):
        user = CustomUser(
            username='user',
            password='1234hello',
            birthday='2000-12-20',
            gender='Male',
            height='189',
            weight=92,
        )

        user.full_clean()
        user.save()

        self.assertEquals(user.age, 21)
