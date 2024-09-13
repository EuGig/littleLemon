from django.urls import include, path
from .views import MenuView, SingleMenuView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('menu/<int:pk>', SingleMenuView.as_view()),
    path('api-token-auth', obtain_auth_token)
]
