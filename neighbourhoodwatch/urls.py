from django.conf.urls import url
from . import views
from .views import PostListView, PostCreateView, NeighbourhoodlistView, NeighbourCreateView, NeighbourDetailView, NeighbourUpdateView, NeighbourDeleteView

urlpatterns = [
      url(r'^$', PostListView.as_view(), name='index'),
      url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
      url(r'neighbourhoodlist/$', NeighbourhoodlistView.as_view(), name='neighbourhoodlist'),
      url(r'^neighbourhood/(?P<pk>\d+)/$', NeighbourDetailView.as_view(), name='neighbourhood-detail'),
      url(r'neighbourhood/new/$', NeighbourCreateView.as_view(), name='neighbourcreate'),
      url(r'^neighbourhood/(?P<pk>\d+)/update/$', NeighbourUpdateView.as_view(), name='neighbourupdate'),
      url(r'^neighbourhood/(?P<pk>\d+)/delete/$', NeighbourDeleteView.as_view(), name='neighbourdelete'),
      url(r'businesses/(?P<id>\d+)/$', views.businesses, name='businesses'),
      url(r'contactinformation/$', views.contactinfo, name='contactinfo')
]