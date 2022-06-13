from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout


class UserLogoutView(View):
    def get(self, request):
        if request.user.is_anonymous:
            return redirect('core:home')
        logout(request)
        return redirect('core:home')


class UserLoginView(View):
    pass
