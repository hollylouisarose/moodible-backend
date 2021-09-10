from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/images', include('images.urls')),
    path('api/auth/', include('jwt_auth.urls'))
]
