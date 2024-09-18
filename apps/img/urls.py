from django.urls import path
from .views import ImgView

urlpatterns = [
    path("", ImgView.as_view(), name="img"),
]