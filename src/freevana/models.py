# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class DatabaseVersion(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    version = models.TextField(blank=True)
    release_date = models.TextField(blank=True)
    class Meta:
        db_table = u'database_version'

class MovieSource(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    movie_id = models.IntegerField(null=True, blank=True)
    source = models.TextField(blank=True)
    definition = models.TextField(blank=True)
    audio = models.TextField(blank=True)
    url = models.TextField(blank=True)
    class Meta:
        db_table = u'movie_sources'


class Movie(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    name = models.TextField(blank=True)
    alt_name = models.TextField(blank=True)
    url = models.TextField(blank=True)
    subs = models.IntegerField(null=True, blank=True)
    sources_quantity = models.IntegerField(null=True, blank=True, db_column='sources')
    class Meta:
        db_table = u'movies'


class Serie(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    name = models.TextField(blank=True)
    url = models.TextField(blank=True)
    class Meta:
        db_table = u'series'

class SerieEpisodeSource(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    series_episode_id = models.IntegerField(null=True, blank=True)
    source = models.TextField(blank=True)
    definition = models.TextField(blank=True)
    audio = models.TextField(blank=True)
    url = models.TextField(blank=True)
    class Meta:
        db_table = u'series_episode_sources'

class SerieEpisode(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    season_id = models.IntegerField(null=True, blank=True)
    number = models.TextField(blank=True)
    short_name = models.TextField(blank=True)
    name = models.TextField(blank=True)
    url = models.TextField(blank=True)
    subs = models.IntegerField(null=True, blank=True)
    sources = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'series_episodes'

class SerieSeason(models.Model):
    id = models.IntegerField(null=True, primary_key=True, blank=True)
    series_id = models.IntegerField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    name = models.TextField(blank=True)
    finished = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'series_seasons'

