from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
)
from ..views import signup_view, profile_view


class TestUrls(SimpleTestCase):
    def test_profile_url_is_resolved(self):
        url = reverse("profile")

        self.assertEquals(resolve(url).func, profile_view)

    def test_login_url_is_resolved(self):
        url = reverse("login")

        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url_is_resolved(self):
        url = reverse("logout")

        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_signup_url_is_resolved(self):
        url = reverse("signup")

        self.assertEquals(resolve(url).func, signup_view)

    def test_password_change_url_is_resolved(self):
        url = reverse("password_change")

        self.assertEquals(resolve(url).func.view_class, PasswordChangeView)

    def test_password_change_done_url_is_resolved(self):
        url = reverse("password_change_done")

        self.assertEquals(resolve(url).func.view_class, PasswordChangeDoneView)

    def test_password_reset_url_is_resolved(self):
        url = reverse("password_reset")

        self.assertEquals(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_done_url_is_resolved(self):
        url = reverse("password_reset_done")

        self.assertEquals(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_complete_url_is_resolved(self):
        url = reverse("password_reset_complete")

        self.assertEquals(resolve(url).func.view_class, PasswordResetCompleteView)
