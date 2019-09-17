from django.conf.urls import url
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('', include(router.urls))
]
