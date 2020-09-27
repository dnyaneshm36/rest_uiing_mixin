from django.conf.urls import url,include
from . import views
from .views import (
    StatusAPIView,
)


urlpatterns = [
    url(r'^hello', views.hello, name='hello'),
    url(r'^$',  StatusAPIView.as_view() ),
]