from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from models import Movie, MovieSource

class MovieResource(ModelResource):
    """
    A movie can be associated with zero or more sources.
    """
    model = Movie
    fields = ('id', 'name', 'alt_name', 'sources')

    def sources(self, instance):
        return reverse('movie-source-list', kwargs={'movie': instance.id})


class MovieSourceResource(ModelResource):
    model = MovieSource

    def movie(self, instance):
        return reverse('movie-detail', kwargs={'id': instance.movie.id})
