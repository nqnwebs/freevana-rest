from tastypie.resources import ModelResource
from tastypie import fields

from models import Serie, SerieEpisode, Movie, MovieSource


class MovieSourceResource(ModelResource):

    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'moviesource'



class MovieResource(ModelResource):
    sources = fields.ToManyField(MovieSourceResource, 'sources')

    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        allowed_methods = ['get']
        filtering = {
            'name': ['exact', 'icontains'],
        }
