from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
# URL to acces our viewset # providing our viewset # giving base name to retrieve our
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
    # inlcudes all the URLs register in the router object created above
]
