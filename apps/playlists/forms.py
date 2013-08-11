from django.forms import ModelForm
from apps.playlists.models import Playlist


class PlaylistForm(ModelForm):
    class Meta:
        model = Playlist
        exclude = ('user', 'date_added')
