from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.urls import reverse_lazy

from . import views

app_name = 'users'
#add some changes
urlpatterns = [
    path("", views.index, name="index"),
    path("add_user/", views.add_user, name="add_user"),
    path("login/", LoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(next_page='polls:question-list'), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("reset_password/", PasswordResetView.as_view(template_name='registration/password_reset_form.html', email_template_name='registration/password_reset_form.html', success_url='users')),
    path("password_change", PasswordChangeView.as_view(template_name='registration/change_password.html',success_url=reverse_lazy('users:password-change-done')), name='password-change'),
    path("password_change_done", PasswordChangeDoneView.as_view(template_name='registration/change_password_done.html'), name='password-change-done', ),
]