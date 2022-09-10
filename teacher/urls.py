

from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.AttendantListView.as_view(),name='teacher.home'),
]