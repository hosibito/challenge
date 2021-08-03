from django.urls import path

from . import views as users_views

app_name = "users"

urlpatterns = [   
    path('login/', users_views.LoginView.as_view() , name="login"),
    path('logout/', users_views.log_out , name="logout"), 
    path("signup/", users_views.SignUpView.as_view(), name="signup"),  
    path("update-profile/", users_views.UpdateProfileView.as_view(), name="update"),
    path("update-password/", users_views.UpdatePasswordView.as_view(), name="password"),
    path("<int:pk>/" , users_views.UserProfileView.as_view(), name="profile"),
]
