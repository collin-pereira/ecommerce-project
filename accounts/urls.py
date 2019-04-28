from accounts import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',auth_views.LogoutView.as_view(template_name='shoes/home.html'),name='logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name='password_reset_complete'),
]