from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.menu.views import index,category_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('category/<str:slug>/', category_detail, name='category_detail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)