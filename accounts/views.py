from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout, login
from .forms import UserLoginRegisterForm, VerifyPhoneNumberForm
from django.http import JsonResponse
from django.core.cache import cache
import random
from .tasks import send_sms_code_task
from .models import User
from permissions import NotLoginRequiredMixin


class UserLogoutView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect('core:home')
        logout(request)
        return redirect('core:home')


class UserLoginView(NotLoginRequiredMixin, View):
    """
        Receive a valid phone number (Iran) from the user,
         then send a code to the phone number with send_sms_code_task and save the code in cache,
          also save to session to more check .
        we save next url in session because we send user to another page, but we need next url to direct.
    """
    template_name = 'accounts/login.html'
    class_form = UserLoginRegisterForm

    def get(self, request):
        request.session['next_url'] = request.GET.get('next', '/')
        return render(request, self.template_name, {"form": self.class_form})

    def post(self, request):
        form = self.class_form(request.POST)
        if form.is_valid():
            phone, code = form.cleaned_data.get('phone_number'), str(random.randint(1000, 9999))
            request.session['phone_number'] = phone
            cache.set(key=code, value=phone, timeout=120)
            send_sms_code_task.delay(phone, code)
            return JsonResponse(data={"status": 'ok', "url": '/accounts/verify_phone_number/'})
        string = render_to_string('accounts/ajax/login_form.html', {"form": form})
        return JsonResponse(data={"data": string, "status": 'bad'})


class VerifyPhoneNumberView(NotLoginRequiredMixin, View):
    """
        for get or create user, I changed method get_or_create to save username and password for new users.
    """
    template_name = 'accounts/verify_phone_number.html'
    class_form = VerifyPhoneNumberForm

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = self.class_form(request=request, data=request.POST)
        if form.is_valid():
            phone = request.session.get('phone_number')
            user = User.objects.get_or_create(phone_number=phone)
            login(request, user)
            next_url = request.session.get('next_url', '/')
            return JsonResponse(data={"status": 'ok', 'url': next_url})
        s = render_to_string('accounts/ajax/verify_form.html', {"form": form})
        return JsonResponse(data={"status": 'bad', 'data': s})
