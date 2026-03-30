from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name='home'),
    path("show_detail", views.show_detail, name='show_detail'),
    path('delete_service/<int:service_id>/', views.delete_service, name='delete_service'),
    path('update_service/<int:service_id>/', views.update_service, name='update_service'),
    path('add_service/', views.add_service, name='add_service'),
    path("service", views.service, name='service'),
    path("contact", views.contact, name='contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)