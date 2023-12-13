from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cuenta/', include('login.urls')),
    path('registro/', include('registro.urls')),
    path('logout/', include('logout.urls'))
]
