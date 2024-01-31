from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from catalog import views
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'artists', views.ArtistViewSet, basename='artists')
router.register(r'albums', views.AlbumViewSet, basename='albums')
router.register(r'songs',views.SongViewSet, basename='songs')
router.register(r'genres', views.GenreViewSet, basename='genres')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path(r'openapi-schema', get_schema_view(
        title="Music API",
        description="Music catalog API",
        version="1.0.0",
        public=True
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name="catalog/swagger-ui.html",
        extra_context= {"schema_url":"openapi-schema"}
        ), name='swagger-ui')
]