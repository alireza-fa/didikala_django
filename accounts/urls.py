from django.urls import path
from . import views


profile_urls = [

]


auth_urls = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]


app_name = 'accounts'
urlpatterns = [

]
