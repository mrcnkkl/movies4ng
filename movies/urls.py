from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import routers
from movies_app.views import MovieViewSet, MovieCommentViewSet, TopCommentViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('comments', MovieCommentViewSet)
router.register('top', TopCommentViewSet, basename='top')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
