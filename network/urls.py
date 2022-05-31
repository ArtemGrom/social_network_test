from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet

router = routers.SimpleRouter()
router.register(r'listposts', PostViewSet)

app_name = 'network'
urlpatterns = [
    path('', include(router.urls)),
]
