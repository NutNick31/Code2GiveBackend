from django.urls import include, path
from rest_framework import routers
from .views import MyModelViewSet

router = routers.DefaultRouter()
router.register(r'', MyModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
