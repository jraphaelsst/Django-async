from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-sync/', views.sync_view),
    path('api-async/', views.async_view),
]
