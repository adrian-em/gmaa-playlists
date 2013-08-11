from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apps.playlists.views import favorite_unfavorite_playlist

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gmaaplaylists.views.home', name='home'),
    # url(r'^gmaaplaylists/', include('gmaaplaylists.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'', include('social_auth.urls')),

    (r'^accounts/', include('registration.backends.default.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.playlists.views.index_page', name='home_page'),
    url(r'^user/playlists/$', 'apps.playlists.views.user_playlists_page',
        name='user_playlists_page'),
    url(r'^user/favorites/$', 'apps.playlists.views.favorites_playlists_page',
        name='favorites_playlists_page'),
    url(r'^add/playlist/$', 'apps.playlists.views.add_playlist_form',
        name='add_playlist_form'),
    url(r'^favorite/(?P<fav>\w{0,50})/(?P<playlistid>\w{0,50})$',
        'apps.playlists.views.favorite_unfavorite_playlist',
        name='create_destroy_favorite'),
    url(r'^delete/playlist/(?P<playlistid>\w{0,50})$', 'apps.playlists.views'
                                                '.delete_playlist',
        name='delete_playlist'),
    #url(r'^about/$', 'apps.playlists.views.about_page', name='about_page'),
    url(r'about/$', TemplateView.as_view(template_name='about.html'),
        name='about_page'),
)
