from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include  
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    
    path("", include("authentication.urls")),  
    path("", include("inventario.urls")),
    path('empleados', include('empleados.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
