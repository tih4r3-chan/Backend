from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuenta/', include('login.urls')),
    path('', include('registro.urls'))
]
