from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    url(r"^login/$", views.UserLoginView, name='login'),
    url(r"logout/$", views.UserLogoutView, name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
    url(r"^editprofile/$", views.EditProfileView, name="editprofile"),
]
