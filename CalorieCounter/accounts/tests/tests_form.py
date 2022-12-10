from django.test import TestCase

from CalorieCounter.accounts.forms import CustomUserDeleteForm


class CustomUserFormsTests(TestCase):

    def test_user_delete_form_hidden_fields__when_all__expect_error(self):
        form = CustomUserDeleteForm()

        hidden_fields = {
            name: field.widget
            for name, field in form.fields.items()
        }

        for name in hidden_fields.keys():
            with self.assertRaises(TypeError) as ex:
                # 'HiddenInput' object is not callable
                self.assertFieldOutput(hidden_fields[name], '', '')

            self.assertIsNotNone(ex.exception)
