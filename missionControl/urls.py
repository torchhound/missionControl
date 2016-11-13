from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
        url(r"^$", views.livingRoom, name = "livingRoom"),
        url(r"^kittycorner$", views.kittyCorner, name = "kittyCorner"),
        url(r"^bathroom$", views.bathroom, name = "bathroom"),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
