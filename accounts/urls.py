from django.urls import path, include
from . import views


profile_urls = [

]


auth_urls = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('verify_phone_number/', views.VerifyPhoneNumberView.as_view(), name='verify_phone_number'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]


app_name = 'accounts'
urlpatterns = [
    path('', include(auth_urls)),
]
