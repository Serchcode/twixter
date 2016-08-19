from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^nuevo/$',views.NuevoPost.as_view(),name="nuevo"),
	url(r'^(?P<id>\d+)$', views.DetailView.as_view(), name="details"),
	url(r'^$', views.ListView.as_view(), name="list"),
]