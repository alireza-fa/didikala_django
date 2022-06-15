from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import gettext_lazy as _
from .models import User
from convert_numbers import persian_to_english
from .validators import check_phone_number
from django.core.cache import cache


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label=_('password'))
    password2 = forms.CharField(widget=forms.PasswordInput(), label=_('confirm password'))

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'username')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError(_('Passwords don\'t match.'))
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text=_('You can change password using <a href="../password/">this link</a>'))

    class Meta:
        model = User
        fields = (
            'phone_number', 'email', 'username', 'fullname', 'image', 'score', 'received_news', 'is_oversea',
            'nationality_code', 'city', 'last_login'
        )


class UserLoginRegisterForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _('please enter your phone number.'), "class": 'input-ui pr-2', "id": 'phone_number'})
    )

    def clean_phone_number(self):
        phone = persian_to_english(self.cleaned_data['phone_number'])
        check_phone_number(phone)
        return phone


class VerifyPhoneNumberForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput())

    def __init__(self, request, *args, **kwargs):
        super(VerifyPhoneNumberForm, self).__init__(*args, **kwargs)
        self.request = request

    def clean_code(self):
        code = persian_to_english(self.cleaned_data.get('code'))
        if len(code) > 4 or len(code) < 4:
            raise forms.ValidationError(_('Code must have 4 chars.'))
        cache_info = cache.get(code)
        if not cache_info:
            raise forms.ValidationError(_('This code not a valid code or has expired.'))
        session_info = self.request.session.get('phone_number')
        if session_info and session_info == cache_info:
            return code
        raise forms.ValidationError(_('There is a problem, please try again.'))
