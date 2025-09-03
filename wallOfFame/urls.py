from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, signup, login


router = DefaultRouter()
router.register(r'wallOfFame', StudentViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]

