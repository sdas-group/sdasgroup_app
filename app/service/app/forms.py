from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=128,
        label='Name',
    )

    phone = forms.CharField(
        label='Phone',
    )

    email = forms.EmailField(
        label='Email',
    )

    message = forms.CharField(
        label='Message',
    )
