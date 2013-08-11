from django.forms import ModelForm, forms, Select
from apps.playlists.models import Playlist


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        exclude = ('user', 'date_added')


class FilterForm(ModelForm):
    class Meta:
        model = Playlist
        #fields = ('name', 'genre', 'date_added')
        fields = ('genre',)
        widgets = {
            'genre': Select()
        }