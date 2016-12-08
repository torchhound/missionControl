from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
        url(r"^$", views.livingRoom, name = "livingRoom"),
        url(r"^kittycorner$", views.kittyCorner, name = "kittyCorner"),
        url(r"^bathroom$", views.bathroom, name = "bathroom"),
        url(r"^kcon$", views.kcon, name = "kcon"), #not sure if kcon or kittycorner/kcon
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
