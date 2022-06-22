from django.urls import path
from rest_framework import routers
from .views import PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'post', PostViewSet, basename="post")  # NOQA

urlpatterns = router.urls