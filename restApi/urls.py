from django.urls import path,include
from rest_framework import routers
from restApi import views

router = routers.DefaultRouter()
router.register(r'developers', views.DeveloperViewSet)

urlpatterns = [
    path('', include(router.urls))
]
