from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
#In case of ModelSerializer, no need to pass the base_name
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('', include(router.urls))
]
