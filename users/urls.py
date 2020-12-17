"""Users URLs."""

# Django
from django.urls import path

# View
from users import views

urlpatterns = [

    # User Management
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('update/', views.UpdateProfileView.as_view(), name='update'),
]
