from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from rest_framework.routers import DefaultRouter


from product import views

router = DefaultRouter()
router.register(r"category", views.CategoryViewSet)
router.register(r"brand", views.BrandViewSet)
router.register(r"product", views.ProductViewSet)


def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('users.urls', namespace='users')),
    path('', home, name='home'),
    path('', include('product.urls', namespace='product'), name='home'),
    path("api/", include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
]
