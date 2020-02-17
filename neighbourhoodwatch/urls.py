from django.conf.urls import url
from . import views
from .views import PostListView, PostCreateView, NeighbourhoodlistView

urlpatterns = [
      url(r'^$', PostListView.as_view(), name='index'),
      url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
      url(r'neighbourhoodlist/$', NeighbourhoodlistView.as_view(), name='neighbourhoodlist'),
      url(r'contactinformation/$', views.contactinfo, name='contactinfo')
]