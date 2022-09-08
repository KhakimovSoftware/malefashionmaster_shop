from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('__debug__', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('users.urls')),
    path('order/', include('orders.urls')),
    path('shop/', include('shop.urls')),
    path('blog/', include('blogs.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
