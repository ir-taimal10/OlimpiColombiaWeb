from django.conf.urls import url
from OlimpiColombiaWeb.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view()),
]