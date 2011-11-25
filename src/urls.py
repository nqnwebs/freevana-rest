from django.conf.urls.defaults import *

from freevana.api import MovieResource


urlpatterns = patterns('',
    url(r'^movies/', include(MovieResource().urls)),
)

