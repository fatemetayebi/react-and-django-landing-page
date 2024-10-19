from django.contrib import admin
from django.urls import path
from main.views import ShowProductView, SendCodeView, VerifyCodeView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ShowProductView.as_view(), name='main'),
    path('verify_code/', VerifyCodeView.as_view()),
    path('sendcode/', SendCodeView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

