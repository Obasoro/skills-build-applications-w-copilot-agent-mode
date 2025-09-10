"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
import os
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'teams', views.TeamViewSet, basename='team')
router.register(r'activities', views.ActivityViewSet, basename='activity')
router.register(r'leaderboard', views.LeaderboardViewSet,
                basename='leaderboard')
router.register(r'workouts', views.WorkoutViewSet, basename='workout')


# Custom api_root to use $CODESPACE_NAME for endpoint URLs
@api_view(['GET'])
def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    base_url = request.build_absolute_uri('/')
    if codespace_name:
        base_url = f"https://{codespace_name}-8000.app.github.dev/"

    def api_url(comp): return f"{base_url}api/{comp}/"
    return Response({
        'users': api_url('users'),
        'teams': api_url('teams'),
        'activities': api_url('activities'),
        'leaderboard': api_url('leaderboard'),
        'workouts': api_url('workouts'),
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('api/', include(router.urls)),
]
