from django.urls import path
from .views import Api_create, Api_createsp, Api_login, Api_profile
from  . import views
urlpatterns = [
    path('api/create/', Api_create.as_view(), name='api_create'),  # Client signup
    path('api/createsp/', Api_createsp.as_view(), name='api_createsp'),  # Service provider signup
    path('api/login/', Api_login.as_view(), name='api_login'),  # Login
    path('api/profile/', Api_profile.as_view(), name='api_profile'),  # Retrieve user profile







    #html
    path('', views.login, name='login'),
    path('cl_signup/', views.cl_signup, name='cl_signup'),
    path('profile/', views.profile, name='profile'),
    path('sp_reg/', views.sp_reg, name='sp_reg'),
]
