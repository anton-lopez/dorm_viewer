from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DormViewSet, RoomViewSet, ReviewViewSet
from .auth_views import register_user, get_tokens

router = DefaultRouter()
router.register(r'dorms', DormViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', register_user, name="register"),
    path('api/token/', get_tokens, name="token"),
]
