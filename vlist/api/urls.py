from rest_framework.routers import DefaultRouter
from .views import UListViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('vlists', UListViewSet)



urlpatterns = [
    path('', include(router.urls)),
]