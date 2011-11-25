
from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListModelView, InstanceModelView
from freevana.resources import MovieResource, MovieSourceResource


urlpatterns = patterns('',
    url(r'^movies/$', ListModelView.as_view(resource=MovieResource), name='movie-list'),
    url(r'^movies/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=MovieResource), name='movie-detail'),
    url(r'^movies/(?P<movie>[^/]+)/sources/$',
         ListModelView.as_view(resource=MovieSourceResource), name='movie-source-list'),
    url(r'^movies/(?P<movie>[^/]+)/sources/(?P<id>[^/]+)/$',
        InstanceModelView.as_view(resource=MovieSourceResource)),
)
