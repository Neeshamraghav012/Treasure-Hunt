
from django.contrib import admin
from django.urls import path
from game.views import QRTokenView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:qrtoken>/', QRTokenView, name = "qrtoken-view"),

]
