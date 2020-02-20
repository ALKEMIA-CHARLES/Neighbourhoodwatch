from django.conf.urls import url
from . import views
from .views import PostListView, PostCreateView, NeighbourhoodlistView, NeighbourCreateView

urlpatterns = [
      url(r'^$', PostListView.as_view(), name='index'),
      url(r'^post/new/$', PostCreateView.as_view(), name='post-create'),
      url(r'neighbourhoodlist/$', NeighbourhoodlistView.as_view(), name='neighbourhoodlist'),
      url(r'neighbourhood/new/$', NeighbourCreateView.as_view(), name='neighbourcreate'),
      url(r'businesses/$', views.businesses, name='businesses' ),
      url(r'contactinformation/$', views.contactinfo, name='contactinfo')
]