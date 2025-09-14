from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, signup, login, one_student, all_students

router = DefaultRouter()
router.register(r'wallOfFame', StudentViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('students/', all_students, name='all_students'),
    path('students/<path:registration_number>/', one_student, name='one_student'),
]

