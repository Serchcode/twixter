from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^tweets/$', views.TweetListView.as_view(),name="tweet_list"),
	url(r'^tweets/(?P<pk>\d+)/$', views.TweetDetailView.as_view(),name="tweet_detail"),
]