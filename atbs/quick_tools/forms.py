
__author = "Derick Mwenda"

from django.forms import ModelForm, Form, IntegerField


class PasswordGeneratorForm(Form):

    length = IntegerField(help_text="How long would you like your password to be?", initial="20")
