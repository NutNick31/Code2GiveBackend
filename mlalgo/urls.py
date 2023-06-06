from django.urls import include, path
from .views import getInfo

urlpatterns = [
    path('', getInfo.as_view(), name='getInfo'),
]
